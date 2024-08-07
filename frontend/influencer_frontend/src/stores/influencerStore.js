import { defineStore } from "pinia";
import axios from "axios";
import { ref } from 'vue';
import { useAlertStore } from '../stores/alertStore';
import { useRouter } from 'vue-router';

export const useInfluencerStore = defineStore('influencerStore', () => {
    const alertStore = useAlertStore();
    const myRouter = useRouter();
    
    async function influencerDetails(userData){
        const userDetails = {
            category: userData.category,
            niche: userData.niche,
            reach: userData.reach,
            furl: userData.furl,
            iurl: userData.iurl,
            lurl: userData.lurl,
            user_id: localStorage.getItem('user_id')
        }

        try{
            await axios.post(`http://127.0.0.1:5000/influencer`, userDetails);
            alertStore.success("Influencer details saved successfully");
            localStorage.clear();
            setTimeout(() => {
            myRouter.push("/");
            }, 1000);
        }
        catch (error){
            alertStore.error("Something went wrong. Please try again.");
            console.log(error);
        }
    }

    const allInfluencer = ref([]);

    async function getAllInfluencer(){
        try{
            let result =await axios.get(`http://127.0.0.1:5000/influencer`,{
                headers:{
                    Authorization: "Bearer " + localStorage.getItem('jwt')
                }
            });
            allInfluencer.value = result.data;
        }
        catch (error){
            console.log(error);
        }
    }

    async function getInfluencerById(id){
        try {

            let result = await axios.get(`http://127.0.0.1:5000/influencer`, {
                headers: {
                    Authorization: "Bearer " + localStorage.getItem("jwt")
                }
            })
            console.log(id)
            let allInfluencerData = result.data;
            let influencer = {}
            for (let s in allInfluencerData){
                if(allInfluencerData[s].user_id == id){
                    influencer = allInfluencerData[s];
                    return {
                        influencer
                    }
                }

            }
        }
        catch (error) {
            console.log(error);
        }
    }

    return{
        getAllInfluencer,
        allInfluencer,
        influencerDetails,
        getInfluencerById
    }
})