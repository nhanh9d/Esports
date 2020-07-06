<template>
  <el-select v-model="value" placeholder="Choose Team Right" @change="onTeamRightChange">
    <el-option v-for="item in options"
               :key="item.team_id"
               :label="item.name"
               :value="item.team_id">
    </el-option>
  </el-select>
</template>

<script>
  import { fetchActiveTeams } from '@/api/team'
  const options = [{
          team_id: '-1',
          name: 'No team'
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
        fetchActiveTeams().then(response => {
          this.options = response.data
        }).catch(err => {
          console.log(err)
        })
      },
      onTeamRightChange() {
        this.$emit('onTeamRightChange', this.value)
      }
    }
  }
</script>
