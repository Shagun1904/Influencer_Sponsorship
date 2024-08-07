<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 offset-md-3 col-lg-6 offset-lg-3 col-sm-6 offset-sm-3">
                <div id="signup" class="mt-5 mb-5">
                    <img src="../assets/logo1.png" alt="" id="img" class="mx-auto d-block">
                    <div id="signupform">
                        <h3>Signup Page</h3>
                        <div>
                            <Form class="form" @submit="onSubmit" :validation-schema="schema" v-slot="{ errors, isSubmitting }">
                                <div class="mb-3">
                                    <label for="name" class="form-label">Name: </label>
                                    <Field type="text" name="name" class="form-control" v-model="userData.name" :class="{ 'is-invalid': errors.name }" />
                                    <div class="invalid-feedback">{{ errors.name }}</div>
                                </div>
                                <div class="mb-3">
                                    <label for="email" class="form-label">E-mail: </label>
                                    <Field type="email" name="email" class="form-control" v-model="userData.email" :class="{ 'is-invalid': errors.email }" />
                                    <div class="invalid-feedback">{{ errors.email }}</div>
                                </div>

                                <div class="mb-3">
                                    <label for="userType" class="form-label">User Type:</label>
                                    <Field as="select" id="userType" name="userType" class="form-control" v-model="userData.userType" :class="{ 'is-invalid': errors.userType }">
                                        <option disabled value="">Select option</option>
                                        <option value="sponsor">Sponsor</option>
                                        <option value="influencer">Influencer</option>
                                    </Field>
                                    <div class="invalid-feedback">{{ errors.userType }}</div>
                                </div>
                                <div class="mb-3">
                                    <label for="password" class="form-label">Password: </label>
                                    <Field name="password" type="password" class="form-control" :class="{ 'is-invalid': errors.password }" v-model="userData.password" />
                                    <div class="invalid-feedback">{{ errors.password }}</div>
                                </div>
                                <button class="btn btn-lg btn-danger" :disabled="isSubmitting">Sign up</button>
                            </Form>
                        </div>
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



import {useUserStore} from '../stores/userStore'; 

const userData= reactive({
    name: ref(null),
    email: ref(null),
    userType: ref(null),
    password: ref(null),
})

const userStore= useUserStore();

const schema = Yup.object().shape({
    name: Yup.string().required('Name is required'),
    email: Yup.string().email().required('E-mail is required'),
    password: Yup.string().required('Password is required').min(3, 'Password must be at least 3 characters'),
    userType: Yup.string().required('Select user type') 
})

const onSubmit= (()=>{
    userStore.signup(userData);
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
