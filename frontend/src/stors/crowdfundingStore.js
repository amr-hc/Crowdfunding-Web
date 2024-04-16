import { defineStore } from "pinia";
export const datastore = defineStore("crowdfunding", {
  state: () => ({
    isAuthenticated: true,
    user: {},
    projectData: [],
    userInfo:
      JSON.parse(localStorage.getItem("userInfo")) ||
      JSON.parse(sessionStorage.getItem("userInfo")),
  }),
  actions: {
    async getUserData(id, token) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/users/${id}`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token} `,
          },
        });
        const user = await response.json();
        console.log(user);
        return user;
      } catch (error) {
        console.error("Error fetching country codes:", error);
      }
    },
    async getAllProjects() {
      try {
        const res = await fetch("http://127.0.0.1:8000/api/projects/", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${this.userInfo.token} `,
          },
        });
        if (!res.ok) {
          throw new Error("can't fetch data from server");
        }
        const projectData = await res.json();
        return projectData;
      } catch (error) {
        console.error("Error fetching projects:", error);
        throw error;
      }
    },
    setAuthentication(value) {
      this.isAuthenticated = value;
    },
  },
  getters: {},
});
