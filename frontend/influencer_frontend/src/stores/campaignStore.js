import axios from "axios";
import { defineStore } from "pinia";
import { useAlertStore } from '../stores/alertStore';
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import { useRequestStore } from "./requestStore";


export const useCampaignStore = defineStore('campaignStore', () => {
    const alertStore = useAlertStore();
    const myRouter = useRouter();
    const currentCampaign = ref(null);
    const requestStore = useRequestStore();

    async function campaignData(campaignData){
        const campaignDetails = {
            name: campaignData.name,
            description: campaignData.description,
            startDate: campaignData.startDate,
            endDate: campaignData.endDate,
            campaignBudget: campaignData.campaignBudget,
            visibility: campaignData.visibility,
            goal: campaignData.goal,
            flag: true,
            sponsor_id: localStorage.getItem('sponsor_id')
        }
        try{
            await axios.post(`http://127.0.0.1:5000/campaign`, campaignDetails);
            alertStore.success("Campaign added successfully");
            setTimeout(() => {
            myRouter.push("/sponsor/campaign");
            }, 1000);
        }
        catch (error){
            console.log(error);
        }
    }


    async function getAllCampaign(){
        try{
            let result =await axios.get(`http://127.0.0.1:5000/campaign`);
            let data = result.data;
            let allCampaignsData = [];
            for (let i in data){
                allCampaignsData.push(data[i]);
            }
            return{
                allCampaignsData
            }
        }
        catch (error){
            console.log(error);
        }
    }


    async function getCampaignById(id){
        try{
            let result = await axios.get(`http://127.0.0.1:5000/campaign/${id}`);
            let campaign = result.data
            return{
                campaign
            }
        }
        catch(error){
            console.log(error)
        }
    }

    async function updateCampaign(formData){
        try{
            
            await axios.put(`http://127.0.0.1:5000/campaign/${formData.id}`, formData);
            alertStore.success("Campaign updated successfully");
            
        }
        catch(error){
            console.log(formData)
            alertStore.error("Something went wrong. Try again after some time.");
            console.log(error)
        }
    }

    async function deleteCampaignById(id){
        try{
            let allRequest = []
            let result = await requestStore.getAllRequest();
            allRequest = result.allRequestData;
            for (const i in allRequest){
                if (allRequest[i].campaign_id ==id && (allRequest[i].status =='Negotiate' || allRequest[i].status == 'Pending')){
                    await requestStore.deleteRequestById(allRequest[i].id)
                }
            }
            await axios.delete(`http://127.0.0.1:5000/campaign/${id}`);
            alertStore.success("Campaign deleted successfully");
        }
        catch (error){
            console.log(error);
        }
    }

    return {
        campaignData,
        getAllCampaign,
        getCampaignById,
        currentCampaign,
        updateCampaign,
        deleteCampaignById
    }
})