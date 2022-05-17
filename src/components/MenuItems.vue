<template>
    <div class="item" >
             {{name}}     
    </div>
    
</template>

<script>

    export default{
        props: {
            name : {
                default: "valeur par default"
            }
        },
    }   
</script>

<style>
.item{
    background-color: aliceblue;
    margin-top:10px;
    padding:15px 0;
    transition: 0.2s;
    cursor: pointer;
    border-radius: 5%;
    text-align: center ;
}
.item:active{
    transition: 0.1s;
    transform: scale(0.9);
    }
</style>