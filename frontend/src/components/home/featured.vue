<template>
  <div class="featured row p-0 m-0 align-items-center">
    <h1 class="col-12 col-lg-3">
      Our <br />
      Featured <br />Projects
    </h1>
    <div class="alert alert-danger text-center py-2 my-3" v-if="isThereProjects">
      <h1>There is no Projects to Show</h1>
    </div>
    <div class="col-12 col-lg carousel" v-else>
      <div class="list">
        <div class="item" v-for="project in this.featuredProject" :key="project.id">
          <img :src="project.project.pics.length > 0
            ? project.project.pics[0].image_path
            : require('@/assets/images/No-Image-Placeholder.svg.png')
            " :alt="project.title" />
          <div class="content">
            <div class="author">
              {{
                `${project.project.owner.first_name} ${project.project.owner.last_name} `
              }}
            </div>
            <div class="title">{{ project.project.title }}</div>
            <div class="description">{{ project.project.description }}</div>
            <div class="rating">
              <i v-for="n in 5" :key="n" :class="{
                'plus fa-solid fa-star': n <= project.project.average_rate,
                'minus fa-regular fa-star': n > project.project.average_rate,
              }"></i>
            </div>
          </div>
        </div>
      </div>
      <div class="thumbnail">
        <div class="item" v-for="project in this.featuredProject" :key="project.id">
          <img :src="project.project.pics.length > 0
            ? project.project.pics[0].image_path
            : require('@/assets/images/No-Image-Placeholder.svg.png')
            " :alt="project.title" />
          <div class="content">
            <div class="title">{{ project.project.title }}</div>
          </div>
        </div>
      </div>
      <div class="arrows">
        <button @click="showSlider('prev')" class="fa-solid fa-angle-left"></button>
        <button @click="showSlider('next')" class="fa-solid fa-angle-right"></button>

      </div>
      <div class="time"></div>
    </div>
  </div>
</template>

<script>
import { datastore } from "@/stors/crowdfundingStore";
export default {
  name: "featured",
  data() {
    return {
      usedatastore: datastore(),
      featuredProject: [],
      isThereProjects: true,
    };
  },
  mounted() {
    // Cache the DOM elements
    this.nextDom = document.getElementById('next');
    this.prevDom = document.getElementById('prev');

    // Set event listeners using method binding
    if (this.nextDom && this.prevDom) {
      this.nextDom.addEventListener('click', this.showSlider.bind(this, 'next'));
      this.prevDom.addEventListener('click', this.showSlider.bind(this, 'prev'));
    }
  },
  async created() {
    const res = await fetch("http://127.0.0.1:8000/api/ImportantProject/");
    if (!res.ok) {
      throw new Error("cant fetch data from server");
    }
    const data = await res.json();
    this.featuredProject = Object.values(data);
    this.featuredProject
      .sort((a, b) => a.project.average_rate - b.project.average_rate)
      .reverse();
    if (this.featuredProject.length > 0) {
      this.isThereProjects = false;
    }
    console.log(this.featuredProject.length);
  },
  methods: {
    showSlider(direction) {
      if (direction === 'next') {
        const firstItem = this.featuredProject.shift();
        this.featuredProject.push(firstItem);
      } else {
        const lastItem = this.featuredProject.pop();
        this.featuredProject.unshift(lastItem);
      }
    }

  },
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.carousel {
  width: 100%;
  height: calc(100vh - 62px);
  overflow: hidden;
  position: relative;
}

.carousel .list .item {
  position: absolute;
  inset: 0 0 0 0;
}

.carousel .list .item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.carousel .list .item .content {
  position: absolute;
  top: 20%;
  width: 1140px;
  max-width: 80%;
  left: 50%;
  transform: translateX(-50%);
  padding-right: 30%;
  box-sizing: border-box;
  color: white;
  text-shadow: 0 5px 10px #0004;
}

.carousel .list .item .content .author {
  font-weight: bold;
  letter-spacing: 10px;
}

.carousel .list .item .content .title,
.carousel .list .item .content .topic {
  font-weight: bold;
  font-size: 3rem;
  line-height: 1.3em;
}

.carousel .list .item .content .topic {
  color: #f1683a;
}



.carousel .list .item .content .plus {
  color: yellow;
}

.carousel .list .item .content .minus {
  color: rgba(255, 255, 0, 0.5);
}

.thumbnail {
  position: absolute;
  bottom: 50px;
  left: 50%;
  width: max-content;
  z-index: 100;
  display: flex;
  gap: 20px;
}

.thumbnail .item {
  width: 150px;
  height: 220px;
  flex-shrink: 0;
  position: relative;
}

.thumbnail .item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 20px;
}

