<template>
  <section>
    <div class="card h-100 mb-5 pb-5">
      <div class="row gap-5 g-0 justify-content-center">
        <div
          class="card-details h-100 w-100 w-md-50 position-relative col-12 col-md"
        >
          <div class="img-wrapper">
            <img
              class="h-100 w-100 rounded-4 object-fit-stretch"
              :src="activeImg"
              alt="Active Image"
              id="active-img"
            />
            <div v-show="isFeatured" class="featured bg-danger">
              featured <i class="fa-solid fa-star"></i>
            </div>
          </div>
          <div class="row gap-1 g-0 flex-nowrap overflow-x-auto py-2">
            <div
              class="img-item"
              v-for="(image, index) in images"
              :key="index"
              :class="{ 'active-img': image.url === activeImg }"
              @click="selectActiveImage(index)"
            >
              <img
                width="100%"
                height="100%"
                :src="image.url"
                alt="Thumbnail Image"
              />
            </div>
          </div>
          <h5 class="text-light-emphasis">
            Title: {{ projectData.title }}
            <div class="rating my-2">
              <i
                v-for="n in 5"
                :key="n"
                :class="{
                  'plus fa-solid fa-star': n <= rating,
                  'minus fa-regular fa-star': n > rating,
                }"
              ></i>
            </div>
          </h5>
          <!-- <div class="text-white-50">
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis quam iste beatae incidunt vitae
                    ad.
                    Iure deserunt recusandae neque aut dolorem, nisi delectus molestiae repudiandae aliquid possimus ab
                    odio
                    voluptas?
                </div> -->
          <div class="text-white-50">
            {{ projectData.description }}
          </div>
          <hr />
          <h5 class="text-light-emphasis">Similar Projects</h5>
          <div class="row g-0 gap-1 overflow-hidden">
            <div
              class="project-item"
              v-for="(image, index) in limitedImages"
              :key="index"
            >
              <img :src="image.url" :alt="image.title" />
              <h6 class="text-light project-item-title">hamada</h6>
              <div class="project-item-rating">
                <i
                  v-for="n in 5"
                  :key="n"
                  :class="{
                    'plus fa-solid fa-star': n <= rating,
                    'minus fa-regular fa-star': n > rating,
                  }"
                ></i>
              </div>
            </div>
          </div>
          <!-- See More Button -->
          <router-link
            v-if="images.length > 3"
            to="projects"
            class="btn text-light-emphasis mt-2"
            >See More</router-link
          >
          <hr />
          <div class="reviews">
            <h5 class="text-light-emphasis my-3">Reviews</h5>
            <!-- Add review input -->
            <textarea
              data-bs-theme="dark"
              id="newComment"
              class="col form-control bg-transparent text-light"
              rows="3"
              placeholder="Write your comment"
            ></textarea>

            <div
              class="d-flex align-items-baseline justify-content-between gap-3 my-3"
            >
              <div data-bs-theme="dark">
                <select
                  id="newRating"
                  class="col form-select bg-body-secondary"
                >
                  <option selected>Your Rating</option>
                  <option value="1">1 star</option>
                  <option value="2">2 stars</option>
                  <option value="3">3 stars</option>
                  <option value="4">4 stars</option>
                  <option value="5">5 stars</option>
                </select>
              </div>
              <button class="col text-center btn btn-main btn-outline-dark">
                Comment
              </button>
            </div>
            <hr />
            <div class="reviewer text-end border-bottom border-dark my-2">
              <div class="d-flex justify-content-between align-items-baseline">
                <div class="d-flex align-items-center gap-2">
                  <div class="avatar">
                    <img src="https://placehold.co/400" alt="Avatar" />
                  </div>
                  <div class="text-light">John Doe</div>
                </div>
                <div class="rating">
                  <i
                    v-for="n in 5"
                    :key="n"
                    :class="{
                      'plus fa-solid fa-star': n <= rating,
                      'minus fa-regular fa-star': n > rating,
                    }"
                  ></i>
                </div>
              </div>
              <p class="text-white-50 text-start">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto,
                quod.
              </p>
              <p class="m-0">10-10-2022 - 10:10 AM</p>
              <button
                class="btn btn-outline-danger p-0 mb-2 border-0 px-2"
                data-bs-toggle="modal"
                data-bs-target="#reportModal"
              >
                report <i class="fa-solid fa-reply"></i>
              </button>
            </div>
          </div>
        </div>

        <div class="col-12 col-md py-3 rounded-4 text-light">
          <!--Owner of Project-->
          <h4 style="text-transform: capitalize;">
            {{ ownerData.first_name }} {{ ownerData.last_name }}
            <span v-if="isOwner == true">(You)</span>
          </h4>
          <h6 class="text-white-50" style="text-transform: capitalize;">
            <i class="fa-solid fa-location-crosshairs"></i>
            {{ ownerData.country }}
          </h6>
          <hr />
          <!-- end of Owner Details -->

          <!--Donation Details-->
          <p class="text-white-50">
            <strong>$999</strong> raised from $1000 / 5 donorsj
          </p>
          <div class="progress">
            <div
              class="progress-bar"
              role="progressbar"
              :style="{ width: donationProgress + '%' }"
              aria-valuenow="0"
              aria-valuemin="0"
              aria-valuemax="100"
            ></div>
          </div>
          <h3 class="my-3">
            ${{ Math.round((totalAmount - currentDonation)*100)/100 }} still needed
          </h3>
          <p class="text-white-50">
            {{ days }} days {{ hours }} hours {{ minutes }} minutes
            {{ seconds }} seconds left
          </p>
          <!--End Of Donation Details-->

          <!-- Project Details -->
          <div v-if="isOwner === false">
            <!-- Project Duration -->
            <div class="d-flex" v-if="projectDuration > 0">
              <input
                type="number"
                data-bs-theme="dark"
                min="0"
                step="0.01"
                :max="totalAmount - currentDonation"
                class="col form-control bg-transparent text-light"
                placeholder="Enter Amount"
                aria-describedby="donationBlock"
                v-model="donationAmount"
              />

              <button
                class="col btn btn-main btn-outline-dark ms-2"
                @click="Donate"
              >
                Donate
              </button>
            </div>
            <div v-else-if="projectDuration <= 0">
              <p
                class="text-danger"
                style="
                  background-color: #f8d7da;
                  border-color: #f5c6cb;
                  color: #721c24;
                  padding: 10px;
                  border-radius: 5px;
                "
              >
                The project duration has ended.
              </p>
            </div>
          </div>
          <!-- End Of Project -->

          <!-- admin -->
          <!-- || userData.user.is_superuser === true -->
          <div
            v-else-if="isOwner === true || userData['is_super']"
            class="admin-for-project mt-3"
          >
            <div v-if="isOwner === true && days < 4 && donationProgress < 30">
              <button class="btn btn-secondary me-2">Cancel</button>
            </div>

            <button class="btn btn-warning">Edit</button>
          </div>
          <!-- Logger-section -->
          <section class="logger-section">
            <div class="container">
              <div class="row justify-content-center">
                <div class="col-md-8">
                  <div
                    class="alert"
                    role="alert"
                    :class="{
                      'alert-danger': logger.hasError,
                      'alert-success': logger.success,
                    }"
                    v-if="logger.hasError || logger.success"
                  >
                    {{
                      logger.hasError
                        ? logger.errorLogger
                        : logger.successMessage
                    }}
                  </div>
                </div>
              </div>
            </div>
          </section>

          <!-- Last five Donations -->
          <hr class="my-5" />
          <h5 class="text-white-50 my-4">Last 5 Donations</h5>
          <div class="text-end border-bottom border-dark my-2">
            <div class="d-flex justify-content-between align-items-baseline">
              <div class="d-flex align-items-center gap-2">
                <div class="avatar">
                  <img src="https://placehold.co/400" alt="Avatar" />
                </div>
                <div class="text-light">John Doe</div>
              </div>
              <p class="text-white-50">3 days ago</p>
            </div>
            <p class="text-white-50 text-start">Donated $1000</p>
          </div>
        </div>
      </div>
    </div>
    <!-- Modal -->
    <div
      class="modal fade"
      data-bs-theme="dark"
      id="reportModal"
      tabindex="-1"
      aria-labelledby="reportModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="reportModalLabel">
              Report Confirmation
            </h1>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            Are you sure you want to report this comment?
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-danger"
              data-bs-dismiss="modal"
            >
              No
            </button>
            <button type="button" class="btn btn-primary">Go ahead!</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { datastore } from "@/stors/crowdfundingStore";
