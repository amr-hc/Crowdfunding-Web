<template>
  <div class="container map">
    <navbar v-show="showNavbar" />
    <div class="row">
      <router-view></router-view>
    </div>
    <pageFooter />
  </div>
</template>

<script>
import navbar from "./components/navbar.vue";
import pageFooter from "./components/footer.vue";
export default {
  data: () => ({}),
  components: {
    navbar,
    pageFooter,
  },
  computed: {
    showNavbar() {
      const paths = [
        "home",
        "about",
        "projects",
        "add",
        "profile",
        "updateUserProfile",
        "congs",
      ];
      const currentPath = this.$route.path.split("/").pop(); 
      return paths.includes(currentPath);
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Bungee+Spice&display=swap");

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
