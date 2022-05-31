<template>
  <header>
      <ul id="right">
            <li class="item"> HyCube Visual Web Interface </li>
      </ul>
      <ul id="left">
        <li class="menu">
          <router-link to="/" class="item">Home</router-link> 
        </li>
        <li class="menu">
          <router-link to="/about" class="item">Show Image</router-link>
        </li>
      </ul>
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
    background-color:#355caf;
    width: 100%;
}
body{
    margin:0;
}
li{
  display: inline-block;
  margin: 5px;
  margin-top: 10px;
  padding:8px;
  color: aliceblue;
  border-radius: 10px;
}
.menu {
  color: aliceblue;
}
.menu.active,
.menu:hover{
  background-color:rgb(73, 93, 182);
  border-bottom-color: rgb(229, 229, 252);
  color: black;
}
ul{
  list-style:none;
}
.item {
  color: aliceblue;
  font-weight: bold;
}
#left{
    float:left;
}
#right{
    float:right;
}
#title{
  color: black;
  background-color: none;
}
</style>
