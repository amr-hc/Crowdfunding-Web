<template>
  <div class="container">
    <table class="table table-dark table-striped mt-4">
      <thead>
        <tr>
          <th class="text-success">ID</th>
          <th class="text-success">report</th>
          <th class="text-success">Project title</th>
          <th class="text-success">User Name</th>
          <th class="text-success">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="report in reports" :key="report.id" class="">
          <td>{{ report.id }}</td>
          <td>{{ report.report }}</td>
          <td>{{ report.project_title }}</td>
          <td>{{ report.full_name }}</td>

          <td>
            <button class="btn btn-danger" @click="deleteReport(report.id)" style="margin-right: 10px;">
              Delete report
            </button>
            <button
              class="btn btn-danger"
              @click="deleteProject(report.project_id)"
            >
              Delete Project
            </button>
          </td>
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
    async deleteReport(id) {
      if (confirm("Are you sure you want to delete?")) {
        try {
          await fetch(`http://127.0.0.1:8000/report/projects/${id}/`, {
            method: "DELETE",
          });
          this.reports = this.reports.filter((rep) => rep.id !== id);
        } catch (error) {
          console.error("Failed to delete report:", error);
        }
      }
    },
    async deleteProject(id) {
      if (confirm("Are you sure you want to delete?")) {
        try {
          await fetch(`http://127.0.0.1:8000/api/projects/${id}/`, {
            method: "DELETE",
          });
          this.reports = this.reports.filter((rep) => rep.project_id !== id);
        } catch (error) {
          console.error("Failed to delete project:", error);
          // Handle error
        }
      }
    },
  },

  created() {
    fetch("http://127.0.0.1:8000/report/projects/")
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
  
  <style >
table {
  background-color: #2e363d;
}
</style>