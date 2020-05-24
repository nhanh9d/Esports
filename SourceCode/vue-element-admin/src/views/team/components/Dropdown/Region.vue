<template>
  <el-select v-model="value" placeholder="Choose Region" @change="onRegionChange">
    <el-option v-for="item in options"
               :key="item.region_id"
               :label="item.name"
               :value="item.region_id">
    </el-option>
  </el-select>
</template>

<script>
  import { fetchRegions } from '@/api/region'
  const options = [{
          region_id: '-1',
          name: 'No region'
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
        fetchRegions().then(response => {
          this.options = response.data
        }).catch(err => {
          console.log(err)
        })
      },
      onRegionChange() {
        this.$emit('onRegionChange', this.value)
      }
    }
  }
</script>
