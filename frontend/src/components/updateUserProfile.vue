<template>
	 
    <div class="container">
		<div class="main-body">
			<form  @submit.prevent="handleFormSubmission($event);" class="needs-validation" novalidate> 
			<div class="row">
				 <div class="col-lg-4">
					<div class="card">
						<div class="card-body">
							<div class="d-flex flex-column align-items-center text-center">
                                <div class="image">
									<div class="imgdiv rounded-circle p-1 bg-primary"
   										 :style="{ 'background-image': 'url(' + user.photo + ')' }">
											
										<label class="rounded-5 rounded-top-0" for="inputimg"><i class="fa fa-2x fa-camera" aria-hidden="true"></i><br> new image</label>
											<input type="file" id="inputimg" @change="handleFileChange">
											<div class="invalid-feedback">Please select a vaild image!</div>

									</div>

                                </div>
								<div class="mt-3">
									<h4>  {{user.first_name}} {{user.last_name}}</h4>
									 
								</div>
							</div>
							<hr class="my-4">
							
						</div>
					</div>
				</div>
				<div class="col-lg-8">
					<div class="card">
						<div class="card-body">
							<div class="row mb-3">
								<div class="col-sm-3">
									<h6 class="mb-0">First Name</h6>
								</div>
								<div class="col-sm-9 text-secondary">
									<input type="text" v-model="fname" class="form-control" pattern="^[a-zA-Z ,.'\-]+$" value="John Doe">
									<div class="invalid-feedback">
										Please enter a valid First name (letters, spaces, commas, periods, single quotes, and hyphens)!.
										</div>
								
								</div>
							</div>
							<div class="row mb-3">
								<div class="col-sm-3">
									<h6 class="mb-0">Last Name</h6>
								</div>
								<div class="col-sm-9 text-secondary">
									<input type="text"  v-model="lname" class="form-control" pattern="^[a-zA-Z ,.'\-]+$" value="John Doe">
								
									<div class="invalid-feedback">
										Please enter a valid Last name (letters, spaces, commas, periods, single quotes, and hyphens)!.
									</div>
								</div>
							</div>
							<div class="row mb-3">
								<div class="col-sm-3">
									<h6 class="mb-0">Email</h6>
								</div>
								<div class="col-sm-9 text-secondary">
									<input type="email" class="form-control" v-model="email"  pattern="[^@\s]+@[^@\s]+\.[^@\s]+" value="john@example.com">
								
									<div class="invalid-feedback">
										Please enter a valid email!.
										</div>
								</div>
							</div>
							<div class="row mb-3">
								<div class="col-sm-3">
									<h6 class="mb-0">Phone</h6>
								</div>
								<div class="col-sm-9 text-secondary">
									<input type="text" class="form-control" v-model="mobile"   pattern='^01[012]\d{8}$'  >
									<div class="invalid-feedback">
										Please enter user Mobile no.!.
										</div>
								</div>
							</div>
						 
							<div class="row mb-3">
								<div class="col-sm-3">
									<h6 class="mb-0">Country</h6>
								</div>
								<div class="col-sm-9 text-secondary">
									<select class="form-select" id="validationCustom04" pattern="^[a-zA-Z ,.'\-]+$" v-model="country">
										<option selected disabled value="">Choose...</option>
										<option v-for="country in countries" :key="country ">{{ country}}</option>
										<option> </option>
									</select>
									<div class="invalid-feedback">
										Please select a valid state.
										</div>
								</div>
							</div>
							<div class="row mb-3">
								<div class="col-sm-3">
									<h6 class="mb-0">Birthdate</h6>
								</div>
								<div class="col-sm-9 text-secondary">
									<input type="date" class="form-control "  
									v-model="birthdate" 
									pattern="^(((0[13-9]|1[012])[-/]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[-/]?31|02[-/]?(0[1-9]|1[0-9]|2[0-8]))[-/]?[0-9]{4}|02[-/]?29[-/]?([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00))$"
									 >
									<div class="invalid-feedback">
										Please provide a valid Birthdate.
										</div>
								</div>
							</div>
							<div class="row mb-3">
								<div class="col-sm-3">
									<h6 class="mb-0">Facebook account</h6>
								</div>
								<div class="col-sm-9 text-secondary">
									<input type="text"
									v-model="facebook"
									 class="form-control"
									 pattern="(?:https?:\/\/)?(?:www\.)?(mbasic.facebook|m\.facebook|facebook|fb)\.(com|me)\/(?:(?:\w\.)*#!\/)?(?:pages\/)?(?:[\w\-\.]*\/)*([\w\-\.]*)"
									  value="www.facebook.com">
									  <div class="invalid-feedback">
                                        Please provide a valid Facebook account.</div>
								</div>
							</div>
							<div class="row">
								<div class="col-sm-3"></div>
								<div class="col-sm-9 text-secondary">
									<button class="btn btn-primary px-4">Save Changes</button>
									 
								</div>
							</div>
						</div>
					</div>
				 
				</div>
			
			</div>
		</form>
		</div>
	</div>
  </template>
  
  <script>
   import{datastore}from '@/stors/crowdfundingStore'
  import FunctionsClass from '../assets/js/registerAndUpdate'
   const functionsObject=new FunctionsClass();
  export default {
	data:()=>({
		storData:datastore(),
	  user:{},
      fname: '',
      lname: '',
      email:'',
      mobile:'',
      country:'',
      birthdate:'',
      facebook:'',
      id:'',
      file:null,
      countries: [],
      }),
	  async  created(){
		await functionsObject.logedInPagesCreated(this)
		await functionsObject.created(this)
		this.fname=this.user.first_name;
		this.lname=this.user.last_name;
		this.email=this.user.email;
		this.mobile=this.user.phone;
        this.country=this.user.country;
        this.birthdate=this.user.birth_date;
        this.facebook=this.user.facebook;
        this.id=this.user.id;
	  },
	  methods:{
		
		handleFormSubmission(e)
		{ 
			functionsObject.handleFormSubmission(e,this,'update')
        },
		 
		handleFileChange(e){
			functionsObject.handleFileChange(e,this)
		}
	  }
		}
	  

  
  </script>
  
  <style>
  .imgdiv{
    background-image: url('https://bootdey.com/img/Content/avatar/avatar6.png');
    background-position: center;
    background-size: cover ;
    height:100px ;
    width:100px;
    position: relative;
  }
  input[type=file]{
 display: none;
  }
  label[for=inputimg]{
    cursor: pointer;
    opacity:0 ;
    background-color: black;
    position: absolute;
    bottom: 0;
    width: 100px;
    left: 0px;
    font-size: 14px;
    transition:all 0.5s;

  }
  .imgdiv:hover label{
    opacity: 1; 

  }
  </style>