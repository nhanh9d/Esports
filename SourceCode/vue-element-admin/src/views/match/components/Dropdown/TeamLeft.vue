<template>
  <el-select v-model="value" placeholder="Choose Team Left" @change="onTeamLeftChange">
    <el-option v-for="item in options"
               :key="item.game_id"
               :label="item.name"
               :value="item.game_id">
    </el-option>
  </el-select>
</template>

<script>
  import { fetchActiveTeams } from '@/api/team'
  const options = [{
          game_id: '-1',
          name: 'No game'
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
      console.log(this.parentValue)
    },
    methods: {
      fetchData() {
        fetchActiveTeams().then(response => {
          this.options = response.data
        }).catch(err => {
          console.log(err)
        })
      },
      onTeamLeftChange() {
        this.$emit('onTeamLeftChange', this.value)
      }
    }
  }
</script>
