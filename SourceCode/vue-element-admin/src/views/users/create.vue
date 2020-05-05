<template>
  <users-detail :is-edit="false" />
</template>

<script>
import UsersDetail from './components/UsersDetail'

export default {
  name: 'CreateUsers',
  components: { UsersDetail }
}
</script>

