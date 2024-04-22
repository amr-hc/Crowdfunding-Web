import { createRouter, createWebHistory } from "vue-router";
import notfound from "../components/notfound";
import registration from "../components/registration.vue";
import about from "../components/about.vue";
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
import befroreactivation from "@/components/befroreactivation.vue";
// dashboard import
import Dashboard from "@/components/dashboard.vue";
import Featured from "@/components/dashboard/featured.vue";
import Projects from "@/components/dashboard/projects.vue";
import ShowProjectDashboard from "@/components/dashboard/show-project.vue";
import CategoryTags from "@/components/dashboard/categoryTags.vue";
import ReportComment from "@/components/dashboard/reportComment.vue";
import ReportProject from "@/components/dashboard/reportProject.vue";
// test
import AllData from "@/components/project/piniaData.vue";

const routes = [
  {
    path: "/",
    component: Home,
  },
  {
    path: "/login",
    component: login,
  },
  {
    path: "/befroreactivation",
    component: befroreactivation,
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
  //test path
  {
    path: "/allData",
    component: AllData,
  },
  {
    path: "/:catchAll(.*)",
    component: notfound,
  },
  // dashboard routes
  {
    path: "/dashboard",
    component: Dashboard,
    meta: { requiresAuth: true, requiresAdmin: true },
    children: [
      {
        path: "",
        name: "dashboard",
        components: {
          default: Featured,
          projects: Projects,
        },
      },
      {
        path: "p/:id",
        name: "dashboardProject",
        components: {
          default: ShowProjectDashboard,
        },
      },
      {
        path: "category-tags",
        name: "categoryTags",
        component: CategoryTags,
      },
      {
        path: "report",
        name: "dashboardReport",
        components: {
          ReportComment: ReportComment,
          ReportProject: ReportProject,
        },
      },
    ],
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

// router.beforeEach((to, from, next) => {
//   const isAuthenticated = localStorage.getItem("userInfo") !== null;
//   const userInfo = JSON.parse(localStorage.getItem("userInfo"));
//   const isAdmin = isAuthenticated && userInfo.is_superuser;

//   if (to.matched.some((record) => record.meta.requiresAuth)) {
//     if (!isAuthenticated) {
//       next({ path: "/login", query: { redirect: to.fullPath } });
//     } else {
//       if (to.matched.some((record) => record.meta.requiresAdmin)) {
//         if (!isAdmin) {
//           next();
//         } else {
//           next();
//         }
//       }
//     }
//   } else {
//     next();
//   }
// });
export default router;
