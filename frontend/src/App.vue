<template>
  <div class="container map">
    <navbar  v-show="showNav"  />
    <div class="row">
      <router-view></router-view>
    </div>
  </div>

</template>

<script>
import navbar from './components/navbar.vue'
export default {

  data:()=>({
    showNav:true
   }),
  created() {

    // this.$route.path   Won't work properly
    const paths=[
    '',
    'about',
    'projects',
    'add',
    'profeil',
    'updateUserProfile',
    'congs',
    ]

    let path=window.location.href.split('/') 
    path=path[path.length-1]
     if(!paths.includes(path)){
      this.showNav=false;
     }
    
  },
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
