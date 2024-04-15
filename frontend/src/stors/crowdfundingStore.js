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
<<<<<<< HEAD
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token} `
          }
         });
         const user = await response.json(); 
         console.log(user)
         
         return user
          
    
    
        }
      catch (error) 
          {
              console.error("Error fetching country codes:", error);
          }
             
                
            
        },
          
    },
    
getters:{
    
   
}
=======
            "Content-Type": "application/json",
            Authorization: `Bearer ${token} `,
          },
        });
        const user = await response.json();
>>>>>>> 2e8fcbf20cdfe283cc02a22ed7f5e2ae3e23afb9

        return user;
      } catch (error) {
        console.error("Error fetching country codes:", error);
      }
    },
  },

  getters: {},
});
