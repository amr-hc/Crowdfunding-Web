<template>
  <section style="background-color: rgb(91 91 91 / 20%) !important">
    <div class="jumbotron h-50 mb-4 row align-items-center">
      <router-link
        class="btn btn-success col-2 ms-3"
        to="/add"
        v-show="showAddBtn"
        >Add Project</router-link
      >
      <div class="headline text-end pb-4">
        <h1 class="display-4 font-weight-bold">Browse Our Projects</h1>
        <h2 class="font-italic mb-0">Try To Be A Part Of The Solution.</h2>
      </div>
    </div>
    <div class="containerSearch">
      <div>
        <input type="text" class="searchInput" placeholder="Search..." />
        <div class="search"></div>
      </div>
      <div class="form-floating selectCategory">
        <select class="form-select" id="floatingSelect">
          <option
            v-for="category in this.categories"
            :key="category.id"
            :value="category.name"
          >
            {{ category.name }}
          </option>
        </select>
        <span class="label">Category</span>
      </div>
    </div>
    <div class="text-center py-3">
      <div class="container">
        <div class="row wall row-gap-5">
          <div
            class="col-md-4 col-sm-6"
            v-for="project in this.projectsData.results"
            :key="project.id"
          >
            <div class="box">
              <img :src="project.pics[0]['image_path']" alt="" />
              <div class="box-overlay"></div>
              <div class="box-content">
                <div class="inner-content">
                  <h3 class="title">{{ project.title }}</h3>
                  <span class="post">{{ project.category["name"] }}</span>
                  <ul class="icon">
                    <li>
                      <router-link
                        :to="'projects/' + project.id"
                        title="project details"
                        ><i class="fa-solid fa-diamond-turn-right"></i
                      ></router-link>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { datastore } from "@/stors/crowdfundingStore";
