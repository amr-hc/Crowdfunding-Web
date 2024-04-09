<template>
    <div class="container">
    <div class="main-body">
    
          <!-- Breadcrumb -->
          <nav aria-label="breadcrumb" class="main-breadcrumb">
  <ol class="breadcrumb">
     
    <router-link to="/" class=" m-1 text-decoration-none"><button class="nav-link ">Home</button></router-link>
    <router-link to="/projects" class=" m-1 text-decoration-none"><button class="nav-link ">Projects</button></router-link>
    <router-link to="/profile" class=" m-1 text-decoration-none "><button class="nav-link  ">User Profile</button></router-link>
  </ol>
</nav>
          <!-- /Breadcrumb -->
    

          <div class="row gutters-sm">
          <div class="row ">
            
              <div class="card col-md-3 mb-3 bg-dark">
                <div class="card-body">
                  <div class="d-flex flex-column align-items-center text-center">
                    <img src="https://bootdey.com/img/Content/avatar/avatar7.png" alt="Admin" class="rounded-circle" width="150">
                    <div class="mt-3">
                      <h4>John Doe</h4>
                      <p class="text-secondary mb-1">Full Stack Developer</p>
                      <p class=" text-secondary font-size-sm">Bay Area, San Francisco, CA</p>
                      
                    </div>
                  </div>
              </div>
            </div>
              <div class="card mb-3 col-md-8 mb-3 bg-dark">
                <div class="card-body">
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">Full Name</h6>
                    </div>
                    <div class="col-sm-9  ">
                      Kenneth Valdez
                    </div>
                  </div>
                  <hr>
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">Email</h6>
                    </div>
                    <div class="col-sm-9  ">
                      fip@jukmuh.al
                    </div>
                  </div>
                  <hr>
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">Phone</h6>
                    </div>
                    <div class="col-sm-9  ">
                      (239) 816-9029
                    </div>
                  </div>
                  <hr>
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">Mobile</h6>
                    </div>
                    <div class="col-sm-9 ">
                      (320) 380-4539
                    </div>
                  </div>
                  <hr>
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">Address</h6>
                    </div>
                    <div class="col-sm-9  ">
                      Bay Area, San Francisco, CA
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

            <div class="row pro  ">
                <div class="card d-flex position-relative flex-column bg-dark">
            <div class='imgContainer'>
                <img src='../assets/imges/vecteezy_miniature-travelers-with-bicycles-in-the-park-healthy_2131939.jpg'>
            </div>
            <div class="content">
                <h2>Card One</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eget velit tristique, sollicitudin leo viverra, suscipit neque. Aliquam ut facilisis urna, in pretium nibh.  Morbi in leo in eros commodo volutpat ac sed dolor.</p>
            </div>
        </div>
        <div class="card d-flex position-relative flex-column bg-dark">
            <div class='imgContainer'>
                <img src='../assets/imges/vecteezy_person-hike-friends-helping-each-other-up-a-mountain-man_10621923.jpg'>
            </div>
            <div class="content">
                <h2>Card Two</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eget velit tristique, sollicitudin leo viverra, suscipit neque. Aliquam ut facilisis urna, in pretium nibh.  Morbi in leo in eros commodo volutpat ac sed dolor.</p>
            </div>
        </div>
        <div class="card d-flex position-relative flex-column bg-dark ">
            <div class='imgContainer'>
                <img src='../assets/imges/vecteezy_travel-man-wait-train-at-platform-people-vacation_8743819.jpg'>
            </div>
            <div class="content">
                <h2>Card Three</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eget velit tristique, sollicitudin leo viverra, suscipit neque. Aliquam ut facilisis urna, in pretium nibh.  Morbi in leo in eros commodo volutpat ac sed dolor.</p>
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
 
</style>
