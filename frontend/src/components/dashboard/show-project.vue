<template>
    <div v-if="project" class="project-wrapper h-100 mb-5 pb-5 container pt-4">
        <div class="row gap-5 g-0 justify-content-center">
            <div class="col-12 col-md py-3 rounded-4 text-light">
                <h4> {{ project.owner.first_name }} {{ project.owner.last_name }}</h4>
                <h6 class="text-white-50"> <i class="fa-solid fa-location-crosshairs"></i> {{ project.owner.country }}
                </h6>
                <hr>
                <p class="text-white-50"> <strong>{{ currency_format(project.total_donations) }}</strong> raised from
                    {{ currency_format(
                        project.target_money) }} / {{
                        project.donations.length }} donors
                </p>
                <div class="progress">
                    <div class="progress-bar" role="progressbar"
                        :style="{ width: (project.total_donations / project.target_money) * 100 + '%' }"
                        aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <h3 class="my-3">{{ currency_format(project.target_money - project.total_donations) }} still needed
                </h3>
                <p class="text-white-50">{{ formatDaysLeft(project.start_date, project.end_date) }} left</p>

                <button v-show="!isRemoved" class="col btn btn-outline-danger text-light ms-2"
                    @click="removeProject">Remove this
                    project<i class="mx-3 fa-solid fa-trash"></i> </button>


            </div>

            <div class="card-details h-100 w-100 w-md-50 position-relative col-12 col-md ">
                <div class="img-wrapper">
                    <img class=" h-100 w-100 rounded-4 object-fit-stretch " :src="activeImg" alt="Active Image"
                        id="active-img" />
                    <div v-show="isFeatured" class="featured bg-danger">featured <i class="fa-solid fa-star"></i></div>
                </div>
                <div class="row gap-1 g-0 flex-nowrap  overflow-x-auto  py-2">
                    <div class="img-item" v-for="(image, index) in project.pics" :key="index"
                        :class="{ 'active-img': image.image_path === activeImg }" @click="selectActiveImage(index)">
                        <img width="100%" height="100%" :src="image.image_path" alt="Thumbnail Image" />
                    </div>
                </div>
                <h5 class="text-light lead">{{ project.title }} <div class="rating my-2">
                        <i v-for="n in 5" :key="n"
                            :class="{ 'plus fa-solid fa-star': n <= project.average_rate, 'minus fa-regular fa-star': n > project.average_rate }"></i>
                    </div>
                </h5>
                <div class="text-white-50">
                    {{ project.description }}
                </div>

                <hr>
                <div class="reviews">
                    <h5 class="text-white my-3">Reviews</h5>
                    <div v-if="project.comments.length > 0" class="reviews">
                        <div class="reviewer text-end border-bottom border-dark my-2"
                            v-for="(comment, index) in project.comments" :key="index">
                            <div class="d-flex justify-content-between align-items-baseline">
                                <div class="d-flex align-items-center gap-2">
                                    <div class="avatar">
                                        <img :src="comment.user_data.image" @error="handleImageError" alt="Avatar" />
                                    </div>
                                    <div class="text-light">{{ comment.user_data.first_name }} {{
                                        comment.user_data.last_name }}</div>
                                </div>
                                <!-- Display rating -->
                                <div class="rating">
                                    <i v-for="n in 5" :key="n"
                                        :class="{ 'plus fa-solid fa-star': n <= 5, 'minus fa-regular fa-star': n > 5 }"></i>
                                </div>
                            </div>
                            <!-- Display comment -->
                            <p class="text-white-50 text-start my-2">{{ comment.comment }}</p>
                            <!-- Display comment date -->
                            <p class="m-0">{{ comment.date }}</p>
                        </div>
                    </div>
                    <div v-else class="alert alert-dark bg-dark border-0">
                        <p>There are no reviews available at the moment.</p>
                    </div>


                </div>
            </div>


        </div>
        <div v-show="isRemoved" class="deleted">Project has been removed! 😲</div>
    </div>
    <div v-else>
        <p>Loading project data...</p>
    </div>
</template>

<script>
import axios from 'axios';
import { datastore } from "@/stors/crowdfundingStore";

