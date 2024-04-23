<template>
  <section style="background-color: rgb(91 91 91 / 20%) !important">
    <div class="jumbotron p-3 mb-4 d-flex justify-content-end">
      <div class="headline">
        <h1 class="display-4 font-weight-bold">Browse Our Projects</h1>
        <h2 class="font-italic">Try To Be A Part Of The Solution.</h2>
      </div>
    </div>
    <section class="container">
      <div class="row align-items-center">
        <router-link class="buttonAdd col-2 ms-2" to="/add" v-show="showAddBtn"
          >Add Project</router-link
        >

        <div class="dropdown col text-end">
          <button
            class="btn btn-light dropdown-toggle"
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

        <div class="col-3">
          <select
            class="form-select"
            id="floatingSelect"
            v-model="this.filteredCategory"
          >
            <option value="">select category</option>
            <option
              v-for="category in this.categories"
              :key="category.id"
              :value="category.id"
            >
              {{ category.name }}
            </option>
          </select>
        </div>
        <div class="input-group col">
          <input
            id="searchBar"
            class="form-control"
            type="search"
            placeholder="Search for Project"
            v-model="this.searchValue"
          />

          <span
            class="searchIcon input-group-text bg-dark text-light"
            @click="filterProject"
            ><i class="fa-solid fa-magnifying-glass"></i
          ></span>
        </div>
      </div>
      <div class="row p-0 p-4">
        <h4>All projects</h4>
        <hr class="my-4" />
        <!-- Loading Indicator -->
        <div v-if="loading" class="alert alert-dark bg-dark border-0">
          <p>Loading projects...</p>
        </div>
        <!-- Projects list -->
        <div v-else-if="projectsData.length > 0" class="row p-0">
          <router-link
            class="project-card p-0"
            v-for="(project, index) in projectsData"
            :key="index"
            :to="'projects/' + project.id"
          >
            <img
              :src="
                project.pics.length > 0
                  ? project.pics[0]['image_path']
                  : require('@/assets/images/No-Image-Placeholder.svg.png')
              "
              :alt="project.title"
            />
            <div class="p-3">
              <h6 class="text-white-50 overflow overflow-hidden">
                {{ project.title }}
              </h6>
              <p class="author badge bg-dark p-1">
                {{ project.owner.first_name }} {{ project.owner.last_name }}
              </p>
              <div class="project-card-rating">
                <i
                  v-for="n in 5"
                  :key="n"
                  :class="{
                    'plus fa-solid fa-star': n <= project.average_rate,
                    'minus fa-regular fa-star': n > project.average_rate,
                  }"
                ></i>
              </div>
              <p>Target: {{ currency_format(project.target_money) }}</p>
              <p>
                Current Donation: {{ currency_format(project.total_donations) }}
              </p>
            </div>
          </router-link>
        </div>
        <!-- No Projects Message -->
        <div v-else class="alert alert-dark bg-dark border-0">
          <p>There are no projects available at the moment.</p>
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
    loading: true,
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
      this.prepareTags();
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
    currency_format(price) {
      return new Intl.NumberFormat("us", {
        style: "currency",
        currency: "usd",
        minimumFractionDigits: 0,
      }).format(price);
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
    this.loading = false;
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
.jumbotron {
  background-image: url("@/assets/images/wallpaperflare.com_wallpaper.jpg");
  background-position: center;
  background-size: cover;
  /* position: relative; */
  /* padding: 5rem; */
  height: 15rem;
}
.jumbotron * {
  color: #48d1d1c2 !important;
  font-weight: 600 !important;
}
.searchIcon {
  cursor: pointer;
}

.project-card {
  position: relative;
  width: 250px;
  height: 400px;
  border: 1px solid var(--primary-color-3);
  border-radius: 20px;
  box-shadow: 0px 0 31px 0px rgb(0 0 0 / 10%);
  backdrop-filter: blur(15px);
  margin: 10px;
  overflow: hidden;
}

.project-card .author {
  position: absolute;
  top: 225px;
  right: 10px;
}

.project-card img {
  width: 100%;
  height: 250px;
  object-fit: cover;
}

.project-card .text-white-50,
.project-card p {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.project-card:hover {
  cursor: pointer;
  outline: 2px solid var(--secondary-color-2);
  transition: all 0.05s ease-in-out;
  background-color: var(--primary-color-1);
  color: white;
}

.project-card-rating i {
  color: yellow;
  font-size: 12px;
}

.buttonAdd {
  --color: #0b7aad;
  font-family: inherit;
  display: inline-block;
  width: 8em;
  height: 2.6em;
  line-height: 2.5em;
  margin: 20px;
  position: relative;
  overflow: hidden;
  border: 2px solid var(--color);
  transition: color 0.5s;
  z-index: 1;
  font-size: 17px;
  border-radius: 6px;
  font-weight: 500;
  color: var(--color);
}

.buttonAdd:before {
  content: "";
  position: absolute;
  z-index: -1;
  background: var(--color);
  height: 150px;
  width: 200px;
  border-radius: 50%;
}

.buttonAdd:hover {
  color: #fff;
}

.buttonAdd:before {
  top: 100%;
  left: 100%;
  transition: all 0.7s;
}

.buttonAdd:hover:before {
  top: -30px;
  left: -30px;
}

.buttonAdd:active:before {
  background: #0b7aad;
  transition: background 0s;
}
</style>
