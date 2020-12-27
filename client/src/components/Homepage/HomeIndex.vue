<template>
  <v-app>
    <Carousel />
    <div class="container">
      <div class="md-title text-center">Latest Courses</div>
      <div class="row">
        <div class="col-md-4"><Card /></div>
        <div class="col-md-4"><Card /></div>
        <div class="col-md-4"><Card /></div>
      </div>
    </div>

    <div style="min-height: 50vh; background-color: blue"></div>
  </v-app>
</template>

<script>
import Carousel from "./CarouselSlider";
import Card from "../utilities/Card/Card";
export default {
  components: {
    Carousel,
    Card,
  },
};
</script>

<style>
</style>