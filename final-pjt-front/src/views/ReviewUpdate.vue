<template>
  <v-container class="review-update-page">
    <v-parallax
      class="barcdrop_path"
      :src="`https://www.themoviedb.org/t/p/original${backdropPath}`"
    ></v-parallax>
    <v-row class="review-update-main">
      <v-col
        cols="10"
      >
        <div class="review-update-space"></div>
          <v-card class="mx-auto movie-update-review">
            <div class="flex-bt">
              <div class="flex-l">
                <p class="update-title">{{ nowMovie.title }}</p>

                <v-rating
                  v-model="context.rank"
                  color="yellow darken-3"
                  background-color="grey darken-1"
                  empty-icon="$ratingFull"
                  half-increments
                  hover
                  large
                ></v-rating>
                <p class="d-d mr-3">{{ context.rank * 2 }}</p>
              </div>
            </div>

              <v-text-field
                placeholder="Intput your title"
                :value="nowReview.title"
                v-model="context.title"
              >
              </v-text-field>

              <v-textarea
                outlined
                name="input-7-4"
                label="Content"
                placeholder="Input your review"
                :value="nowReview.content"
                v-model="context.content"
              ></v-textarea>

            <div class="review-update-btn">
              <v-btn 
                @click="updateReview"
                class="review-submit-btn"
              >수정</v-btn>
            </div>
          </v-card>
      </v-col>

      <v-col 
        cols="2"
      >
        <a @click.prevent="toMovieDetail">
          <img
            class="movie-detail-poster movie-card-poster"
            :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${nowMovie.poster_path}`"
          >
        </a>
        <p class="review-create-movie-text">제목 - {{ nowMovie.title }}</p>
        <p class="review-create-movie-text">개봉일 - {{ nowMovie.release_date }}</p>
        <p class="review-create-movie-text">평점 - {{ nowMovie.vote_average }}</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'ReviewUpdate',
  data () {
    return {
      context: {
        title: null,
        content: null,
        rank: null,
        reviewId: this.$route.params.reviewId,
      }
    }
  },
  methods: {
    updateReview () {
      this.$store.dispatch('updateReview', this.context)
    },
    toMovieDetail () {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.nowMovie.id}})
    }
  },
  computed: {
    ...mapState([
      'nowReview',
      'nowMovie',
      'isUpdateReview',
      'backdropPath',
    ])
  },
  created () {
    this.$store.dispatch('getReviewDetail', this.nowReview.id)
    this.context.title = this.nowReview.title
    this.context.content = this.nowReview.content
    this.context.rank = this.nowReview.rank
  },
  watch: {
    isUpdateReview () {
      this.$router.push({ name: 'ReviewDetail', params: { reviewId: this.nowReview.id } })
    }
  }
}
</script>

<style>
.review-update-page {
  width: 75%;
  padding-top: 0;
}

.review-update-main {
  padding-top: 40px;
  position: relative;
  z-index: 20001 !important;
}

.review-update-space {
  height: 30%;
}

.movie-update-review {
    margin-top: 20px;
    padding: 20px;
}

.update-title {
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 0 !important;
}

.review-update-btn {
  display: flex;
  justify-content: right;
}

.review-submit-btn {
  background: linear-gradient(to bottom right, #F83D3D, #B600EB);
  color: white !important;
  font-weight: bold;
}

.review-create-movie-text {
  margin-top: 10px;
  text-decoration: none;
  color: black !important;
  font-size: 16px;
  font-weight: bold;
}

</style>