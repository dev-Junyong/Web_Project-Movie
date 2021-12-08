<template>
  <v-container v-if="personData" class="collection-page">
    <h3><a @click.prevent="moveUserProfile">{{ personData.username }}</a>'s 컬렉션</h3>
    <v-row class="collections">
      <review-card
        v-for="review in personData.review_author"
        :key="review.id"
        :review="review"
      >
      </review-card>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'
import ReviewCard from '../components/Collection/ReviewCard'

export default {
  name: 'UserCollection',
  components: {
    ReviewCard,
  },
  data () {
    return {
      thisUsername: this.$route.params.username,
    }
  },
  methods: {
    moveUserProfile () {
      this.$router.push({ name: 'UserProfile', params: { username: this.personData.username }})
    }
  },
  computed: {
    ...mapState([
      'loginUser',
      'personData',
    ])
  },
  created () {
    this.$store.dispatch('getUser', this.thisUsername)
  },
  watch: {
    $route () {
      this.thisUsername = this.$route.params.username
      this.$store.dispatch('getUser', this.thisUsername)
    }
  },
}
</script>

<style>
.collection-page {
  width: 75%;
  padding-top: 0;
}

.collections {
  margin-top: 15px;
}
</style>