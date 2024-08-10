<template>
    <div>
        <div class="container-fluid">
            <div>
                <button class="btn m-3"
                    :class="{ 'btn-light': activeStatus !== 'Pending', 'btn-primary': activeStatus === 'Pending' }"
                    @click="setStatus('Pending')">Pending</button>
                <button class="btn m-3"
                    :class="{ 'btn-light': activeStatus !== 'Accepted', 'btn-primary': activeStatus === 'Accepted' }"
                    @click="setStatus('Accepted')">Accept</button>
                <button class="btn m-3"
                    :class="{ 'btn-light': activeStatus !== 'Rejected', 'btn-primary': activeStatus === 'Rejected' }"
                    @click="setStatus('Rejected')">Reject</button>
                <button class="btn m-3"
                    :class="{ 'btn-light': activeStatus !== 'Negotiate', 'btn-primary': activeStatus === 'Negotiate' }"
                    @click="setStatus('Negotiate')">Negotiate</button>
            </div>
            <div class="row" v-for="request in filteredRequests" :key="request.id">
                <div v-if="request.sendBy == 'sponsor'">
                    <div class="col-md-12 col-lg-12 col-sm-12">
                        <div class="card mb-3">
                            <div class="card-body">
                                <div v-if="request.status == 'Rejected'"><button class="btn btn-danger mb-1" disabled>Rejected</button></div>
                                <div v-if="request.status == 'Negotiate'"><button class="btn btn-primary mb-1" disabled>Negotiate again</button></div>
                                <p class="card-text"><strong>Message: </strong>{{ request.message }}</p>
                                <p class="card-text"><strong>Requirement: </strong>{{ request.requirement }}</p>
                                <p class="card-text"><strong>Payment: </strong>{{ request.paymentAmount }}</p>
                            </div>
                            <div class="card-footer" v-if="request.status !== 'Rejected'">
                                <div class="d-flex">
                                    <button class="btn btn-success m-2" @click="requestAccepted(request)">Accept</button>
                                    <button class="btn btn-warning m-2" @click="openNegotiateModal(request)">Negotiate</button>
                                    <component :is="requestNegotiateModal" :negotiateAdRequest="currentNegotiateAdRequest"
                                        @close="closeNegotiateModal" v-if="isNegotiateModalVisible" @submit="handleNegotiateModalSubmit">
                                    </component>
                                    <button class="btn btn-danger m-2 ms-auto" @click="requestRejected(request)">Reject</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div v-if="request.sendBy == 'influencer'">
                    <div class="col-md-12 col-lg-12 col-sm-12">
                        <div class="card mb-3">
                            <div class="card-body">
                                <div v-if="request.status !== 'Pending'"><button class="btn btn-secondary mb-1" disabled>You {{ request.status }}</button></div>
                                <div v-if="request.status == 'Pending'"><button class="btn btn-secondary mb-1" disabled>You Requested</button></div>
                                
                                <p class="card-text"><strong>Message: </strong>{{ request.message }}</p>
                                <p class="card-text"><strong>Requirement: </strong>{{ request.requirement }}</p>
                                <p class="card-text"><strong>Payment: </strong>{{ request.paymentAmount }}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useRequestStore } from '@/stores/requestStore';
import { ref, onMounted, computed, defineAsyncComponent, shallowRef, reactive } from 'vue';

const userType = localStorage.getItem('userType')
const currentUserId = localStorage.getItem(userType + '_id')
const requestStore = useRequestStore();
let allRequest = ref([]);
let activeStatus = ref('Pending');  // Initially set to 'Pending'

const updateRequestList = async () => {
    let result = await requestStore.getAllRequest();
    allRequest.value = result.allRequestData.filter(i =>
        i.influencer_id == currentUserId
    );
};

const setStatus = (status) => {
    activeStatus.value = status;
};

// Filter requests based on activeStatus
const filteredRequests = computed(() => {
    return allRequest.value.filter(request => request.status === activeStatus.value);
});

onMounted(async () => {
    await updateRequestList();
});

//Accept request

const requestAccepted = (async (request)=>{
    const formData = reactive({
    id: ref(request.id),
    message: ref(request.message),
    requirement: ref(request.requirement),
    paymentAmount: ref(request.paymentAmount),
    status: "Accepted",
    sendBy: localStorage.getItem('userType'),
    campaign_id: ref(request.campaign_id),
    influencer_id: ref(request.influencer_id)
})
    await requestStore.updateRequest(formData);
    await updateRequestList();
})

//Reject Request

const requestRejected = (async (request)=>{
    const formData = reactive({
    id: ref(request.id),
    message: ref(request.message),
    requirement: ref(request.requirement),
    paymentAmount: ref(request.paymentAmount),
    status: "Rejected",
    sendBy: localStorage.getItem('userType'),
    campaign_id: ref(request.campaign_id),
    influencer_id: ref(request.influencer_id)
})
    await requestStore.updateRequest(formData);
    await updateRequestList();
})

//Negotiate Modal

const isNegotiateModalVisible = shallowRef(false);
const requestNegotiateModal = shallowRef(null);
const currentNegotiateAdRequest = ref(null);

const openNegotiateModal = (adRequest) => {
    currentNegotiateAdRequest.value = { ...adRequest };
    requestNegotiateModal.value = defineAsyncComponent(() => import("../components/RequestNegotiate.vue"))
    isNegotiateModalVisible.value = true;
};

const closeNegotiateModal = (async () => {
    currentNegotiateAdRequest.value = null;
    isNegotiateModalVisible.value = false;
    requestNegotiateModal.value = null;
    await updateRequestList();
});

const handleNegotiateModalSubmit = (async (formData) => {
    requestStore.updateRequest(formData);
    closeNegotiateModal();
    await updateRequestList();
});

</script>

<style scoped></style>