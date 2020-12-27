import Vue from "vue"
import Router from "vue-router"
const Home = () => import ("./components/Homepage/HomeIndex")

Vue.use(Router);

export default new Router({
    mode: "history",
    routes: [
        {
            path: "/",
            name: "HomeIndex",
            component: Home,
        },                
        {
            name: "AuthCentralController",
            path: "/auth",
            component: () => import("./components/Authentication/AuthCentralController"),
            children:[
                {
                    name: "Registration",
                    path: "signup",
                    component: () => import("./components/Authentication/Registration"),
                },
                {
                // We be rendered if registration is successful
                name: "RegistrationEmailSent",
                path: 'email-sent',
                component: () => import("./components/EmailSent/RegistrationEmailSent")
                },
                {
                    name: "Login",
                    path: "login",
                    component: () => import("./components/Authentication/Login"),
                },
            ]
        },
                
       
        // {
        //     path: "/register/",
        //     name: "Registration",
        //     component: Registration,
        //     children: [
        //         {
        //           // We be rendered if registration is successful
        //           path: 'email-sent',
        //           name: "RegistrationEmailSent",
        //           component: RegistrationEmailSent
        //         }
        //     ]
        // },
        
    ]
})