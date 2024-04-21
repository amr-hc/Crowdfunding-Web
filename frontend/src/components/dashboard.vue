<template>
    <div>
        <div v-if="isAdmin">
            <featured />
            <projects />
        </div>
        <div v-else>
            <p class="text-center text-danger ">You are not allowed to access this page.</p>
        </div>
    </div>
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
        return {};
    },
    computed: {
        isAdmin() {
            const userInfo = JSON.parse(localStorage.getItem('userInfo'));
            return userInfo && userInfo.is_superuser === true;
        }
    }
}
</script>

<style scoped>
/* Your component styles here */
</style>