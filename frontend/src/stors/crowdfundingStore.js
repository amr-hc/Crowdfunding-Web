import { defineStore } from "pinia";
export const datastore = defineStore("crowdfunding", {
  state: () => ({
    user: {},
    categories:[],
    tags:[]
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
      
        this.user=user;
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
        this.categories= categories;
      } catch (error) {
        console.error("Error fetching categories data:", error);
      }
    },
    async getTags() {
      try {
        const response = await fetch(`http://127.0.0.1:8000/tags/`);
        const tags = await response.json();
        this.tags= tags;
      } catch (error) {
        console.error("Error fetching tags data:", error);
      }
    },

    
    
  },

  getters: {},
});