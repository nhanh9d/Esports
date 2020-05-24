<template>
  <match-detail :is-edit="true" />
</template>

<script>
import MatchDetail from './components/MatchDetail'

export default {
  name: 'EditForm',
  components: { MatchDetail }
}
</script>

