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
                                    <label for="companyName" class="form-label">Company Name: </label>
                                    <Field type="text" name="companyName" class="form-control" v-model="userData.companyName" :class="{ 'is-invalid': errors.companyName }" />
                                    <div class="invalid-feedback">{{ errors.companyName }}</div>
                                </div>
                                <div class="mb-3">
                                    <label for="industryType" class="form-label">Industry Type: </label>
                                    <Field type="text" name="industryType" class="form-control" v-model="userData.industryType" :class="{ 'is-invalid': errors.industryType }" />
                                    <div class="invalid-feedback">{{ errors.industryType }}</div>
                                </div>
                                <div class="mb-3">
                                    <label for="budget" class="form-label">Budget: </label>
                                    <Field name="budget" type="number" class="form-control" :class="{ 'is-invalid': errors.budget }" v-model="userData.budget" />
                                    <div class="invalid-feedback">{{ errors.budget }}</div>
                                </div>
                                <button type="submit" class="btn btn-lg btn-danger" :disabled="isSubmitting">Sign up</button>
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



import {useSponsorStore} from '../stores/sponsorStore'; 

const userData= reactive({
    companyName: ref(null),
    industryType: ref(null),
    budget: ref(null),
})

const sponsorStore= useSponsorStore();

const schema = Yup.object().shape({
    companyName: Yup.string().required('Company Name is required'),
    industryType: Yup.string().required('Industry type is required'),
    budget: Yup.number().min(100,'Must be equal to or greater than 100').required('Budget is required')
})

const onSubmit= (()=>{
    sponsorStore.sponsorDetails(userData);
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
