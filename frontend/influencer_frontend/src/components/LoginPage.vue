<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 offset-md-3 col-lg-6 offset-lg-3 col-sm-6 offset-sm-3">
                <div id="login" class="mt-5 mb-5">
                    <img src="../assets/img1.jpg" alt="" id="img">
                    <div id="loginform">
                        <h3>Login</h3>
                        <div>
                            <form action="" class="form">
                                <div class="mb-3">
                                    <label for="email" class="form-label">E-mail: </label>
                                    <input type="email" name="email" class="form-control" id="email">
                                </div>
                                <div class="mb-3">
                                    <label for="password" class="form-label">Password: </label>
                                    <input type="password" name="password" class="form-control" id="password">
                                </div>
                            </form>
                        </div>
                        <button class="btn btn-lg btn-primary">
                            <RouterLink to="/signup" id="mycont"> Submit </RouterLink>
                        </button>
                        <p class="mt-4">New user?<RouterLink to="/signup" style="text-decoration: none;"> Sign up
                            </RouterLink>instead</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
export default {
    name: "LoginPage",
};
</script>

<style scoped>
#login {
    min-width: 50vh;
    min-height: 85vh;
    overflow: hidden; 
    background-color: rgba(253, 253, 253, 0.7);
    border-radius: 10px;
    box-shadow: 3px 3px 10px #000;
}

#loginform {
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
