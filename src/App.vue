<template>
  <header>
    <!--<h3> <a href="javascript:showImage()">show image</a> </h3>-->
  </header>
  <body>
    <!--<ComponentVue></ComponentVue>-->
    <!--<LinkVue></LinkVue>-->
    <!--<img  id="myImageId" src="./assets/Creme_plan_AIT.png" />-->
    <!--<TheMenu></TheMenu>-->
    <TestMenu></TestMenu>
  </body>
  <footer></footer>
</template>

<script>

//import ComponentVue from './components/ComponentVue.vue'
//import LinkVue from './LinkTest/TheMenu.vue'
//import ComponentVue from './TestComponents/ComponentVue.vue'
//import TheMenu from './menu/TheMenu.vue';
import TestMenu from './MenuTest/TestMenu.vue'
export default {
  name: 'App',
  components: {
    //ComponentVue,
    //ComponentVue
    //LinkVue
    //TheMenu,
    TestMenu
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
header{
    position: fixed;
    top : 0;
    height: 60px;
    background-color:#008080;
    width: 100%;
}
body{
    margin:0;
}
</style>
