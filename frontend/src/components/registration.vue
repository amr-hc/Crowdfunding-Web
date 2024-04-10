<template>
  <div class="register  row justify-content-center align-items-center ">
    <div class="registerCard  bg-white  row flex-column   ">
      <ul class="nav nav-pills nav-justified  m-2" id="ex1" role="tablist">
  <li class="nav-item" role="presentation">
    <router-link to="/login"><button class="nav-link " id="tab-register" data-mdb-toggle="pill" role="tab"
      aria-controls="pills-register" aria-selected="false">Login</button></router-link>
     
  </li>
  
  <li class="nav-item" role="presentation">
    <router-link to="/registration"><button class="nav-link " id="tab-register" data-mdb-toggle="pill" role="tab"
      aria-controls="pills-register" aria-selected="false">Register</button></router-link>
  </li>
</ul>
      <form class="row flex-column  justify-content-center align-items-center needs-validation" novalidate>
  
        <div class="text-center ">
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
  <div class="name col-md-10 p-0 row  ">
        <div class="col-md-6">
    <label for="validationCustom01" class="form-label">Frist Name</label>
    <input type="text" class="form-control" id="validationCustom01" value="" name="fname" required>
    <div class="valid-feedback">
      Looks good!
    </div>
  </div>
        <div class="col-md-6">
    <label for="validationCustom1" class="form-label">Last Name</label>
    <input type="text" class="form-control" id="validationCustom1" value="" name="lname" required>
    <div class="valid-feedback">
      Looks good!
    </div>
  </div>
</div>
  <div class="col-md-10">
    <label for="validationCustom02" class="form-label">Email</label>
    <input type="email" class="form-control" id="validationCustom02" value="" required>
    <div class="valid-feedback">
      Looks good!
    </div>
  </div>
 
  <div class="col-md-10">
    <label for="validationCustomMobile" class="form-label">Mobile phone </label>
    <div class="input-group has-validation">
      <input type="number" class="form-control" id="validationCustomMobile" aria-describedby="inputGroupPrepend" required>
      <div class="invalid-feedback">
        Please choose a Mobile phone.
      </div>
    </div>
  </div>
  <div class="col-md-10">
    <label for="validationCustom03" class="form-label">Password </label>
    <input type="password " class="form-control" id="validationCustom03" required>
    <div class="invalid-feedback">
      Please provide a valid password.
    </div>
  </div>
  <div class="col-md-10">
    <label for="validationCustom3" class="form-label">Confirm password </label>
    <input type="password " class="form-control" id="validationCustom3" required>
    <div class="invalid-feedback">
      Please provide a valid password.
    </div>
  </div>

  
  <div class="col-md-10">
    <label for="validationCustom04" class="form-label">Country</label>
    <select class="form-select" id="validationCustom04">
      <option selected disabled value="">Choose...</option>
      <option v-for="country in countries" :key="country ">{{ country}}</option>
      <option  
       > </option>
    </select>
    <div class="invalid-feedback">
      Please select a valid state.
    </div>
  </div>
 
  <div class="col-md-10">
    <label for="validationCustom7" class="form-label">Birthdate</label>
    <input type="date" class="form-control" id="validationCustom7" >
    <div class="invalid-feedback">
      Please provide a valid Birthdate.
    </div>
  </div>

  <div class="col-md-10">
    <label for="validationCustom08" class="form-label">facebook account</label>
    <input type="text" class="form-control" id="validationCustom08" value="" >
    <div class="valid-feedback">
      Looks good!
    </div>
  </div>

  <div class="col-12 m-2 row">
    <button class="btn btn-primary" type="submit">Submit form</button>
  </div>
</form>
      
    </div>
  </div>

 
</template>

<script>
export default {
    data:()=>({
      fname:'',
      lname:'',
      email:'',
      mobile:'sxs',
      password:'',
      cpassword:'',
      country:'',
      birthdate:'',
      facebook:'',
      countries: []
      }),
      async created() {
    try {
        const response = await fetch('https://countriesnow.space/api/v0.1/countries/codes');
        const data = await response.json();
        this.countries=data.data.map((data)=>{
          return data.name
        })
         
    } catch (error) {
        console.error("Error fetching country codes:", error);
    }
},
  
}
</script>


<style scoped>
.register{
  background-image: url("../assets/imges/pexels-branimir-balogović-3959485.jpg");
  background-position: center ;
  background-size: cover ;
  
}
.registerCard{border-radius: 10%;
opacity: 0.8;
color:black;
height: 98vh;
width: 60vw ;
}
p{
  margin-top: 0;
    margin-bottom: 0;
}
</style>
