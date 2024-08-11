<template>
    <div>
        <div class="container-fluid">
            <div class="col">
                <div class="col">
                    <button class="btn btn-success btn-lg mt-3 pe-5 ps-5" @click="openModal2()">Request</button>
                    <component :is="requestModal" :request="currentSelectedRequest" @close="closeModal2"
                        v-if="isModal2Visible">
                    </component>
                </div>
            </div>
            <div class="row mb-5 p-3">
                <div class="col-md-6 col-lg-6 col-sm-12 border border-light rounded p-5">
                    <h3 class="text-light">Pending Request</h3>
                    <div class="myTableCont">
                        <table class="table table-striped" v-if="pendingSponsor.length > 0">
                            <tr>
                                <th>Id</th>
                                <th>Name</th>
                                <th>Email</th>
                                <th>Action</th>
                            </tr>
                            <tr v-for="user in pendingSponsor" :key="user.id">
                                <td>{{ user.id }}</td>
                                <td>{{ user.name }}</td>
                                <td>{{ user.email }}</td>
                                <td><button class="btn btn-sm btn-warning pe-3 ps-3"
                                        @click="openModal(user)">View</button>
                                </td>
                                <component :is="userUpdateModal" :user="currentSelectedUser" @close="closeModal"
                                    v-if="isModalVisible">
                                </component>
                                <td><button class="btn btn-sm btn-warning pe-3 ps-3"
                                        @click="approved(user)">Approve</button></td>
                                <td><button class="btn btn-sm btn-danger pe-3 ps-3"
                                        @click="blockedUser(user)">Block</button></td>
                            </tr>
                        </table>
                        <p v-else>No new request</p>
                    </div>
                </div>
                <div class="col-md-6 col-lg-6 col-sm-12 border border-light rounded p-5">
                    <h3 class="text-light">Blocked users</h3>
                    <div class="myTableCont">
                        <table class="table table-striped" v-if="blockedUsers.length > 0">
                            <tr>
                                <th>Id</th>
                                <th>Name</th>
                                <th>Email</th>
                                <th>Action</th>
                            </tr>
                            <tr v-for="user in blockedUsers" :key="user.id">
                                <td>{{ user.id }}</td>
                                <td>{{ user.name }}</td>
                                <td>{{ user.email }}</td>
                                <td><button class="btn btn-sm btn-warning pe-3 ps-3 me-3"
                                        @click="openModal(user)">View</button>
                                    <component :is="userUpdateModal" :user="currentSelectedUser" @close="closeModal"
                                        v-if="isModalVisible">
                                    </component>
                                    <button class="btn btn-sm btn-danger pe-3 ps-3"
                                        @click="UnBlockedUser(user)">UnBlock</button>
                                </td>
                            </tr>
                        </table>
                        <p v-else>No blocked user</p>
                    </div>
                </div>
                <div class="col-md-12 col-lg-12 col-sm-12 border border-light rounded p-5">
                    <h2 class="text-light">All users</h2>
                    <div class="myTableCont">
                        <table class="table table-striped" v-if="approvedUsers.length > 0">
                            <tr>
                                <th>Id</th>
                                <th>Name</th>
                                <th>Email</th>
                                <th>Action</th>
                            </tr>
                            <tr v-for="user in approvedUsers" :key="user.id">
                                <td>{{ user.id }}</td>
                                <td>{{ user.name }}</td>
                                <td>{{ user.email }}</td>
                                <td><button class="btn btn-sm btn-warning pe-5 ps-5 me-5"
                                        @click="openModal(user)">View</button>

                                    <component :is="userUpdateModal" :user="currentSelectedUser" @close="closeModal"
                                        v-if="isModalVisible">
                                    </component>
                                    <button class="btn btn-sm btn-danger pe-5 ps-5"
                                        @click="blockedUser(user)">Block</button>
                                </td>
                            </tr>
                        </table>
                        <p v-else>No user</p>
                    </div>
                </div>
            </div>
            <div class="row m-5 p-3">
                <div class="col-md-12 col-lg-12 col-sm-12 border rounded p-5">

                    <h2 class="text-light">Campaigns</h2>
                    <div class="myTableCont">
                        <table class="table table-striped" v-if="allCampaign.length > 0">
                            <tr>
                                <th>Id</th>
                                <th>Name</th>
                                <th>Budget</th>
                                <th>Description</th>
                                <th>Goal</th>
                                <th>Visibility</th>
                                <th>Start date</th>
                                <th>End date</th>
                                <th>Action</th>
                            </tr>
                            <tr v-for="campaign in allCampaign" :key="campaign.id">
                                <td>{{ campaign.id }}</td>
                                <td>{{ campaign.name }}</td>
                                <td>{{ campaign.campaignBudget }}</td>
                                <td>{{ campaign.description }}</td>
                                <td>{{ campaign.goal }}</td>
                                <td>{{ campaign.visibility }}</td>
                                <td>{{ campaign.startDate }}</td>
                                <td>{{ campaign.endDate }}</td>
                                <td><button class="btn btn-sm btn-warning pe-3 ps-3"
                                        @click="blocked(campaign)">Block</button></td>
                            </tr>
                        </table>
                        <p v-else>No campaign</p>
                    </div>
                </div>

                <div class="col-md-12 col-lg-12 col-sm-12 border rounded p-5">
                    <h3 class="text-light">Blocked campaigns</h3>
                    <div class="myTableCont">
                        <table class="table table-striped" v-if="blockedCampaign.length > 0">
                            <tr>
                                <th>Id</th>
                                <th>Name</th>
                                <th>Budget</th>
                                <th>Description</th>
                                <th>Goal</th>
                                <th>Visibility</th>
                                <th>Start date</th>
                                <th>End date</th>
                                <th>Action</th>
                            </tr>
                            <tr v-for="campaign in blockedCampaign" :key="campaign.id">
                                <td>{{ campaign.id }}</td>
                                <td>{{ campaign.name }}</td>
                                <td>{{ campaign.campaignBudget }}</td>
                                <td>{{ campaign.description }}</td>
                                <td>{{ campaign.goal }}</td>
                                <td>{{ campaign.visibility }}</td>
                                <td>{{ campaign.startDate }}</td>
                                <td>{{ campaign.endDate }}</td>
                                <td><button class="btn btn-sm btn-warning pe-3 ps-3"
                                        @click="UnBlocked(campaign)">Unblock</button></td>
                            </tr>
                        </table>
                        <p v-else>No campaign</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useUserStore } from '@/stores/userStore';
