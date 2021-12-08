<template>
  <v-container class="review-create-page">
    <v-parallax
      class="barcdrop_path"
      :src="`https://www.themoviedb.org/t/p/original${backdropPath}`"
    ></v-parallax>
    <v-row class="review-create-main">
      <v-col
        cols="10"
      >
        <div class="review-create-space"></div>
          <v-card class="mx-auto movie-create-review">
            <div class="flex-bt">
              <div class="flex-l">
                <p class="create-title">{{ nowMovie.title }}</p>

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
              v-model="context.title"
            >
            </v-text-field>

            <v-textarea
              outlined
              name="input-7-4"
              label="Content"
              placeholder="Input your review"
              v-model="context.content"
            ></v-textarea>


            <div class="review-create-btn">
              <v-btn 
                @click="createReview"
                class="review-submit-btn"
              >작성</v-btn>
            </div>
          </v-card>
      </v-col>

      <v-col cols="2">
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
  name: 'ReviewCreate',
  data () {
    return {
      context: {
        rank: 0,
        title: null,
        content: null,
        movieId: this.$route.params.movieId,
      },
    }
  },
  methods: {
    createReview () {
      this.$store.dispatch('createReview', this.context)
    },
    toMovieDetail () {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.nowMovie.id}})
    }
  },
  computed: {
    ...mapState([
      'nowMovie',
      'isCreateReview',
      'backdropPath',
    ])
  },
  created () {
    if (!this.nowMovie) {
      alert('영화를 선택하세요')
      this.$router.push({ name: 'Movie' })
    }
  },
  watch: {
    isCreateReview() {
      console.log('!!!!!!!!!!!')
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.$route.params.movieId } })
      
    }
  }
}
</script>

<style scoped>
.review-create-page {
  width: 75%;
  padding-top: 0;
}

.review-submit-btn {
  background: linear-gradient(to bottom right, #F83D3D, #B600EB);
  color: white !important;
  font-weight: bold;
}

.review-create-main {
  padding-top: 40px;
  position: relative;
  z-index: 20001 !important;
}

.review-create-space {
  height: 30%;
}

.movie-create-review {
    margin-top: 20px;
    padding: 20px;
}

.flex-bt {
    display: flex;
}

.create-title {
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 0 !important;
}

.review-create-movie-text {
  margin-top: 10px;
  text-decoration: none;
  color: black !important;
  font-size: 16px;
  font-weight: bold;
}

.review-create-btn {
  display: flex;
  justify-content: right;
}

</style>