<template>
    <div class="row p-0 p-4">
        <h4>All projects</h4>
        <hr class="my-4 ">
        <!-- Loading Indicator -->
        <div v-if="loading" class="alert alert-dark bg-dark border-0">
            <p>Loading projects...</p>
        </div>
        <!-- Projects list -->
        <div v-else-if="projects.length > 0" class="row p-0">
            <router-link class="project-card p-0" v-for="(project, index) in projects" :key="index"
                :to="'/dashboard/p/' + project.id">
                <div v-show="project.hidden" class="is-removed"> <i class="fa-solid fa-ban"></i></div>
                <img v-if="project.pics && project.pics.length > 0" :src="getImagePath(project)" alt="">
                <img v-else :src="require('@/assets/images/default.jpg')" alt="">
                <div class="p-3">
                    <h6 class="text-white-50 overflow overflow-hidden">{{ project.title }}</h6>
                    <p class="author badge bg-dark p-1">{{ project.owner.first_name }} {{ project.owner.last_name }}
                    </p>
                    <div class="project-card-rating">
                        <i v-for="n in 5" :key="n"
                            :class="{ 'plus fa-solid fa-star': n <= project.average_rate, 'minus fa-regular fa-star': n > project.average_rate }"></i>
                    </div>
                    <p>Target: {{ currency_format(project.target_money) }}</p>
                    <p>Current Donation: {{ currency_format(project.total_donations) }}</p>
                </div>
            </router-link>
        </div>
        <!-- No Projects Message -->
        <div v-else class="alert alert-dark bg-dark border-0">
            <p>There are no projects available at the moment.</p>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import { datastore } from "@/stors/crowdfundingStore";

export default {
    name: 'projects',

    data() {
        return {
            token: datastore().userInfo.token,
            loading: true,
            projects: []
        };
    },
    async created() {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/projects/', {
                headers: {
                    Authorization: `token ${this.token}`
                }
            });
            this.projects = response.data.results;

            if (this.projects.length > 0) {
                this.isRemoved = this.projects[0].hidden;
            }

            this.loading = false;
        } catch (error) {
            console.error('Error fetching projects:', error);
        }
    },
    methods: {
        getImagePath(project) {
            if (project && project.pics && project.pics.length > 0) {
                return project.pics[0].image_path;

            } else {
                return require('@/assets/images/default.jpg');
            }
        },
        showProjectDetails(project) {
            if (project && project.id) {
                this.$router.push({ name: 'dashboardProject', params: { id: project.id } });
            } else {
                console.error('Invalid project object:', project);
            }
        },
        currency_format(price) {
            return new Intl.NumberFormat("us", {
                style: "currency",
                currency: "usd",
                minimumFractionDigits: 0
            }).format(price);
        },

    }
}
</script>


<style scoped>
* {
    padding: 0;
    margin: 0;
}

.project-card {
    position: relative;
    width: 250px;
    height: 400px;
    border: 1px solid var(--primary-color-3);
    border-radius: 20px;
    box-shadow: 0px 0 31px 0px rgb(0 0 0 / 10%);
    backdrop-filter: blur(15px);
    margin: 10px;
    overflow: hidden;
}

.project-card .author {
    position: absolute;
    top: 225px;
    right: 10px;
}

.project-card img {
    width: 100%;
    height: 250px;
    object-fit: cover;
}

.project-card .text-white-50,
.project-card p {
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}

.project-card:hover {
    cursor: pointer;
    outline: 2px solid var(--secondary-color-2);
    transition: all 0.05s ease-in-out;
    background-color: var(--primary-color-1);
    color: white;
}

.project-card-rating i {
    color: yellow;
    font-size: 12px;
}

.is-removed {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1;
}

.is-removed i {
    position: absolute;
    top: 30%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 82px;
    color: rgba(255, 255, 255, 0.5);
}
</style>
