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

    jsValidations(par)
    {
      
        const namePattern = /^[a-zA-Z ,.'-]+$/;
        const emailPattern = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
        const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
        const mobilePattern = /^[1-9]\d*$/;
        const countryPattern = /^[a-zA-Z ,.'-]+$/;
        const birthdatePattern = /^(((0[13-9]|1[012])[-/]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[-/]?31|02[-/]?(0[1-9]|1[0-9]|2[0-8]))[-/]?[0-9]{4}|02[-/]?29[-/]?([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00))$/;
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
            
           
              return false;
            }
        }
        if(par.facebook!="")
        {
          if(facebookPattern.test(par.facebook))
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
        &&passwordPattern.test(par.password)
        &&mobilePattern.test(par.mobile)    
          )


        {
          return true;
        }
        else
        {
            console.log(
            namePattern.test(par.fname),
             namePattern.test(par.lname),
            emailPattern.test(par.email),
             passwordPattern.test(par.password),
             mobilePattern.test(par.mobile) );   
            console.log(
            par.fname ,
              par.lname ,
            par.email ,
             passwordPattern.test(par.password),
             mobilePattern.test(par.mobile) );   
           
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

      async sendrequest(par)
      {
         
          const formData = new FormData();
          formData.append('first_name', par.fname);
          formData.append('last_name',par.lname);
          formData.append('email', par.email);
          formData.append('password', par.password);
          formData.append('phone', par.mobile);
          formData.append('birth_date', par.birthdate);
          formData.append('facebook', par.facebook);
           formData.append('country', par.country);
          // formData.append('photo', par.file);
          try 
          {
            
                const response = await fetch('http://127.0.0.1:8000/auth/users/',{
              method: "POST",
              body: formData,
            });
                const data = await response.json(); 
              console.log(data)
          }
        catch (error) 
            {
                console.error("Error fetching country codes:", error);
            }
      } 

    handleFormSubmission(e,par) {
        if (this.HTMLValidations(e) && this.jsValidations(par)) {
            this.sendrequest(par);
        }
    }
}

export default FunctionsClass;


 