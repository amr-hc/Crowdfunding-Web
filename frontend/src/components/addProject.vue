<!-- TODO: Validations & add category -->

<template>
  <section class="row justify-content-center">
    <form class="container row align-items-center flex-column">
      <div
        class="container p-5 row align-items-center flex-column gap-2 w-50 m-1 rounded"
        style="background-color: rgb(91 91 91 / 50%) !important"
      >
        <div class="form-floating">
          <input
            type="text"
            class="form-control"
            name="title"
            id="title"
            placeholder="title"
            v-model="title"
            required
          />
          <label for="title" class="text-dark ms-2">Project Title</label>
          <div class="invalid-feedback">Please provide a title.</div>
        </div>

        <div class="form-floating">
          <input
            type="number"
            min="0"
            class="form-control"
            id="target"
            name="target"
            placeholder="target"
            v-model="targetMoney"
            required
          />
          <label for="target" class="text-dark ms-2">Target Money</label>
          <div class="invalid-feedback">Please provide a target amount.</div>
        </div>

        <div class="form-floating">
          <textarea
            class="form-control"
            name="description"
            id="description"
            placeholder="description"
            v-model="description"
            style="height: 100px"
            required
          ></textarea>
          <label for="description" class="text-dark ms-2"
            >Project Description</label
          >
          <div class="invalid-feedback">Please provide a description.</div>
        </div>

        <div class="form-floating">
          <select
            class="form-select"
            name="category"
            id="category"
            v-model="categoryResult"
            required
          >
            <option selected disabled hidden value="">
              Please select a category
            </option>
            <option v-for="cat in categories" :key="cat.id" :value="cat.id">
              {{ cat.name }}
            </option>
          </select>
          <label for="category" class="text-dark ms-2">Category</label>
          <div class="invalid-feedback">Please select a category.</div>
        </div>

        <div class="form-floating">
          <input
            type="date"
            class="form-control"
            name="endDate"
            id="endDate"
            placeholder="endDate"
            v-model="endDate"
            required
          />
          <label for="endDate" class="text-dark ms-2">Project End Date</label>
          <div class="invalid-feedback">Please provide an end date.</div>
        </div>

        <input
          type="submit"
          value="Add"
          class="btn col-3"
          @click="addProject"
        />
      </div>
    </form>
  </section>
</template>
<script>
export default {
  data: () => ({
    title: "",
    description: "",
    targetMoney: 0,
    categoryResult: "",
    photos: [],
    endDate: new Date().toISOString().split("T")[0],
    categories: [],
    userInfo:
      JSON.parse(localStorage.getItem("userInfo")) ||
      JSON.parse(sessionStorage.getItem("userInfo")),
  }),
  methods: {
    addProject($event) {
      let currentDate = new Date();
      let startDate = currentDate.toISOString().split("T")[0];

      let userInfo =
        JSON.parse(localStorage.getItem("userInfo")) ||
        JSON.parse(sessionStorage.getItem("userInfo"));
      const token = userInfo.token;
      console.log(token);

      $event.preventDefault();
      const form = new FormData();
      form.append("id", 10);
      form.append("title", this.title);
      form.append("description", this.description);
      form.append("startDate", startDate);
      form.append("endDate", this.endDate);
      form.append("targetMoney", this.targetMoney);
      form.append("hidden", 0);
      form.append("categoryResult", this.categoryResult);
      form.append("owner_id", userInfo["user_id"]);

      // for (let i = 0; i < this.photos.length; i++) {
      //   form.append("photos[]", this.photos[i]);
      // }

      form.forEach((item) => console.log(item));
      fetch("http://127.0.0.1:8000/api/projects/", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
        },
        body: form,
      })
        .then((response) => {
          if (response.ok) {
            console.log("Project added successfully!");
            this.title = "";
            this.description = "";
            this.targetMoney = "";
            this.categoryResult = "";
            this.endDate = "";
            this.photos = [];
          } else {
            console.error("Failed to add project.");
          }
        })
        .catch((error) => {
          console.error("Error adding project:", error);
        });
    },
    takePhotos($event) {
      const pics = $event.target.files;
      this.photos = Array.from(pics);
    },
  },
  created() {
    fetch("http://127.0.0.1:8000/api/categories/")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch categories");
        }
        return response.json();
      })
      .then((categories) => {
        this.categories = categories;
      })
      .catch((error) => {
        console.error(error);
      });
  },
};
</script>
<style scoped>
.form-control:focus,
select:focus {
  border-color: #28a745 !important;
  box-shadow: 0 0 0 0.2rem rgba(40, 167, 69, 0.25) !important;
}
.btn,
.btn:hover,
.btn:active,
.btn:visited {
  color: #dadee2;
  background-color: #246137;
  border-color: #246137;
}
p {
  color: #dbdcdc;
  text-align: center;
}
.form-floating {
  opacity: 0.6;
}
.form-floating,
.photos {
  opacity: 0.8;
}
.container {
  padding: 2.5rem 3rem !important;
}
</style>
