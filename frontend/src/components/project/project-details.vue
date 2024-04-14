<template>
    <div class="card h-100 mb-5 pb-5">
        <div class="row gap-5 g-0 justify-content-center">
            <div class="card-details h-100 w-100 w-md-50 position-relative col-12 col-md ">
                <div class="img-wrapper">
                    <img class=" h-100 w-100 rounded-4 object-fit-stretch " :src="activeImg" alt="Active Image"
                        id="active-img" />
                    <div v-show="isFeatured" class="featured bg-danger">featured <i class="fa-solid fa-star"></i></div>
                </div>
                <div class="row gap-1 g-0 flex-nowrap  overflow-x-auto  py-2">
                    <div class="img-item" v-for="(image, index) in images" :key="index"
                        :class="{ 'active-img': image.url === activeImg }" @click="selectActiveImage(index)">
                        <img width="100%" height="100%" :src="image.url" alt="Thumbnail Image" />
                    </div>
                </div>
                <h5 class="text-light-emphasis">Title: {{projectData.title}} <div class="rating my-2">
                        <i v-for="n in 5" :key="n"
                            :class="{ 'plus fa-solid fa-star': n <= rating, 'minus fa-regular fa-star': n > rating }"></i>
                    </div>
                </h5>
                <!-- <div class="text-white-50">
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis quam iste beatae incidunt vitae
                    ad.
                    Iure deserunt recusandae neque aut dolorem, nisi delectus molestiae repudiandae aliquid possimus ab
                    odio
                    voluptas?
                </div> -->
                <div class="text-white-50">
                  {{projectData.description}}        
                </div>
                <hr>
                <h5 class="text-light-emphasis">Similar Projects</h5>
                <div class="row g-0 gap-1 overflow-hidden">
                    <div class="project-item" v-for="(image, index) in limitedImages" :key="index">
                        <img :src="image.url" :alt="image.title" />
                        <h6 class="text-light project-item-title">hamada</h6>
                        <div class="project-item-rating"> <i v-for="n in 5" :key="n"
                                :class="{ 'plus fa-solid fa-star': n <= rating, 'minus fa-regular fa-star': n > rating }"></i>
                        </div>
                    </div>
                </div>
                <!-- See More Button -->
                <router-link v-if="images.length > 3" to="projects" class="btn text-light-emphasis mt-2">See
                    More</router-link>
                <hr>
                <div class="reviews ">
                    <h5 class="text-light-emphasis my-3">Reviews</h5>
                    <!-- Add review input -->
                    <textarea data-bs-theme="dark" id="newComment" class="col form-control bg-transparent text-light"
                        rows="3" placeholder="Write your comment"></textarea>

                    <div class="d-flex align-items-baseline justify-content-between gap-3 my-3">
                        <div data-bs-theme="dark">
                            <select id="newRating" class="col form-select bg-body-secondary ">
                                <option selected>Your Rating</option>
                                <option value="1">1 star</option>
                                <option value="2">2 stars</option>
                                <option value="3">3 stars</option>
                                <option value="4">4 stars</option>
                                <option value="5">5 stars</option>
                            </select>
                        </div>
                        <button class=" col text-center btn btn-main btn-outline-dark">Comment</button>
                    </div>
                    <hr>
                    <div class="reviewer text-end  border-bottom border-dark my-2">
                        <div class="d-flex justify-content-between align-items-baseline">
                            <div class="d-flex align-items-center gap-2">
                                <div class="avatar">
                                    <img src="https://placehold.co/400" alt="Avatar" />
                                </div>
                                <div class="text-light">John Doe</div>
                            </div>
                            <div class="rating"> <i v-for="n in 5" :key="n"
                                    :class="{ 'plus fa-solid fa-star': n <= rating, 'minus fa-regular fa-star': n > rating }"></i>
                            </div>
                        </div>
                        <p class="text-white-50 text-start">Lorem ipsum dolor sit amet consectetur adipisicing elit.
                            Iusto,
                            quod.
                        </p>
                        <p class="m-0">10-10-2022 - 10:10 AM</p>
                        <button class=" btn btn-outline-danger p-0 mb-2 border-0 px-2" data-bs-toggle="modal"
                            data-bs-target="#reportModal">report <i class="fa-solid fa-reply"></i> </button>

                    </div>

                </div>
            </div>

            <div class="col-12 col-md py-3 rounded-4 text-light">
                <h4>Harry maquire</h4>
                <h6 class="text-white-50"> <i class="fa-solid fa-location-crosshairs"></i> tanta, Egypt</h6>
                <hr>
                <p class="text-white-50"> <strong>$999</strong> raised from $1000 / 5 donors </p>
                <div class="progress">
                    <div class="progress-bar" role="progressbar" :style="{ width: donationProgress + '%' }"
                        aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <h3 class="my-3">${{ totalAmount - currentDonation }} still needed</h3>
                <p class="text-white-50">3 days left</p>

                <div class="d-flex">
                    <input type="number" data-bs-theme="dark" min="0" class="col form-control bg-transparent text-light"
                        placeholder="Enter Amount" aria-describedby="donationBlock">
                    <button class="col btn btn-main btn-outline-dark ms-2">Donate</button>
                </div>
                <hr class="my-5">
                <h5 class="text-white-50 my-4">Last 5 Donations</h5>
                <div class=" text-end  border-bottom border-dark my-2">
                    <div class="d-flex justify-content-between align-items-baseline">
                        <div class="d-flex align-items-center gap-2">
                            <div class="avatar">
                                <img src="https://placehold.co/400" alt="Avatar" />
                            </div>
                            <div class="text-light">John Doe</div>
                        </div>
                        <p class="text-white-50">3 days ago</p>
                    </div>
                    <p class="text-white-50 text-start">Donated $1000
                    </p>

                </div>

            </div>
        </div>
    </div>
    <!-- Modal -->
    <div class="modal fade " data-bs-theme="dark" id="reportModal" tabindex="-1" aria-labelledby="reportModalLabel"
        aria-hidden="true">
        <div class="modal-dialog ">
            <div class="modal-content  ">
                <div class="modal-header  ">
                    <h1 class="modal-title fs-5" id="reportModalLabel">Report Confirmation</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    Are you sure you want to report this comment?
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-danger" data-bs-dismiss="modal">No</button>
                    <button type="button" class="btn btn-primary">Go ahead!</button>
                </div>
            </div>
        </div>
    </div>
