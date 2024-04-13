<template>
<div class=" basecont py-3 py-md-5">
  <div class="container">
    <div class="row justify-content-md-center">
      <div class="col-12 col-md-11 col-lg-8 col-xl-7 col-xxl-6">
        <div class="bg-dark p-4 p-md-5 rounded shadow-sm">
          <div class="row gy-3 mb-5">
            <div class="col-12">
              <div class="text-center">
                <a href="#!">
                </a>
              </div>
            </div>
            <div class="col-12">
              <h2 class="fs-4 fw-normal text-center text-secondary gont m-0 px-md-5">Now Enter a new password that you want reset to your account.</h2>
            </div>
          </div>
          <form action="#!">
            <div class="row gy-3 gy-md-4 overflow-hidden">
              <div class="col-12">
                <div class="input-group row flex-column ">
                  <label for="password" class="form-label p-0 ">New Password <span class="text-danger">*</span></label>
                  <input type="password" class="form-control rounded w-75 mb-2" name="password" id="password" required>
                </div>
                <div class="col-12">
                <div class="input-group row flex-column">
                <label for="confirmpassword" class="form-label p-0">Confirm New Password <span class="text-danger">*</span></label>

                <input type="password" class="form-control form-control rounded w-75" name="confirmpassword" id="confirmpassword" required>

              </div>
              </div>
              </div>
              <div class="col-12">
                <div class="d-grid">
                  <button class="btn btn-primary btn-lg" type="submit">Reset Password</button>
                </div>
              </div>
            </div>
          </form>
          <div class="row">
            <div class="col-12">
              <hr class="mt-5 mb-4 border-secondary-subtle">
              <div class="d-flex gap-4 justify-content-center">

                 
    <router-link class="fs-5 link-secondary text-decoration-none" to="/login"><button class="nav-link "  data-mdb-toggle="pill" role="tab"
      aria-controls="pills-register" aria-selected="false">Login</button></router-link>
     
    <router-link class=" fs-5 link-secondary text-decoration-none" to="/registration"><button class="nav-link " id="tab-register" data-mdb-toggle="pill" role="tab"
      aria-controls="pills-register" aria-selected="false">Register</button></router-link>
  
 
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

  </template>
  
  <script>
  export default {
  
  }
  </script>
  
  <style scoped>
 .basecont{
    background-color:  rgb(91 91 91 / 50%) ;
 
 }
 /* .bg-white{
    background-color: rgb(91 91 91 / 50%)!important;
  } */
  </style>