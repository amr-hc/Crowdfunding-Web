<template>
    <div class="row  p-0  p-4">
        <h4 class="border-bottom border-dark">All projects</h4>
        <div class="row p-0">
            <div class="project-card p-0" v-for="(project, index) in projects" :key="index">
                <img :src="project.imageUrl" alt="">
                <div class="p-3">
                    <h6 class="text-white-50 overflow overflow-hidden">{{ project.title }}</h6>
                    <p class="author badge bg-primary text-white-50">{{ project.author }}</p>
                    <div class="project-card-rating">
                        <i v-for="n in 5" :key="n"
                            :class="{ 'plus fa-solid fa-star': n <= project.rating, 'minus fa-regular fa-star': n > project.rating }"></i>
                    </div>
                    <p>Target: {{ project.target }}</p>
                    <p>Current Donation: {{ project.currentDonation }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {

    name: 'projects',
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
                },
                {
                    imageUrl: 'https://via.placeholder.com/300',
                    title: 'Machine Learning Project',
                    description: 'Implementing machine learning algorithms for data analysis.',
                    author: 'Charlie Wilson',
                    rating: 3,
                    topic: 'Technology',
                    target: 1800,
                    currentDonation: 1000,
                },
                {
                    imageUrl: 'https://via.placeholder.com/300',
                    title: 'E-commerce Website Upgrade',
                    description: 'Upgrading an e-commerce website with new features and optimizations.',
                    author: 'Grace Lee',
                    rating: 4,
                    topic: 'Software',
                    target: 2500,
                    currentDonation: 1500,
                }

            ],
        };
    },
}
</script>

<style scoped>
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

.project-card .text-white-50 {
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}
</style>