export default {
    name: 'project-details',
    data() {
        return {
            project: null,
            activeImg: null, // Initialize as null
            isFeatured: false,
            isRemoved: false,
            token: datastore().userInfo.token,

        };
    },
    mounted() {
        const projectId = parseInt(this.$route.params.id);
        this.fetchProjectDetails(projectId);
        if (this.project && this.project.pics && this.project.pics.length > 0) {
            this.activeImg = this.project.pics[0].image_path;
        }
        else {
            this.activeImg = require('@/assets/images/default.jpg');
        }
    },
    methods: {
        handleImageError(event) {
            event.target.src = require('@/assets/images/default.jpg');
        },
        fetchProjectDetails(projectId) {
            axios.get(`http://127.0.0.1:8000/api/projects/${projectId}`, {
                headers: {
                    Authorization: `token ${this.token}`
                }
            })
                .then(response => {
                    this.project = response.data;
                    this.isRemoved = this.project.hidden;
                    this.checkIFeaturedProject(projectId);
                    if (this.project && this.project.pics && this.project.pics.length > 0) {
                        this.activeImg = this.project.pics[0].image_path;
                    }
                })
                .catch(error => {
                    console.error('Error fetching project details:', error);
                });
        },
        async removeProject() {
            const projectId = this.$route.params.id;

            try {
                const response = await axios.patch(
                    `http://127.0.0.1:8000/api/projects/${projectId}/`,
                    { hidden: true, },
                    {
                        headers: {
                            Authorization: `token ${this.token}`
                        }
                    }

                );

                if (response.status < 200 || response.status >= 300) {
                    console.error("Error While removing The Project:", response.data);
                }
                else {
                    this.isRemoved = true;
                    this.$router.push({ name: 'dashboard' });
                    console.log("Project Removed Successfully");
                }
            } catch (error) {
                console.error("Error While canceling The Project:", error);
            }
        },
        checkIFeaturedProject(projectId) {
            axios.get(`http://127.0.0.1:8000/api/ImportantProject/`)
                .then(response => {
                    const featuredProjectIds = response.data.map(project => project.id);
                    this.isFeatured = featuredProjectIds.includes(projectId);
                })
                .catch(error => {
                    console.error('Error fetching important projects:', error);
                });
        },

        currency_format(price) {
            return new Intl.NumberFormat("us", {
                style: "currency",
                currency: "usd",
                minimumFractionDigits: 0
            }).format(price);
        },

        selectActiveImage(index) {
            console.log(this.project);
            if (this.project && this.project.pics && this.project.pics.length > 0) {
                this.activeImg = this.project.pics[index].image_path;
            } else {
                this.activeImg = require('@/assets/images/default.jpg');
            }
        },

        formatDaysLeft(startDate, endDate) {
            const start = new Date(startDate);
            const end = new Date(endDate);
            const diffTime = end - start;
            const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
            if (diffDays === 1) {
                return `${diffDays} day`;
            } else if (diffDays < 30) {
                return `${diffDays} days ${diffTime % (1000 * 60 * 60 * 24)} hours`;
            } else if (diffDays < 365) {
                const months = Math.floor(diffDays / 30);
                const remainingDays = diffDays % 30;
                return `${months} months ${remainingDays} days`;
            } else {
                const years = Math.floor(diffDays / 365);
                const remainingMonths = Math.floor((diffDays % 365) / 30);
                const remainingDays = (diffDays % 365) % 30;
                return `${years} years ${remainingMonths} months ${remainingDays} days`;
            }
        }

    },

}
</script>

<style scoped>
.project-wrapper {
    position: relative;
    padding: 12px;
    min-height: 70vh;
    border: 1px solid var(--primary-color-3);
    border-radius: 20px;
    box-shadow: 0px 0 31px 0px rgb(0 0 0 / 10%);
    backdrop-filter: blur(15px);
}

.img-wrapper {
    width: 100%;
    height: 400px;
    position: relative;
}

.active-img,
.img-item:hover,
.project-item:hover {
    border: 2px solid var(--secondary-color-2);
    cursor: pointer;
    opacity: 1 !important;
    transition: all 0.3s ease-in-out;
}

.img-item {
    width: 75px;
    height: 75px;
}

.img-item,
.project-item {
    overflow: hidden;
    border-radius: 10px;
    margin-right: 10px;
    opacity: 0.5;
}

.project-item {
    width: 150px;
    height: 150px;
    position: relative;
}

.project-item-title {
    position: absolute;
    bottom: 0;
    left: 5%;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
    width: 90%;
    font-weight: 500;
}

.project-item-rating {
    position: absolute;
    top: 5%;
    right: 5%;
    font-size: .8rem;
}

.featured {
    position: absolute;
    right: 0;
    top: 0;
    padding: .5rem 1.5rem;
    border-radius: 0 16px 0 1.5rem;
    font-weight: 500;
    font-size: 1rem;
    text-transform: capitalize;
    color: white;
    font-family: Arial, Helvetica, sans-serif;
}

.plus {
    color: yellow;
}

.minus {
    color: rgba(255, 255, 0, 0.5);
}

.avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: 2px solid var(--primary-color-3);
    overflow: hidden;
}

.avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.progress {
    height: 8px;
    border-radius: 10px;
    overflow: hidden;
    background-color: var(--secondary-color-4);
}

.progress-bar {
    transition: width 0.3s ease-in-out;
    background-color: var(--secondary-color-2);
}

.deleted {
    background-color: var(--primary-color-3);
    color: red;
    z-index: 900;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.5rem;
    font-weight: 500;
    text-transform: uppercase;
    border-radius: 20px;
    opacity: .8;
}
</style>