<template>
    <teleport to="body">
        <div v-if="isVisible" class="modal-overlay" @click.self="closeModal">
            <div class="modal-content">
                <div class="modal-header d-flex mb-3">
                    <h2 class="modal-title text-danger text-center">User Details</h2>
                    <button type="button" class="btn-close ms-auto" @click="closeModal"></button>
                </div>
                <div class="modal-body">
                    <div v-if="props.user.companyName">
                        <h4><strong>Sponsor Id </strong> {{ props.user.id }}</h4>
                        <h4><strong>Company name: </strong> {{ props.user.companyName }}</h4>
                        <h4><strong>Industry: </strong> {{ props.user.industry }}</h4>
                        <h4><strong>Budget: </strong> {{ props.user.budget }}</h4>
                    </div>
                    <div v-if="props.user.niche">
                        <h4><strong>Influencer Id: </strong> {{ props.user.id }}</h4>
                        <h4><strong>Category: </strong> {{ props.user.category }}</h4>
                        <h4><strong>Reach: </strong> {{ props.user.reach }}</h4>
                        <h4><strong>Niche: </strong> {{ props.user.niche }}</h4>
                        <h4>Links: <a href="{{ props.user.furl }}">Facebook</a>, 
                            <a href="{{ props.user.iurl }}">Instagram</a>, 
                            <a href="{{ props.user.lurl }}">Linkedin</a></h4>
                    </div>
                </div>
            </div>
        </div>
    </teleport>
</template>

<script setup>
import { defineEmits, ref, defineProps } from 'vue';
// import { Form, Field } from 'vee-validate';

const props = defineProps({
    user: {
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