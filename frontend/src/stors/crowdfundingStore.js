import { defineStore } from "pinia";
export const datastore = defineStore("crowdfunding", {
  state: () => ({
    user: {},
    categories: [],
    tags: [],
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

        this.user = user;
      } catch (error) {
        console.error("Error fetching user data:", error);
      }
    },
    async getCategories() {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/categories/`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });
        const categories = await response.json();
        this.categories = categories;
        return categories;
      } catch (error) {
        console.error("Error fetching categories data:", error);
      }
    },
    async getTags() {
      try {
        const response = await fetch(`http://127.0.0.1:8000/tags/`);
        const tags = await response.json();
        this.tags = tags;
      } catch (error) {
        console.error("Error fetching tags data:", error);
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
