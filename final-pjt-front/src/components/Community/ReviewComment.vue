<template>
  <div>
    <h2>comment</h2>
    <div class="flex-l">
      <v-text-field
          outlined
          dense
          label="comment"
          prepend-inner-icon="mdi-message-reply"
          v-model="context.content"
        @keyup.enter="createComment"
      ></v-text-field>

      <div>
        <v-hover v-slot:default="{ hover }">
          <button class="text-btn" @click="createComment">
            <v-icon v-if="hover" x-large class="site-color-text">
              mdi-tooltip-edit
            </v-icon>
            <v-icon v-else x-large>
              mdi-tooltip-edit-outline
            </v-icon>
          </button>
        </v-hover>
        <div style="height: 22px;"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReviewComment',
  props: {
    review: Object,
  },
  data () {
    return {
      context: {
        content: null,
        reviewId: null,
      }
    }
  },
  methods: {
    createComment () {
      this.$store.dispatch('createComment', this.context)
      this.context.content = null
      this.context.reviewId = this.review.id
    }
  },
  created () {
    this.context.reviewId = this.review.id
  },
  watch: {
    review () {
      this.context.reviewId = this.review.id
    }
  }
}
</script>

<style>

</style>