<template>
  <div>
    <v-container class="movie-page">
      <h2>Movie</h2>
      <movie-genre></movie-genre>
      <div v-if="isSelect" class="text-center mt-16">
        <v-progress-linear
          indeterminate
          rounded
          height="6"
          color="pink lighten-1"
        ></v-progress-linear>
      </div>
      <v-row v-else class="movie-cards">
          <movie-card 
            v-for="movie in movieList" 
            :key="movie.id"
            :movie="movie"
          ></movie-card>
      </v-row>
    </v-container>

    <infinite-loading @infinite="infiniteHandler" spinner="waveDots"></infinite-loading>
  </div>
</template>

<script>
import MovieCard from '../components/Movie/MovieCard'
import MovieGenre from '../components/Movie/MovieGenre'
import { mapState } from 'vuex'
import axios from 'axios'
import InfiniteLoading from "vue-infinite-loading"

const SERVER_URL = 'https://pjt456.herokuapp.com'

export default {
  name: 'Movie',
  components: {
    MovieCard,
    MovieGenre,
    InfiniteLoading,
  },
  data () {
    return {
      movies: [],
      loadNum: 2,
    }
  },
  methods: {
    go_read (idx) {
      this.$router.push('/Movie/'+idx)
    },
    infiniteHandler($state) {
      axios.get(`${SERVER_URL}/movies/movie_list/?page=${this.loadNum}`, {
      })
       .then(res => {
          setTimeout(() => {
            const data = res.data
            $state.loaded()
            for (let i = 0; i < 18; i++){
              this.$store.commit('GET_MORE_MOVIES', data[i])
              this.loadNum++
              if (i == 18) {
                $state.complete()
              }
            }
           }, 1000)
       })
       .catch(() => {
         alert('에러')
         localStorage.clear()
         this.$router.push('/')
       })
    }
  },
  computed: {
    ...mapState([
      'movieList',
      'genreList',
      'isSelect',
    ])
  },
  created () {
    this.$store.dispatch('getMovies')
    this.$store.dispatch('getGenres')
  },
}
</script>

<style>
.movie-page {
  width: 75%;
  padding-top: 0;
}

.movie-cards {
  margin-top: 20px;
}
</style>