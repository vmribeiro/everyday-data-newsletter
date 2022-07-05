import {createRouter, createWebHistory} from 'vue-router'

/* Function that prevents the page to load everything, loading only the files that are actually needed for that page */
/* It will basically import only the files needed for that specific route, instead of importing everything as "packages" in this main file */
function lazyLoad(view){
    return import(`./views/${view}.vue`)
}

const routes = [
    {path: '/newsletters', name: "newsletters", component: lazyLoad('NewsletterView')},
    {path: '/', name: "home", component: lazyLoad('HomeView')},
    {path: '/:pathMatch(.*)*', component: lazyLoad('NotFoundView')} // In case the link doesnt exist. 404 page =)
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes
});


export default router;