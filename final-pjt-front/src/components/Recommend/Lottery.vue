<template>
  <div class="movie-cup-page">
    <div class="movie-cup-title-box">
      <p class="movie-cup-title">Dalgona Movie</p>
    </div>

    <div
      v-if="isLottery"
      class="select-movie"
    >
      <div 
        class="lottery">
        <vue-scratchable
          class="dargona"
          v-slot="{ init }"
          :brushOptions="brush"
          :hideOptions="hide"
          getPercentageCleared
          @percentage-update="updatePoints"
        >
          <div class="wrapper">
            <img
              class="lottery-poster"
              :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${lotteryMovie.poster_path}`"
              @load="init()"
            >

          </div>
        </vue-scratchable>
        <p>You scratched {{ percentage }}% free.</p>
      </div>
    </div>

    <div
      v-else @click="getLottery"
      class="movie-cup-btn-position"
    >
      <v-btn 
        class="movie-worldcup-btn"
      >뽑기</v-btn>
    </div>
    
  </div>
</template>

<script>
import VueScratchable from 'vue-scratchable';
import { mapState } from 'vuex';
import dalgona from '@/assets/dalgona.png'

export default {
  name: 'Lottery',
  components: {
    VueScratchable,
  },
  data () {
    return {
      isLottery: false,
      percentage: 0,
      hide: {
        type: 'pattern',
        src: dalgona,
        repeat: 'repeat',
      },
      brush: {
        size: 40,
        shape: 'round',
      },
    }
  },
  computed: {
    ...mapState([
      'lotteryMovie',
    ]),
  },
  methods: {
    getLottery () {
      this.isLottery = true
    },
    updatePoints(percentage) {
      this.percentage = percentage;
    },
  },
  watch: {
    percentage () {
      if (this.percentage > 80) {
        alert(`${this.lotteryMovie.title} - 당첨🤩`)
        this.$router.push({ name: 'MovieDetail', params: { movieId: this.lotteryMovie.id } })
      }
    }
  }
}
</script>

<style>
.select-movie {
  display: flex;
  justify-content: center;
}

.lottery-poster {
  width: 400px;
}
.lottery {
  width: 400px;
  justify-content: center;
  cursor: url(../../assets/needle.gif), auto;
}

.dargona {
  border-radius: 70%;
}
</style>