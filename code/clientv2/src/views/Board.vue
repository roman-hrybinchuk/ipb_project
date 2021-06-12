<template>
  <div class="board">
    <Layout/>
    <div class="container-fluid">
      <div class="row">
        <div class="row-12">
          <UsersBoard v-if="user && user.type === 'users'"/>
          <ManagerBoard v-if="user && user.type === 'managers'"/>
          <EmployeeBoard v-if="user && user.type === 'employees'"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Layout from "@/components/Layout";
import UsersBoard from "@/components/UsersBoard";
import ManagerBoard from "@/components/ManagerBoard";
import EmployeeBoard from "@/components/EmployeeBoard";

export default {
  name: "Board",
  components: {EmployeeBoard, ManagerBoard, UsersBoard, Layout},
  data() {
    return {
      user: undefined
    }
  }, async created() {
    this.user = await this.getMe();
    console.log(this.user);
  }
}
</script>

<style scoped>

</style>