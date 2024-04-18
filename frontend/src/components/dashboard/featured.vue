<template>
    <div class="featured my-4">
        <div class="container ">
            <div class="row">
                <div class="col-12 col-lg">
                    <h4 class="border-bottom border-dark">Featured Projects <i class="fa-solid fa-crown"></i></h4>
                    <div class="row  p-0 ">
                        <div class="project-card p-0" v-for="(project, index) in projects" :key="index">
                            <img :src="project.imageUrl" alt="">
                            <div class="p-3">
                                <h6 class="text-white-50">{{ project.title }}</h6>
                                <p class="author text-white badge bg-primary">{{ project.author }}</p>
                                <div class="project-card-rating">
                                    <i v-for="n in 5" :key="n"
                                        :class="{ 'plus fa-solid fa-star': n <= project.rating, 'minus fa-regular fa-star': n > project.rating }"></i>
                                </div>

                                <p class="m-0">Target: {{ project.target }}</p>
                                <p class="m-0">Current Donation: {{ project.currentDonation }}</p>
                            </div>


                            <!-- Empty cards -->

                        </div>
                        <div v-for="n in emptyCardsCount" :key="n" class="empty-card ">
                            <i class="fa-solid fa-plus"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'featured',
    data() {
        return {
            projects: [
                {
                    imageUrl: 'https://via.placeholder.com/300',
                    title: 'Dynamic Web Application',
                    description: 'Building a modern web application with dynamic features.',
                    author: 'Alice Johnson',
                    rating: 4,
                    topic: 'Development',
                    target: 1500,
                    currentDonation: 800,
                },
                {
                    imageUrl: 'https://via.placeholder.com/300',
                    title: 'Mobile App Redesign',
                    description: 'Redesigning a mobile application for better user experience.',
                    author: 'Bob Smith',
                    rating: 5,
                    topic: 'Design',
                    target: 2000,
                    currentDonation: 1200,
                },
                {
                    imageUrl: 'https://via.placeholder.com/300',
                    title: 'Social Media Campaign',
                    description: 'Launching a social media campaign to increase brand awareness.',
                    author: 'Eve Brown',
                    rating: 4,
                    topic: 'Marketing',
                    target: 1200,
                    currentDonation: 600,
                }
            ],
        };
    },
    computed: {
        emptyCardsCount() {
            const featuredCount = this.projects.length;
            return Math.max(5 - featuredCount, 0);
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
