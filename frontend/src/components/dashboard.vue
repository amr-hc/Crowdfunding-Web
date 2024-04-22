<template>
    <div v-show="isAdmin">
        <ul class="nav  py-2">
            <li class="nav-item ">
                <router-link class="nav-link" :class="{ active: $route.path === ('/dashboard') }" to="/dashboard"
                    exact>Home</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" active-class="active" to="/dashboard/category-tags">Category &
                    Tags</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" active-class="active" to="/dashboard/report">Report</router-link>
            </li>
        </ul>

        <div class="container p-0">

            <router-view name="default"></router-view>
            <router-view name="projects"></router-view>
            <router-view name="ReportProject"></router-view>
            <router-view name="ReportComment"></router-view>
        </div>
        <div v-show="!isAdmin">
            <p class="text-center text-danger">You are not allowed to access this page.</p>
        </div>
    </div>
</template>

<script>

export default {

    name: 'dashboard',

    computed: {
        isAdmin() {
            const userInfo = JSON.parse(localStorage.getItem('userInfo'));
            return userInfo && userInfo.is_superuser === true;
        }
    },

}
</script>

<style scoped>
.nav {
    background-color: var(--primary-color-1);
    box-shadow: 0px 0 31px 0px rgb(0 0 0 / 10%);
    backdrop-filter: blur(15px);
    z-index: 100;
    position: sticky;
    top: 0;
}

.nav-link {
    width: max-content;
    position: relative;
    color: var(--secondary-color-1);
}

.nav-link::after {
    content: "";
    position: absolute;
    width: 90%;
    height: 2px;
    left: 5%;
    bottom: 0;
    transform: scaleX(0);
}

.nav-link:hover,
.active {
    color: var(--primary-text-light) !important;
}

.nav-link:hover::after,
.active::after {
    background-color: var(--secondary-color-1);
    transition: transform 0.5s ease-in-out;
    transform-origin: left;
    transform: scale(1);
    color: black;
}
</style>
