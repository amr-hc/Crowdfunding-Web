import { createRouter, createWebHistory } from "vue-router";
import worngpaht from "../components/worngpaht";
import intro from "../components/home/intro.vue";
import registration from "../components/registration.vue";
import about from "../components/about.vue";
import investors from "../components/investors.vue";
import projects from "../components/projects.vue";
import login from "../components/login.vue";
import Home from "@/components/home.vue";
import profile from "../components/profile.vue";
import updateUserProfile from "../components/updateUserProfile.vue";
import addProject from "@/components/addProject.vue";
import congratulations from "@/components/congratulations.vue";

const routes = [
  {
    path: "/",
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
    path: "/add",
    component: addProject,
  },
  {
    path: "/investors",
    component: investors,
  },
  {
    path: "/login",
    component: login,
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