export default {
  name: "project-details",
  data() {
    return {
      projectData: {}, // Object to hold project data
      images: [],
      activeImg: "",
      isFeatured: true,
      rating: 4,
      showAllProjects: false,
      totalAmount: 0,
      currentDonation: 0,
      ownerData: {},
      projectDuration: 0,
      days: 0,
      hours: 0,
      minutes: 0,
      seconds: 0,
      donationAmount: 0,
      userData: {},
      isOwner: false,
      allProjectData:0,
      allUserData:0,
      logger: {
        hasError: false,
        errorLogger: "",
        success: false,
        successMessage:"",
      },
    };
  },
  async mounted() {
    // Fetch User Data
    await this.fetchUserData();

    // Fetch project data when the component is mounted
    await this.fetchProjectData();

    //determine if is owner
    await this.isProjectOwner();

    // Fetch User Data From The Local Storage
    // this.logedInUserData = localStorage.getItem('userInfo');
    setInterval(this.updateTimeDifference, 1000);
  },
  methods: {
    async fetchUserData() {
      if (
        localStorage.getItem("userInfo") ||
        sessionStorage.getItem("userInfo")
      ) {
        try {
          // Try To Fetch The Data
          const localStorageData = localStorage.getItem("userInfo");
          const sessionStorageData = sessionStorage.getItem("userInfo");

          this.userData = localStorageData
            ? JSON.parse(localStorageData)
            : JSON.parse(sessionStorageData);
            console.log(this.userData['user_id'])
          const response=await fetch(`http://localhost:8000/api/users/${this.userData['user_id']}`);
          this.allUserData = await response.json();  
          console.log(this.allUserData);
        } catch (error) {
          throw new Error( error);

          this.userData = {};
        }
      } else {
        console.error("userInfo Is Not Found Please reEnsure data");
        userData = {};
      }
    },
    async fetchProjectData() {
      try {
        const projectId = this.$route.params.id;
        const response = await fetch(
          `http://localhost:8000/api/projects/${projectId}`
        );
        if (!response.ok) {
          throw new Error("Failed to fetch project data");
        }
        const data = await response.json();
        this.allProjectData = data;
        //project Basic Data
        this.projectData = {
          id:data['id'],
          title: data["title"],
          description: data["description"],
          tags: data["tags"],
          current_date: new Date(),
          end_date: new Date(data["end_date"]),
        };
        this.projectDuration =
          this.projectData.end_date - this.projectData.current_date;
        // /***Comment This line */
        // this.projectDuration = 2 ;
        /**comment this line */

        //total amount
        this.totalAmount = data["target_money"];
        //current donation
        const totalDonationsFloat = parseFloat(data["total_donations"]);
        this.currentDonation = totalDonationsFloat.toFixed(2);
        //rating
        this.rating = data["average_rate"];
        // images
        console.log(data["pics"]);
        this.images = data["pics"].map((image) => ({
          url: image.image_path,
          active: false,
        }));
        // select the active image
        if (this.images.length > 0) {
          this.activeImg = this.images[0].url;
        }

        // Project owner
        this.ownerData = data["owner"];
      } catch (error) {
        console.error("Error fetching project data:", error);
      }
    },
    async isProjectOwner() {
      console.log("userData");
      // console.log(this.userData);
      // console.log(this.ownerData.id);
      // console.log(typeof(this.userData.user.id))
      // console.log(typeof(this.ownerData.id))
      console.log(this.userData["user_id"]);
      if (parseInt(this.userData["user_id"]) == parseInt(this.ownerData.id)) {
        console.log("yess");
        this.isOwner = true;
        return true;
      } else {
        console.log("nooo");
        this.isOwner = false;
        return false;
      }
    },
    async updateTimeDifference() {
      // Recalculate time difference
      this.projectData.current_date = new Date();
      this.projectDuration =
        this.projectData.end_date - this.projectData.current_date;
      // this.projectDuration=0
      // Handle case when project duration ends
      if (this.projectDuration <= 0) {
        this.projectDuration = 0;
        clearInterval(this.updateTimeDifference); // Stop updating
      }
      this.days = Math.floor(this.projectDuration / (1000 * 60 * 60 * 24));
      this.projectDuration %= 1000 * 60 * 60 * 24;
      this.hours = Math.floor(this.projectDuration / (1000 * 60 * 60));
      this.projectDuration %= 1000 * 60 * 60;
      this.minutes = Math.floor(this.projectDuration / (1000 * 60));
      this.projectDuration %= 1000 * 60;
      this.seconds = Math.floor(this.projectDuration / 1000);
    },

    async Donate() {
        this.donationAmount= parseFloat(this.donationAmount);
        this.donationAmount = Math.round(this.donationAmount * 100)/100;
        const remainingDonation = this.totalAmount - this.currentDonation;
      if (this.donationAmount >= remainingDonation) {
        this.logger.hasError = true;
        this.logger.errorLogger =
          "Amount Of Donation Is Bigger Than the Target Amount";
      } else if (this.isOwner == true) {
        this.logger.hasError = true;
        this.logger.errorLogger = "Donor Can't Donate To Him Self";
      } else if (this.donationAmount == 0) {
        this.logger.hasError = true;
        this.logger.errorLogger = "You Must Enter A Valid Value To Donate";
      } else if (this.projectDuration <= 0 && !this.isOwner) {
        this.logger.hasError = true;
        this.logger.errorLogger = "cannot donate after the time of duration";
      } else {
        //successfully Donation
        //happy senario case
        const donationData = {
          user: this.userData['user_id'],
          project: this.projectData['id'],
          donation_amount: this.donationAmount,
        };
        console.log(donationData);
        try {
          const response = await fetch("http://localhost:8000/donation/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(donationData),
          });
          if (!response.ok) {
            console.log(response);
            this.logger.hasError = true;
            this.logger.errorLogger = "Fail To Donate Due To Techincal ,Network Issue";
          }
          
          //Success Process
          this.logger.success = true;
          this.logger.successMessage = "Donated Successfully";
          let donationProcessInFloat = parseFloat(this.currentDonation) + parseFloat(this.donationAmount);
          this.currentDonation = Math.round(donationProcessInFloat * 100)/100;
          console.log("dataaa");
          console.log(this.currentDonation);
          console.log(typeof(this.currentDonation)); 

        } catch (error) {
            this.logger.hasError=true;
            this.logger.errorLogger=`Donation Failed Due To ${error}`;
        }
      }
    },
    selectActiveImage(index) {
      this.activeImg = this.images[index].url;
      this.images.forEach((img, i) => {
        img.active = i === index;
      });
    },
    showAllSimilarProjects() {
      this.showAllProjects = true;
    },
  },
  computed: {
    filledStars() {
      return this.rating;
    },
    emptyStars() {
      return 5 - this.rating;
    },
    limitedImages() {
      return this.showAllProjects ? this.images : this.images.slice(0, 3);
    },
    donationProgress() {
      return (this.currentDonation / this.totalAmount) * 100;
    },
  },
};
</script>

