import {user_register, user_login} from "../server_side_api_calls/authentication_api_calls"

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
    get_is_user_authenticated: (state) => state.is_authenticated
};

const actions = {
    async login({commit}, payload){
        commit("POST_REQUEST");
        try {
            const response = await user_login(payload)
            console.log(response, "api call")
            commit("LOGIN_SUCCESSFUL", response)
            commit("POST_RESPONSE")   
        } catch (error) {
            commit("SERVER_ERROR", error.response.data)
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
    REGISTRATION_SUCCESSFUL(state, payload){
        state.user = payload
        state.is_authenticated = true
    },
    LOGIN_SUCCESSFUL(state, payload){
        state.user = payload
        state.is_authenticated = true
        state.token = localStorage.setItem(payload.token)
    }


    
}



export default {
	state,
	getters,
	actions,
	mutations,
};
