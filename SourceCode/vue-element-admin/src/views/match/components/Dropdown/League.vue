<template>
  <el-select v-model="value" placeholder="Choose League" @change="onLeagueChange">
    <el-option v-for="item in options"
               :key="item.league_id"
               :label="item.name"
               :value="item.league_id">
    </el-option>
  </el-select>
</template>

<script>
  import { fetchActiveLeagues } from '@/api/league'
  const options = [{
          league_id: '-1',
          name: 'No league'
        }]
  export default {
    data() {
      return {
        options: options,
        value: ''
      }
    },
    props: ['parentValue'],
    created() {
      this.fetchData()
    },
    methods: {
      fetchData() {
        fetchActiveLeagues().then(response => {
          this.options = response.data
        }).catch(err => {
          console.log(err)
        })
      },
      onLeagueChange() {
        this.$emit('onLeagueChange', this.value)
      }
    }
  }
</script>