<style scoped>
.card {
  padding: 12px;
  background-color: var(--primary-color-350);
  border: 2px solid var(--primary-color-3);
  min-height: 70vh;
  border-radius: 20px;
  box-shadow: 0px 0 31px 0px rgb(0 0 0 / 10%);
  backdrop-filter: blur(15px);
}

.img-wrapper {
  width: 100%;
  height: 400px;
  position: relative;
}

.admin-for-project {
  display: flex;
  justify-content: center;
}

.admin-for-project .btn {
  border-radius: 20px;
  padding: 8px 20px;
  font-size: 16px;
  font-weight: 600;
  text-transform: uppercase;
}

.admin-for-project .btn-secondary {
  background-color: #6c757d;
  border-color: #6c757d;
  color: #fff;
}

.admin-for-project .btn-primary {
  background-color: #007bff;
  border-color: #007bff;
  color: #fff;
}

.admin-for-project .btn:hover {
  opacity: 0.9;
}

.active-img,
.img-item:hover,
.project-item:hover {
  border: 2px solid var(--secondary-color-2);
  cursor: pointer;
  opacity: 1 !important;
  transition: all 0.3s ease-in-out;
}

.img-item {
  width: 75px;
  height: 75px;
}

.img-item,
.project-item {
  overflow: hidden;
  border-radius: 10px;
  margin-right: 10px;
  opacity: 0.5;
}

