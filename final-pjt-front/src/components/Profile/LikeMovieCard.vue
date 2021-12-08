<template>
  <v-col
    cols="2"
  >
    <a class="movie-card" @click.prevent="moveMovieDetail"><div>
      <v-hover v-slot:default="{ hover }">
        <v-img
          :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${like_movie.poster_path}`"
          class="rounded movie-card-poster"
        >
          <v-expand-transition>
            <div
              v-if="hover"
              class="d-flex transition-fast-in-fast-out v-card--reveal white--text overflow-auto"
              style="height: 100%;"
            >
              <div>
                <p class="movie-card-title">{{ like_movie.title }}</p>
                <p class="movie-card-title"><i class="fas fa-star fa-xs"></i> {{ like_movie.vote_average }}</p>
              </div>
            </div>
          </v-expand-transition>
        </v-img>
      </v-hover>
      <p class="overflow-x-hidden movie-card-title">{{ like_movie.title }}</p>
      <p class="movie-card-description">{{ like_movie.release_date }} · <i class="fas fa-star fa-xs"></i> {{ like_movie.vote_average }}</p>
    </div></a>
  </v-col>
</template>

<script>
export default {
  name: 'LikeMovieCard',
  props: {
    like_movie: Object,
  },
  methods: {
    moveMovieDetail () {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.like_movie.id }})
    }
  }
}
</script>

<style>

</style>