<template>
  <div class="container layout-view">
    <div class="col-md-8 col-sm-12 mx-auto">
      <h5 class="text-center">Signup here</h5>
      <form novalidate @submit.prevent="handle_register">
        <div class="md-layout-item md-layout md-gutter">
          <div class="md-layout-item">
            <md-field md-clearable>
              <md-input
                v-model="first_name"
                style="padding: 10px"
                placeholder="Firstname"
              ></md-input>
            </md-field>
          </div>
          <div class="md-layout-item">
            <md-field md-clearable>
              <md-input
                v-model="last_name"
                style="padding: 10px"
                placeholder="Lastname"
              ></md-input>
            </md-field>
          </div>
        </div>

        <div class="md-layout-item md-layout md-gutter">
          <div class="md-layout-item">
            <md-field md-clearable>
              <md-input
                type="email"
                v-model="email"
                style="padding: 10px"
                placeholder="Email"
              ></md-input>
            </md-field>
          </div>
          <div class="md-layout-item">
            <md-field>
              <md-select
                v-model="user_type"
                name="user_type"
                id="user_type"
                placeholder="user type"
                style="padding: 0px 10px"
              >
                <md-option value="Instructor">Instructor</md-option>
                <md-option value="Student">Student</md-option>
              </md-select>
            </md-field>
          </div>
        </div>

        <div class="md-layout-item md-layout md-gutter">
          <div class="md-layout-item">
            <md-field>
              <md-input
                v-model="password"
                type="password"
                style="padding: 10px"
                placeholder="password"
              ></md-input>
            </md-field>
          </div>
          <div class="md-layout-item">
            <md-field>
              <md-input
                v-model="confirm_password"
                type="password"
                style="padding: 10px"
                placeholder="confirm password"
              ></md-input>
            </md-field>
          </div>
        </div>
        <div class="text-center">
          <span
            >By clicking “Create Account”, you agree to our
            <router-link to="">Terms of Use </router-link>and
            <router-link to="">Privacy</router-link> Policy.</span
          >
        </div>
        <md-button
          type="submit"
          class="md-raised form-control md-primary"
          style="padding: 10px"
          >Create Account</md-button
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
        <div class="text-center">
          <span
            >Already have an account?
            <router-link to="/login/">Login to your account.</router-link></span
          >
        </div>
      </form>
    </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  name: "Registration",
  data() {
    return {
      email: "",
      first_name: "",
      last_name: "",
      username: "",
      user_type: {
        Instructor: "",
        Student: "",
      },
      password: "",
      confirm_password: "",
    };
  },
  methods: {
    handle_register() {
      this.loading = true;
      const reg_values = {
        email: this.email,
        first_name: this.first_name,
        last_name: this.last_name,
        username: this.username,
        password: this.password,
        confirm_password: this.confirm_password,
        user_type: this.user_type,
      };
      const response = this.$store.dispatch("register", reg_values);
      if (response.status === 200) {
        this.$router.push("/registration/email-sent");
      } else {
        this.$toasted.show(this.get_server_error, { duration: 3000 });
      }
    },
  },
  computed: {
    ...mapGetters(["get_server_error", "get_current_status"]),
  },
};
</script>
<style scoped>
.layout-view {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 90vh;
}
</style>
