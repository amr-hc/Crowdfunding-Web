<template>
   <div class="bg-danger p-3 text-center m-0 oprationsResote" id="faild"></div>
	 <div class="bg-success p-3 text-center m-0 oprationsResote" id="success"></div>
    <div class="container">
    <div class="main-body">
          <div class="row gutters-sm">
          <div class="row data ">
            
              <div class="card col-md-3 mb-3 bg-dark">
                <div class="card-body">
                  <div class="d-flex flex-column align-items-center text-center">
                    <img :src="user.photo" alt="Admin" class="rounded-circle" width="150">
                    <div class="mt-3">
                      <h4> {{user.first_name}} {{user.last_name}}</h4>
                      <p class="text-secondary mb-1">Full Stack Developer</p>
                      <p class=" text-secondary font-size-sm">Bay Area, San Francisco, CA</p>
                      
                    </div>
                  </div>
              </div>
            </div>
              <div class="card mb-3 col-md-9 mb-3 bg-dark">
                <div class="card-body">
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">Full Name</h6>
                    </div>
                    <div class="col-sm-9  ">
                      {{user.first_name}} {{user.last_name}}
                    </div>
                  </div>
                  <hr>
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">Email</h6>
                    </div>
                    <div class="col-sm-9  ">
                      {{user.email}}
                    </div>
                  </div>
                  <hr>
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">Phone</h6>
                    </div>
                    <div class="col-sm-9  ">
                      {{user.last_name}}
                    </div>
                  </div>
                  <hr>
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">Mobile</h6>
                    </div>
                    <div class="col-sm-9 ">
                      {{user.phone}}
                    </div>
                  </div>
                  <hr>
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">Country</h6>
                    </div>
                    <div class="col-sm-9  ">
                      {{user.country}}
                    </div>
                  </div>
                  <hr>
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">Birthdate</h6>
                    </div>
                    <div class="col-sm-9  ">
                      {{user.birth_date}}
                    </div>
                  </div>
                  <hr>
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">facebook account</h6>
                    </div>
                    <div class="col-sm-9  ">
                      {{user.facebook}}
                    </div>
                  </div>
                  <hr>
                  <div class="row">
                    <div class="col-sm-12">
                      <router-link to="/updateUserProfile" class=" m-1 text-decoration-none "><button class="btn btn-info ">Edit</button></router-link>
                    </div>
                  </div>
                </div>
            </div>
        </div>
     <projects /> 
     <donations  /> 

          </div>

        </div>
    </div>
  </template>
  
  <script>
 import{datastore}from '@/stors/crowdfundingStore'
 import FunctionsClass from '../assets/js/registerAndUpdate'
 import projects from "@/components/profile/projects.vue"
 import donations from "@/components/profile/donations.vue"
  const functionsObject=new FunctionsClass();
  export default {
    
    data:()=>({
    storData:datastore(),
   user:{},
    
   }),

  
  methods: {
   
  },
  components: {
    projects,donations
  },
  async created(){
  await functionsObject.logedInPagesCreated(this); 
  }
  }
   
  </script>
  
  <style scoped>
 
</style>
