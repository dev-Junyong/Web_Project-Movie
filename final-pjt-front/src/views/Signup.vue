<template>
  <v-container id="signup-page">
    <v-row class="signup-page-sub">
      <v-parallax class="login-background-img" src="@/assets/signin-background.png"></v-parallax>
      <v-col class="signup-page-sub" cols="6">
        <div class="signup-image-part">
          <div class="z-index-logo">
            <img class="login-page-logo" src="@/assets/logo@3x.png">
            <p class="login-image-s-title">Join and Enjoy CINE Life</p>
          </div>
        </div>
      </v-col>

      <v-col class="signup-page-sub" cols="6">
        <div class="signup-part">
          <div class="signup-input">
            <img id="main-logo" class="login-logo" src="@/assets/logo@3x.png">
            <h2 class="mb-3">Create an account</h2>
            <p>{{ errMsg }}</p>
            <div>
              <v-text-field
                label="Username"
                outlined
                dense
                v-model="credentials.username"
              ></v-text-field>
            </div>

            <div>
              <v-text-field
                label="e-mail"
                outlined
                dense
                v-model="credentials.email"
              ></v-text-field>
            </div>

            <div>
              <v-text-field
                label="Name"
                outlined
                dense
                v-model="credentials.name"
              ></v-text-field>
            </div>

            <div>
              <v-text-field
                label="Password"
                outlined
                dense
                type="password"
                autocomplete="off"
                v-model="credentials.password"
                @keyup.enter="signup"
              ></v-text-field>
            </div>

            <v-btn text @click="signup">create account</v-btn>

            <div class="move-login">
              <p class="login-q">do you have account?</p>
              <v-btn text @click="moveLogin">sign in</v-btn>
            </div>
          </div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

const SERVER_URL = 'https://pjt456.herokuapp.com'

export default {
  name: 'Signup',
  data () {
    return {
      credentials: {
        username: null,
        email: null,
        name: null,
        password: null,
      },
    }
  },
  methods: {
    signup() {
      const fd = new FormData()
      fd.append('username', this.credentials.username)
      fd.append('email', this.credentials.email)
      fd.append('name', this.credentials.name)
      fd.append('password', this.credentials.password)
      
      axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/signup/`,
        data: fd,
      })
        .then(res => {
          console.log(res)
          this.$store.dispatch('signup', this.credentials)
        })
    },
    moveLogin () {
      this.$router.push({ name: 'Login' })
    }
  },
  computed: {
    ...mapState([
      'errMsg',
      'isSignup',
      'isLogin',
    ])
  },
  created () {
    if (this.isLogin) {
      this.$router.push({ name: 'Main' })
    }
  },
  watch: {
    isSignup () {
      console.log('!')
      this.$router.push({ name: 'Login' })
    },
    isLogin () {
      if (this.isLogin) {
        this.$router.push({ name: 'Main' })
      }
    }
  }
}
</script>

<style>
#signup-page {
  width: 80%;
  height: 93%;
  padding-top: 0;
}

.signup-page-sub {
  height: 100%;
}

.signup-part {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 90%;
}

.signup-image-part {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 90%;
}

.signup-input {
  z-index: 20001;
  width: 60%;
  text-align: right;
}

.move-login {
  display: flex;
  justify-content: right;
  align-items: center;
}

.login-q {
  margin: 0 !important;
  font-size: 12px;
}

.login-image-s-title {
  font-size: 20px;
  font-weight: bold;
}
</style>