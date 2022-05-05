import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import './assets/css/global.css'
import axios from 'axios'
import echarts from 'echarts'


// axios.defaults.baseURL ='http://localhost:5000'

Vue.prototype.$http = axios
Vue.config.productionTip = false
Vue.prototype.$echarts = echarts


new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
