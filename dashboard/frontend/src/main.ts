// Import Component hooks before component definitions
import App from './App.vue';
import Vue from 'vue';
import router from './router';
import store from '@/store';
import echarts from 'echarts'
import vuetify from './plugins/vuetify';
import '@babel/polyfill';
import './component-hooks';
import './plugins/vee-validate';
import './registerServiceWorker';
import 'vuetify/dist/vuetify.min.css';
import '@mdi/font/css/materialdesignicons.css';


Vue.prototype.$echarts = echarts

Vue.config.productionTip = false;
new Vue({
  vuetify,
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