.project-item {
  width: 150px;
  height: 150px;
  position: relative;
}

.project-item-title {
  position: absolute;
  bottom: 0;
  left: 5%;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  width: 90%;
  font-weight: 500;
}

.project-item-rating {
  position: absolute;
  top: 5%;
  right: 5%;
  font-size: 0.8rem;
}

.featured {
  position: absolute;
  right: 0;
  top: 0;
  padding: 0.5rem 1.5rem;
  border-radius: 0 16px 0 1.5rem;
  font-weight: 500;
  font-size: 1rem;
  text-transform: capitalize;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
}

.plus {
  color: yellow;
}

.minus {
  color: rgba(255, 255, 0, 0.5);
}

/* logger-section */
.logger-section {
  margin-top: 20px;
}

.alert-danger {
  background-color: #f8d7da;
  color: #721c24;
  border-color: #f5c6cb;
}

.alert-success {
  background-color: #d4edda;
  color: #155724;
  border-color: #c3e6cb;
}
/* end of logger */

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 2px solid var(--primary-color-3);
  overflow: hidden;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.progress {
  height: 8px;
  border-radius: 10px;
  overflow: hidden;
  background-color: var(--secondary-color-4);
}

.progress-bar {
  transition: width 0.3s ease-in-out;
  background-color: var(--secondary-color-2);
}

