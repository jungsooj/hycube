<template>
    <div class="list" :class="{blue: isBlue() }">
        {{ listName }}
        <nav>
            <div class="component">
                <MenuItems v-for="(item, index) in items" :name="item.name" :key="index"></MenuItems>
            </div> 
        </nav>
    </div>
</template>

<script>

import MenuItems from './MenuItems.vue'

export default{
 components: {
    MenuItems
  },
  data: () => {
      return {
          items : [
              {name : "Equipement validation"},
              {name : "Assembly"},
              {name: "Health check"}
          ],
          color: "blue"
        }
    },
    props: {
            listName : {
                default: "valeur par default"
            }
        },
    methods: {
        isBlue(){
            return this.color == "blue";
        },
        isWhite(){
            return this.color == "white";
        },
        isGreen(){
            return this.color == "green";
        },
        isPurple(){
            return this.color == "purple";
        }
    }
}

</script>
<style>
.list{
    width: 15%;
    margin: 30px;
    background-color: #AFB0B5;
    padding: 15px;
    border-radius: 10%;
    display: inline-block;
}
.blue{
    background-color: #c1cbfa;
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