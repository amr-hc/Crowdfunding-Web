<template>
    <div class="donations mt-5">
    <div class="fs-4">Your Donations</div>
    <table class="table table-dark">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Handle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>Larry</td>
      <td>the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</table>
</div>

</template>

<script>
import 'select2';  
import { datastore } from '@/stors/crowdfundingStore';
import FunctionsClass from "../../assets/js/registerAndUpdate";
const functionsObject = new FunctionsClass();

export default {
async created() {
// await this.storData.getCategories();
// await this.storData.getTags();
// this.categories = this.storData.categories;
// this.tags = this.storData.tags;
// functionsObject.tagSelection(this);
},

data() {
return {
  
}
},

methods: {
 

},
unmounted(){
 
  
}
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
 
</style>