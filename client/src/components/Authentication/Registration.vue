<template>
  <div class="container" style="margin-top: 100px">
    <div class="mb-4 text-center">
      <span
        class="text-primary mr-3 hover"
        v-if="!show_student_form"
        @click="display_students_form()"
      >
        Sign up as a Student
      </span>
      <span
        class="text-primary mr-3 hover"
        v-if="!show_instructor_form"
        @click="display_instructor_form()"
      >
        Sign up as Instructor
      </span>
    </div>
    <div v-if="show_student_form">
      <!-- students registration goes here -->
      <StudentReg />
    </div>
    <div v-if="show_instructor_form">
      <!-- students registration goes here -->
      <InstructorReg />
    </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import StudentReg from "./StudentReg";
import InstructorReg from "./InstructorReg";

export default {
  name: "Registration",
  components: {
    StudentReg,
    InstructorReg,
  },
  data() {
    return {
      show_student_form: false,
      show_instructor_form: false,
    };
  },
  methods: {
    display_students_form() {
      this.show_student_form = true;
      this.show_instructor_form = false;
    },
    display_instructor_form() {
      this.show_instructor_form = true;
      this.show_student_form = false;
    },
  },
  computed: {
    ...mapGetters(["get_server_error"]),
  },
};
</script>
<style scoped>
.hover {
  cursor: pointer;
  text-decoration: underline;
}
</style>
