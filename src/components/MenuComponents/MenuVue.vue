<template>
    <AsideView></AsideView>
    <div class="list" v-for="(d,index) in data" :key="index">
        {{ d }} 
        {{iterateItemsEv(index)}}
        {{menuItemCountEv(index)}} 
        {{pathListEv(index)}} 
        {{getStatesEv(index)}} 
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
        whiteCount:0,
        menuItems: Object.keys(Object.values(Object.values(jsonData)[0])[0]), //stack A equipement validation items
        menuItemsAs: "",
        menuItemsHc: "",
        itemPath: "",
        itemPathAs:"",
        itemPathHc:"",
        itemsPath: [],
        itemState:[],
        itemsColor: [],
        color: "",
        state: "",
        stateAs: "",
        stateHc: ""

        }
    },
    props: {
            listName : {
                default: "valeur par default"
            }
        },
    methods: {

        // Equipement Validation
        iterateItemsEv(i){ 
            this.menuItems = Object.keys(Object.values(Object.values(jsonData)[i])[0]);
        },
        menuItemCountEv(i){ 
            this.menuItemsCpt = Object.keys(Object.values(Object.values(jsonData)[i])[0]).length;
        },
        iterateItemsPathEv(i, j){ 
            this.itemPath = Object.values(Object.values(Object.values(jsonData)[i])[0])[j]["path"];
        },
        pathListEv(k){
            let path = [];
            for(i=0; i<this.menuItemsCpt; i++){
                this.iterateItemsPathEv(k,i);
                path.push(this.itemPath);
            }
            this.itemsPath = path;
        },
        getItemStateEv(i,j){
            this.state = (Object.values(Object.values(Object.values(jsonData)[i])[0])[j]["state"]).toLowerCase();
        },
        stateListEv(k){
            let itemsStates=[];
            for(i=0; i<this.menuItemsCpt; i++){
                this.getItemStateEv(k,i);
                itemsStates.push(this.state);
            }
            this.itemState = itemsStates;
        },
        getStatesEv(k){
            this.stateListEv(k);
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

        //Assembly 
        iterateItemsAs(){ 
            this.menuItemsAs = Object.keys(Object.values(Object.values(jsonData)[i])[1]);
        },
        menuItemCountAs(i){ 
            this.menuItemsCptAs = Object.keys(Object.values(Object.values(jsonData)[i])[1]).length;
        },
        iterateItemsPathAs(i, j){ 
            this.itemPathAs = Object.values(Object.values(Object.values(jsonData)[i])[1])[j]["path"];
        },
        /*pathListAs(k){
            
        },*/
        getItemStateAs(i,j){
            this.stateAs = (Object.values(Object.values(Object.values(jsonData)[i])[1])[j]["state"]).toLowerCase();
        },
        /*stateListAs(k){
         
        },
        getStatesAs(k){
          
        },*/

        //Health check
        
        iterateItemsHc(){ 
            this.menuItemsHc = Object.keys(Object.values(Object.values(jsonData)[i])[2]);
        },
        menuItemCountHc(i){ 
            this.menuItemsCptHc = Object.keys(Object.values(Object.values(jsonData)[i])[2]).length;
        },
        iterateItemsPathHc(i, j){ 
            this.itemPathHc = Object.values(Object.values(Object.values(jsonData)[i])[2])[j]["path"];
        },
        /*pathListHc(k){
            
        },*/
        getItemStateHc(i,j){
            this.stateHc = (Object.values(Object.values(Object.values(jsonData)[i])[2])[j]["state"]).toLowerCase();
        },
        /*stateListHc(k){
        },
        getStatesHc(k){
           
        },*/

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
    margin-top: 50px;
    background-color: #eceef3;
    padding: 15px;
    border-radius: 20%;
    display: grid;
    display: inline-block;
    border-style: solid;
    border-color: #9bafae;
}
.menu-item{
    color: black;
    background-color: rgb(205, 225, 243);
    margin:10px;
    transition: 0.1s;
    cursor: pointer;
    border-radius: 10%;
    text-align: center ;
}
.menu-item.active,
.menu-item:hover {
    background-color: rgb(105, 154, 197);
    color:white;
}
a{
    color: black;
    text-decoration: none;
}
.blue{
    background-color: rgb(145, 186, 248);
}
.green{
    background-color: rgb(170, 223, 170);
}
.white{
    background-color: white;
}
</style>