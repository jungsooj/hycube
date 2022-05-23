<template>
    {{countFunction()}}
    {{whiteCount}}
</template>

<script>
export default{
    data () {
        return{
            blueCount: 0,
            whiteCount:""
        }
    },
    methods: {
        countFunction(){
            let cpt=0;
            for(let i=0; i<2; i++){
                cpt++;
                console.log(cpt);
            }
            this.whiteCount=cpt;
    }
    }
}
</script>

