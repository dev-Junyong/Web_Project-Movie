<template>
  <v-container class="profile-update-page">
    <v-row class="signup-page-sub">
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
            <h2 class="mb-3">Change your password</h2>
            <p>{{ errMsg }}</p>
            <v-text-field
              label="Username"
              outlined
              dense
              placeholder="username"
              v-model="changeData.username"
            ></v-text-field>

            <v-text-field
              label="E-mail"
              outlined
              dense
              placeholder="e-mail"
              v-model="changeData.email"
            ></v-text-field>

            <v-text-field
              label="Password"
              outlined
              dense
              type="password"
              autocomplete="off"
              placeholder="password"
              v-model="changeData.password"
            ></v-text-field>

            <v-btn @click="update" text>update</v-btn>
          </div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'PasswordChange',
  data () {
    return {
      changeData: {
        username: null,
        email: null,
        password: null,
      },
    }
  },
  methods: {
    update () {
      this.$store.dispatch('changePassword', this.changeData)
      this.$router.push({ name: 'Login' })
    }
  },
  computed: {
    ...mapState([
      'errMsg',
    ])
  }
}
</script>

<style>

</style>