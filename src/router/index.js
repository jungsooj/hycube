import {createWebHistory, createRouter} from "vue-router";
import MenuVue from "@/components/MenuComponents/MenuVue.vue";
import ImageView from "@/components/ImageComponent/ImageView.vue";
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