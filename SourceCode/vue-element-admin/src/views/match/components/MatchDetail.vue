<template>
  <div class="createPost-container">
    <el-form ref="postForm" :model="postForm" :rules="rules" class="form-container">

      <div class="createPost-main-container">
        <el-row>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Uri name:">
              <el-input v-model="postForm.uri_name" type="text" autosize placeholder="Please enter uri match name" />
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Starting date:">
              <el-date-picker v-model="postForm.starting_date" type="datetime" format="yyyy-MM-dd HH:mm:ss" placeholder="Please enter starting date" />
            </el-form-item>
          </el-col>

        </el-row>

        <el-row>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Team left:">
              <TeamLeftDropdown :parentValue="this.postForm.team_left" v-model="postForm.team_left" @onTeamLeftChange="onTeamLeftChange" />
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Team right:">
              <TeamRightDropdown :parentValue="this.postForm.team_right" v-model="postForm.team_right" @onTeamRightChange="onTeamRightChange" />
            </el-form-item>
          </el-col>

        </el-row>

        <el-row>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Match:">
              <LeagueDropdown :parentValue="this.postForm.match_league" v-model="postForm.match_league" @onLeagueChange="onLeagueChange" />
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Match status:">
              <StatusDropdown :parentValue="this.postForm.match_status" v-model="postForm.match_status" @onStatusChange="onStatusChange" />
            </el-form-item>
          </el-col>

        </el-row>

        <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Is active:">
          <el-checkbox v-model="postForm.is_active" class="filter-item" @change="toggleIsActive(postForm)"></el-checkbox>
        </el-form-item>

        <el-form-item style="margin-bottom: 40px;" label-width="150px">
          <el-button v-loading="loading" style="margin-right: 25px;" type="success" @click="submitForm">
            Submit
          </el-button>
        </el-form-item>
      </div>
    </el-form>
  </div>
</template>

<script>
  import { fetchMatches, createMatches, updateMatches } from '@/api/match'
  import { StatusDropdown, LeagueDropdown, TeamLeftDropdown, TeamRightDropdown } from './Dropdown'

  const defaultForm = {
    match_id: undefined,
    uri_name: undefined,
    starting_date: undefined,
    team_left: undefined,
    team_right: undefined,
    match_status: undefined,
    match_league: undefined,
    is_active: true,
    is_delete: false
  }

  export default {
    name: 'MatchDetail',
    components: { StatusDropdown, LeagueDropdown, TeamLeftDropdown, TeamRightDropdown },
    props: {
      isEdit: {
        type: Boolean,
        default: false
      }
    },
    mounted() {

    },
    data() {
      const validateRequire = (rule, value, callback) => {
        if (value === '') {
          this.$message({
            message: rule.field + ' is required',
            type: 'error'
          })
          callback(new Error(rule.field + ' is required'))
        } else {
          callback()
        }
      }
      return {
        postForm: Object.assign({}, defaultForm),
        loading: false,
        userListOptions: [],
        rules: {
          title: [{ validator: validateRequire }],
          content: [{ validator: validateRequire }]
        },
        tempRoute: {}
      }
    },
    computed: {
      displayTime: {
        // set and get is useful when the data
        // returned by the back end api is different from the front end
        // back end return => "2013-06-25 06:59:25"
        // front end need timestamp => 1372114765000
        get() {
          return (+new Date(this.postForm.display_time))
        },
        set(val) {
          this.postForm.display_time = new Date(val)
        }
      }
    },
    created() {
      if (this.isEdit) {
        const match_id = this.$route.params && this.$route.params.id
        this.fetchData(match_id)
      }

      // Why need to make a copy of this.$route here?
      // Because if you enter this page and quickly switch tag, may be in the execution of the setTagsViewTitle function, this.$route is no longer pointing to the current page
      // https://github.com/PanJiaChen/vue-element-admin/issues/1221
      this.tempRoute = Object.assign({}, this.$route)
    },
    methods: {
      fetchData(match_id) {
        fetchMatches(match_id).then(response => {
          this.postForm = response.data

          // just for test
          // this.postForm.title += `   Match Id:${this.postForm.match_id}`
          // this.postForm.content_short += `   Match Id:${this.postForm.match_id}`

          // set tagsview title
          this.setTagsViewTitle()

          // set page title
          this.setPageTitle()
        }).catch(err => {
          console.log(err)
        })
      },
      setTagsViewTitle() {
        const title = 'Edit Match'
        const route = Object.assign({}, this.tempRoute, { title: `${title}-${this.postForm.match_id}` })
        this.$store.dispatch('tagsView/updateVisitedView', route)
      },
      setPageTitle() {
        const title = 'Edit Match'
        document.title = `${title} - ${this.postForm.match_id}`
      },
      submitForm() {
        this.$refs.postForm.validate(valid => {
          console.log(this.postForm)
          if (valid) {
            if (this.isEdit) {
              updateMatches(this.postForm).then(response => {
                this.$notify({
                  title: 'Success',
                  message: 'Success update match',
                  type: 'success',
                  duration: 2000
                })
                this.$router.push({ path: '/match/list' })
              }).catch(err => {
                console.log(err)
              })
            }
            else {
              createMatches(this.postForm).then(response => {
                this.$notify({
                  title: 'Success',
                  message: 'Success create new match',
                  type: 'success',
                  duration: 2000
                })
                this.$router.push({ path: '/match/list' })
              }).catch(err => {
                console.log(err)
              })
            }
          } else {
            console.log('error submit!!')
            return false
          }
        })
      },
      toggleIsActive(form) {
        form.is_active = !form.is_active
      },
      onLeagueChange(value) {
        this.postForm.match_league = value
      },
      onStatusChange(value) {
        this.postForm.match_status = value
      },
      onTeamLeftChange(value) {
        this.postForm.team_left = value
      },
      onTeamRightChange(value) {
        this.postForm.team_right = value
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "~@/styles/mixin.scss";

  .createPost-container {
    position: relative;
    .createPost-main-container

  {
    padding: 40px 45px 20px 50px;
    .postInfo-container

  {
    position: relative;
    @include clearfix;
    margin-bottom: 10px;
    .postInfo-container-item

  {
    float: left;
  }

  }
  }

  .word-counter {
    width: 40px;
    position: absolute;
    right: 10px;
    top: 0px;
  }

  }

  .match-textarea /deep/ {
    textarea

  {
    padding-right: 40px;
    resize: none;
    border: none;
    border-radius: 0px;
    border-bottom: 1px solid #bfcbd9;
  }

  }

  .el-form-item__label {
    text-align: left
  }
</style>
