<template>
    <featured />
    <projects />

</template>

<script>

import featured from './dashboard/featured.vue'
import projects from './dashboard/projects.vue'
export default {
    components: {
        featured,
        projects
    },
    name: 'dashboard',
    data() {
        return {

        };
    },
}
</script>

<style scoped></style>
