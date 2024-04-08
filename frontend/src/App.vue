<template>
  <div class="container map">
    <navbar />
    <div class="row">
      <router-view></router-view>
    </div>
  </div>

</template>

<script>
import navbar from './components/navbar.vue'
export default {
  components: {
    navbar
  },

}
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Bungee+Spice&display=swap');

#app {
  position: relative;
  font-family: "Poppins", sans-serif;
  font-weight: 200;
  font-style: normal;
}

.container {
  min-height: 100vh;
}
</style>
