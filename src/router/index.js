import Home from '../components/ComponentVue';

import {createRouter, createWebHistory} from 'vue-router'

const router= createRouter({
    history : createWebHistory(),
    routes : [
        {
            path : '', 
            component : Home,
        },
        /*{
            path: '/StackA',
            component : StackA
        }*/
    ]
})

export default router;