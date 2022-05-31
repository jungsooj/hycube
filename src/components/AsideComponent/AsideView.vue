<template>
    <aside>
        <div class="white box">
            Procedure being prepared
        </div>
        <div class="blue box">
            procedure underway
        </div>
        <div class="green box">
            procedure completed
        </div>
    </aside>
</template>

<script>
</script>

<style>
.white {
    color:black;
    background-color: antiquewhite;
}
.blue {
    color:black;
    background-color: rgb(105, 154, 197);
}
.green {
    color:black;
    background-color: rgb(101, 141, 101);
}
aside{
    float: right;
    margin: 5%;
    box-shadow: inset 5px 0 5px -5px #29627e;
    font-style: italic;
    color: #29627e;
}

.box{
    width:min-content;
    margin: 10px;
    padding: 20px;
    border-radius: 10%;
    display:block;
    border-style: solid;
    border-color: #adc2c1;
}
</style>