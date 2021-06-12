<template>
  <div class="EmployeeBoard">
    <div class="container-fluid">
      <div class="row mt-5">
        <div class="col-3">
          <div class="md-form mt-0">
            <input v-model="search" class="form-control" type="text" placeholder="Search" aria-label="Search">
          </div>
        </div>
        <div class="col-3">
          <button @click="searchRequests" class="btn btn-success">Search</button>
        </div>
      </div>

      <div class="row">
        <div class="col-6 mx-auto">
          <table class="table">
            <thead>
            <tr>
              <th scope="col">Status</th>
              <th scope="col">Amount</th>
              <th scope="col">Date</th>
              <th scope="col">Issue</th>

            </tr>
            </thead>
            <tbody>
            <tr :key="request.id" v-for="request in userRequest">
              <td>{{ request.status }}</td>
              <td>{{ request.amount }}</td>
              <td>{{ new Date(request.date).toLocaleString() }}</td>
              <td v-if="request.status === 'approved'">
                <button @click="issueLoan(request)" class="btn btn-success">Issue</button>
              </td>
              <td v-else>Not allowed</td>

            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "EmployeeBoard",
  data() {
    return {
      search: "",
      userRequest: []
    }
  },
  methods: {

    async issueLoan(request) {
      try {
        await this.axios.post(`/loans`, {
          "amount": request.amount,
          "user_id": request.user_id
        }, {
          headers: {
            'Authorization': `Basic ${this.getUser()}`
          }
        })

        this.$toast.open({message: "Request has been archived"})

        await this.searchRequests();
      } catch (e) {
        this.$toast.open({message: JSON.stringify(e), type: "error"})
      }
    },
    async searchRequests() {
      try {
        const res = await this.axios.get(`/requests/employee/${this.search}`, {
          headers: {
            'Authorization': `Basic ${this.getUser()}`
          }
        })


        this.userRequest = res.data.requests

        if (res.data.requests.length === 0) {
          this.$toast.open("User does not have any requests ")
        }

      } catch (e) {
        this.$toast.open({message: JSON.stringify(e), type: "error"})
      }


    }

  }
}
</script>

<style scoped>

</style>