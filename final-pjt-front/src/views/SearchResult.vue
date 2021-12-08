<template>
  <div>
    <v-container v-if="searchResult" class="movie-page">
      <h2>Result</h2>
      <h4 v-if="searchResult.length==0">검색결과가 없습니다</h4>
      <v-row class="movie-cards">
          <movie-card
            v-for="movie in searchResult"
            :key="movie.id"
            :movie="movie"
          ></movie-card>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import MovieCard from '../components/Movie/MovieCard'
import { mapState } from 'vuex'

export default {
  name: 'SearchResult',
  components: {
    MovieCard,
  },
  computed: {
    ...mapState([
      'searchResult',
    ])
  },
  created () {
    this.$store.dispatch('searchKeyword', this.$route.params.keyword)
  }
}
</script>

<style>

</style>