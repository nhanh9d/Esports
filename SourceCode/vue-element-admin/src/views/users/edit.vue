<template>
  <users-detail :is-edit="true" />
</template>

<script>
import UsersDetail from './components/UsersDetail'

export default {
  name: 'EditForm',
  components: { UsersDetail }
}
</script>

