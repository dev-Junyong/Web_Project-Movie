<template>
  <v-container class="login-page">
    <v-row class="login-page-sub">
      <v-parallax class="login-background-img" src="@/assets/login-background.png"></v-parallax>
      <v-col class="login-page-sub" cols="6">
        <div class="login-part">
          <div class="login-input">
            <img id="main-logo" class="login-logo" src="@/assets/logo@3x.png">
            <h2 class="login-title mb-3">Sign In</h2>
            <p>{{ errMsg }}</p>
            <div>
              <v-text-field
                label="Username"
                outlined
                dense
                v-model.trim="credentials.username"
              ></v-text-field>
            </div>

            <div>
              <v-text-field
                label="Password"
                outlined
                dense
                type="password"
                autocomplete="off"
                v-model.trim="credentials.password"
                @keyup.enter="login"
              ></v-text-field>
            </div>

            <div>
              <a class="forgot" @click.prevent="forgotPassword">forgot password?</a>
              <v-btn text @click="login">sing in</v-btn>
            </div>

            <div class="move-create-account">
              <p class="account-q">you don't have account?</p>
              <v-btn class="move-signup-btn" text @click="moveSignUp">create accout</v-btn>
            </div>
            <p>※ 해당 서비스는 반응형 및 모바일을 지원하지 않습니다 ※</p>
          </div>
        </div>
      </v-col>

      <v-col cols="6">
        <div class="login-image-part">
          <div class="z-index-logo">
            <img class="login-page-logo" src="@/assets/logo@3x.png">
            <p class="login-image-title">Join and Enjoy CINE Life</p>
          </div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Login',
  data () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login () {
      this.$store.dispatch('login', this.credentials)
    },
    forgotPassword () {
      alert('명함을 잃어버린 사람은 출입하실 수 없습니다\n명함을 새로 발급받으세요')
    },
    moveSignUp () {
      this.$router.push({ name: 'Signup' })
    }
  },
  computed: {
    ...mapState([
      'errMsg',
      'isLogin',
    ])
  },
  created () {
    if (this.isLogin) {
      this.$router.push({ name: 'Main' })
    }
  },
  watch: {
    isLogin () {
      if (this.isLogin) {
        this.$router.push({ name: 'Main' })
      }
    }
  }
}
</script>

<style>
.login-page {
  width: 80%;
  height: 93%;
  padding-top: 0;
}

.login-background-img {
  position: absolute;
  width: 100%;
  height: 100% !important;
  top: 0;
  left: 0;
}

.v-parallax__image-container > img {
  transform: none !important;
  filter: brightness(80%);
}

.v-parallax__image {
  left: 0 !important;
  z-index: 0 !important;
}

.login-page-sub {
  height: 100%;
}

.login-part {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 90%;
}

.login-title {
  text-align: right;
}

.login-input {
  z-index: 20001;
  width: 60%;
  text-align: right;
}

.login-image-part {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 90%;
}

.z-index-logo {
  z-index: 20001;
}

.login-page-logo {
  width: 300px;
}

.login-image-title {
  font-size: 20px;
  font-weight: bold;
  color: white;
}

.move-create-account {
  display: flex;
  justify-content: right;
  align-items: center;
}

.account-q {
  margin: 0 !important;
  font-size: 12px;
}

.forgot {
  font-size: 12px;
}

.move-signup-btn > .v-btn__content {
  font-size: 16px !important;
  font-weight: bold !important;
}
</style>