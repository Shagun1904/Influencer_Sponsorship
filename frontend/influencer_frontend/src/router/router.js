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
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router