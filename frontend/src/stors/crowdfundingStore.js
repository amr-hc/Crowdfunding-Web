import { defineStore } from "pinia";
export const datastore = defineStore("crowdfunding", {
  state: () => ({
    user: {},
    categories:[],
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
        console.log(user)
        this.user=user;
      } catch (error) {
        console.error("Error fetching country codes:", error);
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
        console.error("Error fetching country codes:", error);
      }
    },
    
    
  },

  getters: {},
});