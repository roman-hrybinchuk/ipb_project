<template>
  <div class="register">
    <Layout/>
    <div class="container-fluid">
      <div class="mt-5 col-12 text-center">
        <h4>Register</h4>
      </div>
      <div class="row">
        <div class="col-4 mx-auto mt-5">
          <form @submit="register">
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
            <div class="mb-3">
              <label for="passport_id" class="form-label">Passport id</label>
              <input v-model="passportId" type="text" class="form-control" id="passport_id">
            </div>

            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
          <div class="col-12 mt-3">
          <span class="mt-5">Already have an account.
          <router-link to="/login">
            <a>
              Login
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
  name: "Register",
  components: {
    Layout
  },
  data() {
    return {
      email: "",
      password: "",
      passportId: ""
    }
  },
  methods: {
    async register(e) {
      e.preventDefault();
      try {
        await this.axios.post('/users', {
          email: this.email,
          passport_id: this.passportId,
          password: this.password
        });

        this.setUser(this.email, this.password);
        await this.$router.push('/board');
      } catch (e) {
        this.$toast.open({message: "Error during message", type: "error", position: 'top-right'});
      }

    }
  }
}
</script>

<style scoped>

</style>