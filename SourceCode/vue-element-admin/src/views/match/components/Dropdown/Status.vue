<template>
  <el-select v-model="value" placeholder="Choose Status" @change="onStatusChange">
    <el-option v-for="item in options"
               :key="item.status_id"
               :label="item.name"
               :value="item.status_id">
    </el-option>
  </el-select>
</template>

<script>
  import { fetchActiveStatus } from '@/api/status'
  const options = [{
          status_id: '-1',
          name: 'No status'
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
        fetchActiveStatus().then(response => {
          this.options = response.data
        }).catch(err => {
          console.log(err)
        })
      },
      onStatusChange() {
        this.$emit('onStatusChange', this.value)
      }
    }
  }
</script>
