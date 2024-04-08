<template>
  <div class="container map">
    <navbar />
    <intro />
    <navbar @clickEvent="activpage" />
    <component :is="targetComponent" />

  </div>
</template>

<script>
import navbar from './components/navbar.vue'
import intro from './components/intro.vue'
import registration from './components/registration.vue'
import hi from './components/hi.vue'
export default {
  name: 'App',
  components: {
    navbar, intro, registration, hi


  },
  data: () => ({
    targetComponent: ""
  }),
  methods: {
    activpage(_v) {
      if (_v == "registration") {
        this.targetComponent = "registration"
      }
      else {

        this.targetComponent = "hi"
      }
    },

  },



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
