<template>
    <div class="list" v-for="(d,index) in data" :key="index">
        {{ d }} {{iterateItems(index)}} {{menuItemCount(index)}} {{pathList(index)}}
        <nav>
            <div class="component">
                <div class="menu-item" >
                    <SubMenu title="Equipement validation" :items="menuItems" :path="itemsPath"></SubMenu>
                </div>
                <div class="menu-item">
                    Assembly
                </div>
                <div class="menu-item">
                    Health check
                </div>
            </div> 
        </nav>
        
    </div>
</template>

<script>
import SubMenu from './SubMenu.vue';

'use strict';
let jsonData = require('../data/AitData2.json');

let i = 0;
let paths=[];

export default{
 components: {
    SubMenu
  },
  data: () => {
      return {
        data: Object.keys(jsonData),
        menuCpt : Object.keys(jsonData).length,
        menuItemsCpt : 0,
        menuItems: Object.keys(Object.values(jsonData)[0]),
        itemPath: "",
        itemsPath: paths,
        }
    },
    props: {
            listName : {
                default: "valeur par default"
            }
        },
    methods: {
        iterateItems(i){
            this.menuItems = Object.keys(Object.values(jsonData)[i]);
        },
        menuItemCount(i){
            this.menuItemsCpt = Object.keys(Object.values(jsonData)[i]).length;
        },
        iterateItemsPath(i, j){
            this.itemPath = Object.values(Object.values(jsonData)[i])[j]["path"];
        },
        pathList(k){
            for(i=0; i<this.menuItemsCpt; i++){
                this.iterateItemsPath(k,i);
                paths.push(this.itemPath);
            }
        }
    }
}

</script>
<style>
.list{
    width: 15%;
    margin: 20px;
    background-color: #d0d9ff;
    padding: 15px;
    border-radius: 10%;
    display: inline-block;
    

}
.menu-item{
    color: black;
    background-color: aliceblue;
    margin:10px;
    padding:3px;
    transition: 0.2s;
    cursor: pointer;
    border-radius: 5%;
    text-align: center ;
}
.menu-item.active,
.menu-item:hover {
    background-color: rgb(132, 140, 214);
    border-bottom-color: rgb(74, 56, 180);
}
a{
    color: inherit;
    text-decoration: none;
}
</style>