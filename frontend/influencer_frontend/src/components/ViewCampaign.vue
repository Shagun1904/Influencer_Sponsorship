<template>
    <div class="container-fluid">
        <div class="row">
            <div class="mt-4 mb-5">
                <h3 class="text-light text-center">All Campaign </h3>
                <div id="signup" class="mt-3 mb-5">
                    <div id="signupform">
                        <h2>{{ }}</h2>
                        <div class="row">
                            <div v-for="campaign in allCampaign" :key="campaign.id"
                                class="col-md-3 col-lg-3 col-sm-10 ">
                                <div class="card text-bg-secondary mb-3" style="max-width: 18rem;">
                                    <div class="card-header">{{ campaign.name }} <button disabled="disabled" class="btn btn-danger btn-sm">{{ campaign.visibility }}</button></div>
                                    <div class="card-header">{{ campaign.campaignBudget }}</div>
                                    <div class="card-body">
                                        <h5 class="card-title">{{ campaign.startDate }}</h5>
                                        <h5 class="card-title">{{ campaign.endDate }}</h5>
                                        <RouterLink class="btn btn-info"
                                            :to="{ name: 'AddRequest', params: { id: campaign.id } }">View</RouterLink>
                                        <button class="btn btn-warning ms-5" @click="openModal(campaign)" v-if="userType == 'sponsor'">Update</button>
                                        <component :is="campaignUpdateModal" :campaign="currentSelectedCampaign" @close="closeModal" v-if="isModalVisible"
                                            @submit="handleModalSubmit">
                                        </component>
                                    </div>
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
import { defineAsyncComponent, onMounted, ref, shallowRef } from 'vue';
import { useCampaignStore } from '@/stores/campaignStore';
const campaignStore = useCampaignStore();
let allCampaign = ref([]);
const userType=localStorage.getItem('userType')
// import { useRouter } from 'vue-router';

const isModalVisible = shallowRef(false);
const campaignUpdateModal = shallowRef(null);
const currentSelectedCampaign = ref(null);

const openModal = (campaign) => {
    currentSelectedCampaign.value = {...campaign};
    campaignUpdateModal.value = defineAsyncComponent(() => import("../components/CampaignUpdateModal.vue"))
    isModalVisible.value = true;
};

const closeModal = ( async () => {
    currentSelectedCampaign.value = null;
    isModalVisible.value = false;
    campaignUpdateModal.value = null;
    await updateCampaignList();
});

const handleModalSubmit = ((formData) => {
    campaignStore.updateCampaign(formData);
    closeModal();
    updateCampaignList();
});

const updateCampaignList = (async () => {
    let result = await campaignStore.getAllCampaign();
    allCampaign.value = result.allCampaignsData;
});

onMounted(async () => {
    await updateCampaignList();
});



</script>

<style scoped>
#signup {
    min-width: 50vh;
    min-height: 85vh;
    overflow-y: scroll;
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
