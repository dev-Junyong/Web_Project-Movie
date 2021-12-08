<script>
import {Bar} from 'vue-chartjs'
import { mapState } from 'vuex'

export default {
  extends: Bar,
  data() {
    return {
      cdata: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      datacollection: {
        labels: ['모험', '판타지', '애니메이션', '드라마', '공포', '액션', '서부', '스릴러', '범죄', '다큐멘터리', 'SF', '미스터리', '음악', '로맨스', '가족', '전쟁', 'TV영화'],
        datasets: [
          {
            label: '선호 장르',
            backgroundColor: '#f87979',
            pointBackgroundColor: 'white',
            borderWidth: 1,
            pointBorderColor: '#249EBF',
            data: this.cdata
          }
        ]
      },
      options: {
        plugins: {
          legend: {
            display: false
          },
        },
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true
            },
            gridLines: {
              display: true
            }
          }],
          xAxes: [ {
            gridLines: {
              display: false
            }
          }]
        },
        legend: {
            display: false,
          },
        responsive: true,
        maintainAspectRatio: false
      }
    }
  },
  computed: {
    ...mapState([
      'chartdata',
      'personData',
    ])
  },
  created () {
    this.$store.dispatch('getChartData', this.personData.username)
  },
  watch: {
    chartdata () {
      this.cdata = this.chartdata
      this.datacollection['datasets'][0]['data'] = this.cdata
      this.renderChart(this.datacollection, this.options)
    },
  }
}
</script>