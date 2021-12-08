<template>
  <v-col
    cols="2"
    v-if="movie.poster_path"
  >
    <a class="movie-card" @click.prevent="moveMovieDetail"><div>
      <v-hover v-slot:default="{ hover }">
        <v-img
          :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${movie.poster_path}`"
          class="rounded movie-card-poster"
        >
          <v-expand-transition>
            <div
              v-if="hover"
              class="d-flex transition-fast-in-fast-out v-card--reveal white--text overflow-auto"
              style="height: 100%;"
            >
              <p class="movie-card-title">{{ movie.title }}</p>
            </div>
          </v-expand-transition>
        </v-img>
      </v-hover>
      <p class="overflow-x-hidden movie-card-title">{{ movie.title }}</p>
      <p class="movie-card-description">{{ movie.release_date }} · <i class="fas fa-star fa-xs"></i> {{ movie.vote_average }}</p>
    </div></a>
  </v-col>
</template>

<script>
// import axios from 'axios'
// import InfiniteLoading from "vue-infinite-loading"

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  methods: {
    moveMovieDetail () {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.movie.id }})
    }
  }
}
</script>

<style>
.movie-card {
  text-decoration: none;
  color: black !important;
}

.movie-card-poster {
  box-shadow: 0px 4px 2px -2px rgb(0 0 0 / 20%), 0px 3px 3px 0px rgb(0 0 0 / 14%), 0px 2px 6px 0px rgb(0 0 0 / 12%);
}

.movie-card-title {
  margin-top: 10px;
  margin-bottom: 0 !important;
  font-size: 16px;
  font-weight: bold;
}

.movie-card-description {
  font-size: 13px;
  color: #707070;
}
</style>