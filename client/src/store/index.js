import Vuex from "vuex";
import Vue from "vue";
import UserAuth from "./modules/authentication";
import createPersistedState from "vuex-persistedstate";

// load vuex
Vue.use(Vuex);

// create store
export default new Vuex.Store({
	plugins: [createPersistedState()],
	modules: {
		UserAuth
	}
});
