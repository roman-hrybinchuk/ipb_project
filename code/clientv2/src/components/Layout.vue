<template>
  <div class="layout">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">FastLoan</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link to="/">
                <a class="nav-link" aria-current="page">Home</a>
              </router-link>
            </li>
          </ul>

          <div class="d-flex  nav-item">
            <p v-if="me">{{ me.email }}</p>
            <router-link to="/login">
              <a class="nav-link" href="/login">Login</a>
            </router-link>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "Layout",
  data() {
    return {
      me: null
    }

  },
  async created() {
    this.me = await this.getMe();

  }

}
</script>

<style scoped>

</style>