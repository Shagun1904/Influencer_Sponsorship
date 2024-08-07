<template>
    <teleport to="body">
        <div v-if="isVisible" class="modal-overlay" @click.self="closeModal">
            <div class="modal-content">
                <div class="modal-header d-flex mb-3">
                    <h3 class="modal-title text-danger">Update Campaign</h3>
                    <button type="button" class="btn-close ms-auto" @click="closeModal"></button>
                </div>
                <div class="modal-body">
                    <Form class="form" @submit="submitUpdateForm" :validation-schema="schema"
                        v-slot="{ errors, isSubmitting }">
                        <div class="mb-3">
                            <label for="name" class="form-label">Campaign Name: </label>
                            <Field type="text" name="name" class="form-control" v-model="campaignData.name"
                                :class="{ 'is-invalid': errors.name }" />
                            <div class="invalid-feedback">{{ errors.name }}</div>
                        </div>
                        <div class="mb-3">
                            <label for="description" class="form-label">Description: </label>
                            <Field type="text" name="description" class="form-control"
                                v-model="campaignData.description" :class="{ 'is-invalid': errors.description }" />
                            <div class="invalid-feedback">{{ errors.description }}</div>
                        </div>
                        <div class="mb-3">
                            <label for="startDate" class="form-label">Start date: </label>
                            <Field type="date" name="startDate" class="form-control" v-model="campaignData.startDate"
                                :class="{ 'is-invalid': errors.startDate }" />
                            <div class="invalid-feedback">{{ errors.startDate }}</div>
                        </div>
                        <div class="mb-3">
                            <label for="endDate" class="form-label">End date: </label>
                            <Field type="date" name="endDate" class="form-control" v-model="campaignData.endDate"
                                :class="{ 'is-invalid': errors.endDate }" />
                            <div class="invalid-feedback">{{ errors.endDate }}</div>
                        </div>
                        <div class="mb-3">
                            <label for="campaignBudget" class="form-label">Campaign Budget: </label>
                            <Field type="number" name="campaignBudget" class="form-control"
                                v-model="campaignData.campaignBudget"
                                :class="{ 'is-invalid': errors.campaignBudget }" />
                            <div class="invalid-feedback">{{ errors.campaignBudget }}</div>
                        </div>
                        <div class="mb-3">
                            <label for="visibility" class="form-label">Visibility:</label>
                            <Field as="select" id="visibility" name="visibility" class="form-control"
                                v-model="campaignData.visibility" :class="{ 'is-invalid': errors.visibility }">
                                <option disabled value="">Select option</option>
                                <option value="public">Public</option>
                                <option value="private">Private</option>
                            </Field>
                            <div class="invalid-feedback">{{ errors.visibility }}</div>
                        </div>
                        <div class="mb-3">
                            <label for="goal" class="form-label">Goal: </label>
                            <Field name="goal" type="text" class="form-control" :class="{ 'is-invalid': errors.goal }"
                                v-model="campaignData.goal" />
                            <div class="invalid-feedback">{{ errors.goal }}</div>
                        </div>
                        <button class="btn btn-success" :disabled="isSubmitting">Update</button>
                    </Form>
                </div>
            </div>
        </div>
    </teleport>
</template>

<script setup>
import { defineEmits, ref, reactive, defineProps } from 'vue';
import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';

const props = defineProps({
    campaign: {
        type: Object,
        required: true,
    }
})


const isVisible = ref(true)

const campaignData = reactive({
    id: ref(props.campaign.id),
    name: ref(props.campaign.name),
    description: ref(props.campaign.description),
    startDate: ref(props.campaign.startDate),
    endDate: ref(props.campaign.endDate),
    campaignBudget: ref(props.campaign.campaignBudget),
    visibility: ref(props.campaign.visibility),
    goal: ref(props.campaign.goal),
    sponsor_id: ref(props.campaign.sponsor_id)
})


const schema = Yup.object().shape({
    name: Yup.string().required('Name is required'),
    description: Yup.string().required('Description is required'),
    startDate: Yup.string().required('Date is required'),
    endDate: Yup.string().required('Date is required'),
    campaignBudget: Yup.number().required('Budget is required'),
    visibility: Yup.string().required('Visibility is required'),
    goal: Yup.string().required('Goal is required')
})


const emits = defineEmits(['close', 'submit']);

const closeModal = () => {
    isVisible.value = false;
    emits('close');
};

const submitUpdateForm = (() =>{
    emits('submit', campaignData);
    closeModal();
})
</script>

<style scoped>
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal-content {
    background: white;
    padding: 20px;
    border-radius: 5px;
    width: 90%;
    max-width: 500px;
    max-height: 80dvh;
    overflow-y: scroll;
}
</style>