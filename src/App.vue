<template>
  <header>
    <div class="texte">
       HyCube Visual Web Interface
    </div>
    <div>
      <ul>
        <li>
          <a href="#"> Home </a>
        </li>
        <li>
          <a href=""> Show Image</a>
        </li>
      </ul>
    </div>
  </header>
  <body>
    <!--<CountTest></CountTest>-->
    <MenuVue></MenuVue>
  </body>
  <footer></footer>
</template>

<script>
import MenuVue from './MenuComponents/MenuVue.vue'
/*import ComponentVue from './components/ComponentVue.vue'*/
//import CountTest from './CountTest.vue'
export default {
  name: 'App',
  components: {
    MenuVue,
    //ComponentVue
    //CountTest
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
    background-color:#358daf;
    width: 100%;
}
.texte{
   font-style: italic;
    font-weight: bold;
    text-align: center;
    color:aliceblue;
    padding-top: 20px;
    padding-left: 10px;
}
body{
    margin:0;
    background-image: url("./assets/pic1.jpg");
}
ul{
  margin: 0px;
  text-align: left;
}
li{
  display: inline-block;
  margin-left: 5px;
  margin-right: 15px;
}
a{
  color: aliceblue;
}
</style>
