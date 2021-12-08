<template>
  <v-container class="timeline-page">
    <h3 class="unmute">배경음악을 듣고싶다면 음소거를 해제해주세요</h3>
    <iframe
      class="unvisibility"
      type="text/html"
      :src="`https://www.youtube.com/embed/lqcio72aD1k?autoplay=1&mute=1&loop=1&playlist=lqcio72aD1k`"
      frameborder="0"
      width="100%"
      height="1080px"
    >
    </iframe>
    <img src="@/assets/timeline.png" class="timeline-back">

    <div class="flex-c timeline-title mb-10">
      <p><a @click.prevent="moveProfile">{{ personData.username }}</a>'s Timeline</p>
    </div>

      <v-row class="timeline-part">
        <v-col cols="6">
          <div
            v-for="(review, index) in personData.review_author"
            :key="index"
          >
            <div
              v-if="index % 6 === 1"
              data-aos="fade-down"
              data-aos-easing="linear"
              data-aos-duration="1000"
              class="left-box align-end"
            >
              <v-card class="timeline-card movie-card-poster mr-5">
                <div class="flex-bt">
                  <p class="d-d time-line-review-title">{{ review.title }}</p>

                  <div class="flex-l">
                    <div class="flex-l">
                      <v-icon small class="site-color-text">
                        mdi-thumb-up-outline
                      </v-icon>
                      <p class="ml-2">{{ review.users_like.length }}</p>
                    </div>
                    <div class="flex-l">
                      <v-icon small class="site-color-text ml-2">
                        mdi-comment-processing-outline
                      </v-icon>
                      <p class="ml-2">{{ review.review_comments.length }}</p>
                    </div>
                  </div>
                </div>
                <p class="mt-2">{{ review.content }}</p>
              </v-card>
              <img
                class="time-line-movie-poster movie-card-poster mr-4"
                :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${review.movie.poster_path}`"
              >
              <p
                :class="{'hidden1': index % 6 === 0, 'hidden2': index % 6 === 2, 'hidden3': index % 6 === 4, 'timeline-date': true}"
              >
                {{ review.created_at.slice(0, 10) }} ●
              </p>
            </div>

            <div
              v-else-if="index % 6 === 3"
              data-aos="fade-right"
              data-aos-easing="linear"
              data-aos-duration="1000"
              class="left-box align-end"
            >
              <v-card class="timeline-card movie-card-poster mr-5">
                <div class="flex-bt">
                  <p class="d-d time-line-review-title">{{ review.title }}</p>
                  
                  <div class="flex-l">
                    <div class="flex-l">
                      <v-icon small class="site-color-text">
                        mdi-thumb-up-outline
                      </v-icon>
                      <p class="ml-2">{{ review.users_like.length }}</p>
                    </div>
                    <div class="flex-l">
                      <v-icon small class="site-color-text ml-2">
                        mdi-comment-processing-outline
                      </v-icon>
                      <p class="ml-2">{{ review.review_comments.length }}</p>
                    </div>
                  </div>
                </div>
                <p class="mt-2">{{ review.content }}</p>
              </v-card>
              <img
                class="time-line-movie-poster movie-card-poster mr-4"
                :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${review.movie.poster_path}`"
              >
              <p
                :class="{'hidden1': index % 6 === 0, 'hidden2': index % 6 === 2, 'hidden3': index % 6 === 4, 'timeline-date': true}"
              >
                {{ review.created_at.slice(0, 10) }} ●
              </p>
            </div>

            <div
              v-else-if="index % 6 === 5"
              data-aos="fade-up-right"
              data-aos-easing="linear"
              data-aos-duration="1000"
              class="left-box align-end"
            >
              <v-card class="timeline-card movie-card-poster mr-5">
                <div class="flex-bt">
                  <p class="d-d time-line-review-title">{{ review.title }}</p>

                  <div class="flex-l">
                    <div class="flex-l">
                      <v-icon small class="site-color-text">
                        mdi-thumb-up-outline
                      </v-icon>
                      <p class="ml-2">{{ review.users_like.length }}</p>
                    </div>
                    <div class="flex-l">
                      <v-icon small class="site-color-text ml-2">
                        mdi-comment-processing-outline
                      </v-icon>
                      <p class="ml-2">{{ review.review_comments.length }}</p>
                    </div>
                  </div>
                </div>
                <p class="mt-2">{{ review.content }}</p>
              </v-card>
              <img
                class="time-line-movie-poster movie-card-poster mr-4"
                :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${review.movie.poster_path}`"
              >
              <p
                :class="{'hidden1': index % 6 === 0, 'hidden2': index % 6 === 2, 'hidden3': index % 6 === 4, 'timeline-date': true}"
              >
                {{ review.created_at.slice(0, 10) }} ●
              </p>
            </div>
            <div if-else style="width: 100%; height: 100px;"></div>
          </div>
        </v-col>

        <div class="center-line"></div>

        <v-col cols="6">
          <div
            v-for="(review, index) in personData.review_author"
            :key="index"
          >
            <div
              v-if="index % 6 === 0"
              data-aos="fade-up"
              data-aos-easing="linear"
              data-aos-duration="1000"
              class="right-box align-start"
            >
              <p
                :class="{'hidden1': index % 6 === 1, 'hidden2': index % 6 === 3, 'hidden3': index % 6 === 5, 'timeline-date': true}"
              >
                ● {{ review.created_at.slice(0, 10) }}
              </p>
              <img
                class="time-line-movie-poster movie-card-poster ml-4"
                :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${review.movie.poster_path}`"
              >
              <v-card class="timeline-card movie-card-poster ml-5">
                <div class="flex-bt">
                  <p class="d-d time-line-review-title">{{ review.title }}</p>
                  
                  <div class="flex-l">
                    <div class="flex-l">
                      <v-icon small class="site-color-text">
                        mdi-thumb-up-outline
                      </v-icon>
                      <p class="ml-2">{{ review.users_like.length }}</p>
                    </div>
                    <div class="flex-l">
                      <v-icon small class="site-color-text ml-2">
                        mdi-comment-processing-outline
                      </v-icon>
                      <p class="ml-2">{{ review.review_comments.length }}</p>
                    </div>
                  </div>
                </div>
                <p class="mt-2">{{ review.content }}</p>
              </v-card>
            </div>

            <div
              v-else-if="index % 6 === 2"
              data-aos="fade-left"
              data-aos-easing="linear"
              data-aos-duration="1000"
              class="right-box align-start"
            >
              <p
                :class="{'hidden1': index % 6 === 1, 'hidden2': index % 6 === 3, 'hidden3': index % 6 === 5, 'timeline-date': true}"
              >
                ● {{ review.created_at.slice(0, 10) }}
              </p>
              <img
                class="time-line-movie-poster movie-card-poster ml-4"
                :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${review.movie.poster_path}`"
              >
              <v-card class="timeline-card movie-card-poster ml-5">
                <div class="flex-bt">
                  <p class="d-d time-line-review-title">{{ review.title }}</p>
                  
                  <div class="flex-l">
                    <div class="flex-l">
                      <v-icon small class="site-color-text">
                        mdi-thumb-up-outline
                      </v-icon>
                      <p class="ml-2">{{ review.users_like.length }}</p>
                    </div>
                    <div class="flex-l">
                      <v-icon small class="site-color-text ml-2">
                        mdi-comment-processing-outline
                      </v-icon>
                      <p class="ml-2">{{ review.review_comments.length }}</p>
                    </div>
                  </div>
                </div>
                <p class="mt-2">{{ review.content }}</p>
              </v-card>
            </div>

            <div
              v-else-if="index % 6 === 4"
              data-aos="fade-up-left"
              data-aos-easing="linear"
              data-aos-duration="1000"
              class="right-box align-start"
            >
              <p
                :class="{'hidden1': index % 6 === 1, 'hidden2': index % 6 === 3, 'hidden3': index % 6 === 5, 'timeline-date': true}"
              >
                ● {{ review.created_at.slice(0, 10) }}
              </p>
              <img
                class="time-line-movie-poster movie-card-poster ml-4"
                :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${review.movie.poster_path}`"
              >
              <v-card class="timeline-card movie-card-poster ml-5">
                <div class="flex-bt">
                  <p class="d-d time-line-review-title">{{ review.title }}</p>
                  
                  <div class="flex-l">
                    <div class="flex-l">
                      <v-icon small class="site-color-text">
                        mdi-thumb-up-outline
                      </v-icon>
                      <p class="ml-2">{{ review.users_like.length }}</p>
                    </div>
                    <div class="flex-l">
                      <v-icon small class="site-color-text ml-2">
                        mdi-comment-processing-outline
                      </v-icon>
                      <p class="ml-2">{{ review.review_comments.length }}</p>
                    </div>
                  </div>
                </div>
                <p class="mt-2">{{ review.content }}</p>
              </v-card>
            </div>
            <div if-else style="width: 100%; height: 100px;"></div>
          </div>
        </v-col>
      </v-row>
      <div style="height: 50px; width: 100%"></div>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'
