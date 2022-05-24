<template>
    <div class="menu-item" @click="setOpen()">
            {{ title }}
         <svg viewBox="0 0 1030 638" width="10">
            <path d="M1017 68L541 626q-11 12-26 12t-26-12L13
            68Q-3 49 6 24.5T39 0h952q24 0 33 24.5t-7 34.5z"
            fill="#FFF"></path>
        </svg>
    </div>
    <transition name="fade" appear>
        <div class="sub-menu" v-if="isMenuOpen()">
            <div class="menu-item" v-for="(item,i) in items" :key="i" >
            <v-switch :case="color[i]">
                <template #blue>
                    <div :class="{blue: color[i]=='blue'}">
                        <a :href="path[i]" target="_blank" rel="noopener noreferrer" v-if="pathExist== true" >
                            {{item}} 
                        </a>
                        <div v-else @click="existLink(path[i])">
                            {{item}} 
                        </div>
                    </div>
                </template>
                <template #white>
                    <div :class="{white: color[i]=='white'}">
                        <a :href="path[i]" target="_blank" rel="noopener noreferrer" v-if="pathExist== true" >
                            {{item}} 
                        </a>
                        <div v-else @click="existLink(path[i])">
                            {{item}} 
                        </div>
                    </div>
                </template>
            </v-switch>
                
            </div>
        </div> 
    </transition>
    
</template>

<script>
import VSwitch from '@lmiller1990/v-switch'
export default{
    components:{
        VSwitch
    },
    props: ['title', 'items', 'path', 'color'],
    data() {
        return {
            open: false,
            pathExist: ""
        }
    },
    methods: {
         isMenuOpen() {
             return this.open;
        },
        setOpen(){
            this.open = !this.open;
        },
        existLink(link){
            if(link == ""){
                this.pathExist = false;
                alert("Link doesn't exist");
            }
            else this.pathExist = true;
        }
    }
}
</script>

<style>
.sub-menu{
    background-color: rgb(255, 255, 255);
}
.menu-item {
    color: black;
}
.menu-item.active,
.menu-item:hover{
    background-color: rgb(255, 254, 254);
    border-bottom-color: rgb(70,96,209);
    color: black;
}
.fade-enter-active,
.fade-leave-active{
    transition: all, 0s ease-out;
    color: black;
}
.fade-enter,
fade-leave-to {
    opacity: 0;
}
.blue{
    background-color: rgb(119, 170, 247);
}
.purple{
    background-color: rgb(194, 166, 194);
}
.green{
    background-color: rgb(170, 223, 170);
}
.white{
    background-color: white;
}
</style>
