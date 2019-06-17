<template>
  <div class="hello">
    <img src='@/assets/logo-django.png' style="width: 250px" />
    <p>This is the CP ATM.</p>
    <br/>

    <p>Who are you?</p>
    <input type="text" placeholder="" v-model="user">
    
    <template v-if="user">
      <p>Pin?</p>
      <input type="password" placeholder="" v-model="pin">
    </template>
    
    <br><br>

    <input 
      type="submit" 
      value="Submit" 
      @click="auth" 
      :disabled="!user || !pin">
    <hr/>
    
    <!-- <h3>Messages on Database</h3>
    <p v-if="messages.length === 0">No Messages</p>
    <div class="msg" v-for="(msg, index) in messages" :key="index">
        <p class="msg-index">[{{index}}]</p>
        <p class="msg-subject" v-html="msg.subject"></p>
        <p class="msg-body" v-html="msg.body"></p>
        <input type="submit" @click="deleteMessage(msg.pk)" value="Delete" />
    </div> -->

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
  data() {
    return {
      user: '',
      pin : '',
      authed: false,
      subject: '',
      msgBody: '',
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
      })
      console.log('Authorisation')
      this.authed = true
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
