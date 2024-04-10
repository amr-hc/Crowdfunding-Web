<template>
  <section
    class="row justify-content-center">
    <div
      class="container p-5 row align-items-center flex-column gap-2 w-50"
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
          v-model="category"
        >
          <option selected>Plz select category</option>
          <option value="1">One</option>
          <option value="2">Two</option>
          <option value="3">Three</option>
        </select>
        <label for="category" class="text-dark ms-2">Category</label>
      </div>
      <div>
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
          v-model="endDate"/>
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
    category: "",
    photos: [],
    endDate: new Date().toISOString().split("T")[0],
    categories:[]
  }),
  methods: {
    addProject($event) {
      $event.preventDefault();
      const form = new FormData();
      form.append('title', this.title);
      form.append('description', this.description);
      form.append('targetMoney', this.targetMoney);
      form.append('category', this.category);
      form.append('endDate', this.endDate);
      for (let i = 0; i < this.photos.length; i++) {
        form.append('photos[]', this.photos[i]);
      }    
       //user_ID From Session !!
      form.forEach(item=>console.log(item)) 
    },
    takePhotos($event) {
      const pics = $event.target.files;
      this.photos = Array.from(pics);
    },
  },
  created() {
    fetch("http://127.0.0.1:8000/api/categories/")
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch categories');
        }
        return response.json(); // Return the promise from data.json()
      })
      .then(categories => {
        console.log(categories);
      })
      .catch(error => {
        console.error(error);
      });
}

};
</script>
<style></style>
