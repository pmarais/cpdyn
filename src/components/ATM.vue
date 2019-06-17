<template>
  <div class="hello">

    <p>Who are you?</p>
    <input type="text" placeholder="" v-model="user">
    
    <template v-if="user">
      <p>Pin?</p>
      <input type="password" placeholder="" v-model="pin" @keyup.enter.exact="auth">
    </template>
    
    <br><br>

    <input 
      type="submit" 
      value="Submit" 
      @click="auth"
      :disabled="!user || !pin">
    <hr/>

    <template v-if="authed">
      Welcome {{user}} <br><br>

      These are the accounts that you have: <br><br>

      <template v-for="(account, key) in accounts">
        {{account.acc_number}} | 
        {{account.acc_type}} | 
        {{account.acc_opened}} -›
        {{account.acc_balance}}
        <input 
          type="submit" 
          value="Withdraw"
          @click="withdrawInit(account)">
        <br>
      </template>
    </template>

    <br><br>

    <template v-if="withdrawing">
      Withdrawing from account 

      {{withdrawAccount.acc_number}} | 
      {{withdrawAccount.acc_type}} | 
      {{withdrawAccount.acc_opened}} -›
      {{withdrawAccount.acc_balance}}

      <br><br>

      Enter the amount you would like to withdraw: <br><br>

      <input type="number" v-model="withrdawAmount">

      <input 
        type="submit" 
        value="Let's go"
        @click="withdraw(withdrawAccount.acc_id)">

    </template>

    <template v-if="withdrawingSuccess">
      <br>
      Successfully withdrew {{withrdawAmount}} from {{withdrawAccount.acc_type}}
    </template>
    
    <br><br>

    <button @click="reset" v-if="user">
      Exit
    </button>

  </div>
</template>

<script>
import axios from 'axios'
import Cookies from 'js-cookie'

const headers = {
  'Content-Type': 'application/json',
  'X-CSRFToken': Cookies.get('csrftoken')
}

export default {
  name: 'ATM',
  data () {
    return {
      user: '',
      pin: '',
      authed: false,
      subject: '',
      msgBody: '',
      client: null,
      withdrawing: false,
      withrdawAmount: 0,
      withdrawAccount: null,
      withdrawingSuccess: false,
      accounts: [],
    };
  },
  mounted () {
    this.init()
  },
  methods: {
    init () {
      console.log('Init')
    },
    auth () {
      axios.post('/api/auth/', {user: this.user, pin: this.pin}, headers).then(response => {
        console.log(response)
        this.client = response.data.client
        console.log('Authorisation')
        this.authed = true
        this.getAccounts(this.client.cl_id)
      })
    },
    getAccounts (clId) {
      axios.get('/api/useraccounts/' + clId + '/').then(response => {
        this.accounts = response.data
        console.log('accounts >>>>', this.accounts)
      })
    },
    withdrawInit (account) {
      this.withdrawing = true
      this.withdrawAccount = account
    },
    withdraw (accId) {
      console.log("Withdrawing >>", accId)
      let payload = {
        'tr_id': '',
        'tr_amount': -1 * this.withrdawAmount,
        'tr_date': new Date().toJSON().slice(0,10),
        'tr_account': accId
      }
      axios.post('/api/transactions/', payload, headers).then(response => {
        console.log(response)
        this.withdrawing = false
        this.getAccounts(this.client.cl_id)
        this.withdrawingSuccess = true
      })
    },
    reset () {
      this.user = ''
      this.pin = ''
      this.authed = false
      this.subject = ''
      this.msgBody = ''
      this.client = null
      this.withdrawing = false
      this.withrdawAmount = 0
      this.withdrawAccount = null
      this.withdrawingSuccess = false
      this.accounts = []
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
hr {
  max-width: 65%;
}

.msg {
  margin: 0 auto;
  max-width: 30%;
  text-align: left;
  border-bottom: 1px solid #ccc;
  padding: 1rem;
}

.msg-index {
  color: #ccc;
  font-size: 0.8rem;
  /* margin-bottom: 0; */
}

img {
  width: 250px;
  padding-top: 50px;
  padding-bottom: 50px;
}

</style>
