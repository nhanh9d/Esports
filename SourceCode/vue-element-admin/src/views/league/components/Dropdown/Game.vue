<template>
  <el-select v-model="value" placeholder="Choose Game" @change="onGameChange">
    <el-option v-for="item in options"
               :key="item.game_id"
               :label="item.name"
               :value="item.game_id">
    </el-option>
  </el-select>
</template>

<script>
  import { fetchActiveGame } from '@/api/game'
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
        fetchActiveGame().then(response => {
          this.options = response.data
        }).catch(err => {
          console.log(err)
        })
      },
      onGameChange() {
        this.$emit('onGameChange', this.value)
      }
    }
  }
</script>
