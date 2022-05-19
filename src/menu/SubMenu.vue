<template>
    <div class="menu-item" @click="setOpen()">
        <a href="">
            {{ title }}
        </a>
         <svg viewBox="0 0 1030 638" width="10">
            <path d="M1017 68L541 626q-11 12-26 12t-26-12L13
            68Q-3 49 6 24.5T39 0h952q24 0 33 24.5t-7 34.5z"
            fill="#FFF"></path>
        </svg>
    </div>
    <transition name="fade" appear>
        <div class="sub-menu" v-if="isMenuOpen()">
            <div class="menu-item" v-for="(item,i) in items" :key="i">
                <a :href="path[i]" target="_blank" rel="noopener noreferrer">
                    {{item}} {{i}}
                </a>
            </div>
        </div> 
    </transition>
    
</template>

<script>

export default{
    props: ['title', 'items', 'path'],
    data() {
        return {
            open: false
        }
    },
    methods: {
         isMenuOpen() {
             return this.open;
        },
        setOpen(){
            this.open = !this.open;
        }
    }
}
</script>

<style>
.sub-menu{
    background-color: rgb(223,219,219);
}

.menu-item.active,
.menu-item:hover{
    background-color: rgb(116,141,141);
    border-bottom-color: rgb(70,96,209);
}
.fade-enter-active,
.fade-leave-active{
    transition: all, 2s ease-out;
}
.fade-enter,
fade-leave-to {
    opacity: 0;
}
</style>
