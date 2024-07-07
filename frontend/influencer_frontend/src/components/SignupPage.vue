<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 offset-md-3 col-lg-6 offset-lg-3 col-sm-6 offset-sm-3">
                <div id="signup" class="mt-5 mb-5">
                    <img src="../assets/img1.jpg" alt="" id="img">
                    <div id="signupform">
                        <h3>Signup Page</h3>
                        <div>
                            <form action="" class="form">
                                <div class="mb-3">
                                    <label for="name" class="form-label">Name: </label>
                                    <input type="text" name="name" class="form-control">
                                </div>
                                <div class="mb-3">
                                    <label for="e-mail" class="form-label">E-mail: </label>
                                    <input type="email" name="e-mail" class="form-control">
                                </div>
                                <div class="mb-3">
                                    <label for="user_type" class="form-label">User Type:</label>
                                    <select id="user_type" name="user_type" class="form-control">
                                        <option value="sponsor">Sponsor</option>
                                        <option value="influencer">Influencer</option>
                                    </select>
                                </div>
                                <div class="mb-3">
                                    <label for="Password" class="form-label">Password: </label>
                                    <input type="password" name="Password" class="form-control">
                                </div>
                            </form>
                        </div>
                        <button class="btn btn-lg btn-danger">
                            <RouterLink to="/signup" id="mycont"> Sign up </RouterLink>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SignupPage',
}
</script>

<style scoped>
#signup {
    min-width: 50vh;
    min-height: 85vh;
    overflow: hidden;
    background-color: rgba(253, 253, 253, 0.7);
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
    width: 100%;
    height: 200px;
}
</style>
