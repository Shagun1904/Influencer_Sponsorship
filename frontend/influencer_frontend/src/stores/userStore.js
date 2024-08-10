import axios from "axios";
import { defineStore } from "pinia";
import { useAlertStore } from '../stores/alertStore';
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import { useSponsorStore } from "./sponsorStore";
import { useInfluencerStore } from "./influencerStore";

export const useUserStore = defineStore('userStore', () => {

    const alertStore = useAlertStore();
    const sponsorStore = useSponsorStore();
    const influencerStore = useInfluencerStore();
    const myRouter = useRouter();

    async function signup(userData) {

        const userDetails = {
            name: userData.name,
            email: userData.email,
            userType: userData.userType,
            password: userData.password,
            flag: userData.flag,
        }
        try {
            let result= await axios.post(`http://127.0.0.1:5000/user`, userDetails);
            let data = result.data
            if (data){
                localStorage.setItem('user_id', data.id)
            }
            alertStore.success("User registered successfully");
            setTimeout(() => {
                if (userDetails.userType=="sponsor"){
                    myRouter.push("/sponsor/registration");
                }
                else if (userDetails.userType=="influencer"){
                    myRouter.push("/influencer/registration");
                }
                
            }, 1500);
        }
        catch (error) {
            alertStore.error(error.response.data.message);
        }
    }

    async function whichpage() {
        let user_id = localStorage.getItem("user_id")
        if (user_id) {
            let result= await getUserById(user_id)
            if (result){
                let data=result.userData
                let userT = localStorage.getItem("userType");
                if (userT === "influencer") {
                    if (!data.flag){myRouter.push("/influencer/home");} 
                    else { alertStore.error("You have been blocked by Admin")}
                } 
                else if (userT === "sponsor") {
                    if (!data.flag){myRouter.push("/sponsor/home");} 
                    else { alertStore.error("You have been blocked by Admin")}
                } 
                else if (userT === "admin"){
                    myRouter.push("/admin")
                }
            }
        }
    }

    async function login(userData) {
        const userDetails = {
            email: userData.email,
            password: userData.password,
        }
        try {
            let result= await axios.post("http://127.0.0.1:5000/login", userDetails);
            let data = result.data;

            if(data.userType == "sponsor"){
                if (data.flag == true){
                    throw new Error('Yet to be Approve or blocked by Admin')
                }
                await sponsorStore.getAllSponsors();
                let selectedSponsor = sponsorStore.allSponsors.filter(s => s.user_id == data.user_id);
                localStorage.setItem("sponsor_id", selectedSponsor[0].id);
            }

            if(data.userType == "influencer"){
                await influencerStore.getAllInfluencer();
                let selectedInfluencer = influencerStore.allInfluencer.filter(i => i.user_id == data.user_id);
                localStorage.setItem("influencer_id", selectedInfluencer[0].id);
            }

            if (data) {
                localStorage.setItem("jwt", data.jwt);
                localStorage.setItem("user_id", data.user_id);
                localStorage.setItem("exp", data.exp);
                localStorage.setItem("userType", data.userType);
                if (data.userType === "influencer") {
                    myRouter.push("/influencer/home");
                } else if (data.userType === "sponsor") {
                    myRouter.push("/sponsor/home");
                }
                else if (data.userType === "admin") {
                    myRouter.push("/admin");
                }
            }
            else {
                console.log(data);
                myRouter.push("/");
            }
        }
        catch (error) {
                console.log(error);
                alertStore.error(error.message)
            }

        }

    async function getUserById(id){
        try{
            let result = await axios.get(`http://127.0.0.1:5000/user/${id}`, {
                headers: {
                    Authorization: "Bearer " + localStorage.getItem("jwt")
                }
            })
            let userData = result.data;
            return{
                userData
            }
        }
        catch(error){
            console.log(error);
        }
    }

    const alluser = ref([]);

    async function getAlluser(){
        try{
            let result =await axios.get(`http://127.0.0.1:5000/user`,{
                headers:{
                    Authorization: "Bearer " + localStorage.getItem('jwt')
                }
            });
            alluser.value = result.data;
        }
        catch (error){
            console.log(error);
        }
    }

    async function updateUser(formData){
        try{
            await axios.put(`http://127.0.0.1:5000/user/${localStorage.getItem('user_id')}`, formData);
            alertStore.success("user updated successfully")
        }
        catch(error){
            alertStore.error("Something went wrong. Try after sometime.")
            console.log(error)
        }
    }

    return {
        signup,
        alertStore,
        myRouter,
        login,
        whichpage,
        getUserById,
        getAlluser,
        updateUser,
        alluser
    }
})

