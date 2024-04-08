<template>
  <nav class=" navbar navbar-expand-lg">
    <div class="container-fluid">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01"
        aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
        <a class="navbar-brand" href="#">Arise</a>
        <ul class="navbar-nav mx-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" @click.prevent="chosing('v')">Projects</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" @click.prevent="chosing('vv')">Investors</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" @click.prevent="chosing('v')" >About</a>
          </li>
          <li class="nav-item">
            <button class="nav-link" @click="chosing('registration')">registration
          </button></li>
        </ul>

      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'navbar',
  props: {
    msg: String
  },
  methods: {
     chosing(selcted){
       
 this.$emit("clickEvent",selcted)
     }
  },
}
</script>

 
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Bungee+Spice&display=swap');

.navbar-brand {
  font-family: "Bungee Spice", sans-serif;
  font-weight: 400;
  font-style: normal;
  color: var(--primary-text-light) !important;
  font-size: x-large;
  letter-spacing: -3px;
  text-transform: uppercase;
}

.nav-link {
  width: max-content;
  position: relative;
  color: var(--secondary-color-1);
}

.nav-link::after {
  content: '';
  position: absolute;
  width: 90%;
  height: 2px;
  left: 5%;
  bottom: 0;
  transform: scaleX(0);

}

.nav-link:hover,
.active {
  color: var(--primary-text-light) !important;
}

.nav-link:hover::after,
.active::after {
  background-color: var(--secondary-color-1);
  transition: transform 0.5s ease-in-out;
  transform-origin: left;
  transform: scale(1);
}
</style>
