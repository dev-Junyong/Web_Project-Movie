<template>
  <section class="container">
    <h1>vue-chart.js</h1>
      <div class="columns">
        <div class="column">
          <h3>Line Chart</h3>
          <LineChart/>
        </div>
        <div class="column">
          <h3>Bar Chart</h3>
          <BarChart/>
        </div>
      </div>

      <div class="columns">
        <div class="column">
          <h3>Bubble Chart</h3>
          <BubbleChart/>
        </div>
        <div class="column">
          <h3>Reactivity</h3>
        <reactive :chart-data="datacollection"></reactive>
        <button class="button is-primary" @click="fillData()">Randomize</button>
        </div>
      </div>

    <!-- <AreaChart/>
    <RaderChart/>
    <BarChart/>
    <PieChart/> -->
  </section>
</template>

<script>
import LineChart from '../components/Profile/LineChart.vue'
import BarChart from '../components/Profile/BarChart.vue'
import BubbleChart from '../components/Profile/BubbleChart.vue'
import Reactive from '../components/Profile/Reactive'
// import AreaChart from '../components/Profile/AreaChart.vue'
// import RaderChart from '../components/Profile/RaderChart.vue'
// import PieChart from '../components/Profile/PieChart.vue'

export default {
  name: 'TempChart',
  components: { 
    LineChart,
    BarChart,
    BubbleChart,
    Reactive,
    // AreaChart,
    // RaderChart,
    // PieChart,
  },
  data() {
    return {
      datacollection: null,
      chartData: {
        Books: 24,
        Magazine: 30,
        Newspapers: 50
      }
    };
  },
  created () {
    this.fillData()
  },
  methods: {
    fillData() {
      this.datacollection = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
          'September', 'October', 'November', 'December'],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            // Data for the x-axis of the chart
            data: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), 
            this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), 
            this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt()]
          }
        ]
      }
    },
    getRandomInt() {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    }
  }
};
</script>

<style>

</style>