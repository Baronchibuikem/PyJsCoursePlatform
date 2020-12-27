<template>
  <div>
    <div class="text-danger text-center">
      <span>...you are about to sign up as an Instructor</span>
    </div>

    <form novalidate @submit.prevent="handle_register">
      <div class="md-layout-item md-layout md-gutter">
        <div class="md-layout-item">
          <md-field md-clearable>
            <md-input
              v-model="first_name"
              style="padding: 10px"
              placeholder="firstname"
            ></md-input>
          </md-field>
        </div>
        <div class="md-layout-item">
          <md-field md-clearable>
            <md-input
              v-model="last_name"
              style="padding: 10px"
              placeholder="lastname"
            ></md-input>
          </md-field>
        </div>
      </div>

      <div class="md-layout-item md-layout md-gutter">
        <div class="md-layout-item">
          <md-field md-clearable>
            <md-input
              v-model="username"
              style="padding: 10px"
              placeholder="username"
            ></md-input>
          </md-field>
        </div>
        <div class="md-layout-item">
          <md-field md-clearable>
            <md-input
              type="email"
              v-model="email"
              style="padding: 10px"
              placeholder="email"
            ></md-input>
          </md-field>
        </div>
      </div>

      <div class="md-layout-item md-layout md-gutter">
        <div class="md-layout-item">
          <md-field>
            <md-select
              v-model="primary_language"
              name="primary_language"
              id="primary_language"
              placeholder="Your primary language"
              style="padding: 0px 10px"
            >
              <md-option value="python">Python</md-option>
              <md-option value="javascript">Javascript</md-option>
              <md-option value="java">Java</md-option>
              <md-option value="golang">Golang</md-option>
              <md-option value="php">PHP</md-option>
              <md-option value="ruby">Ruby</md-option>
              <md-option value="c#">C#</md-option>
            </md-select>
          </md-field>
        </div>
        <div class="md-layout-item">
          <md-field md-clearable>
            <md-input
              v-model="other_languages"
              style="padding: 10px"
              placeholder="other_languages"
            ></md-input>
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
      <div class="mx-auto">
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
      <div class="mx-auto">
        <span
          >Already have an account?
          <router-link to="/auth/login/">Login to your account.</router-link></span
        >
      </div>
    </form>
  </div>
</template>
<script>
export default {
  name: "StudentReg",
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
};
</script>
