import {user_register, user_login} from "../server_side_api_calls/authentication_api_calls"
import router from "../../router"



const state = {
    status : false,
    is_authenticated: false,
    token: localStorage.getItem("token") || "",
    user : {},
    server_error: {}
}
const getters = {
    get_current_user : (state) => state.user,
    get_server_error: (state) => state.server_error,
    get_is_user_authenticated: (state) => state.is_authenticated,
    get_current_status: state => state.status
    
};

const actions = {
    async login({commit}, payload){
        commit("POST_REQUEST");
        try {
            const response = await user_login(payload)
            const token = response.data.token
            localStorage.setItem("token", token);
            commit("POST_RESPONSE")   
            commit("LOGIN_SUCCESSFUL", response.data)
            commit("CLEAR_SERVER_ERROR")
            router.push("/dashboard")
        } catch (error) {
            console.log(error.response.data.message, "Error")
            commit("SERVER_ERROR", error.response.data.message)

            commit("POST_RESPONSE")
        }
        
        
},
    async register({commit}, payload){
        commit('POST_REQUEST');
        try {
            const response = await user_register(payload)
            commit("REGISTRATION_SUCCESSFUL", response.data)
            commit("POST_RESPONSE")                
        } catch (error) {
            commit("SERVER_ERROR", error.response.data)
            commit("POST_RESPONSE")
        } 
    
}  
};

const mutations = {
    POST_REQUEST (state) {
		state.status = true;
    },
    POST_RESPONSE(state){
        state.status = false;
    },
    SERVER_ERROR(state, payload){
        state.server_error = payload;
    },
    CLEAR_SERVER_ERROR(state){
        state.server_error = {}
    },
    REGISTRATION_SUCCESSFUL(state, payload){
        state.user = payload
        state.is_authenticated = true
        state.status = false
    },
    LOGIN_SUCCESSFUL(state, payload){
        const { token, user } = payload;
        state.token = token;
		state.user = { ...user };
        state.is_authenticated = true
    }


    
}



export default {
	state,
	getters,
	actions,
	mutations,
};
