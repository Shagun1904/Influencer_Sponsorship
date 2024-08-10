<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-10 offset-md-1 col-lg-10 offset-lg-1 col-sm-10 offset-sm-1">
                <div class="card mb-5 mt-5">
                    <div class="card-body">
                        <h4 class="card-title text-danger text-center"><strong>Welcome {{ userData.name }}</strong></h4>
                        <div class="card">
                            <h6 class="card-header"><strong>Your details</strong></h6>
                            <div class="card-body">
                                <p class="card-text"><strong>E-mail:</strong> {{ userData.email }} </p>
                                <button class="btn btn-primary mb-4" @click="openModal(userData)">Update Login Details</button>
                                <component :is="userUpdateModal" :user="currentSelectedUser"
                                        @close="closeModal" v-if="isModalVisible" @submit="handleModalSubmit">
                                    </component>
                                <p class="card-text"> <strong>Category:</strong> {{ userData2.category }}, 
                                    <strong>Niche:</strong> {{ userData2.niche }}, 
                                    <strong>Reach:</strong> {{ userData2.reach }}</p>
                                    <button class="btn btn-primary mb-4" @click="openModal2(userData2)">Update Additional Details</button>
                                <component :is="influencerUpdateModal" :influencer="currentSelectedInfluencer"
                                        @close="closeModal2" v-if="isModal2Visible" @submit="handleModal2Submit">
                                    </component>
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
import { onMounted, ref, defineAsyncComponent, shallowRef } from 'vue'
import { useInfluencerStore } from '../stores/influencerStore'
import { useUserStore } from '../stores/userStore'

const influencerStore = useInfluencerStore();
const userData = ref([]);
const userData2 = ref([])
const user_id = localStorage.getItem('user_id')
const userStore = useUserStore();

onMounted(async () => {
    await getUser();
    await getInfluencerDetails();
})

async function getUser() {
    let result = await userStore.getUserById(user_id);
    userData.value = result.userData
}

async function getInfluencerDetails() {
    let result = await influencerStore.getInfluencerById(user_id)
    userData2.value = result.influencer
}

//User Detail Update Modal

const isModalVisible = shallowRef(false);
const userUpdateModal = shallowRef(null);
const currentSelectedUser = ref(null);

const openModal = (user) => {
    currentSelectedUser.value = { ...user };
    userUpdateModal.value = defineAsyncComponent(() => import("../components/UserDetailsUpdateModal.vue"))
    isModalVisible.value = true;
};

const closeModal = (async () => {
    currentSelectedUser.value = null;
    isModalVisible.value = false;
    userUpdateModal.value = null;
});

const handleModalSubmit = (async (formData) => {
    await userStore.updateUser(formData);
    closeModal();
    await getInfluencerDetails();
});

//Influencer Details Update Modal

const isModal2Visible = shallowRef(false);
const influencerUpdateModal = shallowRef(null);
const currentSelectedInfluencer = ref(null);

const openModal2 = (influencer) => {
    currentSelectedInfluencer.value = { ...influencer };
    influencerUpdateModal.value = defineAsyncComponent(() => import("../components/influencerUpdateModal.vue"))
    isModal2Visible.value = true;
};

const closeModal2 = (async () => {
    currentSelectedInfluencer.value = null;
    isModalVisible.value = false;
    influencerUpdateModal.value = null;
});

const handleModal2Submit = (async (formData) => {
    await influencerStore.updateInfluencer(formData);
    closeModal2();
    await getInfluencerDetails();
});

</script>

<style scoped>

</style>