<template>
  <status-detail :is-edit="true" />
</template>

<script>
import StatusDetail from './components/StatusDetail'

export default {
  name: 'EditForm',
  components: { StatusDetail }
}
</script>

