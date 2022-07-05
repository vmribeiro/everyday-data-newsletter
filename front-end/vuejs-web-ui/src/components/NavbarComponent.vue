<template>

    <h4> Everyday Data (navbar) </h4>
    <br>
    <ul>
        <li> <router-link :to="{ path: '/' }">Home</router-link> </li> 
        <li> <router-link :to="{ path: '/newsletters' }">Newsletter</router-link> </li>
    </ul>
    <br><br>

</template>




<script>

    export default {
        data(){
            return {
            }
        } 
    }

</script>