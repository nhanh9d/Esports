<template>
  <match-detail :is-edit="false" />
</template>

<script>
import MatchDetail from './components/MatchDetail'

export default {
  name: 'CreateMatch',
  components: { MatchDetail }
}
</script>

