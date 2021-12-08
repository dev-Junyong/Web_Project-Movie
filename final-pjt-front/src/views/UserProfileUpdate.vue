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
            <div class="file-input">
              <label for="profile-photo">
                <div v-if="selectedFile" class="profile-preview-box">
                  <a>
                    <img :src="fileUrl" class="profile-image">
                  </a>
                </div>

                <div v-else-if="loginUser.profile_photo" class="profile-preview-box">
                  <a>
                    <img :src="`${loginUser.profile_photo}`" class="profile-image">
                  </a>
                </div>

                <div v-else class="profile-preview-box">
                  <a>
                    <v-icon>
                      mdi-account-circle
                    </v-icon>
                  </a>
                </div>
              </label>
              <input type="file" id="profile-photo" class="mt-3" @change="onFileSelected">
            </div>
            <p class="d-d info-txt mt-3">※ 사진을 변경하려면 프로필 이미지를 클릭하세요 ※</p>
            <p class="d-d info-txt mb-5">※ 정사각형 이미지를 권장합니다 ※</p>

            <v-text-field
              label="Name"
              outlined
              dense
              placeholder="Name"
              v-model="loginUser.name"
            ></v-text-field>

            <v-text-field
              label="E-mail"
              outlined
              dense
              placeholder="E-mail"
              v-model="loginUser.email"
            ></v-text-field>

            <v-btn @click="onUpload" text>update</v-btn>
          </div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'

const SERVER_URL = 'https://pjt456.herokuapp.com'

export default {
  name: 'UserProfileUpdate',
  data () {
    return {
      selectedFile: null,
      fileUrl: null,
    }
  },
  methods: {
    onFileSelected(event) {
      this.selectedFile = event.target.files[0]
      this.fileUrl = URL.createObjectURL(this.selectedFile)
      console.log(this.selectedFile)
    },
    onUpload() {
      const fd = new FormData()
      fd.append('image', this.selectedFile, this.selectedFile.name)
      fd.append('email', this.loginUser.email)
      fd.append('name', this.loginUser.name)

      axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/${this.loginUser.username}/profile/photo/`,
        data: fd,
        headers: {
          Authorization: `Bearer ${localStorage.getItem('JWT')}`
        }
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'UserProfile', params: { username: this.loginUser.username }})
        })
      // axios.post(`${SERVER_URL}/accounts/${this.loginUser.username}/profile/photo/`, fd, {
      //     Authorization: `Bearer ${localStorage.getItem('JWT')}`
      //   })
      //   .then(res => {
      //     console.log(res)
      //   })
    }
  },
  computed: {
    ...mapState([
      'loginUser',
    ])
  }
}
</script>

<style>
.profile-update-page {
  width: 80%;
  height: 93%;
  padding-top: 0;
}

.file-input {
  display: flex;
  justify-content: right;
}

.profile-preview-box {
  height: 80px;
  width: 80px;
  border-radius: 70%;
  overflow: hidden;
  box-shadow: 0px 4px 2px -2px rgb(0 0 0 / 20%), 0px 3px 3px 0px rgb(0 0 0 / 14%), 0px 2px 6px 0px rgb(0 0 0 / 12%);
}

.profile-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.file-input input[type="file"] {
    position: absolute;
    width: 0;
    height: 0;
    padding: 0;
    overflow: hidden;
    border: 0;
}

.info-txt {
  font-size: 10px;
}
</style>