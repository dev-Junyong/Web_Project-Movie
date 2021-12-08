<template>
  <v-container class="community-page">
    <h2>Community</h2>
    <v-row>
      <review-card 
        v-for="user in reviewerList"
        :key="user.id"
        :user="user"
      ></review-card>
    </v-row>
  </v-container>
</template>

<script>
import ReviewCard from '../components/Community/ReviewCard'
import { mapState } from 'vuex'

export default {
  name: 'Community',
  components: { 
    ReviewCard 
  },
  computed: {
    ...mapState([
      'reviewerList'
    ])
  },
  created () {
    this.$store.dispatch('getReviews')
  }
}
</script>

<style>
.community-page {
  width: 75%;
  padding-top: 0;
}
</style>