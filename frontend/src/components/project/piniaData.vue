<template>
  <div>
    <h1>All Users</h1>
    <ul>
      <li v-for="user in users" :key="user.id">
        {{ user.name }} - {{ user.email }}
      </li>
    </ul>
  </div>
</template>

<script>
import { datastore } from '../../stors/crowdfundingStore';

export default {
  setup() {
     
    return {
      users
    };
  }
};
</script>
