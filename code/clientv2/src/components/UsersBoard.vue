<template>
  <div class="usersboard">
    <div class="container-fluid">
      <div class="row">
        <div class="col-12 mt-5 mb-3">
          <b-button v-b-modal.modal-1>Apply for loan</b-button>
          <b-modal id="modal-1" title="Apply for loan">
            <form @submit="applyRequest">

              <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Loan amount</label>
                <input v-model="amount" type="number" class="form-control" id="exampleInputPassword1">
              </div>

              <button type="submit" class="btn btn-success">Apply</button>
            </form>
          </b-modal>
        </div>
        <div class="col-6 mt-3">
          <h5>Loans</h5>
          <table class="table">
            <thead>
            <tr>
              <th scope="col">Id</th>
              <th scope="col">Amount</th>
              <th scope="col">Amount payed</th>
              <th scope="col">Status</th>
            </tr>
            </thead>
            <tbody>
            <tr :key="item.id" v-for="item in loans">
              <th>{{ item.id }}</th>
              <td>{{ item.amount }}</td>
              <td>{{ item.amount_payed || 0}}</td>
              <td>{{ item.status }}</td>
            </tr>

            </tbody>
          </table>
        </div>
        <div class="col-6 mt-3">
          <h5>Loans requests</h5>
          <table class="table">
            <thead>
            <tr>
              <th scope="col">Status</th>
              <th scope="col">Amount</th>
              <th scope="col">Date</th>
            </tr>
            </thead>
            <tbody>
            <tr :key="request.id" v-for="request in loansRequests">
              <td>{{ request.status }}</td>
              <td>{{ request.amount }}</td>
              <td>{{ new Date(request.date).toLocaleString() }}</td>
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
  name: "UsersBoard",
  data() {
    return {
      loans: [],
      loansRequests: [],
      amount: 0

    }
  },
  created() {
    this.getLoans();
    this.getLoanRequests();
  },
  methods: {

    async getLoanRequests() {
      const res = await this.axios.get('/loan_request', {
        headers: {
          'Authorization': `Basic ${this.getUser()}`
        }
      });
      this.loansRequests = res.data['loan_requests'];
    },
    async applyRequest(e) {
      e.preventDefault();
      try {

        await this.axios.post(`/loan_request?amount=${this.amount}`, {}, {
          headers: {
            'Authorization': `Basic ${this.getUser()}`
          }
        });

      } catch (e) {
        this.$toast.open({message: JSON.stringify(e?.response?.data), type: "error"})
      }
    },
    async getLoans() {
      try {
        const res = await this.axios.get('/loans', {
          headers: {
            'Authorization': `Basic ${this.getUser()}`
          }
        });
        this.loans = res.data.loans;

        console.log(this.loans);
      } catch (e) {
        this.$toast.open({message: JSON.stringify(e?.response?.data), type: "error"})

      }

    }
  }
}
</script>

<style scoped>

</style>