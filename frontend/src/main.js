import { createApp } from "vue";
import App from "./App.vue";
import { createPinia } from 'pinia'
import "./assets/css/style.css";
import "./assets/css/map.css";
import "./assets/css/profile.css";
import router from './routers/index'
window.$ = window.jQuery = require('jquery');
const app = createApp(App);
app.use(router);
const pinia =createPinia();
app.use(pinia);
 
app.mount('#app')
// createApp(App).use(router).mount("#app");
