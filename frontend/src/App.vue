<template>
  <div class="container map">
    <navbar @clickEvent="activpage" />
    <component :is="targetComponent" />
     
  </div>
</template>

<script>
import navbar from './components/navbar.vue'
import registration from './components/registration.vue'
import hi from './components/hi.vue'

export default {

  data:()=>({
targetComponent:""
  }),
  methods: {
    activpage(_v){
      if(_v=="registration"){
       this.targetComponent="registration"
      }
      else{
         
        this.targetComponent="hi"
      }
    },
     
  },
  components:{
    navbar,
    registration,hi

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
