import { createWebHistory, createRouter } from "vue-router";

import LoginPage from "@/components/LoginPage.vue";

const routes =[

    {
        name: 'LoginPage',
        component: LoginPage,
        path: '/'
    },
    {
        name: 'SignupPage',
        component: () => import("../components/SignupPage.vue"),
        path: '/signup'
    },
    {
        name: 'InfluencerHome',
        component:() => import("../components/InfluencerHome.vue"),
        path: '/influencer/home'
    },
    {
        name: 'SponsorHome',
        component:()=> import("../components/SponsorHome.vue"),
        path: '/sponsor/home'
    },
    {
        name: 'AdminHome',
        component:()=> import("../components/AdminHome.vue"),
        path: '/admin'
    },
    {
        name: 'ProfileDetails',
        component:()=> import("../components/ProfileDetails.vue"),
        path: '/influencer/profile'
    },
    {
        name: 'AllRequest',
        component:()=> import("../components/AllRequest.vue"),
        path: '/request'
    },
    {
        name: 'SponsorRegistration',
        component:()=> import("../components/SponsorRegistration.vue"),
        path: '/sponsor/registration'
    },
    {
        name: 'InfluencerRegistration',
        component:()=> import("../components/InfluencerRegistration.vue"),
        path: '/influencer/registration'
    },
    {
        name: 'AddCampaign',
        component:()=> import("../components/AddCampaign.vue"),
        path: '/sponsor/campaign'
    },
    {
        name: 'AddRequest',
        component:()=> import("../components/AddRequest.vue"),
        path: '/request/:id'
    },
    {
        name: 'ViewCampaign',
        component:()=> import("../components/ViewCampaign.vue"),
        path: '/view'
    },
    {
        name: 'StatisticsPage',
        component:()=> import("../components/StatisticsPage.vue"),
        path: '/stats'
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router