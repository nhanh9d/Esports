<template>
  <status-detail :is-edit="false" />
</template>

<script>
import StatusDetail from './components/StatusDetail'

export default {
  name: 'CreateStatus',
  components: { StatusDetail }
}
</script>

