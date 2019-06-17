import Vue from 'vue'
import Router from 'vue-router'
import VueDemo from '@/components/VueDemo'
import Messages from '@/components/Messages'
import ATM from '@/components/ATM'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: ATM
    }
    // {
    //   path: '/messages',
    //   name: 'messages',
    //   component: Messages
    // },
    // {
    //   path: '/atm',
    //   name: 'atm',
    //   component: ATM
    // }
  ]
})
