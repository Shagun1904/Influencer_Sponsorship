<template>
    <teleport to="body">
        <div v-if="isVisible" class="modal-overlay" @click.self="closeModal">
            <div class="modal-content">
                <div class="modal-header d-flex mb-3">
                    <h3 class="modal-title text-danger">Update Request</h3>
                    <button type="button" class="btn-close ms-auto" @click="closeModal"></button>
                </div>
                <div class="modal-body">
                    <Form @submit="submitUpdateForm" :validation-schema="schema"
                        v-slot="{ errors, isSubmitting }">
                        <div class="mb-3">
                            <Field type="text" name="message" class="form-control" placeholder="Message"
                                v-model="requestData.message" :class="{ 'is-invalid': errors.message }" />
                            <div class="invalid-feedback">{{ errors.message }}</div>
                        </div>
                        <div class="mb-3">
                            <Field type="text" name="requirement" class="form-control" placeholder="Requirement"
                                v-model="requestData.requirement" :class="{ 'is-invalid': errors.requirement }" />
                            <div class="invalid-feedback">{{ errors.requirement }}</div>
                        </div>
                        <div class="mb-3">
                            <Field type="number" name="payment" class="form-control" placeholder="Payment"
                                v-model="requestData.paymentAmount" :class="{ 'is-invalid': errors.payment }" />
                            <div class="invalid-feedback">{{ errors.payment }}</div>
                        </div>
                        <div><button class="btn btn-danger" :disabled="isSubmitting">Update</button>
                        </div>
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
    adRequest: {
        type: Object,
        required: true,
    }
})


const isVisible = ref(true)

const requestData = reactive({
    id: ref(props.adRequest.id),
    message: ref(props.adRequest.message),
    requirement: ref(props.adRequest.requirement),
    paymentAmount: ref(props.adRequest.paymentAmount),
    status: ref(props.adRequest.status),
    sendBy: ref(props.adRequest.sendBy),
    campaign_id: ref(props.adRequest.campaign_id),
    influencer_id: ref(props.adRequest.influencer_id)
})


const schema = Yup.object().shape({
    message: Yup.string().required('Message is required'),
    requirement: Yup.string().required('Requirement is required'),
    payment: Yup.number().required('Payment is required'),
})


const emits = defineEmits(['close', 'submit']);

const closeModal = () => {
    isVisible.value = false;
    emits('close');
};

const submitUpdateForm = (() => {
    emits('submit', requestData);
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