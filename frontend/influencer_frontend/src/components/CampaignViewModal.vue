<template>
    <teleport to="body">
        <div v-if="isVisible" class="modal-overlay" @click.self="closeModal">
            <div class="modal-content">
                <div class="modal-header d-flex mb-3">
                    <h2 class="modal-title text-danger text-center">Campaign Details</h2>
                    <button type="button" class="btn-close ms-auto" @click="closeModal"></button>
                </div>
                <div class="modal-body">
                    <h4><strong>Category: </strong> {{ props.campaign[0].name }}</h4>
                    <h4><strong>Description: </strong> {{ props.campaign[0].description }}</h4>
                    <h4><strong>Goal: </strong> {{ props.campaign[0].goal }}</h4>
                    <h4><strong>Campaign Budget: </strong> {{ props.campaign[0].campaignBudget }}</h4>
                    <h4><strong>Start Date: </strong> {{ props.campaign[0].startDate }}</h4>
                    <h4><strong>End Date: </strong> {{ props.campaign[0].endDate }}</h4>
                </div>
            </div>
        </div>
    </teleport>
</template>

<script setup>
import { defineEmits, ref, defineProps } from 'vue';
// import { Form, Field } from 'vee-validate';

const props = defineProps({
    campaign: {
        type: Object,
        required: true,
    }

})

const isVisible = ref(true)

const emits = defineEmits(['close', 'submit']);

const closeModal = () => {
    isVisible.value = false;
    emits('close');
};



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