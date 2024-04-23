<template>
    <div class="featured my-4">
        <div class="container mx-auto">
            <div class="row">
                <div class="col-12 col-lg">
                    <h4 class="border-bottom border-dark">Featured Projects <i class="fa-solid fa-crown"></i></h4>
                    <div class="row justify-content-center p-0 ">
                        <div class="project-card p-0" v-for="(project, index) in importantProjects.slice(0, 5)"
                            :key="index">
                            <img v-if="project.data.pics && project.data.pics.length > 0"
                                :src="getImagePath(project.data)" alt="">
                            <img v-else :src="require('@/assets/images/default.jpg')" alt="">
                            <div class="p-3">
                                <h6 class="text-white-50 overflow overflow-hidden">{{ project.data.title }}</h6>
                                <p class="author badge bg-dark p-1">{{ project.data.owner.first_name }} {{
                                    project.data.owner.last_name }}
                                </p>
                                <div class="project.data-card-rating">
                                    <i v-for="n in 5" :key="n"
                                        :class="{ 'plus fa-solid fa-star': n <= project.data.average_rate, 'minus fa-regular fa-star': n > project.data.average_rate }"></i>
                                </div>
                                <p>Target: {{ currency_format(project.data.target_money) }}</p>
                                <p>Current Donation: {{ currency_format(project.data.total_donations) }}</p>
                                <div class="delete-project" @click="confirmDelete(project.id)">
                                    <i class="fa-solid fa-trash"></i>
                                </div>
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
                    <select class="selectpicker w-100" aria-label="Default select example" data-live-search="true"
                        v-model="selectedProject">
                        <option v-for="project in filteredProjects" :key="project.id" :value="project.id">{{
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

    <div class="modal fade" data-bs-theme="dark" id="deleteProjectModal" tabindex="-1"
        aria-labelledby="deleteProjectModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="deleteProjectModalLabel">Confirm Deletion</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <p>Are you sure you want to delete this project?</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-danger" @click="deleteProjectConfirmed">Delete</button>
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
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
            selectedProject: '',
            token: datastore().userInfo.token,
            importantProjectIdToDelete: null,
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
        filteredProjects() {
            return this.projects.filter(project => !this.importantProjects.find(impProject => impProject.id === project.id));
        }
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
                    this.importantProjects = response.data.map(item => {
                        // Check if the project is hidden before including it
                        if (!item.project.hidden) {
                            return {
                                id: item.id,
                                data: item.project
                            }
                        }
                    }).filter(Boolean); // Filter out undefined values
                    console.log(this.importantProjects);
                })
                .catch(error => {
                    console.error('Error fetching important projects:', error);
                });
        },

        addSelectedProjects() {
            const data = {
                project_id: this.selectedProject
            };
            axios.post('http://127.0.0.1:8000/api/ImportantProject/', data, {
                headers: {
                    Authorization: `token ${this.token}`
                }
            })
                .then(response => {
                    this.fetchImportantProjects();

                })
                .catch(error => {
                    console.error('Error:', error);
                }).finally(() => {
                    $('#addfeatuerdModal').modal('hide');
                });
        }
        ,
        confirmDelete(importantProjectId) {
            this.importantProjectIdToDelete = importantProjectId;
            $('#deleteProjectModal').modal('show');
        },
        deleteProjectConfirmed() {
            axios.delete(`http://127.0.0.1:8000/api/ImportantProject/${this.importantProjectIdToDelete}/`, {
                headers: {
                    Authorization: `token ${this.token}`
                }
            })
                .then(response => {
                    console.log('Project deleted successfully');
                    this.fetchImportantProjects();
                })
                .catch(error => {
                    console.error('Error deleting project:', error);
                })
                .finally(() => {
                    $('#deleteProjectModal').modal('hide');
                });
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
    right: 10px;
    top: 10px;
    width: 50px;
    height: 50px;
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    border: none;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.project-card .delete-project:hover {
    cursor: pointer;
    background-color: rgba(0, 0, 0, 0.7);
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
