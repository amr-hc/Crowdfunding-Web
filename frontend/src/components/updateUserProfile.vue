<template>
    <div class="container">
		<div class="main-body">
			<form action=""> 
			<div class="row">
				 <div class="col-lg-4">
					<div class="card">
						<div class="card-body">
							<div class="d-flex flex-column align-items-center text-center">
                                <div class="image">
									<div   class=" imgdiv rounded-circle p-1 bg-primary"  > 
											
										<label class="rounded-5 rounded-top-0" for="inputimg"><i class="fa fa-2x fa-camera" aria-hidden="true"></i><br> new image</label>
											<input type="file" id="inputimg">
									</div>

                                </div>
								<div class="mt-3">
									<h4>John Doe</h4>
									<p class="text-secondary mb-1">Full Stack Developer</p>
									<p class="text-secondary font-size-sm">Bay Area, San Francisco, CA</p>
									
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
									<input type="text" class="form-control" pattern="^[a-zA-Z ,.'\-]+$" value="John Doe">
								</div>
							</div>
							<div class="row mb-3">
								<div class="col-sm-3">
									<h6 class="mb-0">Last Name</h6>
								</div>
								<div class="col-sm-9 text-secondary">
									<input type="text" class="form-control" pattern="^[a-zA-Z ,.'\-]+$" value="John Doe">
								</div>
							</div>
							<div class="row mb-3">
								<div class="col-sm-3">
									<h6 class="mb-0">Email</h6>
								</div>
								<div class="col-sm-9 text-secondary">
									<input type="email" class="form-control"  pattern="[^@\s]+@[^@\s]+\.[^@\s]+" value="john@example.com">
								</div>
							</div>
							<div class="row mb-3">
								<div class="col-sm-3">
									<h6 class="mb-0">Phone</h6>
								</div>
								<div class="col-sm-9 text-secondary">
									<input type="number" class="form-control"  pattern="^[1-9]\d*$" value="(239) 816-9029">
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
								</div>
							</div>
							<div class="row mb-3">
								<div class="col-sm-3">
									<h6 class="mb-0">Birthdate</h6>
								</div>
								<div class="col-sm-9 text-secondary">
									<input type="date" class="form-control"
									pattern="^(((0[13-9]|1[012])[-/]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[-/]?31|02[-/]?(0[1-9]|1[0-9]|2[0-8]))[-/]?[0-9]{4}|02[-/]?29[-/]?([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00))$"
									value="22-09-1997">
								</div>
							</div>
							<div class="row mb-3">
								<div class="col-sm-3">
									<h6 class="mb-0">Facebook account</h6>
								</div>
								<div class="col-sm-9 text-secondary">
									<input type="text"
									 class="form-control"
									 pattern="(?:https?:\/\/)?(?:www\.)?(mbasic.facebook|m\.facebook|facebook|fb)\.(com|me)\/(?:(?:\w\.)*#!\/)?(?:pages\/)?(?:[\w\-\.]*\/)*([\w\-\.]*)"
									  value="www.facebook.com">
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
  export default {
  
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