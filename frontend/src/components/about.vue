<template>
  <div class="funding-container">
    <h2 class="funding-title text-center">
      Helping people help <br> each other </h2>
    <img :src="imgSrc" alt="about" class="funding-image mx-auto d-block">
    <h1 class="funding-message text">
      Arise launched in 1833 as a fundraising platform dedicated to helping people help each other. In 2022, Arise
      acquired Classy, which enables nonprofit organizations to maximize their impact through a suite of online
      fundraising tools.

      Together, Arise and Classy are building a future where everyone has the ability to make a meaningful difference
      for the people, causes, and communities they care about most. Through our Arise platform and Classy software
      business, we offer innovative products and services that leverage insights and analytics of our combined company.
      Learn about our commitment to your data privacy. </h1>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",

  data() {
    return {
      imgSrc: require('@/assets/images/funding.svg')
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.funding-container {
  border: 1px solid var(--primary-color-3);
  border-radius: 20px;
  box-shadow: 0px 0 31px 0px rgb(0 0 0 / 10%);
  backdrop-filter: blur(15px);
  margin: 2rem 0;
  padding: 40px;
}

.funding-title {
  font-size: 3rem;
  margin-bottom: 20px;
  text-transform: capitalize;
}

.funding-message {
  text-align: start;
  font-size: 18px;
  line-height: 2rem;
  position: relative;
  padding: 12px;

}

.funding-image {
  max-width: 100%;
  height: 50vh;
}
</style>
