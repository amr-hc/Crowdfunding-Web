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
      <form 
      @submit.prevent="HTMLValidations($event);"
      class="row flex-column  justify-content-center align-items-center needs-validation"
       novalidate>
  
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
        <label for="fname" class="form-label">First name</label>
        <input type="text" class="form-control" id="fname" pattern="^[a-zA-Z ,.'\-]+$"
          placeholder="First name" v-model="fname" required>
        <div class="invalid-feedback">
          Please enter a valid First name (letters, spaces, commas, periods, single quotes, and hyphens)!.
        </div>
      </div>
  <div class="col-md-6">
      <label for="lname" class="form-label">Last name</label>
      <input type="text" class="form-control" id="lname" pattern="^[a-zA-Z ,.'\-]+$" placeholder="Last name"
        v-model="lname" required>
      <div class="invalid-feedback">
        Please enter a valid Last name (letters, spaces, commas, periods, single quotes, and hyphens)!.
      </div>
    </div>
</div>
<div class="name col-md-10 p-0 row  ">
    <div class="col-md-6">
      <label for="useremail" class="form-label">Email</label>
      <input type="email" class="form-control" id="useremail" pattern="[^@\s]+@[^@\s]+\.[^@\s]+"
        placeholder="example@example.com" v-model="email" required>
        <div class="invalid-feedback">
          Please enter a valid email!.
        </div>
    </div>
 
    <div class="col-md-6">
        <label for="room" class="form-label">Mobile phone </label>
        <input type="number" min="1" class="form-control" id="room" pattern="^[1-9]\d*$"
          placeholder="phone number" v-model="mobile" required>
        <div class="invalid-feedback">
          Please enter user Mobile no.!.
        </div>
    </div>
</div>

<div class="name col-md-10 p-0 row  ">
  <div class="col-md-6">
    <label for="password" class="form-label">password</label>
    <input type="password" class="form-control" pattern="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
      id="password" placeholder="enter password" v-model="password" required>
    <div class="invalid-feedback">
      Please enter a valid password Minimum eight characters, at least one letter and one number!.
    </div>
  </div>
  <div class="col-md-6">

    <label for="validationCustom3" class="form-label">Confirm password</label>
    <input type="password" class="form-control" pattern="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
      id="validationCustom3" placeholder="Renter password" v-model="cpassword" required>
    <div class="invalid-feedback">
      Please enter a valid password Minimum eight characters, at least one letter and one number!.
    </div>
  </div>
 </div>
 <div class=" col-md-6 mb-6">
    <label for="userimg" class="form-label">User Image</label>
      <input type="file" @change="handleFileChange" class="form-control" aria-label="user picture"
        id="userimg" required>
      <div class="invalid-feedback">Please select a vaild image!</div>
    </div>
 <div class="name col-md-10 p-0 row  ">
  <div class="col-md-6">
    <label for="validationCustom04" class="form-label">Country</label>
    <select class="form-select" id="validationCustom04" pattern="[^@\s]+@[^@\s]+\.[^@\s]+" v-model="country">
      <option selected disabled value="">Choose...</option>
      <option v-for="country in countries" :key="country ">{{ country}}</option>
      <option  
       > </option>
    </select>
    <div class="invalid-feedback">
      Please select a valid state.
    </div>
  </div>
 
  <div class="col-md-6">
    <label for="validationCustom7" class="form-label">Birthdate</label>
    <input type="date" 
    v-model="birthdate"
    class="form-control"
     id="validationCustom7"
     pattern="^(((0[13-9]|1[012])[-/]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[-/]?31|02[-/]?(0[1-9]|1[0-9]|2[0-8]))[-/]?[0-9]{4}|02[-/]?29[-/]?([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00))$" >
    <div class="invalid-feedback">
      Please provide a valid Birthdate.
    </div>
  </div>
  </div>

  <div class="col-md-10">
    <label for="validationCustom08" class="form-label">facebook account</label>
    <input type="text"
    v-model="facebook"
    class="form-control" 
    id="validationCustom08" 
    pattern="(?:https?:\/\/)?(?:www\.)?(mbasic.facebook|m\.facebook|facebook|fb)\.(com|me)\/(?:(?:\w\.)*#!\/)?(?:pages\/)?(?:[\w\-\.]*\/)*([\w\-\.]*)" value="" >
    <div class="invalid-feedback">
      Please provide a valid facebook account !
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
      mobile:'',
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
  methods:{
    HTMLValidations(e)
    {
      if (!e.target.checkValidity())
       {
          e.preventDefault();
          e.stopPropagation();
          e.target.classList.add("was-validated");
          return false;
        }
        else
        {
          e.target.classList.add("was-validated");
          return true;
        }
    },
  },
}
</script>


<style scoped>
.register{
  background-image: url("../assets/imges/pexels-branimir-balogović-3959485.jpg");
  background-position: center ;
  background-size: cover ;
  height: 100vh;
  
}
.registerCard{
  
  padding: 30px;
  border-radius: 10%;
opacity: 0.8;
color:black;
height: 100%;
width: 60vw ;
}
p{
  margin-top: 0;
    margin-bottom: 0;
}
#userimg{
  display: block;
}
</style>
