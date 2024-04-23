<template>
    <div class="featured my-4">
        <div class="container mx-auto">
            <div class="row">
                <div class="col-12 col-lg">
                    <h4 class="border-bottom border-dark">Featured Projects <i class="fa-solid fa-crown"></i></h4>
                    <div class="row justify-content-center p-0 ">
                        <div class="project-card p-0" v-for="(project, index) in importantProjects.slice(0, 5)"
                            :key="index">
                            <img v-if="project.pics && project.pics.length > 0" :src="getImagePath(project)" alt="">
                            <img v-else :src="require('@/assets/images/default.jpg')" alt="">
                            <div class="p-3">
                                <h6 class="text-white-50 overflow overflow-hidden">{{ project.title }}</h6>
                                <p class="author badge bg-dark p-1">{{ project.owner.first_name }} {{
                                    project.owner.last_name }}
                                </p>
                                <div class="project-card-rating">
                                    <i v-for="n in 5" :key="n"
                                        :class="{ 'plus fa-solid fa-star': n <= project.average_rate, 'minus fa-regular fa-star': n > project.average_rate }"></i>
                                </div>
                                <p>Target: {{ currency_format(project.target_money) }}</p>
                                <p>Current Donation: {{ currency_format(project.total_donations) }}</p>
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
                    <h6> Select project</h6>
                    <select class="selectpicker w-100" multiple aria-label="Default select example"
                        data-live-search="true" v-model="selectedProjects">
                        <option v-for="project in projects" :key="project.id" :value="project.id">{{
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
import { datastore } from "@/stors/crowdfundingStore";

export default {
    name: 'featured',

    data() {
        return {
            projects: [],
            importantProjects: [],
            selectedProjects: [],
            token: datastore().userInfo.token,
        };
    },

    created() {
        this.fetchProjects();
        this.fetchImportantProjects();
    },

    computed: {
        emptyCardsCount() {
            const emptyCards = 5 - this.importantProjects.length;
            return emptyCards > 0 ? emptyCards : 0;
        },
    },

    methods: {
        fetchProjects() {
            axios.get('http://127.0.0.1:8000/api/projects/', {
                headers: {
                    Authorization: `token ${this.token}`
                }
            })
                .then(response => {
                    this.projects = response.data.results.filter(project => !project.hidden);
                })
                .catch(error => {
                    console.error('Error fetching projects:', error);
                });
        },
        fetchImportantProjects() {
            axios.get('http://127.0.0.1:8000/api/ImportantProject/')
                .then(response => {
                    this.importantProjects = response.data.map(item => item.project);
                })
                .catch(error => {
                    console.error('Error fetching important projects:', error);
                });
        },
        addSelectedProjects() {
            const projectIds = this.selectedProjects.map(project => project);
            console.log(typeof projectIds[0]);
            if (projectIds.length > 0) {
                axios.post('http://127.0.0.1:8000/api/ImportantProject/', {
                    headers: {
                        Authorization: `token ${this.token}`
                    }
                    ,
                    body: {
                        'project_id': projectIds[0]
                    },
                })
                    .then(response => {
                        this.importantProjects = response.data.map(item => item.project);
                        console.log('Important Projects:', this.importantProjects);
                    })
                    .catch(error => {
                        console.error('Error adding important projects:', error);
                    });
            }
        },







        getImagePath(project) {
            if (project && project.pics && project.pics.length > 0) {
                return project.pics[0].image_path;
            } else {
                return require('@/assets/images/default.jpg');
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
p {
    padding: 0;
    margin: 0;
}

.selectpicker {
    width: 100%;
    max-height: 80vw;
}

.project-card,
.empty-card {
    position: relative;
    width: 280px;
    height: 400px;
    outline: 1px solid var(--primary-color-3);
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
    transition: all 0.05s ease-in-out;
    background-color: var(--primary-color-1);
    color: white;
}

.project-card {
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}

.project-card-rating i {
    color: yellow;
    font-size: 12px;
}

.project-card .text-white-50,
.project-card p {
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}
</style>
