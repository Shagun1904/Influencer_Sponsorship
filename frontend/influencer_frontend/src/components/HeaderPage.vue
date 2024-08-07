<template>
    <nav class="mynav navbar navbar-expand-lg bg-body-tertiary" v-if="userlogged">
        <div class="container-fluid">
            <a class="navbar-brand" href="{{ userType }}/home">IE&SC</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0" v-if="userType === 'influencer'">
                    <li class="nav-item">
                        <router-link class="nav-link active" to="/influencer/home">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/influencer/request">Request</router-link>
                    </li>
                </ul>
                <ul class="navbar-nav me-auto mb-2 mb-lg-0" v-if="userType === 'sponsor'">
                    <li class="nav-item">
                        <router-link class="nav-link active" to="/sponsor/home">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/view">Campaign</router-link>
                    </li>
                </ul>
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item dropdown pe-5">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                            aria-expanded="false">
                            {{ name }}
                        </a>
                        <ul class="dropdown-menu mydropdown" v-if="userType === 'influencer'">
                            <li> <router-link to="/influencer/profile" class="dropdown-item"> Profile </router-link>
                            </li>
                            <li><a class="dropdown-item" href="#">Stats</a></li>
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <li><a class="dropdown-item" v-on:click="logout">Logout</a></li>
                        </ul>
                        <ul class="dropdown-menu mydropdown" v-if="userType === 'sponsor'">
                            <li> <router-link to="/sponsor/profile" class="dropdown-item"> Profile </router-link>
                            </li>
                            <li><a class="dropdown-item" href="#">Stats</a></li>
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <li><a class="dropdown-item" v-on:click="logout">Logout</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute();
const router = useRouter();
const userType = localStorage.getItem('userType')
const name = localStorage.getItem('name')

const userlogged = computed(() => {
    if (route.path == '/' || route.path == '/signup' || route.path == '/sponsor/registration' || route.path == '/influencer/registration') {
        return false;
    }
    else {
        return true;
    }
})

function logout() {
    localStorage.clear();
    router.push({ name: 'LoginPage' })
}



</script>

<style scoped>
.mydropdown {
    right: 2%;
    left: auto;
    box-shadow: 2px 2px 5px #000;
}

.mynav {
    box-shadow: 2px 2px 5px #000;
}
</style>
