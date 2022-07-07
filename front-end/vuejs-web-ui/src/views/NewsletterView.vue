
<template>

    <NavbarComponent></NavbarComponent>

    <div class="web-body">

        <br/>

        <h2> Newsletters </h2>

        <div class="list-group">
            <div class="list-group-item" v-for="(news) in newsletters" :key="news.id">

                <span class="comment__author" id="{{news.id}}"> Autor: <strong> {{news.name}} </strong> </span><br/><br>
                <b> {{news.title}} </b><br>
                <p> {{news.description}} </p>
            
            </div>
        </div>

        <br/><br/>

    </div>
    
    <FooterComponent></FooterComponent>

</template>




<script>

    import NavbarComponent from '../components/NavbarComponent.vue';
    import FooterComponent from '../components/FooterComponent.vue';

    export default {
        name: 'NewsletterView',
        components: {
            NavbarComponent,
            FooterComponent
        },
        data(){
            return {
                newsletters: [
                    {     id: 1
                        , name: "Usuário 1"
                        , title: "Newsletter 2"
                        , description: "Lorem ipsum blablabla"
                    }
                ]
            }
        } 
    }

</script>