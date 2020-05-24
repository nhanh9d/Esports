<template>
  <game-detail :is-edit="true" />
</template>

<script>
import GameDetail from './components/GameDetail'

export default {
  name: 'EditForm',
  components: { GameDetail }
}
</script>

