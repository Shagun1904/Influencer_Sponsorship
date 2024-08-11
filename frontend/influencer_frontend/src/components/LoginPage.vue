<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 offset-md-3 col-lg-6 offset-lg-3 col-sm-6 offset-sm-3">
                <div id="login" class="mt-5 mb-5">
                    <img src="../assets/logo1.png" alt="" id="img" class="mx-auto d-block">
                    <div id="loginform">
                        <h3>Login</h3>
                        <div>
                            <Form @submit="login" class="form" :validation-schema="schema" v-slot="{ errors, isSubmitting }">
                                <div class="mb-3">
                                    <label for="email" class="form-label">E-mail: </label>
                                    <Field type="email" name="email" class="form-control" id="email" v-model="userData.email" :class="{ 'is-invalid': errors.email }" />
                                    <div class="invalid-feedback">{{ errors.email }}</div>
                                </div>
                                <div class="mb-3">
                                    <label for="password" class="form-label">Password: </label>
                                    <Field type="password" name="password" class="form-control" id="password" v-model="userData.password" :class="{ 'is-invalid': errors.password }" />
                                    <div class="invalid-feedback">{{ errors.password }}</div>
                                </div>
                                <button class="btn btn-lg btn-primary" :disabled="isSubmitting">
                                    Submit
                                </button>
                            </form>
                        </div>
                        
                        <p class="mt-4">New user?<RouterLink to="/signup" style="text-decoration: none;"> Sign up
                            </RouterLink>instead</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';
import { reactive, ref } from 'vue';

import { useUserStore } from '@/stores/userStore';

const userData= reactive({
    email: ref(null),
    password: ref(null),
})

const schema = Yup.object().shape({
    email: Yup.string().email().required('E-mail is required'),
    password: Yup.string().required('Password is required').min(3, 'Password must be at least 3 characters'),
})

const loginStore = useUserStore();

const login=(async()=>{
    await loginStore.login(userData);
})

</script>

<style scoped>
#login {
    min-width: 50vh;
    min-height: 85vh;
    overflow: hidden; 
    background-color: rgb(253, 253, 253);
    border-radius: 10px;
    box-shadow: 3px 3px 10px #000;
}

#loginform {
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
