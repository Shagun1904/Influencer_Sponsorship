import { createToaster } from "@meforma/vue-toaster";
import { defineStore } from "pinia";

const toaster = createToaster({});
export const useAlertStore=defineStore({
    id: 'alert',
    state:()=>({
        alert:null
    }),
    actions:{
        success(message){
            toaster.success(message, {
                position: "top",
                duration: 2000,
                display: "block",
            })
        },
        error(message){
            toaster.error(message, {
                position: "top",
                duration: 2000,
                display: "block",
            })
        }
    }
});