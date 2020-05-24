<template>
  <league-detail :is-edit="true" />
</template>

<script>
import LeagueDetail from './components/LeagueDetail'

export default {
  name: 'EditForm',
  components: { LeagueDetail }
}
</script>

