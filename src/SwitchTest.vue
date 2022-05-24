<template>
    <v-switch :case="color">
        <template #blue >
            <div :class="{blue: color=='blue'}">
                textin blue
            </div>
        </template>
        <template #white>
            <div :class="{white: color=='white'}">
                textin violet
            </div>
        </template>
    </v-switch>
</template>

<script>
//import { defineComponent } from 'vue'
import VSwitch from '@lmiller1990/v-switch'
export default{
    components: {
        VSwitch
    },
    data (){
        return {
            color: "blue"
        }
    }
}
</script>

<style>
.blue {
    color: blue;
}
.white {
    background-color: aquamarine;
}
</style>