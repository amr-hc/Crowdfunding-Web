<template>
  <div class="container">
    <table class="table table-bordered table-striped mt-2">
      <thead>
      <tr >
        <th class="text-success">id</th>
        <th class="text-success">report</th>
        <th class="text-success">comment_id</th>
        <th class="text-success">user_id</th>
        <th class="text-success">Actions</th>
      </tr>
    </thead>
      <tbody>
      <tr v-for="report in reports" :key="report.id" class="">
          <td>{{ report.id }}</td>
          <td>{{ report.report }}</td>
          <td>{{ report.comment_id }}</td>
          <td>{{ report.user_id }}</td>
          <td><button class="btn btn-danger">Delete report</button> <button class="btn btn-danger">Delete Comment</button></td>
      </tr>
    </tbody>
    </table>

  </div>
</template>

<script>
export default {
  data: () => ({
    reports: [],
  }),
  methods: {
  },
  created() {
    fetch('http://127.0.0.1:8000/report/comment/')
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch reports");
        }
        return response.json();
      })
      .then((reports) => {
        this.reports = reports;
      })
      .catch((error) => {
        console.error(error);
      });
  },
};

</script>

<style>

</style>