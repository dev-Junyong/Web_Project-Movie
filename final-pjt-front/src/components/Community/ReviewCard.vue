<template>
  <v-col cols="2">
    <a v-if="user" @click.prevent="moveCollectionPage">
      <v-hover v-slot:default="{ hover }">
        <v-card class="collection-card movie-card-poster">
          <v-row dense>
            <v-expand-transition>
              <div
                v-if="hover"
                class="d-flex transition-fast-in-fast-out v-card--reveal white--text overflow-auto hover-cover"
                style="height: 100%; border-radius: 5px;"
              >
                <div v-if="user.username">
                  <p class="movie-card-title">{{ user.username }}</p>
                  <p class="movie-card-title"><v-icon>mdi-vote</v-icon> {{ likeCnt }}</p>
                </div>
              </div>
            </v-expand-transition>
            <v-col
              v-for="review in computedReviews"
              :key="review.id"
              cols="6"
              class="pb-0"
            >
              <img
                :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${review.movie.poster_path}`"
                class="collection-poster"
              >
            </v-col>
          </v-row>
        </v-card>
      </v-hover>

      <p v-if="user.username" class="collection-owner">{{ user.username }} 님의 컬렉션</p>
      <div class="flex-l">
        <div class="vote-btn site_color">
          <v-icon color="grey lighten-5">mdi-vote</v-icon>
        </div>
        <p class="like-cnt d-d ml-2">{{ this.likeCnt }}</p>
      </div>
    </a>
  </v-col>
</template>

<script>
export default {
  name: 'ReviewCard',
  props: {
    user: Object,
  },
  data () {
    return {
      reviews: this.user.review_author,
      limit: 4,
      likeCnt: 0,
    }
  },
  methods: {
    moveCollectionPage () {
      this.$router.push({ name: 'UserCollection', params: { username: this.user.username } })
    }
  },
  computed: {
    computedReviews() {
      return this.limit ? this.reviews.slice(0,this.limit) : this.reviews
    }
  },
  created () {
    this.likeCnt = this.reviews.reduce((acc, review) => {
        return acc + review.users_like.length
      }, 0)
  }
}
</script>

<style>
.collection-card {
  border-radius: 5px;
  padding: 4px 4px 0 4px;
  background: rgb(199, 199, 199);
}

.collection-poster {
  width: 100%;
  border-radius: 5px;
}

.collection-owner {
  margin-top: 10px;
  text-decoration: none;
  color: black !important;
  font-size: 16px;
  font-weight: bold;
}

.like-cnt {
  color: black !important;
  font-size: 15px;
}

.vote-btn {
  width: 24px;
  height: 24px;
  border-radius: 70%;
  text-align: center;
}
</style>