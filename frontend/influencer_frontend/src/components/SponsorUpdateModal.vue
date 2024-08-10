<template>
    <teleport to="body">
        <div v-if="isVisible" class="modal-overlay" @click.self="closeModal">
            <div class="modal-content">
                <div class="modal-header d-flex mb-3">
                    <h3 class="modal-title text-danger">Update Details</h3>
                    <button type="button" class="btn-close ms-auto" @click="closeModal"></button>
                </div>
                <div class="modal-body">
                    <Form @submit="submitUpdateForm" :validation-schema="schema"
                        v-slot="{ errors, isSubmitting }">
                        <div class="mb-3">
                            <Field type="text" name="companyName" class="form-control" placeholder="Company name"
                                v-model="userData.companyName" :class="{ 'is-invalid': errors.companyName }" />
                            <div class="invalid-feedback">{{ errors.companyName }}</div>
                        </div>
                        <div class="mb-3">
                            <Field type="text" name="industry" class="form-control" placeholder="Industry"
                                v-model="userData.industry" :class="{ 'is-invalid': errors.industry }" />
                            <div class="invalid-feedback">{{ errors.industry }}</div>
                        </div>
                        <div class="mb-3">
                            <Field type="number" name="budget" class="form-control" placeholder="Budget"
                                v-model="userData.budget" :class="{ 'is-invalid': errors.budget }" />
                            <div class="invalid-feedback">{{ errors.budget }}</div>
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
    sponsor: {
        type: Object,
        required: true,
    }
})

const isVisible = ref(true)

const userData = reactive({
    id: ref(props.sponsor.id),
    companyName: ref(props.sponsor.companyName),
    industry: ref(props.sponsor.industry),
    budget: ref(props.sponsor.budget),
    user_id: ref(props.sponsor.user_id)
})

const schema = Yup.object().shape({
    companyName: Yup.string().required('Company Name is required'),
    industry: Yup.string().required('Industry is required'),
    budget: Yup.number().min(100,'Must be equal to or greater than 100').required('Budget is required')
})

const emits = defineEmits(['close', 'submit']);

const closeModal = () => {
    isVisible.value = false;
    emits('close');
};

const submitUpdateForm = (() => {
    emits('submit', userData);
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