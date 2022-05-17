<template>
  <header>
    <!--<h3> <a href="javascript:showImage()">show image</a> </h3>-->
  </header>
  <body>
    <ComponentVue></ComponentVue>
    <!--<LinkVue></LinkVue>-->
    <!--<img  id="myImageId" src="./assets/Creme_plan_AIT.png" />-->
  </body>
  <footer></footer>
</template>

<script>

import ComponentVue from './components/ComponentVue.vue'
//import LinkVue from './LinkTest/TheMenu.vue'

export default {
  name: 'App',
  components: {
   ComponentVue,
   //LinkVue
  },
  methods:{
    showImage() {
    var img = document.getElementById('myImageId');
    img.style.visibility = 'visible';
}
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
    height: 70px;
    background-color:#008080;
    width: 100%;
}
body{
    margin:0;
}
</style>
