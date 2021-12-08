<template>
  <v-sheet
  class="mx-auto"
  max-width="80%"
  >
    <v-row>
      <p class="section-title2">Top Rate</p>
    </v-row>

    <v-slide-group
      v-if="topRate"
      multiple
      show-arrows
    >
      <v-slide-item
        v-for="movie in topRate"
        :key="movie.title"
      >
        <v-hover v-slot:default="{ hover }">
          <a @click.prevent="moveMovieDetail(movie.id)">
            <v-img
              :aspect-ratio="16/9"
              :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${movie.poster_path}`"
              class="ma-4 rounded movie-card-poster"
              height="286"
              width="200"
            >
              <v-expand-transition>
                <div
                  v-if="hover"
                  class="d-flex transition-fast-in-fast-out v-card--reveal white--text overflow-auto"
                  style="height: 100%;"
                >
                  <div>
                    <p class="movie-card-title" style="width: 100%">{{ movie.title }}</p>
                    <p class="d-vote-average"><i class="fas fa-star fa-sm"></i> {{ movie.vote_average }}</p>
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
          </a>
        </v-hover>
      </v-slide-item>
    </v-slide-group>
  </v-sheet>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'TopRate',
  methods: {
    moveMovieDetail (id) {
      this.$router.push({ name: 'MovieDetail', params: { movieId: id} })
    },
  },
  computed: {
    ...mapState([
      'topRate',
    ])
  }
}
</script>

<style>
.section-title2 {
  font-size: 22px;
  font-weight: bold;
  margin-left: 62px;
  margin-bottom: 0 !important;
}
</style>