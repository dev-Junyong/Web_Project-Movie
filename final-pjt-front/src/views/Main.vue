<template>
  <div>
    <div class="main-video-cover"></div>
    <div class="main-video-cover-white"></div>
    <iframe
      v-if="videoId"
      class="video-player main-video"
      type="text/html"
      :src="`https://www.youtube.com/embed/${videoId.key}?autoplay=1&mute=1&loop=1&playlist=${videoId.key}`"
      frameborder="0"
      allowfullscreen
      width="100%"
      height="1080px"
    >
    </iframe>

    <div v-if="trending" class="main-movie">
      <p class="main-movie-title">{{ trending[0].title }}</p>
      <p class="main-movie-overview d-d">{{ trending[0].overview | truncate }}</p>
    </div>

    <div class="main-contents">
      <trending id="trending"></trending>
      <top-rate id="top-rate"></top-rate>
    </div>

    <v-footer padless>
      <v-container>
        <div class="footer-part">
          <v-row>
            <v-col
              cols="8"
            >
            <p class="d-d footer-text">고객센터 | front-man@456.com, 02-456-456</p>
            <p class="d-d footer-text">광고 문의 | ad@456.com</p>
            <p class="d-d footer-text">제휴 및 대외 협력 | https://456.team/contact</p>
            </v-col>
            <v-col
              class="text-right"
              cols="4"
            >
              <img src="@/assets/logo@3x.png" class="footer-logo">
              <p class="d-d footer-text">개발 및 디자인 - 박준용 | 이수환</p>
            </v-col>
          </v-row>
        </div>
      </v-container>
    </v-footer>
  </div>
</template>

<script>
import Trending from '../components/Main/Trending'
import TopRate from '../components/Main/TopRate'
import { mapState } from 'vuex'
import _ from 'lodash'

export default {
  name: 'Main',
  components: {
    Trending,
    TopRate
  },
  computed: {
    ...mapState([
      'trending',
      'videoId',
    ])
  },
  filters: {
    truncate (overview) {
      return _.truncate( overview, {
        'length': 200,
        'separator': ' '
      })
    },
  },
  created () {
    this.$store.dispatch('getDayTrending')
    this.$store.dispatch('getTopRate')
  },
  watch: {
    trending () {
      this.$store.dispatch('getVideoId', this.trending[0].id)
    }
  }
}
</script>

<style>
#top-rate {
  margin-top: 50px;
}

.main-video-cover {
  position: absolute !important;
  top: -130px !important;
  background: white;
  opacity: 0%;
  width: 100%;
  height: 1080px;
  z-index: 20000;
}

.main-video-cover-white {
  position: absolute !important;
  top: 800px !important;
  background: white;
  width: 100%;
  height: 200px;
  z-index: 20001;
}

.main-video {
  position: absolute !important;
  top: -130px !important;
  filter: brightness(70%);
  z-index: 0;
}

.main-movie {
  /* background: rgb(0, 0, 0, 0.1); */
  position: relative;
  border-radius: 5px;
  margin-top: 200px;
  margin-left: 15%;
  padding: 15px;
  width: 430px;
  z-index: 20001;
}

.main-movie-title {
  font-size: 35px;
  font-weight: bold;
  color: white;
}

.main-movie-overview {
  width: 400px;
  font-size: 15px;
  color: rgb(226, 226, 226);
}

.main-contents {
  margin-top: 100px;
  position: relative;
  z-index: 20001;
}
</style>
