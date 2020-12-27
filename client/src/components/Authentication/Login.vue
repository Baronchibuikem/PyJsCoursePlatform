<template>
  <div class="container regStyle" style="margin-top: 100px">
    <h5 class="text-center">Login</h5>
    <form novalidate class="md-layout" @submit.prevent="handle_login">
      <md-field md-clearable>
        <md-input
          type="email"
          v-model="email"
          style="padding: 10px"
          placeholder="Email"
        ></md-input>
      </md-field>

      <md-field>
        <md-input
          v-model="password"
          type="password"
          style="padding: 10px"
          placeholder="password"
        ></md-input>
      </md-field>
      <md-button
        type="submit"
        class="md-raised form-control md-primary"
        style="padding: 10px"
        >Login</md-button
      >
      <div class="text-center mx-auto">
        <span class="text-center h5">OR</span>
      </div>
      <md-button
        type="submit"
        class="md-raised form-control md-primary"
        style="padding: 10px"
        >Login with Google</md-button
      >
      <div class="mx-auto">
        <span
          >Don't have an account?
          <router-link to="/auth/signup/">Sign up here.</router-link></span
        >
      </div>
    </form>
  </div>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  name: "Registration",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    handle_login() {
      this.loading = true;
      const reg_values = {
        email: this.email,
        password: this.password,
      };
      const response = this.$store.dispatch("login", reg_values);
      if (response.status === 200) {
        this.$router.push("/");
      } else {
        this.$toasted.show(this.get_server_error, { duration: 3000 });
      }
    },
  },
  computed: {
    ...mapGetters(["get_server_error"]),
  },
};
</script>
<style scoped></style>
