<template>
    <div>
        <div class="container-fluid">
            <div class="row">
                <table class="table table-striped">
                    <tr>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Action</th>
                    </tr>
                    <tr v-for="user in allUsers" :key="user.id">
                        <td>{{ user.name }}</td>
                        <td>{{ user.email }}</td>
                        <td><button class="btn btn-sm btn-warning pe-3 ps-3">View</button></td>
                    </tr>
                </table>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useUserStore } from '@/stores/userStore';
import { useCampaignStore } from '@/stores/campaignStore';
import { onMounted, ref } from 'vue'

const campaignStore = useCampaignStore();
const userStore = useUserStore();
let allCampaign = ref([]);
let allUsers = ref([])

const getCampaign = (async () => {
    let result = await campaignStore.getAllCampaign();
    allCampaign.value = result.allCampaignsData
})

const getUsers = (async () => {
    await userStore.getAlluser();
    allUsers.value  = userStore.alluser.filter( i => 
        i.userType != 'admin'
    )
})

onMounted(async () => {
    await getCampaign();
    await getUsers();
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