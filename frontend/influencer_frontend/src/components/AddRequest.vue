<template>
    <div class="container-fluid">
        <div class="row p-4">
            <div class="col-md-12 col-lg-12 col-sm-12">
                <div>
                    <h3 class="text-light" v-if="userType == 'sponsor'" >Add Request</h3>
                    <h3 class="text-light" v-if="userType == 'influencer'" >Send Request</h3>
                    <div class="bg-light bg-gradient p-3 rounded">
                        <div>
                            <Form class="form row" @submit="onSubmit" :validation-schema="schema"
                                v-slot="{ errors, isSubmitting }">
                                <div class="mb-3 col-md-3">
                                    <Field type="text" name="message" class="form-control" placeholder="Message"
                                        v-model="requestData.message" :class="{ 'is-invalid': errors.message }" />
                                    <div class="invalid-feedback">{{ errors.message }}</div>
                                </div>
                                <div class="mb-3 col-md-3">
                                    <Field type="text" name="requirement" class="form-control" placeholder="Requirement"
                                        v-model="requestData.requirement"
                                        :class="{ 'is-invalid': errors.requirement }" />
                                    <div class="invalid-feedback">{{ errors.requirement }}</div>
                                </div>
                                <div class="mb-3 col-md-2">
                                    <Field type="number" name="payment" class="form-control" placeholder="Payment"
                                        v-model="requestData.payment" :class="{ 'is-invalid': errors.payment }" />
                                    <div class="invalid-feedback">{{ errors.payment }}</div>
                                </div>
                                <div class="mb-3 col-md-3 d-flex" v-if="userType == 'influencer'">
                                    <Field type="number" name="influencer_id" class="form-control"
                                    v-model="requestData.influencer_id" disabled></Field>
                                </div>
                                <div v-if="userType =='influencer'">
                                    <button class="btn btn-danger ms-2 col-md-4" :disabled="isSubmitting">Send</button>
                                </div>
                                <div class="mb-3 col-md-3 d-flex" v-if="userType == 'sponsor'">
                                    <Field type="number" name="influencer_id" class="form-control"
                                        placeholder="Influencer" v-model="requestData.influencer_id"
                                        :class="{ 'is-invalid': errors.influencer_id }" disabled />
                                    <div class="invalid-feedback">{{ errors.influencer_id }}</div>
                                    <button class="btn btn-warning ms-2" @click="openSearchModal()"
                                        type="button">Find</button>
                                    <component :is="searchModal" @close="closeSearchModal" v-if="isSearchModalVisible"
                                        @assign="handleAssign">
                                    </component>
                                </div>
                                <div class="col-md-4"><button class="btn btn-danger" :disabled="isSubmitting" v-if="userType == 'sponsor'">Add
                                        request</button></div>
                            </Form>
                        </div>
                    </div>
                </div>
            </div>
            <h3 class="text-light mt-4">Campaign Details</h3>
            <div class="col-md-12 col-lg-12 col-sm-12">
                <div class="card mt-2 border border-dark">
                    <div class="card-header text-center bg-dark">
                        <h3 class="fw-bold text-light"> {{ campaign.name }}</h3>
                        <p class="text-light" v-if="userType == 'sponsor'">{{ campaign.visibility }}</p>
                        <h6 class="fw-bold text-light"> Budget: {{ campaign.campaignBudget }} </h6>
                        <p class="card-text fst-italic text-light"> {{ campaign.goal }} </p>
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">Description</h5>
                        <p class="card-text"> {{ campaign.description }}</p>
                    </div>
                    <div class="card-footer text-body-secondary d-flex justify-content-around">
                        <p>Start date: {{ campaign.startDate }}</p>
                        <p>End date: {{ campaign.endDate }} </p>
                    </div>
                    <div class="card-footer text-body-secondary myCardFooter" v-if="userType == 'sponsor'">
                        <h5 class="fw-bolder" v-if="requestSendBySponsor.length>0">Request sent by you</h5>
                        <table class="table table-bordered myTable" v-if="requestSendBySponsor.length>0">
                            <tr>
                                <th>Message</th>
                                <th>Requirements</th>
                                <th>Payment</th>
                                <th>Assignee</th>
                                <th>Status</th>
                                <th>Action</th>
                            </tr>
                            <tr v-for="request in requestSendBySponsor" :key="request.id">
                                <td class="table-info" >{{ request.message }}</td>
                                <td class="table-info" >{{ request.requirement }}</td>
                                <td class="table-info" >{{ request.paymentAmount }}</td>
                                <td class="table-info" >{{ request.influencer_id }}</td>
                                <td class="table-info" >{{ request.status }}</td>
                                <td><button class="btn btn-warning m-2" @click="openModal(request)" 
                                    v-if="request.status !== 'Rejected'">Update</button>
                                    <component :is="requestUpdateModal" :adRequest="currentSelectedAdRequest"
                                        @close="closeModal" v-if="isModalVisible" @submit="handleModalSubmit">
                                    </component>
                                    <button class="btn btn-danger m-2" @click="deleteRequest(request.id)">Delete</button>
                                </td>
                            </tr>
                        </table>
                        <h5 class="fw-bolder" v-if="requestSendByInfluencer.length>0">Received Request</h5>
                        <table class="table table-light" v-if="requestSendByInfluencer.length>0">
                            <tr>
                                <th>Message</th>
                                <th>Requirements</th>
                                <th>Payment</th>
                                <th>Assignee</th>
                                <th>Status</th>
                                <th>Action</th>
                            </tr>
                            <tr v-for="request in requestSendByInfluencer" :key="request.id">
                                <td>{{ request.message }}</td>
                                <td>{{ request.requirement }}</td>
                                <td>{{ request.paymentAmount }}</td>
                                <td>{{ request.influencer_id }}</td>
                                <td>{{ request.status }}</td>
                                <td><button class="btn btn-info" @click="openNegotiateModal(request)">Negotiate</button>
                                    <component :is="requestNegotiateModal" :negotiateAdRequest="currentNegotiateAdRequest"
                                        @close="closeNegotiateModal" v-if="isNegotiateModalVisible" @submit="handleNegotiateModalSubmit">
                                    </component>
                                    <button class="btn btn-danger m-2" @click="requestRejected(request)">Reject</button>
                                    <button class="btn btn-success" @click="requestAccepted(request)">Accept</button>
                                </td>
                            </tr>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';
