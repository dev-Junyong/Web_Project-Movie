<template>
  <div class="movie-cup-page">
    <div class="movie-cup-title-box">
      <p class="movie-cup-title text-center">Ddakji Movie - {{ this.nowStage }}강</p>
    </div>

    <div v-if="!isStart" class="movie-cup-btn-position">
      <v-btn 
        @click="startWorldCup"
        class="movie-worldcup-btn"
      >Start</v-btn>
    </div>

    <div v-else class="matchup">
      <div 
        v-for="movie in nowMatch"
        :key="movie.id"
      >
      <p class="ddakji-t ml-10 mb-0">{{ movie.title }}</p>
      <a @click.prevent="winnerMovie(movie)">
        <div class="ddakji-box">
          <div class="item front">
            <img
              class="ddakji-movie"
              :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${movie.poster_path}`"
            >
          </div>
          <div class="item back">
            <div class="back-title">
              <p class="ddakji-t">{{ movie.title }}</p>
              <p class="ddakji-q mt-3">선택하시겠습니까?</p>
            </div>
            <img
              class="ddakji"
              src="@/assets/ddakji.png"
            >
          </div>
        </div>
      </a>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'MovieWorldCup',
  data () {
    return {
      nowMatch: null,
      isStart: false,
      nowStage: 32,
    }
  },
  methods: {
    startWorldCup () {
      this.nowMatch = []
      if (this.worldCupList.length) {
        this.nowMatch.push(this.worldCupList.shift())
        this.nowMatch.push(this.worldCupList.shift())
        this.isStart = true
      } else {
        this.isStart = false
        this.$store.dispatch('movieWorldCup')
      }
    },
    winnerMovie (movie) {
      this.$store.dispatch('winnerMovie', movie)
      if (this.worldCupList.length===0) {
        this.$store.dispatch('nextStage')
        if (this.nowStage === 2) {
          this.nowStage = 32
        } else {
          this.nowStage /= 2
        }
      }
      this.startWorldCup()
    }
  },
  computed: {
    ...mapState([
      'worldCupList',
    ])
  },
}
</script>

<style>
.movie-cup-page {
  height: 100%;
}

.matchup{
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  height: 700px;
}

.movie-worldcup-btn {
  background: linear-gradient(to bottom right, #F83D3D, #B600EB);
  width: 100px;
  height: 35px !important;
  color: white !important;
  font-size: 20px !important;
}

.movie-cup-back {
  height: 700px;
  width: 1200px;
  border-radius: 5px;
  overflow: hidden;
  box-shadow: 0px 4px 2px -2px rgb(0 0 0 / 20%), 0px 3px 3px 0px rgb(0 0 0 / 14%), 0px 2px 6px 0px rgb(0 0 0 / 12%);
}

.movie-cup-back-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.movie-cup-title-box {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50px;
  background: rgb(0, 0, 0, 0.3);
}

.movie-cup-title {
  font-size: 25px;
  font-weight: bold;
  color: white;
}

.movie-cup-btn-position {
  display: flex;
  justify-content: center;
  padding-top: 500px;
  height: 700px;
}

.v-card__text {
  padding: 0 !important;
}

.ddakji-box {
    width: 300px;
    height: 429px;
    perspective: 700px;
    margin: 40px;
}

.ddakji-box .item {
    width: 100%;
    height: 100%;
    font-size: 35px;
    backface-visibility: hidden;
    transition: 1s;
}

.ddakji-box .item.front {
    position: absolute;
    transform: rotateY(0deg);
}

.ddakji-box:hover .item.front {
    transform: rotateY(180deg);
}

.ddakji-box .item.back {
    display: flex;
    justify-content: center;
    align-items: center;
    transform: rotateY(-180deg);
}

.ddakji-box:hover .item.back {
    transform: rotateY(0deg);
}

.ddakji-movie {
  width: 100%;
  height: 100%;
  border-radius: 5px;
  box-shadow: 0px 8px 6px 0px rgb(0 0 0 / 30%), 0px 10px 10px 0px rgb(0 0 0 / 20%), 0px 6px 10px 0px rgb(0 0 0 / 20%);
}

.ddakji {
  width: 100%;
  border-radius: 5px;
  box-shadow: 0px 6px 4px 0px rgb(0 0 0 / 30%), 0px 5px 5px 0px rgb(0 0 0 / 20%), 0px 4px 8px 0px rgb(0 0 0 / 20%);
}

.back-title {
  text-align: center;
  position: absolute;
  top: 50;
}

.ddakji-t {
  font-size: 25px;
  font-weight: bold;
  color: white;
}

.ddakji-q {
  font-size: 15px;
  color: white;
}
</style>