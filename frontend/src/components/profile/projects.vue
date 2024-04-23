<template>
  <section>
    <div class="row pro">
      <div class="fs-4 m-1">Your Projects</div>
      <div
        class="col-xs-12 col-sm-6 col-md-4 col-lg-4"
        v-for="project in storData.user.owner_projects"
        :key="project.id"
      >
        <div class="card-flyer">
          <div class="text-box pb-5">
            <div class="image-box">
              <img
                :src="
                  project.pics.length > 0
                    ? project.pics[0].image_path
                    : require('@/assets/images/No-Image-Placeholder.svg.png')
                "
                alt=""
              />
            </div>
            <div class="text-container">
              <h6>{{ project.title }}</h6>
              <p>{{ project.description }}</p>
              <div class="bott">
                <router-link 
                :style="{ 'pointer-events': project.hidden ? 'none' : 'auto' }"
                  class="text-light text-decoration-none"
                  :to="'projects/' + project.id"
                  ><button  :disabled="project.hidden" class="btn btn-success">Show</button></router-link
                >
                <button
                  :disabled="project.hidden"
                  class="btn btn-info m-2"
                  data-bs-toggle="modal"
                  data-bs-target="#update"
                  @click="asginData(project)"
                >
                  Edit
                </button>
                <button :disabled="project.hidden"
                  class="btn btn-danger m-2"
                  data-bs-toggle="modal"
                  data-bs-target="#deleteModal"
                 
                >
                  Delete
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!--  update project model  -->

    <div
      class="modal fade"
      id="update"
      data-bs-backdrop="static"
      data-bs-keyboard="false"
      tabindex="-1"
      aria-labelledby="staticBackdropLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="staticBackdropLabel">
              Edit Project Form
            </h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>

          <div class="modal-body">
            <form
              class="row g-3 needs-validation"
              @submit.prevent="handleFormSubmission"
              novalidate
            >
              <div class="col-md-6">
                <label for="validationCustom01" class="form-label">id</label>
                <input
                  v-model="projectId"
                  readonly
                  type="text"
                  class="form-control"
                  id="validationCustom01"
                  required
                />
               
              </div>
              <div class="col-md-6">
                <label for="validationCustom02" class="form-label">
                  Title</label
                >
                <input
                  v-model="title"
                  type="text"
                  class="form-control"
                  id="validationCustom02"
                  required
                />
               
              </div>

              <div class="col-md-6">
                <label for="validationCustom03" class="form-label"
                  >Target Money</label
                >
                <input
                  v-model="targetMoney"
                  type="number"
                  class="form-control"
                  id="validationCustom03"
                  required
                />
                <div class="invalid-feedback">
                  Please provide a valid Target Money.
                </div>
              </div>
              <div class="col-md-6">
                <label for="validationCustom05" class="form-label"
                  >Category</label
                >
                <select
                  class="form-select"
                  id="validationCustom05"
                  pattern="^[a-zA-Z ,.'\-]+$"
                  v-model="category"
                >
                  <option selected disabled value="">Choose...</option>
                  <option
                    v-for="cat in categories"
                    :key="cat.id"
                    :value="cat.id"
                  >
                    {{ cat.name }}
                  </option>
                </select>
                <div class="invalid-feedback">
                  Please select a valid category.
                </div>
              </div>
              <div class="col-md-12">
                <label for="validationCustom04" class="form-label"
                  >Description</label
                >
                <textarea
                  class="form-control"
                  name="description"
                  id="validationCustom04"
                  placeholder="description"
                  v-model="description"
                  style="height: 100px"
                  required
                ></textarea>
                <div class="invalid-feedback">
                  Please provide a valid Description.
                </div>
              </div>

              <div class="col-md-6">
                <label for="validationCustom06" class="form-label"
                  >Project End Date</label
                >
                <input
                  v-model="endDate"
                  type="DATE"
                  class="form-control"
                  id="validationCustom06"
                  required
                />
                <div class="invalid-feedback">Please provide a valid Date Must be in  the future.</div>
              </div>

              <div class="col-md-12">
                <label for="validationCustom05" class="form-label">Tags</label>
                <br />
                <label for="validationCustom05" class="form-label">
                  Project Tags : {{ projectTags }}</label
                >

                <select
                  @change="addSelection"
                  style="width: 100%; z-index: 100"
                  ref="select"
                  class="form-control select2"
                  multiple
                  id="validationCustom05"
                  pattern="^[a-zA-Z ,.'\-]+$"
                  v-model="projectTags"
                ></select>
                <div class="invalid-feedback">
                  Please select a valid category.
                </div>
              </div>
              <div class="modal-footer">
                <button
                  type="button"
                  class="btn btn-secondary"
                  data-bs-dismiss="modal"
                >
                  Close
                </button>
                <button class="btn btn-primary" type="submit">
                  Submit form
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>

    <!-- Model End-->

    <!--  delete project model  -->

    <div
      class="modal fade"
      id="deleteModal"
      tabindex="-1"
      aria-labelledby="deleteModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content bg-dark">
          <div class="modal-header">
            <h5 class="modal-title" id="deleteModalLabel">Delete Book</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            Are you sure you want to delete This project?
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Cancel
            </button>
            <button
              type="button"
              @click="deleteproject"
              data-bs-dismiss="modal"
              class="btn btn-danger"
            >
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import "select2";
import { datastore } from "@/stors/crowdfundingStore";
import FunctionsClass from "../../assets/js/registerAndUpdate";
const functionsObject = new FunctionsClass();

