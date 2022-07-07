<template>

    <v-app>
        <div class="top-banner-background" v-if="isHome">

            <nav class="navbar navbar-expand-lg navbar-light">

                <!--  Show this only on mobile to medium screens  -->
                <a class="navbar-brand d-lg-none" href="#"><b>Everyday Data</b></a>

                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                
                <!--  Use flexbox utility classes to change how the child elements are justified  -->
                <div class="collapse navbar-collapse justify-content-between" id="navbarToggle">

                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="#"><router-link :to="{ path: '/' }"><b>Home</b></router-link></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#"><b>About</b></a>
                        </li>
                    </ul>

                    <!--   Show this only lg screens and up   -->
                    <a class="navbar-brand d-none d-lg-block" href="#"><b>Everyday Data</b></a>
                    
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="#"><router-link :to="{ path: '/newsletters' }"><b>News</b></router-link></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#"><b>Login</b></a>
                        </li>
                    </ul>
                </div>
            </nav>

            <div class="container banner-container row">
                <div class="col sm-12 text-left main-banner">
                    <p class="banner-title d-none d-sm-block">{{newsletter_title}}</p>
                    <p class="banner-description d-none d-sm-block">{{newsletter_text}}</p>
                    <a class="banner-link text-right d-none d-sm-block" href="#"><u>Read more</u></a>
                </div>
            </div>
        
            <br><br><br>
        </div>

        <div class="top-banner-background-nothome" v-if="isNotHome">

            <nav class="navbar navbar-expand-lg navbar-light">

                <!--  Show this only on mobile to medium screens  -->
                <a class="navbar-brand d-lg-none" href="#"><b>Everyday Data</b></a>

                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <!--  Use flexbox utility classes to change how the child elements are justified  -->
                <div class="collapse navbar-collapse justify-content-between" id="navbarToggle">

                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="#"><router-link :to="{ path: '/' }"><b>Home</b></router-link></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#"><b>About</b></a>
                        </li>
                    </ul>

                    <!--   Show this only lg screens and up   -->
                    <a class="navbar-brand d-none d-lg-block" href="#"><b>Everyday Data</b></a>
                    
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="#"><router-link :to="{ path: '/newsletters' }"><b>News</b></router-link></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#"><b>Login</b></a>
                        </li>
                    </ul>
                </div>
            </nav>

            <div class="container banner-container-nothome row">
                <div class="col sm-12 text-center main-banner-nothome">
                    <p class="banner-title ">A new approach to the data world</p>
                    <p class="banner-description d-none d-sm-block">Daily news on your e-mail</p>
                </div>
            </div>
        
            <br><br><br>
        </div>
    </v-app>
    
            

</template>




<script>

    import axios from 'axios';

    export default {
        data(){
            return {
                newsletter_id :                   '',         
                newsletter_user_id :              '',          
                newsletter_title :                '',          
                newsletter_date :                 '',     
                newsletter_text :                 '',                        
                newsletter_author_username :      '',             
                newsletter_author_profile_name :  '', 
                newsletter_author_job :           '', 
                newsletter_category :             ''      
            }
        },
        computed: {
            isHome() {
                return this.$route.name === 'home'
            },
            isNotHome() {
                return this.$route.name != 'home'
            }
        },

        methods: {
            
            // Sample of an API call with axios (POST)
            async listBannerNewsletter(){

                let self = this;

                await  axios.get('http://127.0.0.1:5000/find_newsletter_by_id/4')
                            .then(  
                                response => { 
                                    console.log(response);
                                    self.newsletter_id =                    response['data']['result']['newsletter_id'];               
                                    self.newsletter_user_id =               response['data']['result']['newsletter_user_id'];           
                                    self.newsletter_title =                 response['data']['result']['newsletter_title'];             
                                    self.newsletter_date =                  response['data']['result']['newsletter_date'];         
                                    self.newsletter_text =                  response['data']['result']['newsletter_text'];    
                                    self.newsletter_banner_url =            response['data']['result']['newsletter_banner_url'];          
                                    self.newsletter_author_username =       response['data']['result']['newsletter_author_username'];               
                                    self.newsletter_author_profile_name =   response['data']['result']['newsletter_author_profile_name']; 
                                    self.newsletter_author_job =            response['data']['result']['newsletter_author_job'];       
                                    self.newsletter_category =              response['data']['result']['newsletter_category'];      
                                } )
                            .catch( error    => { console.log(error)    } )

            },

        },

        beforeMount(){
            this.listBannerNewsletter()
        },
    }

</script>