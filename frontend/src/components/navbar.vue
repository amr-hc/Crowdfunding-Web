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
            <a class="nav-link" href="#">Projects</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Investors</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">About</a>
          </li>
        </ul>
        <div v-show="isAuthenticated" class="avatar-container dropdown" data-bs-theme="dark">
          <a class="dropdown-toggle-split text-decoration-none d-flex align-items-center" href="#" role="button"
            data-bs-toggle="dropdown" aria-expanded="false">
            <div class="name">John Doe</div>
            <div class="avatar">
              <img :src="avatarSrc" alt="Avatar">
            </div>
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item text-center" href="#">Log out &nbsp;<i
                  class=" fa-solid fa-right-from-bracket"></i></a>
            </li>
          </ul>
        </div>

        <a v-show="!isAuthenticated" class=" text-light text-decoration-none" href="#">Log in</a>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'navbar',
  data() {
    return {
      isAuthenticated: false,
      avatarSrc: require('@/assets/images/avatar.png')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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

.avatar-container {
  display: flex;
  align-items: center;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 2px solid var(--primary-color-3);
  margin-left: 10px;
  overflow: hidden;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.name {
  font-size: 16px;
  color: var(--secondary-color-4);
}
</style>
