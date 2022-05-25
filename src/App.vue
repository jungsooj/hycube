<template>
  <header>
      <div id="right">
            HyCube Visual Web Interface
      </div>
      <ul id="left">
        <li class="menu">
          <router-link to="/">Home</router-link> 
        </li>
        <li class="menu">
          <router-link to="/about">Show Image</router-link>
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
    background-color:#358daf;
    width: 100%;
}
body{
    margin:0;
    background-image: url("./assets/pic1.jpg");
}
li{
  display: inline-block;
  margin: 5px;
  margin-top: 10px;
  padding:8px;
  color: aliceblue;
  border-radius: 10px;
}
.menu.active,
.menu:hover{
  color:black;
  background-color:beige;
  border-bottom-color: rgb(75, 75, 255);
}
ul{
  list-style:none;
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
