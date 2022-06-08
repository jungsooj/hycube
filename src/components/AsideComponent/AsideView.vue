<template>
    {{getColorList()}}
    <aside>
        <div v-for="(color, i) in colors" :key="i">
            <div class="box" v-bind:style="{ backgroundColor : colors[i]}">
                {{names[i]}}
            </div>
        </div>
    </aside>
</template>

<script>
'use strict';
let asideData = require('../../../data/AsideData.json');
export default{
    data (){
        return{
            names: Object.keys(asideData),
            cpt: Object.keys(asideData).length,
            colors:[]
        }
    },
    methods:{
        getColorList(){
            let colorArray=[];
            for(var i=0; i<this.cpt; i++){
                colorArray[i] = Object.values(Object.values(asideData))[i]['color']
            }
            this.colors = colorArray;
        }
    }
}
</script>

<style>
aside{
    float: right;
    margin: 5%;
    box-shadow: inset 5px 0 5px -5px #29627e;
    font-style: italic;
    color: #29627e;
}

.box{
    width:min-content;
    margin: 10px;
    padding: 20px;
    border-radius: 10%;
    display:block;
    border-style: solid;
    border-color: #adc2c1;
    color: black;
}
</style>