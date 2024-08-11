<template>
    <div>
        <div class="container-fluid">
            <div class="row">
                <div class="col">
                    <div class="col-lg-3">
                        <h3 class="text-light">Pending Request</h3>
                        <table class="table table-striped" v-if="pendingSponsor.length > 0">
                            <tr>
                                <th>Name</th>
                                <th>Email</th>
                                <th>Action</th>
                            </tr>
                            <tr v-for="user in pendingSponsor" :key="user.id">
                                <td>{{ user.name }}</td>
                                <td>{{ user.email }}</td>
                                <td><button class="btn btn-sm btn-warning pe-3 ps-3" @click="approved(user)">Approve</button></td>
                            </tr>
                        </table>
                        <h2 v-else>No new request</h2>
                    </div>
                </div>
                <div class="col">
                    <div class="col-lg-3">
                        <h2 class="text-light">All users</h2>
                        <table class="table table-striped" v-if="approvedUsers.length > 0">
                            <tr>
                                <th>Name</th>
                                <th>Email</th>
                                <th>Action</th>
                            </tr>
                            <tr v-for="user in approvedUsers" :key="user.id">
                                <td>{{ user.name }}</td>
                                <td>{{ user.email }}</td>
                                <td><button class="btn btn-sm btn-warning pe-3 ps-3" @click="blockedUser(user)">Block</button></td>
                            </tr>
                        </table>
                        <h2 v-else>No user</h2>
                    </div>
                </div>
                <div class="col">
                    <div class="col-lg-3">
                        <h2 class="text-light">All users</h2>
                        <table class="table table-striped" v-if="allCampaign.length > 0">
                            <tr>
                                <th>Name</th>
                                <th>Email</th>
                                <th>Action</th>
                            </tr>
                            <tr v-for="campaign in allCampaign" :key="campaign.id">
                                <td>{{ campaign.name }}</td>
                                <td>{{ campaign.email }}</td>
                                <td><button class="btn btn-sm btn-warning pe-3 ps-3" @click="blocked(campaign)">Block</button></td>
                            </tr>
                        </table>
                        <h2 v-else>No campaign</h2>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useUserStore } from '@/stores/userStore';
import { useCampaignStore } from '@/stores/campaignStore';
import { onMounted, ref } from 'vue';
import { useRequestStore } from '../stores/requestStore'

const campaignStore = useCampaignStore();
const userStore = useUserStore();
const requestStore = useRequestStore();
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
        i.status == "pending"
    )
    approvedUsers.value = userStore.alluser.filter(i =>
        i.status == "approved" &&
        i.userType != "admin"
    )
    blockedUsers.value = userStore.alluser.filter(i =>
        i.flag == true
    )
})

const getRequest = (async ()=>{
    let request= await requestStore.getAllRequest();
    allRequest.value = request.allRequestData
})

const approved = (async (user)=>{
    user.status = "approved"
    await userStore.updateUser(user);
    await getUsers();
})

const blockedUser = (async (user)=>{
    user.flag = true
    await userStore.updateUser(user)
    await getUsers();
})

onMounted(async () => {
    await getCampaign();
    await getUsers();
    await getRequest();
})

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