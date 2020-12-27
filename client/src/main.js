import Vue from 'vue'
import App from './App.vue'
import router from "./router"
import vueToasted from "vue-toasted"
import "bootstrap/dist/css/bootstrap.min.css";
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

// imports the store for state management
import store from "./store";

import vuetify from './plugins/vuetify';


// used to disable development warning
Vue.config.productionTip = false

// load toast plugin
Vue.use(vueToasted, {
  iconPack: "fontawesome"
})
Vue.use(VueMaterial)

new Vue({
  store,
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
