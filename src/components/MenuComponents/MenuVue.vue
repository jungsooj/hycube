<template>
    <AsideView></AsideView>
    <div class="list" v-for="(d,index) in data" :key="index">
        {{ d }} 
        {{iterateItems(index)}}
        {{menuItemCount(index)}} 
        {{pathList(index)}} 
        {{getStates(index)}} 
        {{getColor()}}
        <nav>
            <div class="component">
                <div class="menu-item" v-if="isBlue()" :class="{blue: isBlue()}">
                    <SubMenu title="Equipement validation" :items="menuItems" :path="itemsPath" :color="itemsColor"></SubMenu>
                </div>
                <div class="menu-item" v-else :class="{white: isWhite()}" >
                    <SubMenu title="Equipement validation" :items="menuItems" :path="itemsPath" :color="itemsColor"></SubMenu>
                </div>
                <div class="menu-item" @click="existLink()">
                    Assembly  
                </div>
                <div class="menu-item" @click="existLink()">
                    Health check
                </div>
                
            </div> 
        </nav>
    </div>
</template>

<script>
import SubMenu from './SubMenu.vue';
import AsideView from '../AsideComponent/AsideView.vue'
'use strict';
let jsonData = require('../../data/AitData.json');
let i=0;
export default{
 components: {
    SubMenu,
    AsideView,
},
  data: () => {
      return {
        data: Object.keys(jsonData),
        menuCpt : Object.keys(jsonData).length,
        menuItemsCpt : 0,
        blueCount:0,
        //greenCount:0,
        //purpleCount:0,
        whiteCount:0,
        menuItems: Object.keys(Object.values(Object.values(jsonData)[0])[0]), //stack A equipement validation items
        itemPath: "",
        itemsPath: [],
        itemState:[],
        itemsColor: [],
        color: "",
        state: ""
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
        getItemState(i,j){
            this.state = (Object.values(Object.values(Object.values(jsonData)[i])[0])[j]["state"]).toLowerCase();
        },
        stateList(k){
            let itemsStates=[];
            for(i=0; i<this.menuItemsCpt; i++){
                this.getItemState(k,i);
                itemsStates.push(this.state);
            }
            this.itemState = itemsStates;
        },
        getStates(k){
            this.stateList(k);
            let cptBlue=0;
            let cptWhite=0;
            let colors=[];
            for(i=0; i<this.menuItemsCpt; i++){
               switch(this.itemState[i]){
                   case "reception" : cptBlue++; colors[i] = "blue";  break;
                   case "NaN" : cptWhite++; colors[i]= "white"; break;
                   default: cptWhite++; colors[i]="white";
               }
            }
            this.blueCount = cptBlue;
            this.whiteCount = cptWhite;
            this.itemsColor = colors;
        },
        getColor(){
            this.color="";
            if(this.blueCount == this.menuItemsCpt){
                this.color = "blue";
                this.blueCpt = 0;
            }
            else {
                this.color == "white";
            }
        },
        existLink(){
                alert("Link doesn't exist");
        },
        isBlue(){
            return this.color == "blue";
        },
        isGreen(){
            return this.color == "green";
        },
        isPurple(){
            return this.color == "purple";
        },
        isWhite(){
            return this.color == "white";
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
    border-style: solid;
    border-color: #b0b6d1;
}
.menu-item{
    color: black;
    background-color: aliceblue;
     margin:10px;
    transition: 0.1s;
    cursor: pointer;
    border-radius: 5%;
    text-align: center ;
}
.menu-item.active,
.menu-item:hover {
    background-color: rgb(255, 255, 255);
}
a{
    color: black;
    text-decoration: none;
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