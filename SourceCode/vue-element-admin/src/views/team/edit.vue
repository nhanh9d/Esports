<template>
  <team-detail :is-edit="true" />
</template>

<script>
import TeamDetail from './components/TeamDetail'

export default {
  name: 'EditForm',
  components: { TeamDetail }
}
</script>

