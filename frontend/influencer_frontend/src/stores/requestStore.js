import axios from "axios";
import { defineStore } from "pinia";
import { useAlertStore } from '../stores/alertStore';
import { useRoute } from 'vue-router';
import { useCampaignStore } from "./campaignStore";
import { ref } from 'vue';

export const useRequestStore = defineStore('requestStore', () => {
    const alertStore = useAlertStore();
    const campaignStore = useCampaignStore();
    const route= useRoute();

    async function requestData(requestData){
        let result = await campaignStore.getCampaignById(route.params.id);
        const campaign = ref({});
        campaign.value = result.campaign
        const requestDetails = {
            message: requestData.message,
            requirement: requestData.requirement,
            paymentAmount: requestData.payment,
            status: "Pending",
            sendBy: localStorage.getItem('userType'),
            campaign_id: route.params.id,
            influencer_id: requestData.influencer_id,
            sponsor_id: campaign.value.sponsor_id
        }
        try{
            let result = await axios.post(`http://127.0.0.1:5000/adRequest`, requestDetails);
            alertStore.success("Request send successfully");
            return result.data
        }
        catch (error){
            console.log(error);
        }
    }

    async function getAllAdRequestByCampaignId(){
        try{
            let result =await axios.get(`http://127.0.0.1:5000/adRequest`);
            let data = result.data;
            let allAdRequestData = [];
            for (let i in data){
                if (data[i].campaign_id==route.params.id){
                    allAdRequestData.push(data[i]);
                }
            }
            return{
                allAdRequestData
            }
        }
        catch (error){
            console.log(error);
        }
    }

    async function getCampaignByRequestId(request){
        try{
            let result = await axios.get(`http://127.0.0.1:5000/campaign`);
            let data = result.data;
            let campaign =[]
            for (let i in data){
                if (data[i].id==request.campaign_id){
                    campaign = data[i]
                }
            }
            return {
                campaign
            }
        }
        catch(error){
            console.log(error)
        }
    }

    async function getAllRequest(){
        let result =await axios.get(`http://127.0.0.1:5000/adRequest`);
            let data = result.data;
            let allRequestData = [];
            for (let i in data){
                allRequestData.push(data[i]);
            }
            return{
                allRequestData
            }
    }

    async function updateRequest(formData){
        try{
            await axios.put(`http://127.0.0.1:5000/adRequest/${formData.id}`, formData)
            alertStore.success("Request updated successfully")
        }
        catch(error){
            alertStore.error("Something went wrong. Try after sometime.")
            console.log(error)
        }
    }

    async function deleteRequestById(id){
        try{
            await axios.delete(`http://127.0.0.1:5000/adRequest/${id}`);
            alertStore.success("Request deleted successfully");
        }
        catch (error){
            console.log(error);
        }
    }

    return {
        requestData,
        getAllAdRequestByCampaignId,
        deleteRequestById,
        updateRequest,
        getAllRequest,
        getCampaignByRequestId
    }
})