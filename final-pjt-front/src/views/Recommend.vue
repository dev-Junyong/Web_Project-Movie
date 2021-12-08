<template>
  <v-container class="recommend-page">

    <v-container class="mx-auto">
      <v-card width="100%" height="800px" class="card-back-color">
        <v-tabs vertical height="800px">
          <v-tab class="tab-detail">DDakji Movie</v-tab>
          <v-tab class="tab-detail">Dalgona Movie</v-tab>

          <v-tab-item>
            <v-card-text>
              <movie-world-cup></movie-world-cup>
            </v-card-text>
          </v-tab-item>
          <v-tab-item>
            <v-card-text>
              <lottery></lottery>
            </v-card-text>
          </v-tab-item>
        </v-tabs>
      </v-card>
    </v-container>
  </v-container>
</template>

<script>
import Lottery from '../components/Recommend/Lottery'
import MovieWorldCup from '../components/Recommend/MovieWorldCup'

export default {
  name: 'Recommend',
  components: { 
    MovieWorldCup,
    Lottery
  },
  data () {
    return {
      tab: null,
      items: [
        { name: 'One', content: 'Tab1 Content' },
        { name: 'Two', content: 'Tab2 Content' },
      ]
    }
  },
  created () {
    this.$store.dispatch('movieWorldCup')
    this.$store.dispatch('getLottery')
  }
}
</script>

<style>
.recommend-page {
  width: 75%;
  padding-top: 0;
}

.card-back-color {
  background: white !important;
}

.tab-detail {
  font-size: 15px !important;
  height: 50px !important;
  font-weight: bold !important;
}

.v-window__container {
    display: flex;
    flex-direction: column;
    height: 700px !important;
    position: relative;
    transition: 0.3s cubic-bezier(0.25, 0.8, 0.5, 1);
}

.v-card__text {
    width: 100%;
}

.theme--light.v-tabs > .v-tabs-bar {
  background-color: rgb(248, 248, 248) !important;
}

.theme--light.v-tabs-items {
  background-image: url(../assets/movie_cup.png);
  background-size: cover;
  background-position: center;
}
</style>