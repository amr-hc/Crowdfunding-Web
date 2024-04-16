<template>
  <div class="container map">
    <navbar v-show="showNav" />
    <div class="row">
      <router-view></router-view>
    </div>
    <pageFooter />

  </div>

</template>

<script>
import navbar from './components/navbar.vue'
import pageFooter from './components/footer.vue';
export default {

  data: () => ({
    showNav: true
  }),
  created() {

    // this.$route.path   Won't work properly
    const paths = [
      '',
      'about',
      'projects',
      'add',
      'profile',
      'updateUserProfile',
      'congs',
      'login',
      'registration',
      'forgetPassword',
      'dashboard'
    ]

    let path = window.location.href.split('/')
    path = path[path.length - 1]
    if (!paths.includes(path)) {
      this.showNav = false;
    }

  },
  components: {
    navbar, pageFooter
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
