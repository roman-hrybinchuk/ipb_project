<template>
  <div class="ManagerBoard">
    <div class="container-fluid">
      <div class="row mt-5">
        <div class="col-9 mx-auto">
          <table class="table">
            <thead>
            <tr>
              <th scope="col">ClientId</th>
              <th scope="col">Status</th>
              <th scope="col">Amount</th>
              <th scope="col">Some important data</th>

              <th scope="col">Approve</th>
              <th scope="col">Reject</th>
            </tr>
            </thead>
            <tbody>
            <tr :key="item.id" v-for="item in requests">
              <th>{{ item.user_id }}</th>
              <td>{{ item.status }}</td>
              <td>{{ item.amount }}</td>
              <td>Has 100 children</td>

              <td>
                <button @click="changeStatus('approved',item.id)" class="btn btn-success">Approve</button>
              </td>
              <td>
                <button @click="changeStatus('rejected',item.id)" class=" btn btn-danger">Reject</button>
              </td>

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
  name: "ManagerBoard",
  data() {
    return {
      requests: [],

    }
  },
  created() {
    this.getPending();

    setInterval(() => {
      this.getPending();
    }, 1500)

  },
  methods: {
    async changeStatus(newStatus, req_id) {

      try {
        await this.axios.post(`/requests/manager/${req_id}?new_status=${newStatus}`, {}, {
          headers: {
            'Authorization': `Basic ${this.getUser()}`
          }
        })

        await this.getPending();
      } catch (e) {
        this.$toast.open({message: JSON.stringify(e), type: "error"})
      }
    },
    async getPending() {
      try {
        const res = await this.axios.get('/requests/manager', {
          headers: {
            'Authorization': `Basic ${this.getUser()}`
          }
        })

        this.requests = res.data.requests;
        console.log(this.requests);
      } catch (e) {
        this.$toast.open({message: JSON.stringify(e), type: "error"})
      }

    }
  }
}
</script>

<style scoped>

</style>