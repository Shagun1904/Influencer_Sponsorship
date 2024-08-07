import axios from "axios";
import { defineStore } from "pinia";
import { useAlertStore } from '../stores/alertStore';
import { useRouter } from 'vue-router';
import { ref } from 'vue';

export const useUserStore = defineStore('userStore', () => {

    const alertStore = useAlertStore();
    const myRouter = useRouter();

    async function signup(userData) {

        const userDetails = {
            name: userData.name,
            email: userData.email,
            userType: userData.userType,
            password: userData.password,
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

    function whichpage() {
        if (localStorage.getItem("name")) {
            let userT = localStorage.getItem("userType");
            if (userT === "influencer") {
                myRouter.push("/influencer/home");
            } else if (userT === "sponsor") {
                myRouter.push("/sponsor/home");
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
            if (data) {
                localStorage.setItem("jwt", data.jwt);
                localStorage.setItem("name", data.name);
                localStorage.setItem("user_id", data.user_id);
                localStorage.setItem("exp", data.exp);
                localStorage.setItem("userType", data.userType);
                if (data.userType === "influencer") {
                    myRouter.push("/influencer/home");
                } else if (data.userType === "sponsor") {
                    myRouter.push("/sponsor/home");
                }
            }
            else {
                console.log(data);
                myRouter.push("/");
            }
        }
        catch (error) {
                console.log(error);
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

    return {
        signup,
        alertStore,
        myRouter,
        login,
        whichpage,
        getUserById,
        getAlluser,
    }
})