</template>



<script>
export default {
    name: 'project-details',
    data() {
        return {
            projectData: {}, // Object to hold project data
            images: [],
            activeImg: '',
            isFeatured: true,
            rating: 4,
            showAllProjects: false,
            totalAmount: 1000,
            currentDonation: 630
        };
    },
    async mounted() {
        // Fetch project data when the component is mounted
        await this.fetchProjectData();
        await this.fetchProjectPicsData();
    },
    methods: {
        async fetchProjectData() {
            try {
                const projectId = 1; //this.$route.params.id;
                const response = await fetch(`http://localhost:8000/projects/${projectId}`);
                if (!response.ok) {
                    throw new Error('Failed to fetch project data');
                }
                const data = await response.json();
                this.projectData = data;
                this.totalAmount = data.target_money;
                this.rating = data.rates;
            } catch (error) {
                console.error('Error fetching project data:', error);
            }
        },
       async fetchProjectPicsData() {
            try {
                const projectId = 1;
                const response = await fetch(`http://localhost:8000/project_pics/get_pics_of_project/?project_id=${projectId}`);
                if (!response.ok) {
                    throw new Error('Failed to fetch project pics data');
                }
                const data = await response.json();
                this.images = data.map(image => ({
                    url: image.url,
                    active: false
                }));
                // Set the active image to the first image in the array
                if (this.images.length > 0) {
                    this.activeImg = this.images[0].url;
                }
            } catch (error) {
                console.error('Error fetching project pics data:', error);
            }
        },

        selectActiveImage(index) {
            this.activeImg = this.images[index].url;
            this.images.forEach((img, i) => {
                img.active = i === index;
            });
        },
        showAllSimilarProjects() {
            this.showAllProjects = true;
        }
    },
    computed: {
        filledStars() {
            return this.rating;
        },
        emptyStars() {
            return 5 - this.rating;
        },
        limitedImages() {
            return this.showAllProjects ? this.images : this.images.slice(0, 3);
        },
        donationProgress() {
            return (this.currentDonation / this.totalAmount) * 100;
        }
    }
}
</script>


<style scoped>
.card {
    padding: 12px;
    background-color: var(--primary-color-350);
    border: 2px solid var(--primary-color-3);
    min-height: 70vh;
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

option {
    background-color: transparent;
}
</style>




<!--<script>
   Template



// export default {
//     name: 'project-details',
//     data() {
//         return {
//             images: [
//                 { url: 'https://s3.amazonaws.com/ooomf-com-files/wdXqHcTwSTmLuKOGz92L_Landscape.jpg', title: 'New carousel layout', description: 'Responsive thumbnail preview in carousel indicators.' },
//                 { url: 'https://s3.amazonaws.com/ooomf-com-files/mtNrf7oxS4uSxTzMBWfQ_DSC_0043.jpg', title: 'One more for good measure.', description: 'Nullam id dolor id nibh ultricies vehicula ut id elit.' },
//                 { url: 'https://s3.amazonaws.com/ooomf-com-files/tU3ptNgGSP6U2fE67Gvy_SYDNEY-162.jpg', title: 'Another example headline.', description: 'Cras justo odio, dapibus ac facilisis in, egestas eget quam.' },
//             ],
//             activeImg: '',
//             isFeatured: true,
//             rating: 4,
//             showAllProjects: false,
//             totalAmount: 1000,
//             currentDonation: 630


//         };
//     },

//     mounted() {
//         this.activeImg = this.images[0].url;
//     },
//     methods: {
//         selectActiveImage(index) {
//             this.activeImg = this.images[index].url;
//             this.images.forEach((img, i) => {
//                 img.active = i === index;
//             });
//         }
//         , showAllSimilarProjects() {
//             this.showAllProjects = true;
//         }
//     },
//     computed: {
//         filledStars() {
//             return this.rating;
//         },
//         emptyStars() {
//             return 5 - this.rating;
//         },
//         limitedImages() {
//             return this.showAllProjects ? this.images : this.images.slice(0, 3);
//         },
//         donationProgress() {
//             return (this.currentDonation / this.totalAmount) * 100;
//         }
//     },
// }
</script> -->