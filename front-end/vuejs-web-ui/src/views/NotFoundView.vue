<template>

    <NavbarComponent></NavbarComponent>
    <br/><br/>

    <h1 class = "text-danger"> 404 NOT FOUND!  Check links above! </h1>

    <br/><br/><br/>
    <FooterComponent></FooterComponent>

</template>




<script>

    import NavbarComponent from '../components/NavbarComponent.vue';
    import FooterComponent from '../components/FooterComponent.vue';

    export default {
        name: 'NotFoundView',
        components: {
            NavbarComponent,
            FooterComponent
        },
        data(){
            return {
            }
        } 
    }

</script>