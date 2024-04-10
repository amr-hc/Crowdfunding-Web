<template>
 <div class="login vh-100 row justify-content-center align-items-center ">
<div class="loginCard w-50  bg-white  row flex-column   ">

<ul class="nav nav-pills nav-justified mb-3" id="ex1" role="tablist">
  <li class="nav-item" role="presentation">
    <router-link to="/login"><button class="nav-link " id="tab-register" data-mdb-toggle="pill" role="tab"
      aria-controls="pills-register" aria-selected="false">Login</button></router-link>
     
  </li>
  
  <li class="nav-item" role="presentation">
    <router-link to="/registration"><button class="nav-link " id="tab-register" data-mdb-toggle="pill" role="tab"
      aria-controls="pills-register" aria-selected="false">Register</button></router-link>
  </li>
</ul>
<!-- Pills navs -->

      <!-- Pills content -->
      <div class="tab-content">
        <div
          class="tab-pane fade show active"
          id="pills-login"
          role="tabpanel"
          aria-labelledby="tab-login"
        >
          <form>
            <div class="text-center mb-3">
              <p>Sign in with:</p>
              <button type="button" class="btn btn-link btn-floating mx-1">
                <i class="fab fa-facebook-f"></i>
              </button>

              <button type="button" class="btn btn-link btn-floating mx-1">
                <i class="fab fa-google"></i>
              </button>

              <button type="button" class="btn btn-link btn-floating mx-1">
                <i class="fab fa-twitter"></i>
              </button>

              <button type="button" class="btn btn-link btn-floating mx-1">
                <i class="fab fa-github"></i>
              </button>
            </div>

            <p class="text-center">or:</p>

            <!-- Email input -->
            <div class="form-outline mb-4">
              <input type="email" id="loginName" class="form-control" />
              <label class="form-label" for="loginName"
                >Email or username</label
              >
            </div>

            <!-- Password input -->
            <div class="form-outline mb-4">
              <input type="password" id="loginPassword" class="form-control" />
              <label class="form-label" for="loginPassword">Password</label>
            </div>

            <!-- 2 column grid layout -->
            <div class="row mb-4">
              <div class="col-md-6 d-flex justify-content-center">
                <!-- Checkbox -->
                <div class="form-check mb-3 mb-md-0">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value=""
                    id="loginCheck"
                    checked
                  />
                  <label class="form-check-label" for="loginCheck">
                    Remember me
                  </label>
                </div>
              </div>

              <div class="col-md-6 d-flex justify-content-center">
                <!-- Simple link -->
                <a href="#!">Forgot password?</a>
              </div>
            </div>

            <!-- Submit button -->
            <button type="submit" class="btn btn-primary btn-block mb-4">
              Sign in
            </button>

      <!-- Register buttons -->
      <div class="text-center">
        <p>Not a member? <a href="#!">Register</a></p>
      </div>
    </form>
  </div>
   
</div>
</div>
</div>
  </template>
  
  <script>
  export default {
    name: 'HelloWorld',
    props: {
      msg: String
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .login{
    background-image: url("../assets/imges/pexels-branimir-balogović-3959485.jpg");
    background-position: center ;
    background-size: cover ;
    height: 100vh;
    flex-wrap: nowrap !important;

    
  }
  .loginCard{border-radius: 10%;
  opacity: 0.8;
  color:black;

  height: 100%;
  flex-wrap: nowrap !important;

  }
  </style>
  