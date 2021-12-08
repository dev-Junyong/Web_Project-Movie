<template>
  <v-container class="movie-detail-page">
    <v-parallax
      v-if="backdropPath"
      class="barcdrop_path"
      :src="`https://www.themoviedb.org/t/p/original${backdropPath}`"
    ></v-parallax>

    <div v-if="nowMovie">
      <v-row class="movie-detail-main">
        <v-col
          cols="2"
        >
          <img
            class="movie-detail-poster movie-card-poster"
            :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${nowMovie.poster_path}`"
          >
        </v-col>

        <v-col
          cols="10"
        >
          <div class="movie-detail-space"></div>

          <div class="movie-title-description ml-3">
            <p class="d-title">{{ nowMovie.title }}</p>
            <p></p>
            <span class="genre-btns">
              <v-btn
                class="genre-btn-item white--text"
                rounded
                height="24"
                v-for="genre in nowMovie.genres"
                :key="genre.id"
              >{{ genre.name }}</v-btn>
            </span>
          </div>

          <p class="movie-simple-description ml-3">
            <span class="d-vote-average">
            <i class="fas fa-star fa-sm"></i> {{ nowMovie.vote_average * 2 }}
            </span>
            <span class="d-release-date">
              · {{ nowMovie.release_date }}
            </span>
          </p>

          <v-rating
            readonly
            v-model="nowMovie.vote_average"
            color="yellow darken-3"
            background-color="grey darken-1"
            empty-icon="$ratingFull"
            half-increments
            large
          ></v-rating>

          <div class="ml-2" v-if="loginUser">
            <span v-if="nowMovieLikes.includes(loginUser.username)">
              <v-hover v-slot:default="{ hover }">
                <button class="text-btn" @click="likeMovie">
                  <v-icon v-if="hover" large style="color: red;">
                    mdi-bookmark-remove-outline
                  </v-icon>
                  <v-icon v-else large class="site-color-text">
                    mdi-bookmark
                  </v-icon>
                </button>
              </v-hover>
            </span>

            <span v-else>
              <v-hover v-slot:default="{ hover }">
                <button class="text-btn" @click="likeMovie">
                  <v-icon v-if="hover" large class="site-color-text">
                    mdi-bookmark-plus
                  </v-icon>
                  <v-icon v-else large>
                    mdi-bookmark-outline
                  </v-icon>
                </button>
              </v-hover>
            </span>

            {{ nowMovie.user_set.length }}

            <v-icon large class="site-color-text comment-count">
              mdi-comment-processing
            </v-icon>
            {{ nowMovie.movie_reviews.length }}
          </div>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="4">
          <div>
            <v-card class="mx-auto movie-detail-description">
              <span
                v-for="crew in nowMovieCrew"
                :key="crew.credit_id"
              >
                <div
                  class="d-group"
                  v-if="crew.job === 'Director'"
                >
                  <p class="d-d">감독</p>
                  <p class="d-d-i">{{ crew.name }}</p>
                </div>
              </span>
              <hr class="d-line">

              <div class="d-group">
                <p class="d-d">개봉일</p>
                <p class="d-d-i">{{ nowMovie.release_date }}</p>
              </div>
              <hr class="d-line">

              <div class="d-group">
                <p class="d-d">장르</p>
                <span class="d-genres">
                  <p
                  class="d-genre d-d-i"
                  v-for="genre in nowMovie.genres"
                  :key="genre.name"
                  >{{ genre.name }}</p>
                </span>
              </div>
              <hr class="d-line">

              <p class="d-d-i">내용</p>
              <hr class="d-line">
              <p class="overview d-d">{{ nowMovie.overview }}</p>
            </v-card>

            <v-card class="mx-auto movie-detail-review">
              <p class="d-d">배우</p>
              <hr class="d-line">

              <v-slide-group
                multiple
                show-arrows
              >
                <v-slide-item
                  v-for="cast in nowMovieCast"
                  :key="cast.id"
                >
                  <v-hover v-slot:default="{ hover }">
                    <a v-if="cast.profile_path" @click.prevent>
                      <v-img
                        :aspect-ratio="16/9"
                        :src="`https://image.tmdb.org/t/p/w500${cast.profile_path}`"
                        class="ma-4 rounded movie-card-poster"
                        width="138"
                        height="200"
                      >
                        <v-expand-transition>
                          <div
                            v-if="hover"
                            class="d-flex transition-fast-in-fast-out black darken-2 v-card--reveal white--text overflow-auto"
                            style="height: 100%;"
                          >
                            <div>
                              <p class="cast-name movie-card-title" style="width: 100%">{{ cast.character }}</p>
                              <br>
                              <p class="cast-name">{{ cast.name }}</p>
                            </div>
                          </div>
                        </v-expand-transition>
                        <v-row
                          class="fill-height"
                          align="center"
                          justify="center"
                        >
                        </v-row>
                      </v-img>
                      <p class="d-d cast-name-d">{{ cast.name }}</p>
                    </a>
                  </v-hover>
                </v-slide-item>
              </v-slide-group>
            </v-card>

            <v-card class="mx-auto movie-detail-review">
              <div class="flex">
                <button class="text-btn" @click="createReview">
                  리뷰작성
                  <v-icon>
                    mdi-chevron-double-right
                  </v-icon>
                </button>
              </div>

              <div
                class="m-d-review-detail"
                v-for="review in nowMovie.movie_reviews"
                :key="review.id"
              >
                <div class="each-review">
                  <div>
                    <div class="flex-bt">
                      <div class="flex-l">
                        <p class="m-d-review-title d-d ml-2 r-simple-item">{{ review.title }}</p>
                        <v-icon class="r-simple-item" small>
                          mdi-thumb-up
                        </v-icon>
                        <p class="d-d r-simple-item">{{ review.users_like.length }}</p>
                      </div>
                      <div class="flex">
                        <p class="mr-3 d-d m-d-review-author">작성자</p>
                        <p class="d-d m-d-review-author-name">{{ review.author.username }}</p>
                      </div>
                    </div>
                    <div class="flex-l">
                      <v-rating
                        readonly
                        v-model="review.rank"
                        color="yellow darken-3"
                        background-color="grey darken-1"
                        empty-icon="$ratingFull"
                        half-increments
                        size="18"
                        width="100px"
                      ></v-rating>
                      <p class="d-d">{{ review.rank * 2 }}</p>
                    </div>

                    <div class="flex">
                      <a @click="moveReviewDetail(review)">상세보기</a>
                    </div>
                  </div>
                </div>
              </div>
            </v-card>
          </div>
        </v-col>

        <v-col cols="8">
          <div v-if="videoId" class="player">
            <iframe
              class="video-player movie-card-poster"
              type="text/html"
              :src="`https://www.youtube.com/embed/${videoId.key}`"
              frameborder="0"
              allowfullscreen
              width="100%"
              height="555px"
            >
            </iframe>
          </div>

          <v-card v-if="recommendMovies" class="mx-auto recommends">
            <p class="recommends-title">추천 영화 목록</p>
            <v-row
              class="recommend-movies"
            >
              <v-col
                cols="3"
                v-for="movie in recommendMovies" 
                :key="movie.id"
              >
                <a class="movie-card" @click.prevent="moveMovieDetail(movie.id)">
                  <v-img
                    :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${movie.poster_path}`"
                    class="rounded movie-card-poster"
                  >
                  </v-img>
                  <h5>{{ movie.title }}</h5>
                </a>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </div>

    <div v-else>
      <h2>※ 해당 영화가 존재하지 않습니다 ※</h2>
    </div>

  </v-container>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'MovieDetail',
  data () {
    return {
      movieId: this.$route.params.movieId
    }
  },
  methods: {
    createReview () {
      this.$router.push({ name: 'ReviewCreate', params: { movieId: this.movieId} })
    },
    moveReviewDetail (review) {
      this.$store.dispatch('getReviewDetail', review.id)
      this.$router.push({ name: 'ReviewDetail', params: { reviewId: review.id } })
    },
    likeMovie () {
      this.$store.dispatch('likeMovie', this.movieId)
    },
    moveMovieDetail (id) {
      this.$router.push({ name: 'MovieDetail', params: { movieId: id }})
    }
  },
  computed: {
    ...mapState([
      'nowMovie',
      'nowMovieCrew',
      'nowMovieCast',
      'nowMovieLikes',
      'loginUser',
      'backdropPath',
      'videoId',
      'recommendMovies',
    ]),
  },
  created () {
    this.$store.dispatch('getMovieDetail', this.movieId)
    this.$store.dispatch('getBackdropPath', this.movieId)
    this.$store.dispatch('getMovieCredits', this.movieId)
    this.$store.dispatch('getVideoId', this.movieId)
  },
  watch: {
    $route () {
      this.$router.go()
    }
  }
}
</script>

<style>
.movie-detail-page {
  width: 80%;
  padding-top: 0;
}

.barcdrop_path {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    height: 250px !important;
    width: 100%;
    z-index: 0;
}

.movie-detail-main {
  padding-top: 50px;
  position: relative;
  z-index: 20001 !important;
}

.movie-detail-poster {
  width: 100%;
  border-radius: 5px;
}

.movie-detail-space {
  height: 40%;
}

.genre-btns {
  margin-left: 10px;
}

.genre-btn-item {
  margin: 0 10px;
  background: linear-gradient(to bottom right, #F83D3D, #B600EB);
  font-weight: bold;
}

.movie-title-description {
  display: flex;
  align-items: center;
}

.d-title {
  font-size: 30px;
  font-weight: bold;
  margin-bottom: 0 !important;
}

.movie-simple-description {
  margin-bottom: 0 !important;
}

.d-vote-average {
  font-weight: bold;
}

.d-release-date {
  color: #707070;
}

.movie-detail-description {
  padding: 20px;
  border-radius: 5px;
}

.theme--light.v-card {
    background-color: rgb(248, 248, 248) !important;
}

.d-genres {
  display: flex;
}

.d-genre {
  margin-left: 10px;
}

.movie-detail-review {
  margin-top: 20px;
  padding: 20px;
}

.overview {
  white-space: pre-line
}

.d-group {
  display: flex;
  justify-content: space-between;
}

.d-d {
  margin-bottom: 0 !important;
}

.d-d-i {
  margin-bottom: 0 !important;
  font-size: 16px;
  font-weight: bold;
}

.d-line {
  margin-bottom: 15px;
}

.text-btn {
  background: none;
  font-weight: bold;
}

.m-d-review-detail {
  width: 100%;
}

.each-review {
  width: 100%;
  margin-top: 15px;
  padding: 15px 10px 0 10px;
  border-top: 1px solid rgb(100, 100, 100);
}

.m-d-review-title {
  font-size: 16px;
  font-weight: bold;
}

.m-d-review-author {
  font-size: 12px;
}

.m-d-review-author-name {
  font-size: 15px;
  font-weight: bold;
}

.flex {
  display: flex;
  justify-content: right;
  align-items: baseline;
}

.flex-l {
  display: flex;
  align-items: center;
}

.flex-bt {
  display: flex;
  justify-content: space-between;
}

.r-simple-item {
  margin-right: 5px;
}

.site-color-text {
  background: linear-gradient(to bottom right, #F83D3D, #B600EB);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.recommends {
  padding: 20px;
}

.recommends-title {
  font-size: 17px;
  font-weight: bold;
}

.comment-count {
  margin-left: 10px;
}

.cast-name {
  font-size: 12px;
  font-weight: bold;
}

.cast-name-d {
  color: black !important;
  padding: 0 16px;
}
</style>