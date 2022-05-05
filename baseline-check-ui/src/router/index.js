import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '../components/index.vue'
import Home from '../components/home.vue'
import Linuxcheck from '../components/linuxcheck.vue'
import Welcome from '../components/Welcome.vue'
import Empty from '../components/empty.vue'
import Checklist from '../components/checklist.vue'
import Checkphoto from '../components/checkphoto.vue'


Vue.use(VueRouter)

const routes = [
    { path: '/', redirect: '/index' },
    { path: '/index', component: Index },
    { path: '/checkphoto', component: Checkphoto },
    { path: '/home',
      component: Home,
      redirect: '/welcome',
      children:[
          { path: '/welcome', component: Welcome },
          { path: '/linuxcheck', component: Linuxcheck },
          { path: '/empty', component: Empty },
          { path: '/checklist', component: Checklist },
      ]
    },

]

const router = new VueRouter({
  routes
})

export default router
