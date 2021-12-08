<template>
  <v-col
    cols="4"
  >
    <a class="movie-card" @click.prevent="moveReviewDetail"><div>
      <v-hover v-slot:default="{ hover }">
        <v-img
          :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${review.movie.poster_path}`"
          class="rounded movie-card-poster"
        >
          <v-expand-transition>
            <div
              v-if="hover"
              class="d-flex transition-fast-in-fast-out v-card--reveal white--text overflow-auto"
              style="height: 100%;"
            >
              <div>
                <p class="movie-card-title">{{ review.title }}</p>
                <p class="movie-card-title"><i class="fas fa-star fa-xs"></i> {{ review.rank * 2 }}</p>
              </div>
            </div>
          </v-expand-transition>
        </v-img>
      </v-hover>
      <p class="overflow-x-hidden movie-card-title">{{ review.movie.title }}</p>
      <p class="movie-card-description">{{ review.movie.release_date }} · <i class="fas fa-star fa-xs"></i> {{ review.movie.vote_average }}</p>
    </div></a>
  </v-col>
</template>

<script>
export default {
  name: 'ReviewCard',
  props: {
    review: Object,
  },
  methods: {
    moveReviewDetail () {
      this.$router.push({ name: 'ReviewDetail', params: { reviewId: this.review.id }})
    }
  }
}
</script>

<style>

</style>