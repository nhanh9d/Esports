<template>
  <league-detail :is-edit="false" />
</template>

<script>
import LeagueDetail from './components/LeagueDetail'

export default {
  name: 'CreateLeague',
  components: { LeagueDetail }
}
</script>

