<template>
    <div class="whyus row m-0 align-items-center text-center">
        <div class="col d-none d-lg-block">
            <img :src="imgSrc" width="75%" alt="img">
        </div>
        <div class="col row gap-2">
            <h1 class=" w-auto btn disabled rounded-3">Features</h1>
            <h3 class="text-center fw-lighter">Trusted platform to get <br> money & invest</h3>
            <p class="text-start text-white-50">We are here for those of you who find it difficult to find a platform to
                find funds for your business presents a platform that can be accessed and get funds from all parts of
                the world</p>
            <div class="row gap-2">
                <div class="col item text-white-50 d-flex flex-column justify-content-center">
                    <p><i class="fa-solid fa-location-arrow fa-2x"></i></p>
                    <p>Easy navigate and have a lot of categories</p>
                </div>
                <div class="col item text-white-50 d-flex flex-column justify-content-center">
                    <p><i class="fa-solid fa-list-check fa-2x"></i></p>
                    <p>Complete category variants you can use to cover your project</p>
                </div>
            </div>
            <div class="row gap-2">

                <div class="col item text-white-50 d-flex flex-column justify-content-center">
                    <p><i class="fa-solid fa-shield-halved fa-2x"></i></p>
                    <p>Save payment and transparent money flow</p>
                </div>
                <div class="col item text-white-50 d-flex flex-column justify-content-center">
                    <p><i class="fa-solid fa-earth-africa fa-2x"></i></p>
                    <p>A lot of choice arround the world</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'whyus',
    data() {
        return {
            imgSrc: require('@/assets/images/features.svg')

        }
    }
}
</script>

<style scoped>
.whyus {
    min-height: 100vh;
}

.item {
    font-size: 12px;
    width: 300px;
    height: 150px;
    border-radius: 20px;
    background-color: var(--primary-color-350);
}
</style>