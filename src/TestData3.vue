<template>
    <div class="level1">
        <h4 v-for="(item,index) in menuItems" :key="index"> {{item}} </h4>
    </div>
    <div class="level2">
        <h4 v-for="(evi,index) in EquipementValidationItems" :key="index"> 
            {{evi}}
        </h4>
    </div>
    <div> item path = {{itemPath}} </div>
</template>

<script>
'use strict';
let jsonData = require('./data/AitData3.json');

export default{
    data () {
        return{
        menuItems: Object.keys(jsonData),
        EquipementValidationItems: Object.keys(Object.values(Object.values(jsonData)[0])[0]), // for Stack A
        itemPath: Object.values(Object.values(Object.values(jsonData)[0])[0])[0]["path"] //for the Path
        }
    }
}
</script>

