import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/components/Home'
import News from '@/components/News'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/news/:urlname',
        name: 'News',
        component: News
    }
]

export default new VueRouter({
    routes: routes
})