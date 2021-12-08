<template>
  <v-container v-if="personData" class="profile-page">
    <v-row>
      <v-col
        cols="4"
      >
        <v-row class="profile-back-img">
          <v-col cols="5">
            <div v-if="personData.profile_photo" class="profile-image-box">
              <img :src="`${personData.profile_photo}`" class="profile-image">
            </div>

            <div v-else class="profile-image-box">
              <img src="@/assets/non_profile.png" class="profile-image">
            </div>
          </v-col>

          <v-col cols="7" class="profile-description">
            <div class="flex-l">
              <p class="profile-description-t">{{ personData.name }}</p>
              <span v-if="personData.username == loginUser.username"></span>

              <span v-else-if="personFollowersUsername.includes(loginUser.username)">
                <button
                  @click="follow"
                  class="follow-btn ml-5"
                >
                  <v-icon color="grey lighten-5">
                    mdi-account-check
                  </v-icon>
                </button>
              </span>

              <span v-else>
                <button
                  @click="follow"
                  height="24"
                  class="follow-btn ml-5"
                >
                  <v-icon color="grey lighten-5">
                    mdi-account-plus-outline
                  </v-icon>
                </button>
              </span>
              <a
                v-if="personData.username === loginUser.username"
                @click.prevent="moveProfileUpdate"
                class="profile-edit-btn ml-5"
              >
                프로필 수정
              </a>
            </div>
            <p>{{ personData.email }}</p>

            <div class="profile-follow">
              <span>
                <p v-if="personFollowings">팔로잉: {{ personFollowings.length }}</p>
                <p v-if="personFollowers">팔로워: {{ personFollowers.length }}</p>
              </span>
            </div>

            <div class="flex-l mt-3">
              <div class="vote-btn site_color">
                <v-icon color="grey lighten-5" small>mdi-thumb-up</v-icon>
              </div>
              <p class="profile-like-cnt d-d ml-2 mr-3">{{ this.likeCnt }}</p>

              <div class="vote-btn site_color">
                <v-icon color="grey lighten-5" small>mdi-bookmark-multiple</v-icon>
              </div>
              <p class="profile-like-cnt d-d ml-2 mr-3">{{ this.personData.like_movies.length }}</p>

              <div class="vote-btn site_color">
                <v-icon color="grey lighten-5" small>mdi-comment-text-multiple</v-icon>
              </div>
              <p v-if="userReviews" class="profile-like-cnt d-d ml-2 mr-3">{{ this.userReviews.length }}</p>
            </div>
          </v-col>

          <v-col cols="12">
            <div class="flex-bt">
              <p class="profile-user-id ml-2">{{ personData.username }} - No.{{ userNum }}</p>

              <div>
                <v-btn
                  rounded
                  @click="moveCollection"
                  height="24"
                  class="profile-collection-btn site_color mr-5"
                >
                  컬렉션
                </v-btn>
                <v-btn
                  rounded
                  height="24"
                  class="profile-collection-btn site_color"
                  @click="moveTimeline"
                >
                  Timeline
                </v-btn>
              </div>
            </div>
          </v-col>
        </v-row>

        <v-container class="mt-10 text-left">
          <div>
            <h4>{{ personData.username }}'s Reviews</h4>
          </div>
          <v-row v-if="personData">
              <review-card
                v-for="review in personData.review_author.slice(-9, personData.review_author.length)"
                :key="review.id"
                :review="review"
                class="collections"
              >
              </review-card>
          </v-row>
        </v-container>
      </v-col>

      <v-col
        cols="8"
        class="chart-part"
      >
        <bar-chart style="height: 300px;"></bar-chart>

        <v-container>
          <div>
            <h4>{{ personData.username }}'s Like Movie</h4>
          </div>
          <v-row v-if="personData">
              <like-movie-card
                v-for="like_movie in personData.like_movies.slice(-18, personData.like_movies.length)"
                :key="like_movie.id"
                :like_movie="like_movie"
                class="collections"
              >
              </like-movie-card>
          </v-row>
        </v-container>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ReviewCard from '../components/Profile/ReviewCard'
