<template>

    <NavbarComponent></NavbarComponent>
    <br/><br/>

    <h2> Bem-vindo ao Everyday Data! </h2> <br/>

    <div id="example">
        <button v-on:click="pingFlask">Ping Flask!</button>
    </div>

    <br><br>

    <div class="list-group">
        <div class="list-group-item" v-for="(ping) in pings" :key="ping.id">

            <span> Autor: <i> {{ping.time_of_ping}} </i> </span> <br>
            <span> Did it work? <strong> {{ping.worked}} </strong> </span><br>
            <p> Status: {{ping.status}} </p><br>
        
        </div>
    </div>

    <br/><br/><br/>
    <FooterComponent></FooterComponent>

</template>




<script>

    import NavbarComponent from '../components/NavbarComponent.vue';
    import FooterComponent from '../components/FooterComponent.vue';

    import axios from 'axios';

    export default {
        name: 'HomeView',

        components: {
            NavbarComponent,
            FooterComponent
        },

        data(){
            return {
                pings: [],
                count_pings: 0
            }
        },

        methods: {
            
            // Sample of an API call with axios (POST)
            pingFlask(){

                
               axios.get('http://127.0.0.1:5000/ping')
                     .then(  
                        response => { 
                            this.count_pings = this.count_pings + 1;
                            this.pings.push(
                                {     
                                      time_of_ping: new Date(Date.now()).toISOString().split('T')
                                    , id: this.count_pings
                                    , worked: response['data']['members']['did_it_work']
                                    , status: response['data']['status']
                                }
                            );
                        } )
                     .catch( error    => { console.log(error)    } )

               /* 
               const data = {
                    user: 'Victor Ribeiro'
                };

               axios.post('http://127.0.0.1:5000/ping', data)
                     .then(  
                        response => { 
                            this.count_pings = this.count_pings + 1;
                            this.pings.push(
                                {     
                                      time_of_ping: new Date(Date.now()).toISOString().split('T')
                                    , id: this.count_pings
                                    , worked: response['data']['members']['did_it_work']
                                    , status: response['data']['status']
                                }
                            );
                        } )
                     .catch( error    => { console.log(error)    } )
               */ 

                
            },

        },
    }

</script>