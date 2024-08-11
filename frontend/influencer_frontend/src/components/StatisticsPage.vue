<template>
    <div>
        <div>
            <PieChart :chart-data="chartData" :chart-options="chartOptions" />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { PieChart } from 'vue-chartjs';
import { useUserStore } from '../stores/userStore';
import { useInfluencerStore } from '../stores/influencerStore';
import { useSponsorStore } from '../stores/sponsorStore';
import { useCampaignStore } from '../stores/campaignStore';
import { useRequestStore } from '../stores/requestStore';
import { Chart as ChartJS, BarElement, LineElement, ArcElement, CategoryScale, LinearScale, Tooltip, Legend } from 'chart.js';

ChartJS.register(BarElement, LineElement, ArcElement, CategoryScale, LinearScale, Tooltip, Legend);

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

// const adminChartData = ref({});
// const sponsorChartData = ref({});
// const influencerChartData = ref({});

// const userType = localStorage.getItem('userType');

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
};

const chartData = ref({
    labels: ['Users', 'Sponsors', 'Influencers', 'Campaigns', 'Requests'],
    datasets: [{
        label: 'Overview',
        data: [0, 0, 0, 0, 0], // Initial empty data
        backgroundColor: [
            'rgb(255, 99, 132)',  // Red
            'rgb(54, 162, 235)',  // Blue
            'rgb(201, 203, 207)', // Grey
            'rgb(255, 205, 86)',  // Yellow
            'rgb(75, 192, 192)'   // Green
        ],
        hoverOffset: 4
    }]
});

const chartOptions = ref({
    responsive: true,
    plugins: {
        legend: {
            position: 'top',
        },
        title: {
            display: true,
            text: 'Data Overview'
        }
    }
});


const fetchData = async () => {
    await Promise.all([
        getAllUsers(),
        getAllInfluencer(),
        getAllSponsor(),
        getAllCampaign(),
        getAllRequest()
    ]);

    chartData.value.datasets[0].data = [
        userStore.alluser.length,
        sponsorStore.allSponsors.length,
        influencerStore.allInfluencer.length,
        // campaignStore.allCampaignsData.length,
        // requestStore.allRequestData.length
    ];
};

// const setupSponsorChart = () => {
//     const accepted = allRequest.value.filter(req => req.status == 'accepted').length;
//     const rejected = allRequest.value.filter(req => req.status == 'rejected').length;
//     const pending = allRequest.value.filter(req => req.status == 'pending').length;

//     sponsorChartData.value = {
//         labels: ['Accepted', 'Rejected', 'Pending'],
//         datasets: [
//             {
//                 label: 'Request Status',
//                 data: [accepted, rejected, pending],
//                 backgroundColor: ['#36a2eb', '#ff6384', '#ffce56'],
//             },
//         ],
//     };
// };

// const setupInfluencerChart = () => {
//     const sentRequests = allRequest.value.filter(req => req.sentBy === userStore.currentUser.id).length;
//     const acceptedRequests = allRequest.value.filter(req => req.sentBy === userStore.currentUser.id && req.status === 'accepted').length;
//     const receivedRequests = allRequest.value.filter(req => req.receivedBy === userStore.currentUser.id).length;

//     influencerChartData.value = {
//         labels: ['Sent Requests', 'Accepted Requests', 'Received Requests'],
//         datasets: [
//             {
//                 label: 'Requests',
//                 data: [sentRequests, acceptedRequests, receivedRequests],
//                 backgroundColor: ['#ff6384', '#36a2eb', '#cc65fe'],
//             },
//         ],
//     };
// };

onMounted(async () => {
    await getAllUsers();
    await getAllInfluencer();
    await getAllSponsor();
    await getAllCampaign();
    await getAllRequest();
    // setupAdminChart();
    await fetchData();
    // if (userType == 'admin') {
    //     setupAdminChart();
    // } else if (userType == 'sponsor') {
    //     setupSponsorChart();
    // } else if (userType == 'influencer') {
    //     setupInfluencerChart();
    // }
});

</script>

<style scoped>
/* Add any custom styles if needed */
</style>