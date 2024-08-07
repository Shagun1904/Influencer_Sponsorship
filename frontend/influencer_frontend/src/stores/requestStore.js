import axios from "axios";
import { defineStore } from "pinia";
import { useAlertStore } from '../stores/alertStore';
import { useRoute } from 'vue-router';

export const useRequestStore = defineStore('requestStore', () => {
    const alertStore = useAlertStore();
    const route= useRoute();

    async function requestData(requestData){
        const requestDetails = {
            message: requestData.message,
            requirement: requestData.requirement,
            paymentAmount: requestData.payment,
            status: "Pending",
            sendBy: localStorage.getItem('userType'),
            campaign_id: route.params.id,
            influencer_id: requestData.influencer_id
        }

        try{
            let result = await axios.post(`http://127.0.0.1:5000/adRequest`, requestDetails);
            alertStore.success("Request added successfully");
            return result.data
            
        }
        catch (error){
            console.log(error);
        }
    }

    async function getAllAdRequest(){
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
        getAllAdRequest,
        deleteRequestById,
        updateRequest
    }
})