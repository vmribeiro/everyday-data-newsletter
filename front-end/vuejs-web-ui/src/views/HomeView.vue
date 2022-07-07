<template>

    <NavbarComponent></NavbarComponent>


    <div class="web-body">
        <br/><br/>

        <div class="container">
            <div class="row">
                <div class="col">
                    <h2 class="news-category-title"> <span class="vert-dash-category-title"></span>Latest News</h2> <br/>
                </div>
                <div class="col-8 horiz-dash-category-title d-none d-sm-block"></div>
            </div>
        </div>

        <div class="container">
            <div class="row">
                <div class="col-12 card-newsletter" v-for="(newsletter, index) in newsletters_list" :key="newsletter.id">
                    <div class="card-news-inside" v-bind:style="{ backgroundImage: 'url(' + newsletter.newsletter_banner_url + ')' }">
                        <p class="newsletter-category-big text-center" v-if="index%1 == 0"> <b>{{newsletter.newsletter_category}}</b> </p>
                        <p class="newsletter-title-big text-center"    v-if="index%1 == 0"> <b>{{newsletter.newsletter_title}}</b> </p>
                        <p class="newsletter-author-big text-center"   v-if="index%1 == 0"> <i> {{newsletter.newsletter_date}} | by {{newsletter.newsletter_author_profile_name}} (@{{newsletter.newsletter_author_username}})</i> </p>            
                        <a class="newsletter-link text-center d-none d-sm-block" href="#"><u>Read more</u></a>
                    </div>

                    <div class="card-newsletter-divisor d-flex justify-content-center"><div class="card-newsletter-divisor-int"></div></div>
                </div>
            </div>
        </div>

    </div>

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
                  newsletters_list: []
            }
        },

        methods: {
            
            // Sample of an API call with axios (POST)
            async listNewsletters(){

                let self = this;

                await  axios.get('http://127.0.0.1:5000/find_all_newsletters')
                            .then(  
                                response => { 
                                    console.log(response);
                                    self.newsletters_list = []
                                    self.count_pings = self.count_pings + 1;
                                    response['data']['result'].forEach(function(newsletter){
                                        
                                        self.newsletters_list.push(
                                        {     
                                              newsletter_id:                    newsletter['newsletter_id']                
                                            , newsletter_user_id:               newsletter['newsletter_user_id']           
                                            , newsletter_title:                 newsletter['newsletter_title']             
                                            , newsletter_date:                  newsletter['newsletter_date']         
                                            , newsletter_text:                  newsletter['newsletter_text']     
                                            , newsletter_banner_url:            newsletter['newsletter_banner_url']          
                                            , newsletter_author_username:       newsletter['newsletter_author_username']               
                                            , newsletter_author_profile_name:   newsletter['newsletter_author_profile_name'] 
                                            , newsletter_author_job:            newsletter['newsletter_author_job']       
                                            , newsletter_category:              newsletter['newsletter_category']       
                                        });

                                    });

                                } )
                            .catch( error    => { console.log(error)    } )

            },

        },

        beforeMount(){
            this.listNewsletters()
        },
    }

</script>