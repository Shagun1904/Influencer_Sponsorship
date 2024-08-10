<template>
    <teleport to="body">
        <div v-if="isVisible" class="modal-overlay" @click.self="closeModal">
            <div class="modal-content">
                <div class="modal-header d-flex mb-3">
                    <h3 class="modal-title text-danger">Update Details</h3>
                    <button type="button" class="btn-close ms-auto" @click="closeModal"></button>
                </div>
                <div class="modal-body">
                    <Form @submit="submitUpdateForm">
                        <div class="mb-3">
                            <label for="category">Category</label>
                            <Field type="text" name="category" class="form-control" placeholder="Category"
                                v-model="userData.category" disabled />
                        </div>
                        <div class="mb-3">
                            <label for="category">Niche</label>
                            <Field type="text" name="niche" class="form-control" placeholder="Niche"
                                v-model="userData.niche" disabled />
                        </div>
                        <div class="mb-3">
                            <label for="category">Reach</label>
                            <Field type="number" name="reach" class="form-control" placeholder="Reach"
                                v-model="userData.reach" disabled />
                        </div>
                        <div class="mb-3">
                            <label for="url" class="form-label mb-3">Social media links:</label>
                            <input type="url" name="furl" id="furl" placeholder="Facebook" class="form-control mb-3"
                                v-model="userData.furl" disabled>
                            <input type="url" name="iurl" id="iurl" placeholder="Instagram" class="form-control mb-3"
                                v-model="userData.iurl" disabled>
                            <input type="url" name="lurl" id="lurl" placeholder="LinkedIn" class="form-control mb-3"
                                v-model="userData.lurl" disabled>
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