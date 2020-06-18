import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'

Vue.config.productionTip = false
//and router
Vue.use(VueRouter)

new Vue({
  render: h => h(App),
}).$mount('#app')