export default {
  async created() {
    await this.storData.getCategories();
    await this.storData.getTags();
    this.categories = this.storData.categories;
    this.tags = this.storData.tags;
    functionsObject.tagSelection(this);
  },

  data() {
    return {
      storData: datastore(),
      owner_projects: [],
      projectId: "",
      title: "",
      description: "",
      targetMoney: 0,
      category: "",
      endDate: "",
      categories: [],
      storgData: "",
      tags: [],
      projectTags: "",
      selectedTags: "",
    };
  },

  methods: {
    asginData(project) {
      this.title = project.title;
      this.description = project.description;
      this.targetMoney = project.target_money;
      this.category = project.category.id;
      this.endDate = project.end_date;
      this.projectId = project.id;

      this.projectTags = project.tages
        .map((tagId) => {
          const correspondingTag = this.tags.find((tag) => tag.id === tagId);
          return correspondingTag ? correspondingTag.tagName : null;
        })
        .toString();
    },
    handleFormSubmission(e) {
      functionsObject.handleProjectFormSubmission(e, this);
    },

    deleteproject() {
      functionsObject.deleteProject(this);
    },
  },
  unmounted() {
    const selectElement = document.querySelector(".select2");
    if (selectElement) {
      $(selectElement).select2("destroy");
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card-flyer {
  border-radius: 5px;
  height: 52vh;
}
.card-flyer .image-box {
  background: #ffffff;
  overflow: hidden;
  box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.5);
  border-radius: 5px;
}
.card-flyer .image-box img {
  -webkit-transition: all 0.9s ease;
  -moz-transition: all 0.9s ease;
  -o-transition: all 0.9s ease;
  -ms-transition: all 0.9s ease;
  width: 100%;
  height: 200px;
}
.card-flyer:hover .image-box img {
  opacity: 0.7;
  -webkit-transform: scale(1.15);
  -moz-transform: scale(1.15);
  -ms-transform: scale(1.15);
  -o-transform: scale(1.15);
  transform: scale(1.15);
}
.card-flyer .text-box {
  text-align: center;
  height: 100%;
}
.card-flyer .text-box .text-container {
  padding: 30px 18px;
}
.card-flyer {
  background: #ffffff;
  margin-top: 50px;
  -webkit-transition: all 0.2s ease-in;
  -moz-transition: all 0.2s ease-in;
  -ms-transition: all 0.2s ease-in;
  -o-transition: all 0.2s ease-in;
  transition: all 0.2s ease-in;
  box-shadow: 0px 3px 4px rgba(0, 0, 0, 0.4);
}
.card-flyer:hover {
  background: #fff;
  box-shadow: 0px 15px 26px rgba(0, 0, 0, 0.5);
  -webkit-transition: all 0.2s ease-in;
  -moz-transition: all 0.2s ease-in;
  -ms-transition: all 0.2s ease-in;
  -o-transition: all 0.2s ease-in;
  transition: all 0.2s ease-in;
  margin-top: 50px;
}
.card-flyer .text-box p {
  margin-top: 10px;
  margin-bottom: 0px;
  padding-bottom: 0px;
  font-size: 14px;
  letter-spacing: 1px;
  color: #000000;
}
.card-flyer .text-box h6 {
  margin-top: 0px;
  margin-bottom: 4px;
  font-size: 18px;
  font-weight: bold;
  text-transform: uppercase;
  font-family: "Roboto Black", sans-serif;
  letter-spacing: 1px;
  color: #00acc1;
}
</style>
