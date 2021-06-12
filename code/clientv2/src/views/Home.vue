<template>
  <div class="home">
    <Layout/>
    <div class="container-fluid money_bg">

      <div class="row pt-5 ">
        <div class="col-3 mx-auto text-white  p-5 text-center" style="background-color: rgba(0,0,0,0.9)">
          <h3>FastLoan</h3>
          <h5 class="mt-5">Loan in 15 mins</h5>
          <h5>Simple to apply</h5>
          <h5 class="mt-5">
            <router-link to="login">
              <a>Login to apply</a>
            </router-link>
          </h5>

        </div>
      </div>
    </div>

  </div>
</template>

<script>
// @ is an alias to /src
import Layout from "@/components/Layout";

export default {
  name: 'Home',
  components: {
    Layout
  }
}

</script>


<style scoped>
.money_bg {
  background: url("~@/assets/loan_bg.jpg");

  height: 100vh;
}

</style>