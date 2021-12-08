<template>
  <v-sheet
  class="mx-auto main-content-item"
  max-width="80%"
  >
    <v-row class="flex-l">
      <p class="section-title">MOVIE Trending</p>
      <v-btn
        v-if="isDay"
        class="mx-2 movie-genre-btns site_color white--text"
        @click="dayTrending"
        rounded
        depressed
        height="24"
      >
        DAY
      </v-btn>
      <v-btn
        v-else
        class="mx-2 movie-genre-btns"
        @click="dayTrending"
        rounded
        depressed
        height="24"
      >
        DAY
      </v-btn>

      <v-btn
        v-if="isDay"
        class="mx-2 movie-genre-btns"
        @click="weekTrending"
        rounded
        depressed
        height="24"
      >
        WEEK
      </v-btn>
      <v-btn
        v-else
        class="mx-2 movie-genre-btns site_color white--text"
        @click="weekTrending"
        rounded
        depressed
        height="24"
      >
        WEEK
      </v-btn>
    </v-row>

    <v-slide-group
      v-if="trending"
      class="mt-3 top-rate-slide"
      multiple
      show-arrows
    >
      <v-slide-item
        v-for="movie in trending"
        :key="movie.id"
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
  name: 'Trending',
  data () {
    return {
      isDay: true,
    }
  },
  methods: {
    moveMovieDetail (id) {
      this.$router.push({ name: 'MovieDetail', params: { movieId: id} })
    },
    dayTrending () {
      this.$store.dispatch('getDayTrending')
      if (!this.isDay) {
        this.isDay = true
      }
    },
    weekTrending () {
      this.$store.dispatch('getWeekTrending')
      if (this.isDay) {
        this.isDay = false
      }
    }
  },
  computed: {
    ...mapState([
      'trending',
    ])
  },
}
</script>

<style>
.v-card--reveal {
    text-align: center;
    align-items: center;
    bottom: 0;
    justify-content: center;
    /* opacity: .7; */
    position: absolute;
    width: 100%;
    background: rgb(0, 0, 0, 0.7);
}

.section-title {
  font-size: 22px;
  font-weight: bold;
  color: white;
  margin-left: 62px;
  margin-bottom: 0 !important;
}

.main-content-item {
  background: none !important;
}

.theme--light.v-icon {
  color: #818181 !important;
}
</style>