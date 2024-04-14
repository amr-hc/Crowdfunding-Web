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
                  Provide the email address associated with your account to
                  recover your password.
                </h2>
              </div>
            </div>
            <form action="#!" @submit.prevent="checkEmail">
              <div class="row gy-3 gy-md-4 overflow-hidden">
                <div class="col-12">
                  <label for="email" class="form-label"
                    >Email <span class="text-danger">*</span></label
                  >
                  <div class="input-group">
                    <span class="input-group-text">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="16"
                        height="16"
                        fill="currentColor"
                        class="bi bi-envelope"
                        viewBox="0 0 16 16"
                      >
                        <path
                          d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z"
                        />
                      </svg>
                    </span>
                    <input
                      type="email"
                      class="form-control"
                      name="email"
                      id="email"
                      required
                      v-model="email"
                      pattern="[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
                    />
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
  data: () => ({
    email: "",
    showMessage: false, 
    message:"",
    showError: false,
    showSuccess: false,
  }),
  methods: {
    checkEmail() {
      const emailData = new FormData();
      emailData.append("email", this.email);
      fetch("http://127.0.0.1:8000/password/forget-password/", {
        method: "POST",
        body: emailData,
      })
        .then((res) => {
          if (!res.ok) {
            this.showError = true;
            this.showSuccess = false;
            this.showMessage = true;
            this.message="This email isn`t exist"
            console.log("Failed to send email");

          } else {
            console.log("Email sent successfully");
            this.showMessage = true;
            this.showError = false;
            this.showSuccess = true;
            this.message="Email sent successfully"
            setTimeout(() => {
              this.showMessage = false;
            }, 2000);
          }
          return res.json();
        })
        .then((data) => {})
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>
  
  <style scoped>
.basecont {
  background-color: rgb(91 91 91 / 50%);
}
.message-container {
  display: none;
}
.message-container.show {
  display: block;
}
/* .bg-white{
    background-color: rgb(91 91 91 / 50%)!important;
  } */
</style>