<template>
  <div>
    <hr class="my-3">
    <span v-if="isUpdate" class="flex-l">
      <v-text-field
        outlined
        dense
        label="comment"
        prepend-inner-icon="mdi-message-reply"
        v-model="context.content"
        @keyup.enter="update"
      ></v-text-field>

      <div>
        <v-hover v-slot:default="{ hover }">
          <button class="text-btn" @click="update">
            <v-icon v-if="hover" class="site-color-text">
              mdi-cog
            </v-icon>
            <v-icon v-else>
              mdi-cog-outline
            </v-icon>
          </button>
        </v-hover>
        <div style="height: 22px;"></div>
      </div>
    </span>

    <span class="flex-bt" v-else>
      <div class="flex-l">
        <p class="d-d mr-3 mt-1">
          {{ comment.content }}
        </p>
        <p class="d-d mr-5 mt-1 comment-author">
          .{{ comment.author }}
        </p>

         <span v-if="loginUser">
          <span v-if="comment.like_users.includes(loginUser.id)">
            <v-hover v-slot:default="{ hover }">
              <button class="text-btn" @click="likeComment">
                <v-icon v-if="hover" style="color: red;">
                  mdi-thumb-down-outline
                </v-icon>
                <v-icon v-else class="site-color-text">
                  mdi-thumb-up
                </v-icon>
              </button>
            </v-hover>
          </span>

          <span v-else>
            <v-hover v-slot:default="{ hover }">
              <button class="text-btn" @click="likeComment">
                <v-icon v-if="hover" class="site-color-text">
                  mdi-thumb-up
                </v-icon>
                <v-icon v-else>
                  mdi-thumb-up-outline
                </v-icon>
              </button>
            </v-hover>
          </span>
        </span>

        <span v-else>
          <button>
            <v-icon class="site-color-text">
              mdi-thumb-up
            </v-icon>
          </button>
        </span>
        <p class="d-d ml-2 mt-1">{{ comment.like_users.length }}</p>
      </div>

      <div>
        <span v-if="loginUser">
          <span v-if="comment.author == loginUser.username">
            <v-hover v-slot:default="{ hover }">
              <button class="text-btn" @click="commentDelete">
                <v-icon v-if="hover" class="site-color-text">
                  mdi-delete-empty
                </v-icon>
                <v-icon v-else>
                  mdi-delete-outline
                </v-icon>
              </button>
            </v-hover>

            <v-hover v-slot:default="{ hover }">
              <button class="text-btn" @click="update">
                <v-icon v-if="hover" class="site-color-text">
                  mdi-cog
                </v-icon>
                <v-icon v-else>
                  mdi-cog-outline
                </v-icon>
              </button>
            </v-hover>
          </span>
        </span>
      </div>
    </span>

  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'CommentDetail',
  props: {
    comment: Object,
  },
  data () {
    return {
      isUpdate: false,
      context: {
        content: this.comment.content
      },
      reviewId: this.$route.params.reviewId
    }
  },
  methods: {
    update () {
      if (this.isUpdate) {
        this.$store.dispatch('commentUpdate', [this.reviewId, this.comment.id, this.context])
      }
      this.isUpdate = !this.isUpdate
    },
    commentDelete () {
      const data = [
        this.reviewId,
        this.comment.id
      ]
      this.$store.dispatch('commentDelete', data)
    },
    likeComment () {
      const data = [
        this.reviewId,
        this.comment.id
      ]
      this.$store.dispatch('likeComment', data)
    }
  },
  computed: {
    ...mapState([
      'loginUser',
    ])
  }
}
</script>

<style>
.comment-author {
  font-weight: bold;
}
</style>