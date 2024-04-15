import { createRouter, createWebHistory } from "vue-router";
import worngpaht from "../components/worngpaht";
import intro from "../components/home/intro.vue";
import registration from "../components/registration.vue";
import about from "../components/about.vue";
import investors from "../components/investors.vue";
import projects from "../components/projects.vue";
import projectDetails from "@/components/project/project-details.vue";
import login from "../components/login.vue";
import Home from "@/components/home.vue";
import profile from "../components/profile.vue";
import updateUserProfile from "../components/updateUserProfile.vue";
import addProject from "@/components/addProject.vue";
import congratulations from "@/components/congratulations.vue";
import forgetPassword from "@/components/forgetPassword.vue";
import confirmForgetPassword from "@/components/confirmForgetPassword.vue";

const routes = [
  {
    path: "/",
    component: login,
  },
  {
    path: "/Home",
    component: Home,
  },
  {
    path: "/registration",
    component: registration,
  },

  {
    path: "/about",
    component: about,
  },
  {
    path: "/projects",
    component: projects,
  },
  {
    path: "/projects/:id",
    component: projectDetails,
  },
  {
    path: "/add",
    component: addProject,
  },
  {
    path: "/profile",
    component: profile,
  },
  {
    path: "/updateUserProfile",
    component: updateUserProfile,
  },
  {
    path: "/forgetPassword",
    component: forgetPassword,
  },
  {
    path: "/confirmForgetPassword",
    component: confirmForgetPassword,
  },
  {
    path: "/congs",
    component: congratulations,
  },
  {
    path: "/:catchAll(.*)",
    component: worngpaht,
  },
];
const router = createRouter({
  routes,
  history: createWebHistory(),
});
export default router;
