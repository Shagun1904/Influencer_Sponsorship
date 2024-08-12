class LocalConfig:
    JWT_SECRET_KEY="mysecretkey"
    SQLALCHEMY_DATABASE_URI="sqlite:///IFDataBase.sqlite3"
    CELERY_BROKER_URL = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND= "redis://localhost:6379/2"