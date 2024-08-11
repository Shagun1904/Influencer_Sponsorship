<template>
    <teleport to="body">
        <div v-if="isVisible" class="modal-overlay" @click.self="closeModal">
            <div class="modal-content">
                <div class="modal-header d-flex mb-3">
                    <h3 class="modal-title text-danger">Search</h3>
                    <button type="button" class="btn-close ms-auto" @click="closeModal"></button>
                </div>
                <div class="modal-body">
                    <Form @submit="submitSearchForm" :validation-schema="schema" v-slot="{ errors, isSubmitting }">
                        <div class="mb-3">
                            <Field type="text" name="search" class="form-control" placeholder="Search here.."
                                v-model="searchData.search" :class="{ 'is-invalid': errors.search }" />
                            <div class="invalid-feedback">{{ errors.search }}</div>
                        </div>
                        <div><button class="btn btn-danger" :disabled="isSubmitting">Search</button>
                        </div>
                    </Form>
                    <div v-if="searchedData.length>0">
                        <h3>Your Search result</h3>
                        <div>
                            <table class="table table-responsive table-bordered">
                                <tr>
                                    <th>Id</th>
                                    <th>Name</th>
                                    <th>Category</th>
                                    <th>Niche</th>
                                    <th>Reach</th>
                                </tr>
                                <tr v-for="data in searchedData1" :key="data.id">
                                    <td>{{ data.id }}</td>
                                    <td>{{ data.name }}</td>
                                    <td>{{ data.category }}</td>
                                    <td>{{ data.niche }}</td>
                                    <td>{{ data.reach }}</td>
                                    <button class="btn btn-warning btn-sm m-1" @click="assignInflu(data.id)" >Assign</button>
                                </tr>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </teleport>
</template>

<script setup>
import { defineEmits, ref, reactive } from 'vue';
import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';
import { useInfluencerStore } from '../stores/influencerStore';
import { useUserStore } from '../stores/userStore';

const isVisible = ref(true)
const influencerStore = useInfluencerStore();
const userStore = useUserStore();

const searchData = reactive({
    search: ref(null)
})

const searchedData = ref([])

const schema = Yup.object().shape({
    search: Yup.string().required('Write what you want to search'),
})

const emits = defineEmits(['close', 'submit', 'assign']);

const closeModal = () => {
    isVisible.value = false;
    emits('close');
};

const submitSearchForm = (async () => {
    await influencerStore.getAllInfluencer();
    const searchLower = searchData.search.toLowerCase();
    searchedData.value = influencerStore.allInfluencer.filter(i =>
        i.niche.toLowerCase().includes(searchLower) ||
        i.category.toLowerCase().includes(searchLower)
    );
    getInfluencersDetails();
});

const searchedData1 = ref([]);

async function getInfluencersDetails() {
    searchedData1.value = []
    for (const i in searchedData.value) {
        let res = await userStore.getUserById(searchedData.value[i].user_id);
        let combineData = {
            ...res.userData,
            ...searchedData.value[i]
        }
        searchedData1.value.push(combineData);
    }
}

const assignInflu= ((id)=> {
    emits('assign', id)
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
