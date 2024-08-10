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
                            <Field type="text" name="name" class="form-control" placeholder="Name"
                                v-model="userData.name" :class="{ 'is-invalid': errors.name }" disabled/>
                            <div class="invalid-feedback">{{ errors.name }}</div>
                        </div>
                        <div class="mb-3">
                            <Field type="email" name="email" class="form-control" placeholder="E-mail"
                                v-model="userData.email" :class="{ 'is-invalid': errors.email }" />
                            <div class="invalid-feedback">{{ errors.email }}</div>
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
    user: {
        type: Object,
        required: true,
    }
})

const isVisible = ref(true)

const userData = reactive({
    id: ref(props.user.id),
    name: ref(props.user.name),
    email: ref(props.user.email),
    userType: ref(props.user.userType),
    password: ref(props.user.password)
})

const schema = Yup.object().shape({
    name: Yup.string().required('Name is required'),
    email: Yup.string().required('E-mail is required'),
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