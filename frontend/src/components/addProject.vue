<!-- TODO: Validations & add category -->

<template>
  <section class="row justify-content-center">
    <div
      class="container row align-items-center flex-column gap-2 w-50 rounded"
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
        />
        <label for="title" class="text-dark ms-2">Project Tilte</label>
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
        />
        <label for="target" class="text-dark ms-2">Target Money</label>
      </div>
      <div class="form-floating">
        <textarea
          class="form-control"
          name="description"
          id="description"
          placeholder="description"
          v-model="description"
          style="height: 100px"
        ></textarea>
        <label for="description" class="text-dark ms-2"
          >Project Description</label
        >
      </div>
      <div class="form-floating">
        <select
          class="form-select"
          name="category"
          id="category"
          v-model="categoryResult"
        >
          <option disabled>Plz seect a category</option>
          <option
            :value="category.name"
            v-for="category in categories"
            :key="category.name"
          >
            {{ category.name }}
          </option>
        </select>
        <label for="category" class="text-dark ms-2">Category</label>
      </div>
      <div class="photos">
        <label class="input-group-text" for="photo"
          >Upload multiple photo</label
        >
        <input
          type="file"
          class="form-control"
          id="photo"
          multiple
          @change="takePhotos"
        />
      </div>
      <div class="form-floating">
        <input
          type="date"
          class="form-control"
          name="endDate"
          id="endDate"
          placeholder="endDate"
          v-model="endDate"
        />
        <label for="endDate" class="text-dark ms-2">Project End Date</label>
      </div>
      <input
        type="submit"
        value="Add"
        class="btn btn-primary col-4"
        @click="addProject"
      />
    </div>
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
    addProject() {
      const form = new FormData();
      form.append("title", this.title);
      form.append("description", this.description);
      form.append("targetMoney", this.targetMoney);
      form.append("category", this.category);
      form.append("endDate", this.endDate);
      form.append("user_id", this.userInfo["user_id"]);
      for (let i = 0; i < this.photos.length; i++) {
        form.append("photos[]", this.photos[i]);
      }
      form.forEach((item) => console.log(item));
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
.form-floating,
.photos {
  opacity: 0.8;
}
.container {
  padding: 2.5rem 3rem !important;
}
</style>
