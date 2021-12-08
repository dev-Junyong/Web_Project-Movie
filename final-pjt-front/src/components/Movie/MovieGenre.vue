<template>
  <span>
    <v-sheet
    class="mx-auto"
    max-width="100%"
  >
    <v-slide-group
      multiple
      show-arrows
    >
      <v-slide-item
        v-for="genre in genreList"
        :key="genre.id"
        :genre="genre"
        v-slot="{ active, toggle }"
      >
        <v-btn
          class="mx-2 movie-genre-btns"
          :input-value="active"
          active-class="site_color white--text"
          depressed
          rounded
          height="24"
          @click="[toggle(), selectGenre(genre.id)]"
        >
          {{ genre.name }}
        </v-btn>
      </v-slide-item>
    </v-slide-group>
  </v-sheet>
  </span>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'MovieGenre',
  props: {
    genre: Object,
  },
  methods: {
    selectGenre (id) {
      this.$store.dispatch('selectGenre', id)
    }
  },
  computed: {
    ...mapState([
      'genreList',
    ])
  }
}
</script>

<style>
.movie-genre-btns {
    font-weight: bold;
  }

.site_color {
  background: linear-gradient(to bottom right, #F83D3D, #B600EB);
}
</style>