.thumbnail .item .content {
  position: absolute;
  bottom: 10px;
  left: 10px;
  right: 10px;
}

.thumbnail .item .content .title {
  font-weight: bold;
}

.arrows {
  position: absolute;
  top: 80%;
  right: 52%;
  width: 300px;
  max-width: 30%;
  display: flex;
  gap: 10px;
  align-items: center;
}

.arrows button {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: none;
  background-color: var(--primary-color-3);
  color: white;
  font-size: 1.5rem;
  font-weight: bold;
  transition: 0.5s;
  z-index: 10;
}

.arrows button:hover {
  background-color: #eee;
  color: #555;
}

.carousel .list .item:nth-child(1) {
  z-index: 1;
}

.carousel .list .item:nth-child(1) .author,
.carousel .list .item:nth-child(1) .title,
.carousel .list .item:nth-child(1) .description,
.carousel .list .item:nth-child(1) .rating,
.carousel .list .item:nth-child(1) .topic,
.carousel .list .item:nth-child(1) .btn {
  transform: translateY(50px);
  filter: blur(20px);
  opacity: 0;
  animation: showContent 0.5s 1s linear 1 forwards;
}

@keyframes showContent {
  to {
    opacity: 1;
    filter: blur(0);
    transform: translateY(0);
  }
}

.carousel .list .item:nth-child(1) .author {
  animation-delay: 0.5s;
}

.carousel .list .item:nth-child(1) .title {
  animation-delay: 0.7;
}

.carousel .list .item:nth-child(1) .topic {
  animation-delay: 0.9s;
}

.carousel .list .item:nth-child(1) .description {
  animation-delay: 1.1s;
}

.carousel .list .item:nth-child(1) .rating {
  animation-delay: 1.3s;
}

.carousel .list .item:nth-child(1) .btn {
  animation-delay: 1.5s;
}

.carousel .list .item:nth-child(1) img {
  width: 150px;
  height: 220px;
  position: absolute;
  left: 50%;
  bottom: 50px;
  border-radius: 20px;
  animation: showImae 0.5s linear 0.5s forwards;
}

@keyframes showImae {
  to {
    width: 100%;
    height: 100%;
    left: 0;
    bottom: 0;
    border-radius: 0;
  }
}

.carousel.next .thumbnail .item:nth-last-child(1) {
  width: 0;
  overflow: hidden;
  animation: showThumbnail 0.5s linear 0.5s forwards;
}

@keyframes showThumbnail {
  to {
    width: 150px;
  }
}

.carousel.next .thumbnail {
  transform: translateX(150px);
  animation: transformThumbnail 0.5s linear 0.5s forwards;
}

@keyframes transformThumbnail {
  to {
    transform: translateX(0);
  }
}

.carousel.prev .list .item:nth-child(2) {
  z-index: 2;
}

.carousel.prev .list .item:nth-child(2) img {
  position: absolute;
  bottom: 0;
  left: 0;
  animation: outImage 0.5s linear 0.5s forwards;
}

@keyframes outImage {
  to {
    width: 150px;
    height: 220px;
    border-radius: 20px;
    left: 50%;
    bottom: 50px;
  }
}

.carousel.prev .thumbnail .item:nth-child(1) {
  width: 0;
  overflow: hidden;
  opacity: 0;
  animation: showThumbnail 0.5s linear 0.5s forwards;
}

.carousel.prev .list .item:nth-child(2) .author,
.carousel.prev .list .item:nth-child(2) .title,
.carousel.prev .list .item:nth-child(2) .topic,
.carousel.prev .list .item:nth-child(2) .description,
.carousel.prev .list .item:nth-child(2) .rating,
.carousel.prev .list .item:nth-child(2) .btn {
  animation: contentOut 1.5s linear 1s forwards;
}

@keyframes contentOut {
  to {
    transform: translateX(-150px);
    filter: blur(20px);
    opacity: 0;
  }
}

.carousel.next .arrows button,
.carousel.prev .arrows button {
  pointer-events: none;
}

.time {
  width: 0;
  height: 5px;
  background-color: #f1683a;
  position: absolute;
  z-index: 100;
  top: 0;
  left: 0;
}

.carousel.next .time,
.carousel.prev .time {
  width: 100%;
  animation: timeRunning 2s linear 1s forwards;
}

@keyframes timeRunning {
  to {
    width: 0;
  }
}

@media screen and (max-width: 678px) {
  .carousel .list .item .content {
    padding-right: 0;
  }

  .carousel .list .item .content .title {
    font-size: 30px;
  }
}
</style>
