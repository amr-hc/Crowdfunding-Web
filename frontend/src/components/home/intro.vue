<template>
    <div class="intro text-center">
        <div class="title">
            Connecting <span>Projects</span> <br>and Make Your <span>Invest</span> <br> Comes True
        </div>
        <div class="more btn text-light p-0">
            learn more <i class="ms-1 fa-solid fa-arrow-right-long"></i>
        </div>
        <div class="statics row gap-2 ">
            <div class="statics_card d-flex flex-column justify-content-center align-items-center">
                <h2 class="m-0">100+</h2>
                <p class="m-0 text-light ">Years Of Experience</p>
            </div>
            <div class="statics_card d-flex flex-column justify-content-center align-items-center">
                <h2 class="m-0">1M+</h2>
                <p class="m-0 text-light ">Completed Projects</p>
            </div>
            <div class="statics_card d-flex flex-column justify-content-center align-items-center">
                <h2 class="m-0">100K+</h2>
                <p class="m-0 text-light ">Trusted Company</p>
            </div>
            <div class="statics_card d-flex flex-column justify-content-center align-items-center">
                <h2 class="m-0">10B+</h2>
                <p class="m-0 text-light ">Total Transactions</p>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    name: 'intro',
    data() {
        return {

        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.intro {
    min-height: calc(100vh - 62px);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;
}

.title {
    font-size: 60px;
    text-align: center;
}

@media only screen and (max-width: 600px) {
    .title {
        font-size: 30px;
    }
}

span {
    color: var(--secondary-color-1);
}

.statics .statics_card {
    width: 200px;
    height: 100px;
    background-color: var(--primary-color-2);
    margin: 0 auto;
    border-radius: 10px;
    margin-top: 50px;
    margin-bottom: 50px;

}
</style>