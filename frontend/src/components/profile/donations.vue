<template>
  <div class="donations mt-5">
    <div class="fs-4 m-3">Your Donations</div>
    <div class="tbl-container bdr">
      <table class="table table-dark">
        <thead>
          <tr>
            <th scope="col">Donation_id</th>
            <th scope="col">Donated_at</th>
            <th scope="col">Donation_amount</th>
            <th scope="col">Project</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="donation in storData.user.donations" :key="donation.id">
            <th scope="row">{{ donation.id }}</th>
            <td>{{ dateFormat(donation.created_at) }}</td>
            <td>{{ donation.donation_amount }}</td>
            <td>{{ projectName(donation.project) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import "select2";
import { datastore } from "@/stors/crowdfundingStore";
import FunctionsClass from "../../assets/js/registerAndUpdate";
const functionsObject = new FunctionsClass();

export default {
  async created() {
    if (functionsObject.getStorgData()) {
      await this.storData.getAllProjects();
      this.allProjects = this.storData.allProjects.results;
    }
  },

  data() {
    return {
      storData: datastore(),
      allProjects: [],
    };
  },

  methods: {
    dateFormat(par) {
      return par.split("T")[0];
    },
    projectName(par) {
      if (this.allProjects.length != 0) {
        return this.allProjects.find((obj) => {
          return obj.id == par;
        }).title;
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.tbl-container {
  margin-top: 10px;
  margin-left: 10px;
}
th,
td {
  padding: 15px;
}

.bdr {
  border-radius: 10px;
  overflow: hidden;
}
</style>
