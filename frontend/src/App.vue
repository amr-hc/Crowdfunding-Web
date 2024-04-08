<template>
  <div class="container map">
    <navbar msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
import navbar from './components/navbar.vue'

export default {
  name: 'App',
  components: {
    navbar
  }
}
</script>

<style>
#app {
  font-family: "Tajawal", sans-serif;
  font-weight: 400;
  font-style: normal;
}

.container {
  min-height: 100vh;
}
</style>
