  class FunctionsClass {
    constructor() {
  
    }
    async created(par) {
        try {
            const response = await fetch('https://countriesnow.space/api/v0.1/countries/codes');
            const data = await response.json();
            par.countries=data.data.map((data)=>{
              return data.name
            })
             
        } catch (error) {
            console.error("Error fetching country codes:", error);
        }
    }

    HTMLValidations(e) {
        if (!e.target.checkValidity()) {
            e.preventDefault();
            e.stopPropagation();
            e.target.classList.add("was-validated");
            return false;
        } else {
            e.target.classList.add("was-validated");
            return true;
        }
    }

    jsValidations(par,modul)
    {
        const namePattern = /^[a-zA-Z ,.'-]+$/;
        const emailPattern = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
        const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
        const mobilePattern = /^01[012]\d{8}$/;
        const countryPattern = /^[a-zA-Z ,.'-]+$/;
        const birthdatePattern = /^([0-9]{4}[-/]?((0[13-9]|1[012])[-/]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[-/]?31|02[-/]?(0[1-9]|1[0-9]|2[0-8]))|([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00)[-/]?02[-/]?29)$/;
        const facebookPattern = /^(?:https?:\/\/)?(?:www\.)?(mbasic.facebook|m\.facebook|facebook|fb)\.(com|me)\/(?:(?:\w\.)*#!\/)?(?:pages\/)?(?:[\w\-\.]*\/)*([\w\-\.]*)/;
        if(par.country!="")
        {
          if(countryPattern.test(par.country))
              {
                return true;
              }
          else
              {
                return false;
              }
        }
        if(par.birthdate!="")
        {
          if(birthdatePattern.test(par.birthdate))
            {
              return true;
            }
          else
            {
              console.log(par.birthdate)
              return false;
            }
        }
        if(par.facebook!=null)
        {
          if(facebookPattern.test(par.facebook))
              {
                return true;
              }
          else
              {
                console.log(par.facebook)

                return false;
              }
        }
        if (!modul){
          if(passwordPattern.test(par.password))
              {
                return true;
              }
          else
              {
                return false;
              }
        }
        if(
        namePattern.test(par.fname)
        &&namePattern.test(par.lname)
        &&emailPattern.test(par.email)
        &&mobilePattern.test(par.mobile)    
          )
        {
          return true;
        }
        else
        {  
      
          return false;
        }
    }
    projectValidations(par) {
      const titlePattern = /^[a-zA-Z0-9\s]{1,50}$/; 
      const descriptionPattern = /^.{1,400}$/;
      
      if (titlePattern.test(par.title)
          && descriptionPattern.test(par.description))
           {
          return true;
      } else {
          console.log(
              titlePattern.test(par.title),
              descriptionPattern.test(par.description),
          );
          console.log(
              par.title,
              par.description,
          );
          return false;
      }
  }
  


    confirm(e,par){
         
        if(par.cpassword!=par.password)
        {
          e.target.setCustomValidity("Passwords don't match");
        }
        else
        {
          e.target.setCustomValidity('');
        }
      }

      handleFileChange(event,par)
      {
        par.file = event.target.files[0];
      }
      createForm(par){
        const formData = new FormData();
        formData.append('first_name', par.fname);
        formData.append('last_name',par.lname);
        formData.append('email', par.email);
        formData.append('phone', par.mobile);
        formData.append('birth_date', par.birthdate);
        formData.append('photo', par.file);
        formData.append('facebook', par.facebook);
         formData.append('country', par.country);
      

        return formData;
      }
      async insertrequest(par)
      {
        
        const formData=this.createForm(par);
        formData.append('password', par.password);
         // Validate the form data object to delete empty Properties before sending  
        const form = Object.fromEntries(formData.entries());
        for (let [key,value] of Object.entries(form)) 
        {
          console.log(key,value);
            if (!value ||value === "null") 
            {
                formData.delete(key);
            }
        }
        formData.append('address', 'dssddsdsd');

         // sending Request
          try 
          {
            const response = await fetch('http://127.0.0.1:8000/api/users/',{
              method: "POST",
              body: formData,
            });
            const data = await response.json(); 
          sessionStorage.setItem("needactivation", "true");
            par.$router.push('/befroreactivation');

              console.log(data)
          }
        catch (error) 
            {
                console.error("Error fetching api:", error);
            }
      } 
      async updateRequest(par)
      {

        const formData = this.createForm(par);
        // Validate the form data object to delete empty Properties before sending  
        const form = Object.fromEntries(formData.entries());
        for (let [key,value] of Object.entries(form)) 
        {
            if (!value ||value === "null") 
            {
                formData.delete(key);
            }
        }
        // Get user Id and token
        const token=par.storgData.token;
        
        // sending Request
          try 
          { 
              const response = await fetch(`http://127.0.0.1:8000/api/users/${par.id}/`,{
              method: "PATCH",
              headers: {
                'Authorization': `token ${token} `
              },
              body: formData,
            });
            
                const data = await response.json(); 
              console.log(data)
          }
        catch (error) 
            {
                console.error("Error fetching api:", error);
            }
      } 

    handleFormSubmission(e,par,modul) {
        if (this.HTMLValidations(e) && this.jsValidations(par,modul)) {
          if(modul){
            
            this.updateRequest(par);
          }else{
            this.insertrequest(par);
          }
           
        }
    }

    async logedInPagesCreated(par){
      const localStorageData =JSON.parse(localStorage.getItem('userInfo'));
      const sessionStorageData=JSON.parse(sessionStorage.getItem("userInfo"));
        if(!sessionStorageData&&!localStorageData){
          par.$router.push('/login');
        }
        else if(localStorageData||sessionStorageData){
          let userData=localStorageData?localStorageData : sessionStorageData 
          par.storgData=userData;
          par.user=await par.storData.getUserData(userData.user_id,userData.token)
          
        }
      }

      async deleteUser(par){
        const storgData=par.storgData;
        try 
        { 
          
            const response = await fetch(`http://127.0.0.1:8000/api/users/${storgData.user_id}`,{
            method: "DELETE",
            headers: {
              'Authorization': `Bearer ${storgData.token} `
            },
          });
            const data = await response.json(); 
            // if (!response) {
            //   throw new Error(`HTTP error! Status: ${response.status}`);
            // }
            window.location.href='http://localhost:8080/login'
            console.log(data)
        }
      catch (error) 
          {
              console.error("Error fetching api:", error);
          }
      }
}

export default FunctionsClass;


 