<template>
  <header>
    <div class="texte">
       HyCube Visual Web Interface
    </div>
    <div>
      <ul>
        <li>
          <router-link to="/">Home</router-link> |
        </li>
        <li>
          <router-link to="/about">Show Image</router-link>
        </li>
      </ul>
    </div>
  </header>
  <body>
    <router-view/>
  </body>
  <footer></footer>
</template>

<script>

export default {
  name: 'App',
  components: {
    //MenuVue,
    //SwitchTest
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
