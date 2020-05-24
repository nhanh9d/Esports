<template>
  <team-detail :is-edit="false" />
</template>

<script>
import TeamDetail from './components/TeamDetail'

export default {
  name: 'CreateTeam',
  components: { TeamDetail }
}
</script>

