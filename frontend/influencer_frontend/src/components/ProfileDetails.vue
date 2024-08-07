<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 offset-md-3 col-lg-6 offset-lg-3 col-sm-10 offset-sm-1">
                <h2 class="text-center text-white mt-5">Profile Details</h2>
                <div class="mycont m-5 p-5">
                    <form @submit.prevent="moreDetails">
                        <div class="mb-3">
                            <label for="category">Category</label>
                            <input type="text" name="category" class="form-control" v-model="category">
                        </div>

                        <div class="mb-3">
                            <label for="niche">Niche</label>
                            <input type="text" name="niche" class="form-control" v-model="niche">
                        </div>

                        <div class="mb-3">
                            <label for="reach">Reach</label>
                            <input type="number" name="reach" class="form-control" v-model="reach">
                        </div>
                        <div class="mb-3">
                            <div class="mb-3">
                                <label for="url" class="form-label mb-3">Social media links:</label>
                                <input type="url" name="furl" id="furl" pattern="https://.*" placeholder="Facebook"
                                    class="form-control mb-3" v-model="furl">
                                <input type="url" name="iurl" id="iurl" pattern="https://.*" placeholder="Instagram"
                                    class="form-control mb-3" v-model="iurl">
                                <input type="url" name="lurl" id="lurl" pattern="https://.*" placeholder="LinkedIn"
                                    class="form-control mb-3" v-model="lurl">
                            </div>
                        </div>
                        <div class="d-grid">
                            <button type="submit" class="btn btn-success" >Update</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
// import { createToaster } from '@meforma/vue-toaster';
export default {
    name: 'ProfileDetails',
    setup() {
        return {
            category: "",
            niche: "",
            reach: "",
            furl: "",
            iurl: "",
            lurl: "",
        };
    },
    methods: {
        async moreDetails() {
            try {
                let result = await axios.post(`http://127.0.0.1:5000/influencer`,
                    {
                        category: this.category,
                        niche: this.niche,
                        reach: this.reach,
                        furl: this.furl,
                        iurl: this.iurl,
                        lurl: this.lurl,
                        user_id: localStorage.getItem("user_id"),
                    });
                let data = result.data
                console.log(data);
                this.$router.push("/influencer/home")
            }
            catch (error) {
                console.log(error)
            }
        }
    }}
</script>
<style scoped>
.myprofilepic {
    width: 30dvh;
    height: 30dvh;
    border-radius: 50%;
    margin: 2dvh;
    box-shadow: 2px 2px 5px #712458, 2px 2px 5px #BF2F2C;
}

.mycont {
    border-radius: 20px;
    box-shadow: 2px 2px 5px #000;
    background-color: rgba(255, 255, 255, 0.7);
}
</style>