import _ from 'lodash'
import AOS from 'aos'
import 'aos/dist/aos.css'

AOS.init();

export default {
  name: 'TimeLine',
  data () {
    return {
      thisUsername: this.$route.params.username,
    }
  },
  methods: {
    moveProfile () {
      this.$router.push({ name: 'UserProfile', params: { username: this.$route.params.username } })
    }
  },
  computed: {
    ...mapState([
      'personData',
    ])
  },
  filters: {
    truncate (overview) {
      return _.truncate( overview, {
        'length': 10,
        'separator': '-'
      })
    },
  },
  created () {
    this.$store.dispatch('getUser', this.thisUsername)
  },
  watch: {
    $route () {
      this.thisUsername = this.$route.params.username
      this.$store.dispatch('getUser', this.thisUsername)
    }
  },
}
</script>

<style>
.timeline-page {
  width: 80%;
  padding-top: 0;
}

.timeline-part {
  width: 100%;
}

.left-box {
  display: flex;
  justify-content: right;
}

.right-box {
  display: flex;
  justify-content: left;
}

.timeline-card {
  padding: 10px;
  background: rgb(248, 248, 248);
  min-width: 300px;
  max-width: 450px;
  max-height: 150px;
}

.time-line-movie-poster {
  width: 150px;
  border-radius: 5px;
}

.timeline-title {
  font-size: 25px;
  font-weight: bold;
  position: relative;
  z-index: 20001;
}

.flex-c {
  display: flex;
  justify-content: center;
}

.center-line {
  position: absolute;
  z-index: 20000;
  left: 49.3%;
  width: 2px;
  height: 100%;
  background: black;
  margin: 0 auto;
}

.time-line-review-title {
  font-weight: bold;
}

.timeline-date {
  display: flex;
  position: relative;
  font-weight: bold;
  z-index: 20001;
}

.hidden1 {
  visibility: hidden;
}
.hidden2 {
  visibility: hidden;
}
.hidden3 {
  visibility: hidden;
}

.timeline-back {
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
}

.unvisibility {
  position: absolute;
  /* visibility: hidden; */
  top: -1040px;
  left: 0;
  z-index: 10;
}

.unmute {
  color: white;
  position: absolute;
  top: 8px;
  left: 230px;
  z-index: 100;
}
</style>