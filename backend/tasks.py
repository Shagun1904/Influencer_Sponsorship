from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from celery import Celery
from celery.schedules import crontab
from influencer_backend.models.influencers import Influencers
from influencer_backend.models.sponsors import Sponsors
from influencer_backend.models.adRequest import AdRequest
from influencer_backend.models.users import Users 

celery_app = Celery(
    "tasks",
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0",
)

@celery_app.on_after_finalize.connect
def setup_delete_periodic_tasks(sender,**kwargs):
    sender.add_periodic_task(crontab(minute='*/2'),send_mail_task.s(),name="run every 2 minutes")

@celery_app.task
def daily_run():
    adReqs = AdRequest.query.filter(AdRequest.status=="Pending").all()
    for req in adReqs:
        sponsor = Sponsors.query.filter(Sponsors.id==req.sponsor_id).first()
        user1 = Users.query.filter(Users.id==sponsor.user_id)
        user_data1 = {
            "name": user1.name,
            "email": user1.email,
        }
        send_mail_task(user=user_data1)
        influencer = Influencers.query.filter(Influencers.id==req.influencer_id).first()
        user2 = Users.query.filter(Users.id==influencer.user_id)
        user_data2 = {
            "name": user2.name,
            "email": user2.email,
        }
        send_mail_task(user=user_data2)


def send_mail_task(user):
    # Email configuration
    sender = '22dp2000121@ds.study.iitm.ac.in'
    receiver = user.email
    subject = 'Scheduled Email'
    body = f'''
    Dear {user['name']},

    I hope this email finds you well.

    This is a gentle reminder that this email has been scheduled to be sent as part of a testing or automation process. 
    You have pending requests, please login to take actions.
    The details of the user involved in this process are as follows:

    Name: {user['name']}
    Email: {user['email']}

    Best regards,
    Shagun Niranjan
    22dp2000121
    22dp2000121@ds.study.iitm.ac.in
    '''

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email using smtplib
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login('22dp2000121@ds.study.iitm.ac.in', 'xfpt sqio erdc kvdy')
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send email: {e}')
