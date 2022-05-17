<template>
    <nav>
        <div class="items" >
            <p> Stack A</p>
            <div class="menu-item" :class="{blue: isBlue}">
                <DropDown title="Equipement validation" :items="menu"></DropDown>
            </div>
            <div class="menu-item">
                <DropDown title="Assembly" :items="menu"></DropDown>
            </div>
            <div class="menu-item">
                <DropDown title="Health check" :items="menu"></DropDown>
            </div>
        </div>
    </nav> 
</template>

<script>
import DropDown from './DropDown.vue'
export default{
    compoenents: {
        DropDown
    },
    data() {
        return {
            menu: [
                {
                    title: "OBC",
                    link: "https://gitlab.isae-supaero.fr/creme/creme-ait/-/tree/master/1_Parts/OBC_495798_1171-01"
                },
                {
                    title: "MTB",
                    link: "https://gitlab.isae-supaero.fr/creme/creme-ait/-/tree/master/1_Parts/MTB_877354_1151-01"
                },
                {
                    title: "SBT",
                    link: "https://gitlab.isae-supaero.fr/creme/creme-ait/-/tree/master/1_Parts/SBT_856457_1161-01"
                }
            ]
        };
    },
    components: { DropDown },
    methods:{
        isBlue(){
            return true;
        }
    }
}
</script>

<style>
.items {
    width: 15%;
    margin: 20px;
    background-color: #d0d9ff;
    padding: 15px;
    border-radius: 10%;
    display: inline-block;
}
.menu-item.active,
.menu-item:hover {
    background-color: rgb(132, 140, 214);
    border-bottom-color: rgb(74, 56, 180);
}
a {
    color: inherit;
    text-decoration:none;
}
.menu-item{
    color: black;
    border-bottom: 3px solid transparent;
    transition:0.4s;
    background-color: aliceblue;
    margin:10px; 
    padding: 3px;
    cursor: pointer;
    border-radius: 5%;
    text-align: center;

}
.blue{
    background-color: #b0bdf8;
}
</style>