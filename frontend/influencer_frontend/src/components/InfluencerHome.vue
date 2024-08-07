<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-10 offset-md-1 col-lg-10 offset-lg-1 col-sm-10 offset-sm-1">
                <div class="card mb-5 mt-5">
                    <img src="" class="card-img-top" alt="">
                    <div class="card-body">
                        <h4 class="card-title text-danger text-center"><strong>Welcome {{ userData.name }}</strong></h4>
                        <div class="card">
                            <h6 class="card-header"><strong>Your details</strong></h6>
                            <div class="card-body">
                                <p class="card-text"><strong>E-mail:</strong> {{ userData.email }}</p>
                                <p class="card-text"> <strong>Category:</strong> {{ userData2.category }}, 
                                    <strong>Niche:</strong> {{ userData2.niche }}, 
                                    <strong>Reach:</strong> {{ userData2.reach }}</p>
                                <a href="#" class="btn btn-primary">Update Details</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <div class="col">
                        <div class="card">
                            <img src="" class="card-img-top" alt="">
                            <div class="card-body">
                                <h5 class="card-title">Explore all the active campaigns</h5>
                                <p class="card-text"> <button class="btn btn-success"> <router-link class="text-decoration-none text-light" to="/view" > View </router-link> </button></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>


</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useInfluencerStore } from '../stores/influencerStore'
import { useUserStore } from '../stores/userStore'

const influencerStore = useInfluencerStore();
const userData = ref({});
const userData2 = ref({})
const user_id = localStorage.getItem('user_id')
const userStore = useUserStore();

onMounted(() => {
    getUser();
    getInfluencerDetails();
})

async function getUser() {
    let result = await userStore.getUserById(user_id);
    userData.value = result.userData
}

async function getInfluencerDetails() {
    let result = await influencerStore.getInfluencerById(user_id)
    userData2.value = result.influencer
}




</script>

<style scoped>

</style>