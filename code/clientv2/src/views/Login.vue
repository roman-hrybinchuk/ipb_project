<template>
  <div class="login">
    <Layout/>
    <div class="container-fluid">
      <div class="mt-5 col-12 text-center">
        <h4>Login</h4>
      </div>
      <div class="row">
        <div class="col-4 mx-auto mt-5">
          <form @submit="login">
            <div class="mb-3">
              <label for="exampleInputEmail1" class="form-label">Email address</label>
              <input v-model="email" type="email" class="form-control" id="exampleInputEmail1"
                     aria-describedby="emailHelp">
              <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
            </div>
            <div class="mb-3">
              <label for="exampleInputPassword1" class="form-label">Password</label>
              <input v-model="password" type="password" class="form-control" id="exampleInputPassword1">
            </div>

            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
          <div class="col-12 mt-3">
          <span class="mt-5">If you are not registered.
          <router-link to="/register">
            <a>
              Register
            </a>
          </router-link>
          </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Layout from "@/components/Layout";

export default {
  name: "Login",
  components: {Layout},
  data() {
    return {
      email: '',
      password: '',
    }
  }, methods: {
    async login(e) {
      e.preventDefault();

      this.setUser(this.email, this.password);
      try {
        await this.getMe();

        await this.$router.push('/board');

      } catch (e) {
        this.$toast.open({message: JSON.stringify(e?.response.data), type: "error", position: 'top-right'});

        localStorage.removeItem("user-login");
      }


    }
  }
}
</script>

<style scoped>

</style>