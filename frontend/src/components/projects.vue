<template>
    <div class="register vh-100 row justify-content-center align-items-center ">
    </div>
  </template>
  
  <script>
  export default {
    name: 'HelloWorld',
    props: {
      msg: String
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .register{
    background-image: url("../assets/imges/pexels-julia-m-cameron-6994982.jpg");
    background-position: center ;
    background-size: cover ;
    
  }
  .registerCard{border-radius: 10%;
  opacity: 0.8;
  color:black
  }
  </style>
  