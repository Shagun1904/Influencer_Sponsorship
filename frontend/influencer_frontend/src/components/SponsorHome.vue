<template>
    <div>
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-10 offset-md-1 col-lg-10 offset-lg-1 col-sm-10 offset-sm-1">
                    <div class="card mb-5 mt-5">
                        <div class="card-body">
                            <h4 class="card-title text-danger text-center"><strong>Welcome {{ userData.name }}</strong>
                            </h4>
                            <div class="card">
                                <h6 class="card-header"><strong>Your details</strong></h6>
                                <div class="card-body">
                                    <p class="card-text"><strong>E-mail:</strong> {{ userData.email }}</p>
                                    <button class="btn btn-primary mb-4" @click="openModal(userData)">Update Login Details</button>
                                <component :is="userUpdateModal" :user="currentSelectedUser"
                                        @close="closeModal" v-if="isModalVisible" @submit="handleModalSubmit">
                                    </component>
                                    <p class="card-text"> <strong>Company name: </strong> {{ userData2.companyName }},
                                        <strong>Industry:</strong> {{ userData2.industry }},
                                        <strong>Budget:</strong> {{ userData2.budget }}
                                    </p>
                                    <button class="btn btn-primary mb-4" @click="openModal2(userData2)">Update Additional Details</button>
                                <component :is="sponsorUpdateModal" :sponsor="currentSelectedSponsor"
                                        @close="closeModal2" v-if="isModal2Visible" @submit="handleModal2Submit">
                                    </component>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, shallowRef, defineAsyncComponent } from 'vue'
import { useSponsorStore } from '../stores/sponsorStore'
import { useUserStore } from '../stores/userStore'

const sponsorStore = useSponsorStore();
const userData = ref([]);
const userData2 = ref([])
const user_id = localStorage.getItem('user_id')
const userStore = useUserStore();

onMounted(async() => {
    await getUser();
    await getSponsorDetails();
})

async function getUser() {
    let result = await userStore.getUserById(user_id);
    userData.value = result.userData
}

async function getSponsorDetails() {
    let result = await sponsorStore.getSponsorById(user_id)
    userData2.value = result.sponsor
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
    setTimeout(() => {
        getUser();
    }, 1000);
});

//sponsor Details Update Modal

const isModal2Visible = shallowRef(false);
const sponsorUpdateModal = shallowRef(null);
const currentSelectedSponsor = ref(null);

const openModal2 = (sponsor) => {
    currentSelectedSponsor.value = { ...sponsor };
    sponsorUpdateModal.value = defineAsyncComponent(() => import("../components/SponsorUpdateModal.vue"))
    isModal2Visible.value = true;
};

const closeModal2 = (async () => {
    currentSelectedSponsor.value = null;
    isModalVisible.value = false;
    sponsorUpdateModal.value = null;
});

const handleModal2Submit = (async (formData) => {
    await sponsorStore.updateSponsor(formData);
    closeModal2();
    await getSponsorDetails();
});

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