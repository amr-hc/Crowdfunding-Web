<template>
     <div class="congratulation-area text-center mt-5">
    <div class="container">
        <div class="congratulation-wrapper">
            <div class="congratulation-contents center-text"> 
                        <p class="congratulation-contents-para"> 
                             You have successfully completed the registration. The only remaining step is to verify the account via email. Please check your email to activate the account. </p>
               
            </div>
        </div>
    </div>
</div>
  </template>


  
  <script>
  export default {
  beforeCreate(){
    const sessionStorageData=JSON.parse(sessionStorage.getItem("needactivation"));
    if(!sessionStorageData){
        this.$router.push('/login');
    }
  }
  }
  </script>
  
  <style scoped>
  .congratulation-wrapper {
        max-width: 550px;
        margin-inline: auto;
        -webkit-box-shadow: 0 0 20px #f3f3f3;
        box-shadow: 0 0 20px #f3f3f3;
        padding: 30px 20px;
        background-color: #ffffffd9;
        border-radius: 10px;
        color: #06641f;

    }
    .congratulation-contents-title {
        font-size: 32px;
        line-height: 36px;
        margin: -6px 0 0;
    }
    .congratulation-contents-para {
        font-size: 18px;
        line-height: 24px;
        margin-top: 15px;
    }
    .btn-wrapper {
        display: block;
    }
    .cmn-btn.btn-bg-1 {
        background: #6176f6;
        color: #fff;
        border: 2px solid transparent;
        border-radius:3px;
        text-decoration: none;
        padding:5px;
    }

    .success-animation { margin:40px auto;}

.checkmark {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    display: block;
    stroke-width: 5;
    stroke: #f1f5ef;
    stroke-miterlimit: 10;
    box-shadow: inset 0px 0px 0px #4bb71b;
    animation: fill .4s ease-in-out .4s forwards, scale .3s ease-in-out .9s both;
    position:relative;
    top: 5px;
    right: 5px;
   margin: 0 auto;
}
.checkmark__circle {
    stroke-dasharray: 166;
    stroke-dashoffset: 166;
    stroke-width: 2;
    stroke-miterlimit: 10;
    stroke: #eaf1e7;
    fill: #4bb71b;
    animation: stroke 0.6s cubic-bezier(0.65, 0, 0.45, 1) forwards;
 
}

.checkmark__check {
    transform-origin: 50% 50%;
    stroke-dasharray: 48;
    stroke-dashoffset: 48;
    animation: stroke 0.3s cubic-bezier(0.65, 0, 0.45, 1) 0.8s forwards;
}
 
 

@keyframes stroke {
    100% {
        stroke-dashoffset: 0;
    }
}

@keyframes scale {
    0%, 100% {
        transform: none;
    }

    50% {
        transform: scale3d(1.1, 1.1, 1);
    }
}

@keyframes fill {
    100% {
        box-shadow: inset 0px 0px 0px 30px #4bb71b;
    }
}
  </style>