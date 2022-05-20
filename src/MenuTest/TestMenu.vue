<template>
    <div class="list" v-for="(d,index) in data" :key="index">
        {{ d }} {{iterateItems(index)}} {{menuItemCount(index)}} {{pathList(index)}}
        <nav>
            <div class="component">
                <div class="menu-item" >
                    <SubmenuTest title="Equipement validation" :items="menuItems" :path="itemsPath"></SubmenuTest>
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
import SubmenuTest from './SubmenuTest.vue';

'use strict';
let jsonData = require('../data/AitData3.json');
let i=0;

export default{
 components: {
    SubmenuTest
  },
  data: () => {
      return {
        data: Object.keys(jsonData),
        menuCpt : Object.keys(jsonData).length,
        menuItemsCpt : 0,
        menuItems: Object.keys(Object.values(Object.values(jsonData)[0])[0]), //stack A equipement validation items
        itemPath: "",
        itemsPath: [],
        }
    },
    props: {
            listName : {
                default: "valeur par default"
            }
        },
    methods: {
        iterateItems(i){ //for equipement validation (the 0 refer to Equipement validation)
            this.menuItems = Object.keys(Object.values(Object.values(jsonData)[i])[0]);
        },
        menuItemCount(i){ //for equipement validation
            this.menuItemsCpt = Object.keys(Object.values(Object.values(jsonData)[i])[0]).length;
        },
        iterateItemsPath(i, j){ //for equipement validation
            this.itemPath = Object.values(Object.values(Object.values(jsonData)[i])[0])[j]["path"];
        },
        pathList(k){
            let path = [];
            for(i=0; i<this.menuItemsCpt; i++){
                this.iterateItemsPath(k,i);
                path.push(this.itemPath);
            }
            this.itemsPath = path;
        },
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