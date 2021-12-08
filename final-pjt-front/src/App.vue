<template>
  <v-app id="app">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css" integrity="sha512-YWzhKL2whUzgiheMoBFwW8CKV4qpHQAEuvilg9FAn5VJUDwKZZxkJNuGM4XkWuk94WCrrwslk8yWNGmY1EduTA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <v-app-bar
      class="px-16"
      color="grey lighten-4"
      dense
      dark
      app
      height="62px"
    >
      <span style="width: 10%"></span>
      <router-link :to="{ name: 'Main' }" class="pt-1"><img id="main-logo" src="@/assets/logo@3x.png" alt=""></router-link>
      <router-link class="nav-link" :to="{ name: 'Movie' }">영화</router-link>
      <router-link class="nav-link" :to="{ name: 'Community' }">리뷰</router-link>
      <router-link class="nav-link" :to="{ name: 'Recommend' }">추천</router-link>

      <v-spacer></v-spacer>

      <v-text-field
        hide-details
        solo
        dense
        placeholder="영화 제목 검색"
        append-icon="mdi-magnify"
        class="shrink mx-4"
        v-model.trim="keyword"
        @keyup.enter="searchKeyword"
      >
      </v-text-field>

      <span v-if="isLogin" class="flex-l">
        <a class="nav-link" @click.prevent="moveProfile">
          <div v-if="loginUser.profile_photo" class="profile-box">
            <img :src="`${loginUser.profile_photo}`" class="profile-image">
          </div>
          <v-avatar v-else class="profile-photo">
            <v-icon style="color: black;" >
              mdi-account-circle
            </v-icon>
          </v-avatar>
        </a>

        <a v-if="loginUser.is_staff" href="http://pjt456.herokuapp.com/admin/" class="admin-text">관리자 페이지</a>

        <router-link class="nav-link" to="#" @click.native="logout">로그아웃</router-link>
      </span>

      <span v-else>
        <router-link class="nav-link" :to="{ name: 'Signup' }">회원가입</router-link>
        <router-link class="nav-link" :to="{ name: 'Login' }">로그인</router-link>
      </span>
      <span style="width: 10%"></span>
    </v-app-bar>

    <v-main>
      <div style="height: 64px"></div>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'App',

  data: function () {
    return {
      keyword: null,
    }
  },
  methods: {
    logout () {
      this.$store.dispatch('logout')
      this.$router.push({ name: 'Login' })
    },
    moveProfile () {
      this.$router.push({ name: 'UserProfile', params: { username: this.loginUser.username } })
    },
    searchKeyword () {
      if (this.keyword) {
        this.$store.dispatch('searchKeyword', this.keyword)
        this.$router.push({ name: 'SearchResult', params: { keyword: this.keyword }})
      } else {
        alert('※ 검색어는 한 글자 이상이어야 합니다 ※')
      }
      this.keyword = null
    },
  },
  computed: {
    ...mapState([
      'isLogin',
      'loginUser',
    ])
  },
  created () {
    if (localStorage.getItem('JWT')) {
      this.$store.dispatch('getLoginUser')
    } else {
      this.$router.push({ name: 'Login' }).catch(() => {})
    }
  },
  watch: {
    isLogin () {
      if (this.isLogin) {
        this.$store.dispatch('getLoginUser')
      }
    }
  },
  destroyed () {
    localStorage.removeItem('JWT')
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

#main-logo {
  width: 86px;
}

.nav-link {
  color: black !important;
  font-weight: bold;
  text-decoration: none;
  margin: 0 20px;
}

.theme--dark.v-text-field--solo > .v-input__control > .v-input__slot {
    background: #cecece !important;
}

.v-text-field.v-text-field--solo:not(.v-text-field--solo-flat) > .v-input__control > .v-input__slot {
    box-shadow: none !important;
}

::deep .v-text-field{
      width: 300px;
}

.profile-btn {
  color: black !important;
}

.profile-photo {
  width: 30px !important;
  height: 30px !important;
}

.v-app-bar.v-app-bar--fixed {
    z-index: 30000 !important;
}

.profile-box {
  height: 30px;
  width: 30px;
  border-radius: 70%;
  overflow: hidden;
  box-shadow: 0px 4px 2px -2px rgb(0 0 0 / 20%), 0px 3px 3px 0px rgb(0 0 0 / 14%), 0px 2px 6px 0px rgb(0 0 0 / 12%);
}

.admin-text {
  text-decoration: none;
}

.footer-part {
  width: 75%;
  margin: 0 auto;
}

.footer-logo {
  height: 15px;
}

.footer-text {
  font-size: 12px;
  color: #696969;
}
</style>