export default {
  data: () => ({
    datastore: datastore(),
    projectsData: [],
    categories: [],
  }),
  methods: {},
  async created() {
    this.projectsData = await this.datastore.getAllProjects();
    this.categories = await this.datastore.getCategories();
    console.log(this.projectsData.results);
    console.log(this.categories);
  },
  computed: {
    showAddBtn() {
      if (localStorage.length != 0 || sessionStorage.length != 0) return true;
      return false;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.wall {
  background-color: rgb(65 65 65 / 38%);
}
.box {
  overflow: hidden;
  position: relative;
}
.box img {
  width: 100%;
  height: 200px;
  /* height: auto; */
}
.box .box-content {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  transition: all 0.3s ease 0.5s;
}
.box:before,
.box:after,
.box .box-content:before,
.box .box-content:after,
.box .box-overlay {
  content: "";
  width: 20%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  position: absolute;
  top: 0;
  left: 0;
  opacity: 0;
  transform: scale(1.2);
  transition: all 0.3s ease 0.1s;
}
.box:after {
  left: 20%;
  transition-delay: 0.2s;
}
.box .box-content:before {
  left: 40%;
  transition-delay: 0.3s;
}
.box .box-content:after {
  left: 60%;
  transition-delay: 0.4s;
}
.box .box-overlay {
  left: 80%;
  transition-delay: 0.5s;
}
.box:hover:before,
.box:hover:after,
.box:hover .box-content:before,
.box:hover .box-content:after,
.box:hover .box-overlay {
  opacity: 1;
  transform: scale(1);
}
.box .inner-content {
  width: 100%;
  color: #fff;
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  opacity: 0;
  z-index: 1;
  transform: translate(-50%, -50%) scale(1.5);
  transition: all 0.3s ease 0.5s;
}
.box:hover .inner-content {
  opacity: 1;
  transform: translate(-50%, -50%) scale(1);
}
.box .title {
  font-size: 25px;
  font-weight: 600;
  text-transform: uppercase;
  margin: 0;
}
.box .post {
  display: inline-block;
  font-size: 16px;
  font-style: italic;
  letter-spacing: 1px;
  text-transform: capitalize;
  margin: 5px 0 20px 0;
}
.box .icon {
  padding: 0;
  margin: 0;
  list-style: none;
}
.box .icon li {
  display: inline-block;
  margin: 0 5px;
}
.box .icon li a {
  display: block;
  width: 30px;
  height: 30px;
  line-height: 30px;
  border-radius: 50% 0;
  background: #8421ef;
  font-size: 18px;
  color: #fff;
  box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.5), 0 0 0 4px rgba(255, 255, 255, 0.8);
  transition: all 0.3s ease 0s;
}
.box .icon li a:hover {
  background: #fff;
  color: #8421ef;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.5) inset, 0 0 10px #fff;
}
@media only screen and (max-width: 990px) {
  .box {
    margin-bottom: 30px;
  }
}
.jumbotron {
  background-image: url("@/assets/images/wallpaperflare.com_wallpaper.jpg");
  background-position: center;
  background-size: cover;
}
.jumbotron * {
  color: #442b10 !important;
  font-weight: 600 !important;
}
.headline {
  position: relative;
  bottom: 25%;
  right: 5%;
}

@import url("https://fonts.googleapis.com/css?family=Inconsolata:700");

.containerSearch {
  position: absolute;
  margin: auto;
  top: 0;
  left: 60%;
  right: 0;
  bottom: 0;
}

.containerSearch .search {
  position: absolute;
  margin: auto;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  width: 60px;
  height: 60px;
  background: #442b10;
  border-radius: 50%;
  transition: all 1s;
  z-index: 4;
  box-shadow: 0 0 25px 0 rgba(0, 0, 0, 0.4);
}

.containerSearch .search:hover {
  cursor: pointer;
}

.containerSearch .search::before {
  content: "";
  position: absolute;
  margin: auto;
  top: 15px;
  right: 0;
  bottom: 0;
  left: 15px;
  width: 10px;
  height: 2px;
  background: white;
  transform: rotate(45deg);
  transition: all 0.5s;
}

.containerSearch .search::after {
  content: "";
  position: absolute;
  margin: auto;
  top: -5px;
  right: 0;
  bottom: 0;
  left: -5px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 2px solid white;
  transition: all 0.5s;
}

.containerSearch .searchInput {
  font-family: "Inconsolata", monospace;
  position: absolute;
  margin: auto;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  width: 50px;
  height: 50px;
  outline: none;
  border: none;
  background: #442b10;
  color: white;
  text-shadow: 0 0 10px #442b10;
  padding: 0 80px 0 20px;
  border-radius: 30px;
  box-shadow: 0 0 25px 0 #442b10, 0 20px 25px 0 rgba(0, 0, 0, 0.2);
  transition: all 1s;
  opacity: 0;
  z-index: 5;
  font-weight: bolder;
  letter-spacing: 0.1em;
}

.containerSearch .searchInput:hover {
  cursor: pointer;
}

.containerSearch .searchInput:focus {
  width: 300px;
  opacity: 1;
  cursor: text;
}

.containerSearch .searchInput:focus ~ .search {
  right: -250px;
  background: #151515;
  z-index: 6;
}

.containerSearch .searchInput:focus ~ .search::before {
  top: 0;
  left: 0;
  width: 20px;
}

.containerSearch .searchInput:focus ~ .search::after {
  top: 0;
  left: 0;
  width: 20px;
  height: 2px;
  border: none;
  background: white;
  border-radius: 0%;
  transform: rotate(-45deg);
}

.containerSearch .searchInput::placeholder {
  color: white;
  opacity: 0.5;
  font-weight: bolder;
}
.selectCategory > * {
  background-color: transparent;
  color: #442b10;
}
.selectCategory {
  width: 30% !important;
  position: relative;
  top: 45%;
  left: -50px;
  /* background-color: #442b10; */
}
div.containerSearch > div.form-floating.selectCategory > span {
  position: absolute;
  top: 2px;
  left: 5px;
}
</style>
