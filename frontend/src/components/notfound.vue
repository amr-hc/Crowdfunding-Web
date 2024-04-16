<template>
  <div class="not-found-container">
    <h2 class="not-found-title text-center">
      Oops! Page Not Found
    </h2>
    <p class="not-found-message text-center">
      We're sorry, but the page you are looking for doesn't exist.
    </p>
    <img :src="imgSrc" alt="Page Not Found" class="not-found-image mx-auto d-block">
  </div>
</template>

<script>
export default {
  data() {
    return {
      imgSrc: require('@/assets/images/404.svg')
    }
  }
}
</script>

<style scoped>
.not-found-container {
  max-height: calc(100vh - 80px);
  padding: 40px;
}

.not-found-title {
  font-size: 28px;
  margin-bottom: 20px;
}

.not-found-message {
  font-size: 18px;
  margin-bottom: 20px;
}

.not-found-image {
  max-width: 100%;
  height: 90%;
}
</style>
