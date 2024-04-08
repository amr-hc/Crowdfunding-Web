import { createApp } from "vue";
import App from "./App.vue";
import "./assets/css/style.css";
import "./assets/css/map.css";
import router from './routers/index'

const app = createApp(App);
app.use(router);
app.mount('#app')
// createApp(App).use(router).mount("#app");
