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
                            <Field type="text" name="category" class="form-control" placeholder="Category"
                                v-model="userData.category" :class="{ 'is-invalid': errors.category }" />
                            <div class="invalid-feedback">{{ errors.category }}</div>
                        </div>
                        <div class="mb-3">
                            <Field type="text" name="niche" class="form-control" placeholder="Niche"
                                v-model="userData.niche" :class="{ 'is-invalid': errors.niche }" />
                            <div class="invalid-feedback">{{ errors.niche }}</div>
                        </div>
                        <div class="mb-3">
                            <Field type="number" name="reach" class="form-control" placeholder="Reach"
                                v-model="userData.reach" :class="{ 'is-invalid': errors.reach }" />
                            <div class="invalid-feedback">{{ errors.reach }}</div>
                        </div>
                        <div class="mb-3">
                                    <label for="url" class="form-label mb-3">Social media links:</label>
                                    <input type="url" name="furl" id="furl" placeholder="Facebook"
                                        class="form-control mb-3" v-model="userData.furl">
                                    <input type="url" name="iurl" id="iurl" placeholder="Instagram"
                                        class="form-control mb-3" v-model="userData.iurl">
                                    <input type="url" name="lurl" id="lurl" placeholder="LinkedIn"
                                        class="form-control mb-3" v-model="userData.lurl">
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
    influencer: {
        type: Object,
        required: true,
    }
})

const isVisible = ref(true)

const userData = reactive({
    id: ref(props.influencer.id),
    category: ref(props.influencer.category),
    niche: ref(props.influencer.niche),
    reach: ref(props.influencer.reach),
    furl: ref(props.influencer.furl),
    iurl: ref(props.influencer.iurl),
    lurl: ref(props.influencer.lurl),
    user_id: ref(props.influencer.user_id)
})

const schema = Yup.object().shape({
    category: Yup.string().required('category is required'),
    niche: Yup.string().required('Niche is required'),
    reach: Yup.number().required('Number of followers is required for better reach.'),
    furl: Yup.string(),
    iurl: Yup.string(),
    lurl: Yup.string()
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