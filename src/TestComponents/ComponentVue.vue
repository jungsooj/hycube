<template>
    <nav>
        <div class="items" v-for="(name,index) in menu" :key="index" >
            <p> {{name}} </p>
            <div class="menu-item" :class="{blue: isBlue}">
                <DropDown title="Equipement validation" :items="menu" :data="data"></DropDown>
            </div>
            <div class="menu-item">
                <DropDown title="Assembly" :items="menu"></DropDown>
            </div>
            <div class="menu-item">
                <DropDown title="Health check" :items="menu"></DropDown>
            </div>
        </div>
    </nav> 
</template>

<script>
import DropDown from './DropDown.vue'

'use strict';
let jsonData = require('../data/AitData2.json');

export default{
    compoenents: {
       DropDown
    },
    data() {
        return {
            data: Object.values(Object.values(jsonData)[0])[2]["path"], // get paths /states and names
            data2: Object.values(Object.values(Object.values(jsonData)[0]))['name'],
            data3: Object.keys(Object.values(jsonData)[0]), //Menu list
            menu: Object.keys(jsonData),
            subMenu: Object.keys(Object.values(jsonData)[0]),

        };
    },
    methods:{
        isBlue(){
            return true;
        }
    }
}
</script>

<style>
.items {
    width: 15%;
    margin: 20px;
    background-color: #d0d9ff;
    padding: 15px;
    border-radius: 10%;
    display: inline-block;
}
.menu-item.active,
.menu-item:hover {
    background-color: rgb(132, 140, 214);
    border-bottom-color: rgb(74, 56, 180);
}
a {
    color: inherit;
    text-decoration:none;
}
.menu-item{
    color: black;
    border-bottom: 3px solid transparent;
    transition:0.4s;
    background-color: aliceblue;
    margin:10px; 
    padding: 3px;
    cursor: pointer;
    border-radius: 5%;
    text-align: center;

}
.blue{
    background-color: #b0bdf8;
}
</style>