import { useCampaignStore } from '@/stores/campaignStore';
import { onMounted, ref, defineAsyncComponent, shallowRef } from 'vue';
import { useRequestStore } from '../stores/requestStore';
import { useSponsorStore } from '../stores/sponsorStore';
import { useInfluencerStore } from '../stores/influencerStore'

const campaignStore = useCampaignStore();
const userStore = useUserStore();
const requestStore = useRequestStore();
const sponsorStore = useSponsorStore();
const influencerStore = useInfluencerStore();
let allCampaign = ref([]);
let blockedCampaign = ref([]);
let pendingSponsor = ref([]);
let approvedUsers = ref([]);
let allRequest = ref([]);
let blockedUsers = ref([]);

const getCampaign = (async () => {
    let result = await campaignStore.getAllCampaign();
    allCampaign.value = result.allCampaignsData.filter(i =>
        i.flag == false
    )
    blockedCampaign.value = result.allCampaignsData.filter(i =>
        i.flag == true
    )
})

const getUsers = (async () => {
    await userStore.getAlluser();
    pendingSponsor.value = userStore.alluser.filter(i =>
        i.status == "pending" &&
        i.flag == false
    )
    approvedUsers.value = userStore.alluser.filter(i =>
        i.status == "approved" &&
        i.userType != "admin" &&
        i.flag == false
    )
    blockedUsers.value = userStore.alluser.filter(i =>
        i.flag == true
    )
})

const getRequest = (async () => {
    let request = await requestStore.getAllRequest();
    allRequest.value = request.allRequestData
})

const approved = (async (user) => {
    user.status = "approved"
    await userStore.updateUser(user);
    await getUsers();
})

const blockedUser = (async (user) => {
    user.flag = true
    await userStore.updateUser(user)
    await getUsers();
})

const UnBlockedUser = (async (user) => {
    user.flag = false
    await userStore.updateUser(user)
    await getUsers();
})

const blocked = (async (campaign) => {
    campaign.flag = true
    await campaignStore.updateCampaign(campaign)
    await getCampaign();
})

const UnBlocked = (async (campaign) => {
    campaign.flag = false
    await campaignStore.updateCampaign(campaign)
    await getCampaign();
})

onMounted(async () => {
    await getCampaign();
    await getUsers();
    await getRequest();
})

// View Modal 

const isModalVisible = shallowRef(false);
const userUpdateModal = shallowRef(null);
const currentSelectedUser = ref(null);

const openModal = (async (user) => {
    if (user.userType == "sponsor") {
        let result = await sponsorStore.getSponsorById(user.id);
        currentSelectedUser.value = { ...result.sponsor };
    }
    if (user.userType == "influencer") {
        let result = await influencerStore.getInfluencerById(user.id);
        currentSelectedUser.value = { ...result.influencer };
    }

    userUpdateModal.value = defineAsyncComponent(() => import("../components/UserDetailsCardModal.vue"))
    isModalVisible.value = true;
});

const closeModal = (async () => {
    currentSelectedUser.value = null;
    isModalVisible.value = false;
    userUpdateModal.value = null;
});

//Request view Modal

const isModal2Visible = shallowRef(false);
const requestModal = shallowRef(null);
const currentSelectedRequest = ref(null);

const openModal2 = (async () => {
    currentSelectedRequest.value = { ...allRequest.value };
    requestModal.value = defineAsyncComponent(() => import("../components/RequestViewModal.vue"))
    isModal2Visible.value = true;
});

const closeModal2 = (async () => {
    currentSelectedRequest.value = null;
    isModal2Visible.value = false;
    requestModal.value = null;
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

.myTableCont {
    overflow-x: auto;
    max-height: 50dvh;
    overflow-y: auto;
}

table {
    width: 100%;
    border: 2px solid #000;
    border-collapse: collapse;
    border-spacing: 0;
}

th,
td {
    padding: 10px;
    text-align: center;
    color: #000;
    border: 2px solid #000;
}

th {
    color: #fff;
    background-color: #000;
}
</style>