<template>
  <div class="dashboard-container">
    <component :is="currentRole" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import adminDashboard from './admin'
import editorDashboard from './editor'
import visitorDashboard from './visitor'

export default {
  name: 'Dashboard',
  components: { adminDashboard, editorDashboard, visitorDashboard },
  data() {
    return {
      currentRole: 'adminDashboard'
    }
  },
  computed: {
    ...mapGetters([
      'roles'
    ])
  },
  mounted() {
    this.checkLoggedIn()
  },
  created() {
    if (this.roles.includes('admin')) {
      this.currentRole = 'adminDashboard'
    }
    if (this.roles.includes('editor')) {
      this.currentRole = 'editorDashboard'
    }
    if (this.roles.includes('visitor')) {
      this.currentRole = 'visitorDashboard'
    }
  },
  methods: {
    checkLoggedIn() {
      this.$router.push('/login')
    }
  }
}
</script>
