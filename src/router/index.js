import {createWebHistory, createRouter} from "vue-router";
import MenuVue from "@/MenuComponents/MenuVue.vue";
import ImageView from "@/ImageComponent/ImageView.vue";
const routes = [
    {
        path: "/",
        name: "MenuVue",
        component: MenuVue,
    },
    {
        path: "/about",
        name: "ImageView",
        component: ImageView,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;