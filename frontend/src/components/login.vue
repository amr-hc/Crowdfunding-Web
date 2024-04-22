<template>
  <div class="login mt-3 row justify-content-center align-items-center rounded">
    <div
      class="loginCard bg-white rounded row flex-column justify-content-evenly"
    >
      <!-- Pills content -->

      <div class="normalLogIn row gap-4 justify-content-center">
        <p class="text-center text-danger d-none errMsg">
          Invalid Email or Password
        </p>
        <!-- Email input -->
        <div class="form-floating">
          <input
            type="email"
            id="loginName"
            class="form-control"
            placeholder="email"
            v-model="email"
          />
          <label for="loginName" class="text-dark">Email</label>
        </div>

        <!-- Password input -->
        <div class="form-floating">
          <input
            type="password"
            id="loginPassword"
            class="form-control"
            placeholder="password"
            v-model="password"
          />
          <label class="text-dark" for="loginPassword">Password</label>
        </div>

        <!-- 2 column grid layout -->
        <div class="row g-0">
          <div class="col-md-6 d-flex justify-content-center">
            <!-- Checkbox -->
            <div class="form-check mb-3 mb-md-0">
              <input
                class="form-check-input"
                type="checkbox"
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
            <a href="#!" class="text-decoration-none text-dark"
              >Forgot password?</a
            >
          </div>
        </div>
      </div>

      <!-- Submit button -->
      <button
        type="submit"
        class="btn btn-outline-primary rounded-5"
        @click="checkUser"
      >
        Sign in
      </button>

      <div class="text-center socailsignUp">
        <p>Sign Up with</p>
        <button
          type="button"
          class="btn rounded-circle text-light mx-1"
          style="background-color: #1877f2"
        >
          <i class="fab fa-facebook-f"></i>
        </button>

        <button
          type="button"
          class="btn rounded-circle text-light mx-1"
          style="background-color: #ea4335"
        >
          <i class="fab fa-google"></i>
        </button>

        <button
          type="button"
          class="btn rounded-circle text-light mx-1"
          style="background-color: #2b3137"
        >
          <i class="fab fa-github"></i>
        </button>
      </div>

      <!-- Register buttons -->
      <div class="text-center">
        <span>Not a member? </span>
        <router-link to="/registration" class="text-primary text-decoration-underline ">Register Now</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { datastore } from "@/stors/crowdfundingStore";
export default {
  name: "login",
  data: () => ({
    email: "",
    password: "",
    datastore:datastore(),
  }),
  beforeCreate() {
    localStorage.clear();
    sessionStorage.clear();
  },
  methods: {
    checkUser() {
      const userData = {
        username: this.email,
        password: this.password,
      };
      fetch("http://127.0.0.1:8000/api/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
      })
        .then((res) => {
          if (!res.ok) {
            document.querySelector(".errMsg").classList.remove("d-none");
            throw new Error("invalid");
          }
          return res.json();
        })
        .then((data) => {
          if (document.querySelector("input[type=checkbox]").checked) {
            localStorage.setItem("userInfo", JSON.stringify(data));
          } else {
            sessionStorage.setItem("userInfo", JSON.stringify(data));
          }
          window.location.href='http://localhost:8080/'
                    // this.datastore.setAuthentication(true);
        })
        .catch((err) => console.error(err));
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.login {
  height: 85vh;
}
.loginCard {
  opacity: 0.8;
  color: black;
  width: 33%;
  height: 100%;
}
#loginName,
#loginPassword {
  border: none;
  border-bottom: 0.5px solid #777777e1;
  border-radius: 0% !important;
}
#loginName:focus,
#loginPassword:focus {
  box-shadow: none !important;
}
@media (orientation: portrait) {
  .loginCard {
    width: 60%;
  }
}
input:-webkit-autofill,
input:-webkit-autofill:focus {
  transition: background-color 0s 600000s, color 0s 600000s !important;
}
@media (max-width: 768px) {
  .loginCard {
    width: 50%;
  }
}

@media (min-width: 769px) and (max-width: 1024px) {
  .loginCard {
    width: 40%;
  }
}
</style>
