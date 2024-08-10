import axios from "axios";
import { defineStore } from "pinia";
import { useAlertStore } from '../stores/alertStore';
import { useRouter } from 'vue-router';
import { ref } from 'vue'

export const useSponsorStore = defineStore('sponsorStore', () => {
    const alertStore = useAlertStore();
    const myRouter = useRouter();

    async function sponsorDetails(userData){
        const userDetails = {
            companyName: userData.companyName,
            industry: userData.industryType,
            budget: userData.budget,
            user_id: localStorage.getItem('user_id')
        }

        try{
            await axios.post(`http://127.0.0.1:5000/sponsor`, userDetails);
            alertStore.success("Sponsor details saved successfully");
            localStorage.clear();
            setTimeout(() => {
            myRouter.push("/");
            }, 1000);
        }
        catch (error){
            console.log(error);
        }
    }

    const allSponsors = ref([]);

    async function getAllSponsors(){
        try{
            let result =await axios.get(`http://127.0.0.1:5000/sponsor`,{
                headers:{
                    Authorization: "Bearer " + localStorage.getItem('jwt')
                }
            });
            allSponsors.value = result.data;
        }
        catch (error){
            console.log(error);
        }
    }

    async function getSponsorById(id){
        try {
            let result = await axios.get(`http://127.0.0.1:5000/sponsor`, {
                headers: {
                    Authorization: "Bearer " + localStorage.getItem("jwt")
                }
            })
            let allSponsors = result.data;
            let sponsor = {}
            for (let s in allSponsors){
                if(allSponsors[s].user_id == id){
                    sponsor = allSponsors[s];
                    return {
                        sponsor
                    }
                }
            }
        }
        catch (error) {
            console.log(error);
        }
    }

    async function updateSponsor(formData){
        try{
            await axios.put(`http://127.0.0.1:5000/sponsor/${formData.id}`, formData)
            alertStore.success("Details updated successfully")
        }
        catch(error){
            alertStore.error("Something went wrong. Try after sometime.")
            console.log(error)
        }
    }

    return {
        sponsorDetails,
        getSponsorById,
        getAllSponsors,
        allSponsors,
        updateSponsor
    }
})