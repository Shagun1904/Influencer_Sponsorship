<template>
    <teleport to="body">
        <div v-if="isVisible" class="modal-overlay" @click.self="closeModal">
            <div class="modal-content">
                <div class="modal-header d-flex mb-3">
                    <h3 class="modal-title text-danger">Negotiate Request</h3>
                    <button type="button" class="btn-close ms-auto" @click="closeModal"></button>
                </div>
                <div class="modal-body">
                    <Form @submit="submitUpdateForm" :validation-schema="schema"
                        v-slot="{ errors, isSubmitting }">
                        <div class="mb-3">
                            <Field type="text" name="message" class="form-control" placeholder="Message"
                                v-model="requestData.message" :class="{ 'is-invalid': errors.message }" :disabled="isInfluencer"/>
                            <div class="invalid-feedback">{{ errors.message }}</div>
                        </div>
                        <div class="mb-3">
                            <Field type="text" name="requirement" class="form-control" placeholder="Requirement"
                                v-model="requestData.requirement" :class="{ 'is-invalid': errors.requirement }" :disabled="isInfluencer" />
                            <div class="invalid-feedback">{{ errors.requirement }}</div>
                        </div>
                        <div class="mb-3">
                            <Field type="number" name="payment" class="form-control" placeholder="Payment"
                                v-model="requestData.paymentAmount" :class="{ 'is-invalid': errors.payment }" />
                            <div class="invalid-feedback">{{ errors.payment }}</div>
                        </div>
                        <div><button class="btn btn-danger" :disabled="isSubmitting">Negotiate</button>
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
const userType = localStorage.getItem('userType')

const props = defineProps({
    negotiateAdRequest: {
        type: Object,
        required: true,
    }
})

const isInfluencer = (()=>{
    if (userType == "sponsor"){
        return false
    }
    else { return true }
})

const isVisible = ref(true)

const requestData = reactive({
    id: ref(props.negotiateAdRequest.id),
    message: ref(props.negotiateAdRequest.message),
    requirement: ref(props.negotiateAdRequest.requirement),
    paymentAmount: ref(props.negotiateAdRequest.paymentAmount),
    status: "Negotiate",
    sendBy: localStorage.getItem('userType'),
    campaign_id: ref(props.negotiateAdRequest.campaign_id),
    influencer_id: ref(props.negotiateAdRequest.influencer_id)
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