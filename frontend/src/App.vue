<template>
  <div class="container map">
    <navbar />
    <intro />
  </div>
</template>

<script>
import navbar from './components/navbar.vue'
import intro from './components/intro.vue'

export default {
  name: 'App',
  components: {
    navbar, intro
  }
}
</script>

<style>
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
