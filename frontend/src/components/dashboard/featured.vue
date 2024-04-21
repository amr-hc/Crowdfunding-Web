<template>
    <div class="featured my-4">
        <div class="container ">
            <div class="row">
                <div class="col-12 col-lg">
                    <h4 class="border-bottom border-dark">Featured Projects <i class="fa-solid fa-crown"></i></h4>
                    <div class="row  p-0 ">
                        <div class="project-card p-0" v-for="(project, index) in projects" :key="index">
                            <img :src="project.project.imageUrl ? project.project.imageUrl : require('@/assets/images/2.jpg')"
                                alt="">
                            <div class="btn btn-danger delete-project"> <i class="fa-solid fa-remove"></i></div>
                            <div class="p-3">
                                <h6 class="text-white-50">{{ project.project.title }}</h6>
                                <p class="author text-white badge bg-primary">{{ project.project.author }}</p>
                                <div class="project-card-rating">
                                    <i v-for="n in 5" :key="n"
                                        :class="{ 'plus fa-solid fa-star': n <= project.project.rating, 'minus fa-regular fa-star': n > project.project.rating }"></i>
                                </div>
                                <p class="m-0 badge">Target: {{ project.project.target_money }}</p>
                                <p class="m-0 badge">Current Donation: {{ project.project.currentDonation }}</p>
                            </div>
                            <!-- Empty cards -->
                        </div>
                        <div v-for="n in emptyCardsCount" :key="n" class="empty-card " data-bs-toggle="modal"
                            data-bs-target="#addfeatuerdModal">
                            <i class=" fa-solid fa-plus"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Modal trigger -->
    <button class="btn btn-outline-danger p-0 mb-2 border-0 px-2" data-bs-toggle="modal"
        data-bs-target="#addfeatuerdModal">Add Featured <i class="fa-solid fa-reply"></i> </button>

    <!-- Modal -->
    <div class="modal fade" data-bs-theme="dark" id="addfeatuerdModal" tabindex="-1"
        aria-labelledby="addfeatuerdModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="addfeatuerdModalLabel">Add new featured projects</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    Please pick up to 5 projects
                    <select class="selectpicker" multiple aria-label="Default select example" data-live-search="true"
                        v-model="selectedProjects">
                        <option v-for="project in fetchedProjects" :key="project.id" :value="project.id">{{
                            project.title }}</option>
                    </select>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Cancel</button>
                    <button type="button" class="btn btn-primary" @click="addSelectedProjects">Add</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: 'featured',
    data() {
        return {
            projects: [],
            selectedProjects: [],
            ratings: [], // Add ratings array
        };
    },
    computed: {
        emptyCardsCount() {
            return Math.max(5 - this.projects.length, 0);
        },
        fetchedProjects() {
            return this.projects.filter(project => !this.selectedProjects.includes(project.id));
        }
    },
    mounted() {
        this.fetchData();
    },
    methods: {
        fetchData() {
            // Fetch projects data
            axios.get('http://127.0.0.1:8000/api/ImportantProject/')
                .then(response => {
                    this.projects = response.data;
                })
                .catch(error => {
                    console.error('Error fetching projects:', error);
                });

            // Fetch ratings data
            axios.get('http://127.0.0.1:8000/api/rate/')
                .then(response => {
                    this.ratings = response.data;
                })
                .catch(error => {
                    console.error('Error fetching ratings:', error);
                });
        },
        addSelectedProjects() {
            console.log('Selected projects:', this.selectedProjects);
        },
        getRating(projectId) {
            const ratingData = this.ratings.find(rating => rating.project === projectId);
            return ratingData ? ratingData.rate : 0;
        }
    }
}
</script>
<style scoped>
.project-card,
.empty-card {
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

.project-card .delete-project {
    position: absolute;
    right: 0;
    top: 0;
    border-radius: 0 15px 0 15px;
}

.empty-card {
    position: relative;
    background-color: var(--primary-color-350);
}

.empty-card i {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 82px;
    color: rgba(255, 255, 255, 0.5);
}

.empty-card:hover {
    cursor: pointer;
    border: 2px solid var(--secondary-color-2);
    transition: all 0.25s ease-in-out;
    background-color: var(--primary-color-1);
    color: white;
    transform: scale(1.025);
}

.project-card .text-white-50 {
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}
</style>
