<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 offset-md-3 col-lg-6 offset-lg-3 col-sm-6 offset-sm-3">
                <div id="signup" class="mt-5 mb-5">
                    <img src="../assets/logo1.png" alt="" id="img" class="mx-auto d-block">
                    <div id="signupform">
                        <h3>Additional Details</h3>
                        <div>
                            <Form class="form" @submit="onSubmit" :validation-schema="schema"
                                v-slot="{ errors, isSubmitting }">
                                <div class="mb-3">
                                    <label for="category" class="form-label">Category </label>
                                    <Field type="text" name="category" class="form-control" v-model="userData.category"
                                        :class="{ 'is-invalid': errors.category }" />
                                    <div class="invalid-feedback">{{ errors.category }}</div>
                                </div>
                                <div class="mb-3">
                                    <label for="niche" class="form-label">Niche </label>
                                    <Field type="text" name="niche" class="form-control" v-model="userData.niche"
                                        :class="{ 'is-invalid': errors.niche }" />
                                    <div class="invalid-feedback">{{ errors.niche }}</div>
                                </div>
                                <div class="mb-3">
                                    <label for="reach" class="form-label">Reach </label>
                                    <Field name="reach" type="number" class="form-control"
                                        :class="{ 'is-invalid': errors.reach }" v-model="userData.reach" />
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
                                <button type="submit" class="btn btn-lg btn-danger" :disabled="isSubmitting">Sign
                                    up</button>
                            </Form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';
import { reactive, ref } from 'vue';



import { useInfluencerStore } from '../stores/influencerStore';

const userData = reactive({
    category: ref(null),
    niche: ref(null),
    reach: ref(null),
    furl: ref(null),
    iurl: ref(null),
    lurl: ref(null)
})

const influencerStore = useInfluencerStore();

const schema = Yup.object().shape({
    category: Yup.string().required('category is required'),
    niche: Yup.string().required('Niche is required'),
    reach: Yup.number().required('Number of followers is required for better reach.'),
    furl: Yup.string(),
    iurl: Yup.string(),
    lurl: Yup.string()
})

const onSubmit = (() => {
    influencerStore.influencerDetails(userData);
})

</script>

<style scoped>
#signup {
    min-width: 50vh;
    min-height: 85vh;
    overflow: hidden;
    background-color: rgb(253, 253, 253);
    border-radius: 10px;
    box-shadow: 3px 3px 10px #000;
}

#signupform {
    padding: 3% 3%;
}

#mycont {
    text-decoration: none;
    color: rgb(255, 255, 255);
}

#img {
    width: 50%;
    height: 280px;
}
</style>