import { reactive, ref, onMounted, shallowRef, defineAsyncComponent } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useRequestStore } from '../stores/requestStore';
import { useCampaignStore } from '../stores/campaignStore';

const requestStore = useRequestStore();
const campaignStore = useCampaignStore();
const route = useRoute();
const myRouter = useRouter();
const campaign = ref({});
const userType= localStorage.getItem('userType')
let requestSendBySponsor = ref([]);
let requestSendByInfluencer = ref([]);

// Influencer


//Sponsor
const requestData = reactive({
    message: ref(null),
    requirement: ref(null),
    payment: ref(null),
    influencer_id: ref(null),
    sponsor_id: ref(null)
})

const schema = Yup.object().shape({
    message: Yup.string().required('Message is required'),
    requirement: Yup.string().required('Requirement is required'),
    payment: Yup.number().required('Payment is required'),
    influencer_id: Yup.number().required('Select influencer to create request')
})

let allAdRequest = ref([])

const onSubmit = (async () => {
    let res = await requestStore.requestData(requestData);
    allAdRequest.value.push(res);
    myRouter.push('/request/' + route.params.id);
})

onMounted(async () => {
    let result = await campaignStore.getCampaignById(route.params.id);
    campaign.value = result.campaign;
    await updateRequestListForSponsor();
    if (userType =='influencer'){
        requestData.influencer_id = localStorage.getItem('influencer_id')
    }
})

const updateRequestListForSponsor = (async () => {
    let result = await requestStore.getAllAdRequestByCampaignId();
    requestSendBySponsor.value = result.allAdRequestData.filter(i => i.sendBy == "sponsor");
    requestSendByInfluencer.value = result.allAdRequestData.filter(i => i.sendBy == "influencer");
})

const deleteRequest = (async (id) => {
    await requestStore.deleteRequestById(id);
    allAdRequest.value = allAdRequest.value.filter(request => request.id !== id);
    myRouter.push('/request/' + route.params.id);
})

//search modal

const isSearchModalVisible = shallowRef(false);
const searchModal = shallowRef(null);
const selectedInfluencerId = ref(null);

const openSearchModal = () => {
    searchModal.value = defineAsyncComponent(() => import("../components/SearchModal.vue"))
    isSearchModalVisible.value = true;
};

const closeSearchModal = (async () => {
    selectedInfluencerId.value = null;
    isSearchModalVisible.value = false;
    searchModal.value = null;
});

const handleAssign= ( async (influencer_id)=>{
    requestData.influencer_id= influencer_id;
    closeSearchModal();
});

//request modal

const isModalVisible = shallowRef(false);
const requestUpdateModal = shallowRef(null);
const currentSelectedAdRequest = ref(null);

const openModal = (adRequest) => {
    currentSelectedAdRequest.value = { ...adRequest };
    requestUpdateModal.value = defineAsyncComponent(() => import("../components/RequestUpdateModal.vue"))
    isModalVisible.value = true;
};

const closeModal = (async () => {
    currentSelectedAdRequest.value = null;
    isModalVisible.value = false;
    requestUpdateModal.value = null;
    await updateRequestListForSponsor();
});

const handleModalSubmit = (async (formData) => {
    await requestStore.updateRequest(formData);
    closeModal();
    await updateRequestListForSponsor();
});

//Negotiate Request

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
    await updateRequestListForSponsor();
});

const handleNegotiateModalSubmit = (async (formData) => {
    await requestStore.updateRequest(formData);
    closeNegotiateModal();
    await updateRequestListForSponsor();
});

//Request actions 

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
    await updateRequestListForSponsor();
})

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
    await updateRequestListForSponsor();
})

</script>

<style scoped>
.myCardFooter {
    min-height: 50dvh;
    max-height: 50dvh;
    overflow-y: scroll;
}
</style>
