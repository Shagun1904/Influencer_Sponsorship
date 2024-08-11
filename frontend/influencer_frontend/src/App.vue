<template>
  <HeaderPage/>
  <router-view />
</template>

<script>
import HeaderPage from './components/HeaderPage.vue'
export default {
  name: 'App',
  components: {
    HeaderPage,
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #712458;
  background-image: linear-gradient(147deg, #712458 0%, #bf2f2c 74%);
  background-size: cover;
  background-repeat: no-repeat;
}
</style>
<!-- colors
712458
BF2F2C
  -->