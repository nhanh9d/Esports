<template>
  <region-detail :is-edit="false" />
</template>

<script>
import RegionDetail from './components/RegionDetail'

export default {
  name: 'CreateRegion',
  components: { RegionDetail }
}
</script>

