<template>
    <div class="statistics-container">
        <h2>Statistics</h2>
        <div v-if="userType === 'admin'" class="stats-section">
            <div class="stat-item">
                <span class="stat-label">Total Users:</span>
                <span class="stat-value">{{ allUsers.length }}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Total Influencers:</span>
                <span class="stat-value">{{ allInfluencer.length }}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Total Sponsors:</span>
                <span class="stat-value">{{ allSponsors.length }}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Total Campaigns:</span>
                <span class="stat-value">{{ allCampaign.length }}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Total Requests:</span>
                <span class="stat-value">{{ allRequest.length }}</span>
            </div>
        </div>
        <div v-else-if="userType === 'sponsor'" class="stats-section">
            <div class="stat-item">
                <span class="stat-label">Total Campaigns:</span>
                <span class="stat-value">{{ allCampaign.length }}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Accepted Requests:</span>
                <span class="stat-value">{{ acceptedRequests }}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Rejected Requests:</span>
                <span class="stat-value">{{ rejectedRequests }}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Pending Requests:</span>
                <span class="stat-value">{{ pendingRequests }}</span>
            </div>
        </div>
        <div v-else-if="userType === 'influencer'" class="stats-section">
            <div class="stat-item">
                <span class="stat-label">Sent Requests:</span>
                <span class="stat-value">{{ sentRequests }}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Accepted Requests:</span>
                <span class="stat-value">{{ acceptedRequests }}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Rejected Requests:</span>
                <span class="stat-value">{{ rejectedRequests }}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Received Requests:</span>
                <span class="stat-value">{{ receivedRequests }}</span>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useUserStore } from '../stores/userStore';
import { useInfluencerStore } from '../stores/influencerStore';
import { useSponsorStore } from '../stores/sponsorStore';
import { useCampaignStore } from '../stores/campaignStore';
import { useRequestStore } from '../stores/requestStore';
import { onMounted, ref } from 'vue';

const userStore = useUserStore();
const influencerStore = useInfluencerStore();
const sponsorStore = useSponsorStore();
const campaignStore = useCampaignStore();
const requestStore = useRequestStore();

let allUsers = ref([]);
let allInfluencer = ref([]);
let allSponsors = ref([]);
let allCampaign = ref([]);
let allRequest = ref([]);

let acceptedRequests = ref(0);
let rejectedRequests = ref(0);
let pendingRequests = ref(0);
let sentRequests = ref(0);
let receivedRequests = ref(0);

const userType = localStorage.getItem('userType');

const getAllUsers = async () => {
    await userStore.getAlluser();
    allUsers.value = userStore.alluser;
};

const getAllInfluencer = async () => {
    await influencerStore.getAllInfluencer();
    allInfluencer.value = influencerStore.allInfluencer;
};

const getAllSponsor = async () => {
    await sponsorStore.getAllSponsors();
    allSponsors.value = sponsorStore.allSponsors;
};

const getAllCampaign = async () => {
    let result = await campaignStore.getAllCampaign();
    allCampaign.value = result.allCampaignsData;
};

const getAllRequest = async () => {
    let result = await requestStore.getAllRequest();
    allRequest.value = result.allRequestData;

    if (userType === 'sponsor') {
        acceptedRequests.value = result.allRequestData.filter(req => req.status === 'accepted').length;
        rejectedRequests.value = result.allRequestData.filter(req => req.status === 'rejected').length;
        pendingRequests.value = result.allRequestData.filter(req => req.status === 'pending').length;
    } else if (userType === 'influencer') {
        sentRequests.value = result.allRequestData.filter(req => req.senderType === 'influencer').length;
        acceptedRequests.value = result.allRequestData.filter(req => req.status === 'accepted' && req.senderType === 'influencer').length;
        rejectedRequests.value = result.allRequestData.filter(req => req.status === 'rejected' && req.senderType === 'influencer').length;
        receivedRequests.value = result.allRequestData.filter(req => req.receiverType === 'influencer').length;
    }
};

onMounted(async () => {
    await getAllUsers();
    await getAllInfluencer();
    await getAllSponsor();
    await getAllCampaign();
    await getAllRequest();
});
</script>

<style scoped>
.statistics-container {
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    max-width: 600px;
    margin: 0 auto;
}

h2 {
    text-align: center;
    font-size: 24px;
    color: #333;
    margin-bottom: 20px;
}

.stats-section {
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.stat-item {
    display: flex;
    justify-content: space-between;
    background-color: #fff;
    padding: 10px 15px;
    border-radius: 5px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.stat-label {
    font-weight: bold;
    color: #555;
}

.stat-value {
    font-size: 18px;
    color: #000;
}
</style>