<template>
    <button type="button" class="btn btn-info" data-bs-toggle="modal" data-bs-target="#staticBackdrop">Edit</button>
    
      <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header">
                  <h5 class="modal-title" id="staticBackdropLabel">Edit Project Form</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
             </div>
                        
            <div class="modal-body">
              <form class="row g-3 needs-validation" novalidate>
                    <div class="col-md-6">
                      <label for="validationCustom01" class="form-label">id</label>
                      <input v-model="id" type="text" class="form-control" id="validationCustom01"  required>
                      <div class="valid-feedback">
                          Looks good!
                      </div>
                  </div>
                  <div class="col-md-6">
                      <label for="validationCustom02" class="form-label"> Title</label>
                      <input  v-model="title" type="text" class="form-control" id="validationCustom02"  required>
                      <div class="valid-feedback">
                          Looks good!
                      </div>
                  </div>
    
                <div class="col-md-6">
                  <label for="validationCustom03" class="form-label">Target Money</label>
                  <input  v-model="targetMoney" type="text" class="form-control" id="validationCustom03" required>
                  <div class="invalid-feedback">
                    Please provide a valid Target Money.
                  </div>
                </div>
                <div class="col-md-6">
                    <label for="validationCustom05" class="form-label">Category</label>
                    <select class="form-select" id="validationCustom05" 
                    pattern="^[a-zA-Z ,.'\-]+$" v-model="category">
                    <option selected disabled value="">Choose...</option>
                    <option v-for="cat in categories" :key="cat.id" >
                    </option>
                    <option  
                    > </option>
                    </select>
                    <div class="invalid-feedback">
                    Please select a valid category.
                    </div>
                </div>
                <div class="col-md-12">
                  <label for="validationCustom04" class="form-label">Description</label>
                  <textarea
                        class="form-control"
                        name="description"
                        id="validationCustom04"
                        placeholder="description"
                        v-model="description"
                        style="height: 100px"
                        required
                    ></textarea>
                  <div class="invalid-feedback">
                    Please provide a valid Description.
                  </div>
                </div>
              
                <div class="col-md-6">
                  <label for="validationCustom06" class="form-label">Project End Date</label>
                  <input v-model="city" type="DATE" class="form-control" id="validationCustom06" required>
                  <div class="invalid-feedback">
                    Please provide a valid Date.
                  </div>
                </div>
             
            </form>
            </div>         
            <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                  <button  @click="reseevent()" class="btn btn-primary" type="submit" data-bs-dismiss="modal"  >Submit form</button>
            </div>
                                   
        </div>
      </div>
    </div>
    </template>
  
  <script>
  export default {
            
            
    props: {
      project_id: String
    },
    data:()=>({

    }),
     async created(){
      console.log(this.project_id)
    
    },
    methods:{
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
        color: #058728;

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

.congratulation-contents button {
  border-radius: 16px;
  background-color: #007bd3bd;
  border: none;
  color: #fff;
  text-align: center;
  font-size: 32px;
  padding: 6px;
  width: 400px;
  transition: all 0.5s;
  cursor: pointer;
  margin: 36px;
  box-shadow: 0 10px 20px -8px rgba(0, 0, 0,.7);
}

button{
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}

button:after {
  content: '»';
  position: absolute;
  opacity: 0;  
  top: 6px;
  right: -20px;
  transition: 0.5s;
}

button:hover{
  padding-right: 24px;
  padding-left:8px;
}

button:hover:after {
  opacity: 1;
  right: 10px;
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