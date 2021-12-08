import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../views/Main'
import Movie from '../views/Movie'
import MovieDetail from '../views/MovieDetail'
import Community from '../views/Community'
import ReviewCreate from '../views/ReviewCreate'
import ReviewUpdate from '../views/ReviewUpdate'
import ReviewDetail from '../views/ReviewDetail'
import Recommend from '../views/Recommend'
import SearchResult from '../views/SearchResult'

import TempChart from '../views/TempChart'

import UserCollection from '../views/UserCollection'
import TimeLine from '../views/TimeLine'
import UserProfile from '../views/UserProfile'
import UserProfileUpdate from '../views/UserProfileUpdate'
import PasswordChange from '../views/PasswordChange'
import Signup from '../views/Signup'
import Login from '../views/Login'

Vue.use(VueRouter)

const routes = [
  {
    path: '/tempchart',
    name: 'tempchart',
    component: TempChart
  },
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  {
    path: '/movies',
    name: 'Movie',
    component: Movie
  },
  {
    path: '/movies/:movieId',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/review-create/:movieId',
    name: 'ReviewCreate',
    component: ReviewCreate
  },
  {
    path: '/review-update/:reviewId',
    name: 'ReviewUpdate',
    component: ReviewUpdate
  },
  {
    path: '/community/review/:reviewId',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: Recommend
  },
  {
    path: '/:keyword/search_result',
    name: 'SearchResult',
    component: SearchResult
  },
  {
    path: '/accounts/:username/collection',
    name: 'UserCollection',
    component: UserCollection
  },
  {
    path: '/accounts/:username/profile',
    name: 'UserProfile',
    component: UserProfile
  },
  {
    path: '/accounts/:username/timeline',
    name: 'TimeLine',
    component: TimeLine
  },
  {
    path: '/accounts/:username/profile_update',
    name: 'UserProfileUpdate',
    component: UserProfileUpdate
  },
  {
    path: '/accounts/PasswordChange',
    name: 'PasswordChange',
    component: PasswordChange
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
