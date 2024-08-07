<template>
    <div>
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-10 offset-md-1 col-lg-10 offset-lg-1 col-sm-10 offset-sm-1">
                    <div id="signup" class="mt-5 mb-5">
                        <div id="signupform">
                            <h3>Sponsor Details</h3>
                            <ul class="col-md-6">
                                <li>{{ userData.name }}</li>
                                <li>{{ userData.email }}</li>
                            </ul>
                            <ul class="col-md-6">
                                <li>{{ userData2.companyName }}</li>
                                <li>{{ userData2.industry }}</li>
                                <li>{{ userData2.budget }}</li>
                            </ul>
                            <h3>Add new campaign</h3>
                            <button><router-link to="/sponsor/campaign"> Add </router-link></button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useSponsorStore } from '../stores/sponsorStore'
import { useUserStore } from '../stores/userStore'

const sponsorStore = useSponsorStore();
const userData = ref({});
const userData2 = ref({})
const user_id = localStorage.getItem('user_id')
const userStore = useUserStore();

onMounted(()=>{
    getUser();
    getSponsorDetails();
})

async function getUser(){
    let result = await userStore.getUserById(user_id);
    userData.value = result.userData
}

async function getSponsorDetails(){
    let result = await sponsorStore.getSponsorById(user_id)
    userData2.value = result.sponsor
    console.log(userData2);
}

</script>

<style scoped>
#signup {
    min-width: 50vh;
    min-height: 85vh;
    overflow: hidden;
    background-color: rgb(253, 253, 253);
    border-radius: 10px;
    box-shadow: 3px 3px 10px #000;
}

#signupform {
    padding: 3% 3%;
}

#mycont {
    text-decoration: none;
    color: rgb(255, 255, 255);
}

#img {
    width: 50%;
    height: 280px;
}
</style>