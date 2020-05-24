<template>
  <region-detail :is-edit="true" />
</template>

<script>
import RegionDetail from './components/RegionDetail'

export default {
  name: 'EditForm',
  components: { RegionDetail }
}
</script>