option {
  background-color: transparent;
}
</style>

<!--<script>
   Template



   const targetAmount = this.target_money - this.currentDonation;
       if(this.donationAmount> this.currentDonation)
       {
        this.logger.hasError=true;
        this.logger.errorLogger="Amount Of Donation Is Bigger Than the Target Amount";
       }
       else if(this.isOwner == true)
       {
        this.logger.hasError=true;
        this.logger.errorLogger="Donor Can't Donate To Him Self";
       }
       else if(this.donationAmount==0)
       {
        this.logger.hasError=true;
        this.logger.errorLogger="You Must Enter A Valid Value To Donate";
       }
       else if(projectDuration<=0 && !this.isOwner){
        this.logger.hasError=true;
        this.logger.errorLogger="cannot donate after the time of duration";
       }
       else
       {
         //successfully Donation
         //happy senario case
          const donationData = {
        user: this.userData['id'],
        project: this.projectId,
        donation_amount: this.targetAmount
      };

    try {
        const response = await fetch('http://localhost:8000/api/donations/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(donationData),
        });

        if (!response.ok) {
          this.logger.hasError=true;
          this.logger.errorLogger = "Fail To Donate";
        }

        this.logger.success=true;
        this.logger.sucessMessage="Donated Successfully"
    } catch (error) {
        // Handle errors, e.g., show an error message to the user
        this.logger.hasError=true;
        this.logger.errorLogger = error;
    }
}

       }





// export default {
//     name: 'project-details',
//     data() {
//         return {
//             images: [
//                 { url: 'https://s3.amazonaws.com/ooomf-com-files/wdXqHcTwSTmLuKOGz92L_Landscape.jpg', title: 'New carousel layout', description: 'Responsive thumbnail preview in carousel indicators.' },
//                 { url: 'https://s3.amazonaws.com/ooomf-com-files/mtNrf7oxS4uSxTzMBWfQ_DSC_0043.jpg', title: 'One more for good measure.', description: 'Nullam id dolor id nibh ultricies vehicula ut id elit.' },
//                 { url: 'https://s3.amazonaws.com/ooomf-com-files/tU3ptNgGSP6U2fE67Gvy_SYDNEY-162.jpg', title: 'Another example headline.', description: 'Cras justo odio, dapibus ac facilisis in, egestas eget quam.' },
//             ],
//             activeImg: '',
//             isFeatured: true,
//             rating: 4,
//             showAllProjects: false,
//             totalAmount: 1000,
//             currentDonation: 630


//         };
//     },

//     mounted() {
//         this.activeImg = this.images[0].url;
//     },
//     methods: {
//         selectActiveImage(index) {
//             this.activeImg = this.images[index].url;
//             this.images.forEach((img, i) => {
//                 img.active = i === index;
//             });
//         }
//         , showAllSimilarProjects() {
//             this.showAllProjects = true;
//         }
//     },
//     computed: {
//         filledStars() {
//             return this.rating;
//         },
//         emptyStars() {
//             return 5 - this.rating;
//         },
//         limitedImages() {
//             return this.showAllProjects ? this.images : this.images.slice(0, 3);
//         },
//         donationProgress() {
//             return (this.currentDonation / this.totalAmount) * 100;
//         }
//     },
// }





 //Old Picture Fetching
 //    async fetchProjectPicsData() {
    //         try {
    //             const projectId = 16;
    //             const response = await fetch(`http://localhost:8000/api/projects/${projectId}/`);
    //             if (!response.ok) {
    //                 throw new Error('Failed to fetch project pics data');
    //             }
    //             const data = await response.json();
    //             this.images = data.map(image => ({
    //                 url: image.image_path,
    //                 active: false
    //             }));
    //             // Set the active image to the first image in the array
    //             if (this.images.length > 0) {
    //                 this.activeImg = this.images[0].url;
    //             }
    //         } catch (error) {
    //             console.error('Error fetching project pics data:', error);
    //         }
    //     },

</script> -->