import LikeMovieCard from '../components/Profile/LikeMovieCard'
import BarChart from '../components/Profile/BarChart'
import { mapState } from 'vuex'

export default {
  name: 'UserProfile',
  components: {
    ReviewCard,
    LikeMovieCard,
    BarChart,
  },
  data () {
    return {
      thisUsername: this.$route.params.username,
      isFollow: null,
      dialog: false,
      notifications: false,
      sound: true,
      widgets: false,
      likeCnt: 0,
    }
  },
  methods: {
    follow () {
      this.$store.dispatch('follow', this.thisUsername)
    },
    moveProfileUpdate () {
      this.$router.push({ name: 'UserProfileUpdate', params: { username: this.loginUser.username }})
    },
    moveTimeline () {
      this.$router.push({ name: 'TimeLine', params: { useranem: this.loginUser.username }})
    },
    moveCollection () {
      this.$router.push({ name: 'UserCollection', params: { username: this.personData.username }})
    },
  },
  computed: {
    ...mapState([
      'isLogin',
      'personData',
      'userReviews',
      'loginUser',
      'personFollowings',
      'personFollowers',
      'personFollowersUsername',
      'chartdata',
      'userNum',
    ]),
  },
  created () {
    this.$store.dispatch('getLoginUser')
    this.$store.dispatch('getUser', this.thisUsername)
    this.$store.dispatch('getPersonFollowings', this.thisUsername)
    this.$store.dispatch('getPersonFollowers', this.thisUsername)
  },
  watch: {
    $route () {
      this.thisUsername = this.$route.params.username
      this.$store.dispatch('getUser', this.thisUsername)
      this.$store.dispatch('getPersonFollowings', this.thisUsername)
      this.$store.dispatch('getPersonFollowers', this.thisUsername)
    },
    isLogin () {
      this.$store.dispatch('getLoginUser')
    }
  }
}
</script>

<style>
.profile-image-box {
  width: 100%;
  height: 200px;
  border-radius: 5px;
  overflow: hidden;
  box-shadow: 0px 4px 2px -2px rgb(0 0 0 / 20%), 0px 3px 3px 0px rgb(0 0 0 / 14%), 0px 2px 6px 0px rgb(0 0 0 / 12%);
}

.profile-description {
  color: white;
}

.profile-description-t {
  font-size: 25px;
  font-weight: bold;
}

.profile-edit-btn {
  font-size: 10px !important;
  color: aqua !important;
}

.profile-page {
  width: 75%;
  padding-top: 0;
}

.profilepage-photo {
  width: 110px !important;
  height: 110px !important;
}

.profile-top {
  font-size: 16px;
  text-align: center;
  color: white;
  padding-top: 5px;
  padding-bottom: 0px;
}

.edit-profile-btn {
  text-decoration: none;
  color: blueviolet !important;
  font-size: 16px;
}

.profile-middle {
  font-size: 20px;
  text-align: center;
  color: white;
  padding-top: 5px;
  padding-bottom: 0px;
}

.profile-collection-btn {
  font-size: 20px;
  font-weight: bold;
  color: white !important;
}

.profile-collection-position {
  padding-top: 50px;
}

.profile-follow {
  font-size: 16px;
  padding-top: 15px;
}

.follow-btn {
  background: linear-gradient(to bottom right, #F83D3D, #B600EB);
  color: white !important;
  font-weight: bold;
  border-radius: 5px;
  width: 100%;
}

.profile-bottom {
  font-size: 12px;
  text-align: center;
  color: white;
  padding-top: 0px;
  padding-bottom: 0px;
}

.profile-bottom-title {
  font-size: 16px;
}

.profile-bottom-review-title {
  font-size: 12px;
  margin-bottom: 0px;
}

.profile-back-img {
  background-image: url('../assets/profile_back.png');
  background-size: cover;
  background-position: center;
}

.v-application p {
  margin-bottom: 0px;
}

.chart-part {
  padding-top: 0 !important;
}

.profile-like-cnt {
  color: white;
  font-size: 15px;
}

.profile-user-id {
  color: white;
  font-size: 20px;
}
</style>