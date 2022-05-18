<template>
    <div class="list">
        {{ listName }}
        <nav>
            <div class="component">
                <div class="menu-item">
                    <SubMenu title="Equipement validation" :items="menuItems"></SubMenu>
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

export default{
 components: {
    SubMenu
  },
  data: () => {
      return {
         menuItems: Object.keys(Object.values(jsonData)[0])
        }
    },
    props: {
            listName : {
                default: "valeur par default"
            }
        },
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