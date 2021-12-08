<template>
  <v-container class="review-detail-page">
    <v-parallax
      v-if="backdropPath"
      class="barcdrop_path"
      :src="`https://www.themoviedb.org/t/p/original${backdropPath}`"
    ></v-parallax>

    <div>
      <v-row class="review-detail-main">
        <v-col cols="10">
          <div class="review-detail-space"></div>

          <v-card v-if="nowReview" class="mx-auto movie-detail-review">
            <div class="flex-bt">
              <div class="flex-l">
                <p class="d-title">{{ nowReview.title }}</p>

                <v-rating
                  readonly
                  v-model="nowReview.rank"
                  color="yellow darken-3"
                  background-color="grey darken-1"
                  empty-icon="$ratingFull"
                  half-increments
                  large
                ></v-rating>
                <p class="d-d mr-3">{{ nowReview.rank * 2 }}</p>

                <div class="flex-l">
                  <span v-if="loginUser">
                    <span v-if="nowReview.users_like.includes(loginUser.id)">
                      <v-hover v-slot:default="{ hover }">
                        <button class="text-btn" @click="likeReview">
                          <v-icon v-if="hover" style="color: red;">
                            mdi-thumb-down-outline
                          </v-icon>
                          <v-icon v-else class="site-color-text">
                            mdi-thumb-up
                          </v-icon>
                        </button>
                      </v-hover>
                    </span>

                    <span v-else>
                      <v-hover v-slot:default="{ hover }">
                        <button class="text-btn" @click="likeReview">
                          <v-icon v-if="hover" class="site-color-text">
                            mdi-thumb-up
                          </v-icon>
                          <v-icon v-else>
                            mdi-thumb-up-outline
                          </v-icon>
                        </button>
                      </v-hover>
                    </span>
                  </span>

                  <span v-else>
                    <button>
                      <v-icon class="site-color-text">
                        mdi-thumb-up
                      </v-icon>
                    </button>
                  </span>
                  <p class="d-d ml-2">{{ nowReview.users_like.length }}</p>
                </div>
              </div>

              <div v-if="nowReview" class="flex-l">
                <p class="mr-2 m-d-review-author">작성자</p>
                <a class="d-d movie-card review-detail-author" @click.prevent="moveProfile">
                  <p>{{ nowReview.author.username }}</p>
                </a>
              </div>
            </div>

            <a v-if="nowReview" class="d-d movie-card" @click.prevent="toMovieDetail">Movie title: {{ nowReview.movie.title }}</a>
            <hr>

            <p v-if="nowReview" class="review-content">{{ nowReview.content }}</p>

            <div v-if="nowComments" class="flex-bt">
              <div class="flex-l">
                <v-icon class="site-color-text">
                  mdi-comment-processing
                </v-icon>
                <p class="d-d">{{ nowComments.length }}</p>
              </div>
              <div class="flex" v-if="loginUser">
                <div v-if="nowReview.author.username == loginUser.username">
                  <v-hover v-slot:default="{ hover }">
                    <button class="text-btn" @click="moveReviewUpdate">
                      <v-icon v-if="hover" large class="site-color-text">
                        mdi-file-document-edit
                      </v-icon>
                      <v-icon v-else large>
                        mdi-pencil-outline
                      </v-icon>
                    </button>
                  </v-hover>
                  <v-hover v-slot:default="{ hover }">
                    <button class="text-btn" @click="reviewDelete">
                      <v-icon v-if="hover" large class="site-color-text">
                        mdi-delete-empty
                      </v-icon>
                      <v-icon v-else large>
                        mdi-delete-outline
                      </v-icon>
                    </button>
                  </v-hover>
                </div>
              </div>
            </div>
          </v-card>

          <v-card class="mx-auto comment-area">
            <review-comment v-if="nowReview" :review="nowReview"></review-comment>
            <comment-detail
              v-for="comment in nowComments"
              :key="comment.id"
              :comment="comment"
            >
            </comment-detail>
          </v-card>
        </v-col>

        <v-col cols="2">
          <a v-if="nowMovie" @click.prevent="toMovieDetail">
            <img
              class="movie-detail-poster movie-card-poster"
              :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${nowMovie.poster_path}`"
            >
          </a>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'
import ReviewComment from '../components/Community/ReviewComment'
import CommentDetail from '../components/Community/CommentDetail'

export default {
  name: 'ReviewDetail',
  components: { 
    ReviewComment,
    CommentDetail,
  },
  data () {
    return {
      reviewId: this.$route.params.reviewId,
    }
  },
  methods: {
    moveReviewUpdate () {
      this.$router.push({ name: 'ReviewUpdate', params: { reviewId: this.reviewId } })
    },
    reviewDelete () {
      this.$store.dispatch('reviewDelete', this.reviewId)
    },
    moveProfile () {
      this.$router.push({ name: 'UserProfile', params: { username: this.nowReview.author.username } })
    },
    likeReview () {
      this.$store.dispatch('likeReview', this.reviewId)
    },
    toMovieDetail () {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.nowMovie.id}})
    }
  },
  computed: {
    ...mapState([
      'nowReview',
      'nowMovie',
      'backdropPath',
      'isDelete',
      'nowComments',
      'loginUser',
    ])
  },
  created () {
    this.reviewId = this.$route.params.reviewId
    this.$store.dispatch('getReviewDetail', this.reviewId)
    this.$store.dispatch('getComments', this.reviewId)
  },
  watch: {
    isDelete () {
      this.$router.push({ name: 'Movie' })
    },
  }
}
</script>

<style>
.review-detail-page {
  width: 75%;
  padding-top: 0;
}

.review-detail-space {
  height: 130px;
}

.review-detail-main {
  padding-top: 40px;
  position: relative;
  z-index: 20001 !important;
}

.review-detail-author {
  font-size: 16px;
  font-weight: bold;
}

.review-content {
  margin-top: 10px;
  font-size: 16px;
  white-space: pre-line;
}

.comment-area {
  margin-top: 20px;
  padding: 20px;
}
</style>