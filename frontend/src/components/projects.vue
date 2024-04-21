<template>
  <section style="background-color: rgb(91 91 91 / 20%) !important">
    <div
      class="jumbotron p-3 mb-4 d-flex justify-content-between align-items-start"
    >
      <router-link class="btn btn-success" to="/add" v-show="showAddBtn"
        >Add Project</router-link
      >
      <div class="headline">
        <h1 class="display-4 font-weight-bold">Browse Our Projects</h1>
        <h2 class="font-italic">Try To Be A Part Of The Solution.</h2>
      </div>
    </div>
    <section class="container">
      <div class="d-flex justify-content-end  gap-3 ">
        <div class="dropdown col-2 d-flex justify-content-center ">
          <button
            class="btn btn-light dropdown-toggle btn-lg"
            type="button"
            data-bs-toggle="dropdown"
            data-bs-auto-close="outside"
          >
            Select tags
          </button>
          <ul class="dropdown-menu text-center">
            <li v-for="tag in this.tags" :key="tag.id">
              <label class="dropdown-item" :for="tag.tagName + tag.id"
                ><input
                  type="checkbox"
                  :id="tag.tagName + tag.id"
                  :value="tag.id"
                />
                {{ tag.tagName }}</label
              >
            </li>
          </ul>
        </div>

        <div class="form-floating col-2">
          <select
            class="form-select"
            id="floatingSelect"
            v-model="this.filteredCategory"
          >
            <option value="">Show All</option>
            <option
              v-for="category in this.categories"
              :key="category.id"
              :value="category.id"
            >
              {{ category.name }}
            </option>
          </select>
          <label for="floatingSelect" class="ms-2">Category</label>
        </div>
        <div class="d-flex input-group w-25">
          <div class="form-floating">
            <input
              id="searchBar"
              class="form-control"
              type="search"
              placeholder="Search"
              v-model="this.searchValue"
            />
            <label for="searchBar" class="text-dark">Search for Project</label>
          </div>
          <span
            class="searchIcon input-group-text col-2 pe-auto bg-dark text-light"
            @click="filterProject"
            ><i class="fa-solid fa-magnifying-glass"></i
          ></span>
        </div>
      </div>
      <div
        class="alert alert-danger text-center py-2 my-3"
        v-if="isThereProjects"
      >
        <h1>There is no Projects to Show</h1>
      </div>
      <div class="text-center py-3" v-else>
        <div class="container">
          <div class="row wall row-gap-5">
            <div
              class="col-md-4 col-sm-6"
              v-for="project in this.projectsData"
              :key="project.id"
            >
              <div class="box">
                <img
                  :src="
                    project.pics.length > 0
                      ? project.pics[0]['image_path']
                      : require('@/assets/images/No-Image-Placeholder.svg.png')
                  "
                  :alt="project.title"
                />
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
  </section>
</template>

<script>
import { datastore } from "@/stors/crowdfundingStore";
export default {
  data: () => ({
    datastore: datastore(),
    projectsData: [],
    categories: [],
    tags: [],
    isThereProjects: true,
    filteredCategory: "",
    searchValue: "",
    filteredTags: "",
  }),
  methods: {
    prepareTags() {
      const allTags = [...document.querySelectorAll("input[type=checkbox]")];
      this.filteredTags = allTags;
      this.filteredTags = this.filteredTags
        .filter((tag) => tag.checked === true)
        .map((tag) => tag.value)
        .map((tag) => `tages=${tag}`)
        .join("&");
      allTags.map((tag) => (tag.checked = false));
    },
    filterProject() {
      const fetchURL = `http://127.0.0.1:8000/api/projects/?title=${this.searchValue}&category=${this.filteredCategory}&${this.filteredTags}`;
      console.log(fetchURL);
      fetch(fetchURL)
        .then((res) => {
          if (!res.ok) {
            throw new Error("there is no project to fetch");
          }
          return res.json();
        })
        .then((data) => {
          this.projectsData = data.results;
          if (this.projectsData.count > 0) {
            this.isThereProjects = false;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  async created() {
    this.projectsData = await this.datastore.getAllProjects();
    if (this.projectsData.count > 0) {
      this.isThereProjects = false;
    }
    this.projectsData = this.projectsData.results;
    this.categories = await this.datastore.getCategories();
    this.tags = await this.datastore.getTags();
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
  /* position: relative; */
  /* padding: 5rem; */
  height: 15rem;
}
.jumbotron * {
  color: #442b10 !important;
  font-weight: 600 !important;
}
.searchIcon {
  cursor: pointer;
}
</style>
