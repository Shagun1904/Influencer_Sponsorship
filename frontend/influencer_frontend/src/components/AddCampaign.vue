<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 offset-md-3 col-lg-6 offset-lg-3 col-sm-6 offset-sm-3">
                <div id="signup" class="mt-5 mb-5">
                    <div id="signupform">
                        <h3>Campaign Form</h3>
                        <div>
                            <Form class="form" @submit="onSubmit" :validation-schema="schema" v-slot="{ errors, isSubmitting }">
                                <div class="mb-3">
                                    <label for="name" class="form-label">Campaign Name: </label>
                                    <Field type="text" name="name" class="form-control" v-model="campaignData.name" :class="{ 'is-invalid': errors.name }" />
                                    <div class="invalid-feedback">{{ errors.name }}</div>
                                </div>
                                <div class="mb-3">
                                    <label for="description" class="form-label">Description: </label>
                                    <Field type="text" name="description" class="form-control" v-model="campaignData.description" :class="{ 'is-invalid': errors.description }" />
                                    <div class="invalid-feedback">{{ errors.description }}</div>
                                </div>
                                <div class="mb-3">
                                    <label for="startDate" class="form-label">Start date: </label>
                                    <Field type="date" name="startDate" class="form-control" v-model="campaignData.startDate" :class="{ 'is-invalid': errors.startDate }" />
                                    <div class="invalid-feedback">{{ errors.startDate }}</div>
                                </div>
                                <div class="mb-3">
                                    <label for="endDate" class="form-label">End date: </label>
                                    <Field type="date" name="endDate" class="form-control" v-model="campaignData.endDate" :class="{ 'is-invalid': errors.endDate }" />
                                    <div class="invalid-feedback">{{ errors.endDate }}</div>
                                </div>
                                <div class="mb-3">
                                    <label for="campaignBudget" class="form-label">Campaign Budget: </label>
                                    <Field type="number" name="campaignBudget" class="form-control" v-model="campaignData.campaignBudget" :class="{ 'is-invalid': errors.campaignBudget }" />
                                    <div class="invalid-feedback">{{ errors.campaignBudget }}</div>
                                </div>
                                <div class="mb-3">
                                    <label for="visibility" class="form-label">Visibility:</label>
                                    <Field as="select" id="visibility" name="visibility" class="form-control" v-model="campaignData.visibility" :class="{ 'is-invalid': errors.visibility }">
                                        <option disabled value="">Select option</option>
                                        <option value="public">Public</option>
                                        <option value="private">Private</option>
                                    </Field>
                                    <div class="invalid-feedback">{{ errors.visibility }}</div>
                                </div>
                                <div class="mb-3">
                                    <label for="goal" class="form-label">Goal: </label>
                                    <Field name="goal" type="text" class="form-control" :class="{ 'is-invalid': errors.goal }" v-model="campaignData.goal" />
                                    <div class="invalid-feedback">{{ errors.goal }}</div>
                                </div>
                                <button class="btn btn-lg btn-danger" :disabled="isSubmitting">Add Campaign</button>
                            </Form>
                            <button class="btn btn-lg btn-info"> <router-link to="/view"> view </router-link> </button>
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



import {useCampaignStore} from '../stores/campaignStore'; 

const campaignData= reactive({
    name: ref(null),
    description: ref(null),
    startDate: ref(null),
    endDate: ref(null),
    campaignBudget: ref(null),
    visibility: ref(null),
    goal: ref(null),
    flag: ref(false),
})

const campaignStore= useCampaignStore();

const schema = Yup.object().shape({
    name: Yup.string().required('Name is required'),
    description: Yup.string().required('Description is required'),
    startDate: Yup.string().required('Date is required'),
    endDate: Yup.string().required('Date is required'), 
    campaignBudget: Yup.number().required('Budget is required'), 
    visibility: Yup.string().required('Visibility is required'), 
    goal: Yup.string().required('Goal is required')
})

const onSubmit= (()=>{
    campaignStore.campaignData(campaignData);
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
