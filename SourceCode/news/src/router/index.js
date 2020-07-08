import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/components/Home'
import NewsDetail from '@/components/NewsDetail'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/news/:id',
        name: 'NewsDetail',
        component: NewsDetail
    }
]

export default new VueRouter({
    routes: routes
})