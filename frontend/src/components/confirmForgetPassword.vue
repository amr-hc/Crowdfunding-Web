<template>
  <div class="basecont py-3 py-md-5">
    <div class="container">
      <div class="row justify-content-md-center">
        <div class="col-12 col-md-11 col-lg-8 col-xl-7 col-xxl-6">
          <div class="bg-dark p-4 p-md-5 rounded shadow-sm">
            <div class="row gy-3 mb-5">
              <div class="col-12">
                <div class="text-center">
                  <a href="#!"> </a>
                </div>
              </div>
              <div class="col-12">
                <h2
                  class="fs-4 fw-normal text-center text-secondary gont m-0 px-md-5"
                >
                  Now Enter a new password that you want reset to your account.
                </h2>
              </div>
            </div>
            <form action="#!" @submit.prevent="changePassword" >
              <div class="row gy-3 gy-md-4 overflow-hidden">
                <div class="col-12">
                  <div class="input-group row flex-column">
                    <label for="password" class="form-label p-0"
                      >New Password <span class="text-danger">*</span></label
                    >
                    <input
                      type="password"
                      pattern="^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
                      class="form-control rounded w-75 mb-2"
                      name="password"
                      id="password"
                      v-model="password"
                      required
                    />
                  </div>
                  <div class="col-12">
                    <div class="input-group row flex-column">
                      <label for="confirmpassword" class="form-label p-0"
                        >Confirm New Password
                        <span class="text-danger">*</span></label
                      >

                      <input
                        type="password"
                        pattern="^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
                        class="form-control form-control rounded w-75"
                        name="confirmpassword"
                        id="confirmpassword"
                        v-model="comfirmPassword"
                        required
                      />
                    </div>
                  </div>
                </div>
                <div class="col-12">
                  <div class="d-grid">
                    <button class="btn btn-primary btn-lg" type="submit">
                      Reset Password
                    </button>
                  </div>
                </div>
              </div>
            </form>
            <div
  id="message-container"
  class="alert mt-3"
  :class="{'bg-danger': showError, 'bg-success': showSuccess}"
  v-if="showMessage"
>
  {{message}}
</div>
            <div class="row">
              <div class="col-12">
                <hr class="mt-5 mb-4 border-secondary-subtle" />
                <div class="d-flex gap-4 justify-content-center">
                  <router-link
                    class="fs-5 link-secondary text-decoration-none"
                    to="/login"
                    ><button
                      class="nav-link"
                      data-mdb-toggle="pill"
                      role="tab"
                      aria-controls="pills-register"
                      aria-selected="false"
                    >
                      Login
                    </button></router-link
                  >

                  <router-link
                    class="fs-5 link-secondary text-decoration-none"
                    to="/registration"
                    ><button
                      class="nav-link"
                      id="tab-register"
                      data-mdb-toggle="pill"
                      role="tab"
                      aria-controls="pills-register"
                      aria-selected="false"
                    >
                      Register
                    </button></router-link
                  >
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
  created(){
    const urlParams = new URLSearchParams(window.location.search);
     this.uid = urlParams.get("uid");
     this.token = urlParams.get("token");
      if(!this.uid || !this.token){
        this.$router.push('/')
      }
  },
  data: () => ({
    token: "",
    uid: "",
    password: "",
    comfirmPassword: "",
    showMessage: false, 
    showError: false,
    showSuccess: false,
  }),
  methods: {
    changePassword() {
      if (this.password !== this.comfirmPassword) {
        console.log("Passwords do not match");
        this.showMessage = true;
        this.showError = true;
        this.showSuccess = false;
        this.message = "The new password and confirm password don`t match. Please make sure they are the same."
        setTimeout(() => {
              this.showMessage = false;
            }, 2000);
        return;

      }
      if (!this.isValidPassword(this.password)) {
        this.showMessage = true;
        this.showError = true;
        this.showSuccess = false;
        this.message = "Password must be at least 8 characters long and contain at least one letter and one number.";
        setTimeout(() => {
          this.showMessage = false;
        }, 4000);
        return;
      }
      
      // const urlParams = new URLSearchParams(window.location.search);
      // const uid = urlParams.get("uid");
      // const token = urlParams.get("token");

      const passwordData = new FormData();
      passwordData.append("uidb64", this.uid);
      passwordData.append("token", this.token);
      passwordData.append("new_password", this.password);
      fetch("http://127.0.0.1:8000/password/reset-password/", {
        method: "POST",
        body: passwordData,
      })
        .then((res) => {
          if (!res.ok) {
            this.message="failed to change password";
            this.showMessage = true;
            this.showError = true;
            this.showSuccess = false;
            console.log("failed to change password");
            setTimeout(() => {
              this.showMessage = false;
            }, 2000);

          } else {
            this.showMessage = true;
            this.showError = false;
            this.showSuccess = true;
            this.message="Password change successfuly"
            setTimeout(() => {
              this.showMessage = false;
            }, 2000);
            console.log("Password change successfuly");
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
    isValidPassword(password) {
      const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
      return passwordRegex.test(password);
    },
  },
  
};
</script>
  
  <style scoped>
  .message-container {
    display: none;
  }
  .message-container.show {
    display: block;
  }
.basecont {
  background-color: rgb(91 91 91 / 50%);
}
/* .bg-white{
    background-color: rgb(91 91 91 / 50%)!important;
  } */
</style>