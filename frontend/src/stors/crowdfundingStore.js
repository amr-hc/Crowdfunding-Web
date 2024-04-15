import { defineStore } from "pinia";
export const datastore = defineStore("crowdfunding", {
  state: () => ({
    user: {},
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

        return user;
      } catch (error) {
        console.error("Error fetching country codes:", error);
      }
    },
  },

  getters: {},
});