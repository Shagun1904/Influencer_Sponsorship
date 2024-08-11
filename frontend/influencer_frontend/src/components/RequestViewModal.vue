<template>
    <teleport to="body">
        <div v-if="isVisible" class="modal-overlay" @click.self="closeModal">
            <div class="modal-content">
                <div class="modal-header d-flex mb-3">
                    <h2 class="modal-title text-danger text-center">All Requests</h2>
                    <button type="button" class="btn-close ms-auto" @click="closeModal"></button>
                </div>
                <div class="modal-body">
                    <table class="table table-bordered">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Message</th>
                                <th>Requirement</th>
                                <th>Payment Amount</th>
                                <th>Status</th>
                                <th>Sent By</th>
                                <th>Influencer Id</th>
                                <th>Campaign Id</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(request, index) in requestArray" :key="index">
                                <td>{{ request.id }}</td>
                                <td>{{ request.message }}</td>
                                <td>{{ request.requirement }}</td>
                                <td>{{ request.paymentAmount }}</td>
                                <td>{{ request.status }}</td>
                                <td>{{ request.sendBy }}</td>
                                <td>{{ request.influencer_id }}</td>
                                <td>{{ request.campaign_id }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </teleport>
</template>

<script setup>
import { ref, defineProps, defineEmits, computed } from 'vue';

const props = defineProps({
    request: {
        type: Object,
        required: true,
    }
});

const isVisible = ref(true);

const emits = defineEmits(['close']);

const closeModal = () => {
    isVisible.value = false;
    emits('close');
};

const requestArray = computed(() => Object.values(props.request));
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
    max-width: 1200px;
    max-height: 400dvh;
    overflow-y: auto;
    overflow-x: auto;
}

.table {
    width: 100%;
    margin-bottom: 1rem;
    color: #212529;
    border-collapse: collapse;
}

.table th,
.table td {
    padding: 0.75rem;
    vertical-align: top;
    border-top: 1px solid #dee2e6;
}

.table th {
    text-align: inherit;
    background-color: #f8f9fa;
}
</style>