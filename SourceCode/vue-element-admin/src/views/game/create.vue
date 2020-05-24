<template>
  <game-detail :is-edit="false" />
</template>

<script>
import GameDetail from './components/GameDetail'

export default {
  name: 'CreateGame',
  components: { GameDetail }
}
</script>

