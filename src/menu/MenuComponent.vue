<template>
    <div class="component">
        <TheMenu v-for="(d, index) in data" :listName="d" :key="index"></TheMenu>
    </div>
</template>

<script>
'use strict';
let jsonData = require('../data/AitData2.json');

import TheMenu from './TheMenu.vue'

export default{
    components:{
        TheMenu
    },
    data() {
        return{
            data: Object.keys(jsonData)
        }
    }
}
</script>

<style>

</style>