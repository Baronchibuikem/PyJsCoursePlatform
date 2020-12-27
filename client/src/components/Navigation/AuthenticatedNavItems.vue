<template>
  <div>
    <md-list-item>
      <!-- <md-icon>move_to_inbox</md-icon> -->
      <span class="md-list-item-text">Home</span>
    </md-list-item>

    <md-list-item>
      <!-- <md-icon>send</md-icon> -->
      <span class="md-list-item-text">Already Enrolled</span>
    </md-list-item>

    <md-list-item>
      <!-- <md-icon>error</md-icon> -->
      <span class="md-list-item-text">My Courses</span>
    </md-list-item>

    <md-list-item>
      <!-- <md-icon>delete</md-icon> -->
      <span class="md-list-item-text">All Courses</span>
    </md-list-item>

    <md-list-item>
      <!-- <md-icon>error</md-icon> -->
      <span class="md-list-item-text">Blog</span>
    </md-list-item>

    <md-list-item>
      <!-- <md-icon>error</md-icon> -->
      <span class="md-list-item-text">My Inbox</span>
    </md-list-item>

    <md-list-item>
      <!-- <md-icon>error</md-icon> -->
      <span class="md-list-item-text">FAQ</span>
    </md-list-item>

    <md-list-item>
      <!-- <md-icon>error</md-icon> -->
      <span class="md-list-item-text">Contact Support</span>
    </md-list-item>
  </div>
</template>

<script>
export default {
  name: "AuthenticatedNavItems",
};
</script>
<style lang="scss" scoped>
.md-list-item-text {
  color: white !important;
  margin-left: 20px !important;
}
</style>
