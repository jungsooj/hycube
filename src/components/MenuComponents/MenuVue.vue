<template>
    <AsideView></AsideView>
    <div class="list" v-for="(d,index) in data" :key="index">
        {{iterateItemsEv(index)}}
        {{menuItemCountEv(index)}} 
        {{pathListEv(index)}} 
        {{getStatesEv(index)}} 
        {{getEvColor()}}
        {{ d }} 
        <nav>
            <div class="component">
                <div class="menu-item" v-if="isBlue()" :class="{blue: isBlue()}">
                    <SubMenu title="Equipement validation" :items="EvMenuItems" :path="EvItemsPath" :color="EvItemsColor"></SubMenu>
                </div>
                <div class="menu-item" v-else :class="{white: isWhite()}" >
                    <SubMenu title="Equipement validation" :items="EvMenuItems" :path="EvItemsPath" :color="EvItemsColor"></SubMenu>
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

        //Equipement Validation data
        EvMenuItemsCpt : 0,
        EvMenuItems: [],
        EvItemsPath: [],
        EvItemsColor: [],
        EvItemPath: "",
        EvItemState:[],
        EvState: "",
        EvColor: "",
        EvBlueCount:0,
        EvWhiteCount:0,

        //Assembly data
        AsMenuItemsCpt : 0,
        AsMenuItems: [],
        AsItemsPath: [],
        AsItemsColor: [],
        AsItemPath: "",
        AsItemState:[],
        AsState: "",
        AsColor: "blue",
        AsBlueCount:0,
        AsWhiteCount:0,
        

        //Health check
        HcMenuItemsCpt : 0,
        HcMenuItems: [],
        HcItemsPath: [],
        HcItemsColor: [],
        HcItemPath: "",
        HcItemState:[],
        HcState: "",
        HcColor: "blue",
        HcBlueCount:0,
        HcWhiteCount:0,
        //HcGreenCount:0,

        color: "",
        componentColor: "",
        MenuBlueCount: 0,
        MenuWhiteCount:0,
        }
    },
    props: {
            listName : {
                default: "default value"
            }
        },
    methods: {

        // Equipement Validation
        iterateItemsEv(i){ 
            this.EvMenuItems = Object.keys(Object.values(Object.values(jsonData)[i])[0]);
        },
        menuItemCountEv(i){ 
            this.EvMenuItemsCpt = Object.keys(Object.values(Object.values(jsonData)[i])[0]).length;
        },
        iterateItemsPathEv(i, j){ 
            this.EvItemPath = Object.values(Object.values(Object.values(jsonData)[i])[0])[j]["path"];
        },
        pathListEv(k){
            let path = [];
            for(i=0; i<this.EvMenuItemsCpt; i++){
                this.iterateItemsPathEv(k,i);
                path.push(this.EvItemPath);
            }
            this.EvItemsPath = path;
        },
        getItemStateEv(i,j){
            this.EvState = (Object.values(Object.values(Object.values(jsonData)[i])[0])[j]["state"]).toLowerCase();
        },
        stateListEv(k){
            let itemsStates=[];
            for(i=0; i<this.EvMenuItemsCpt; i++){
                this.getItemStateEv(k,i);
                itemsStates.push(this.EvState);
            }
            this.EvItemState = itemsStates;
        },
        getStatesEv(k){
            this.stateListEv(k);
            let cptBlue=0;
            let cptWhite=0;
            let colors=[];
            for(i=0; i<this.EvMenuItemsCpt; i++){
               switch(this.EvItemState[i]){
                   case "reception" : cptBlue++; colors[i] = "blue";  break;
                   case "NaN" : cptWhite++; colors[i]= "white"; break;
                   default: cptWhite++; colors[i]="white";
               }
            }
            this.blueCount = cptBlue;
            this.whiteCount = cptWhite;
            this.EvItemsColor = colors;
        },

        //Assembly 
        iterateItemsAs(i){ 
            this.AsMenuItems = Object.keys(Object.values(Object.values(jsonData)[i])[0]);
        },
        menuItemCountAs(i){ 
            this.AsMenuItemsCpt = Object.keys(Object.values(Object.values(jsonData)[i])[0]).length;
        },
        iterateItemsPathAs(i, j){ 
            this.AsItemPath = Object.values(Object.values(Object.values(jsonData)[i])[0])[j]["path"];
        },
        pathListAs(k){
            let path = [];
            for(i=0; i<this.AsMenuItemsCpt; i++){
                this.iterateItemsPathAs(k,i);
                path.push(this.AsItemPath);
            }
            this.AsItemsPath = path;
        },
        getItemStateAs(i,j){
            this.AsState = (Object.values(Object.values(Object.values(jsonData)[i])[0])[j]["state"]).toLowerCase();
        },
        stateListAs(k){
            let itemsStates=[];
            for(i=0; i<this.AsMenuItemsCpt; i++){
                this.getItemStateAs(k,i);
                itemsStates.push(this.AsState);
            }
            this.AsItemState = itemsStates;
        },
        getStatesAs(k){
            this.stateListAs(k);
            let cptBlue=0;
            let cptWhite=0;
            let colors=[];
            for(i=0; i<this.AsMenuItemsCpt; i++){
               switch(this.AsItemState[i]){
                   case "reception" : cptBlue++; colors[i] = "blue";  break;
                   case "NaN" : cptWhite++; colors[i]= "white"; break;
                   default: cptWhite++; colors[i]="white";
               }
            }
            this.blueCount = cptBlue;
            this.whiteCount = cptWhite;
            this.AsItemsColor = colors;
        },


        //Health check
        iterateItemsHc(i){ 
            this.HcMenuItems = Object.keys(Object.values(Object.values(jsonData)[i])[0]);
        },
        menuItemCountHc(i){ 
            this.HcMenuItemsCpt = Object.keys(Object.values(Object.values(jsonData)[i])[0]).length;
        },
        iterateItemsPathHc(i, j){ 
            this.HcItemPath = Object.values(Object.values(Object.values(jsonData)[i])[0])[j]["path"];
        },
        pathListHc(k){
            let path = [];
            for(i=0; i<this.HcMenuItemsCpt; i++){
                this.iterateItemsPathHc(k,i);
                path.push(this.HcItemPath);
            }
            this.HcItemsPath = path;
        },
        getItemStateHc(i,j){
            this.HcState = (Object.values(Object.values(Object.values(jsonData)[i])[0])[j]["state"]).toLowerCase();
        },
        stateListHc(k){
            let itemsStates=[];
            for(i=0; i<this.HcMenuItemsCpt; i++){
                this.getItemStateHc(k,i);
                itemsStates.push(this.HcState);
            }
            this.HcItemState = itemsStates;
        },
        getStatesHc(k){
            this.stateListHc(k);
            let cptBlue=0;
            let cptWhite=0;
            let colors=[];
            for(i=0; i<this.HcMenuItemsCpt; i++){
               switch(this.HcItemState[i]){
                   case "reception" : cptBlue++; colors[i] = "blue";  break;
                   case "NaN" : cptWhite++; colors[i]= "white"; break;
                   default: cptWhite++; colors[i]="white";
               }
            }
            this.blueCount = cptBlue;
            this.whiteCount = cptWhite;
            this.HcItemsColor = colors;
        },

        // Equipement validation color function
        getEvColor(){
            this.Color="";
            this.EvColor="";
            if(this.EvBlueCount == this.EvMenuItemsCpt){
                this.color = "blue";
                this.EvColor= "blue";
                this.EvBlueCpt = 0;
            }
            else {
                this.color = "white";
                this.EvColor = "white";
            }
        },

        // Assembly color function
        getAsColor(){
            this.Color="";
            this.AsColor="";
            if(this.AsBlueCount == this.AsMenuItemsCpt){
                this.color = "blue";
                this.AsColor= "blue";
                this.AsBlueCpt = 0;
            }
            else {
                this.color = "white";
                this.AsColor = "white";
            }
        },

        // Health check color function
        getHcColor(){
            this.Color="";
            this.HcColor="";
            if(this.HcBlueCount == this.HcMenuItemsCpt){
                this.color = "blue";
                this.HcColor = "blue";
                this.HcBlueCpt = 0;
            }
            else {
                this.color == "white";
            }
        },

        isComponentBlue(){
            return this.EvIsBlue()&&this.AsIsBlue()&&this.HcIsBlue();
        },

        EvIsBlue(){
            return this.EvColor == "blue";
        },
        AsIsBlue(){
            return this.AsColor == "blue";
        },
        HcIsBlue(){
            return this.HcColor == "blue";
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
        },
        getMenusColor(){

        }
    }
}

</script>
<style>
.list{
    width: 15%;
    margin: 20px;
    margin-top: 100px;
    background-color: #fefeff;
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