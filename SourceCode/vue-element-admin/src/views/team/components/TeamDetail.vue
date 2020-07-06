<template>
  <div class="createPost-container">
    <el-form ref="postForm" :model="postForm" :rules="rules" class="form-container">

      <div class="createPost-main-container">
        <el-row>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Team name:">
              <el-input v-model="postForm.name" type="text" autosize placeholder="Please enter team name" @change="changeUriName(postForm)"/>
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Uri name:">
              <el-input v-model="postForm.uri_name" type="text" autosize placeholder="Please enter team name to auto fill uri name" />
            </el-form-item>
          </el-col>

        </el-row>

        <el-row>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Team short name:">
              <el-input v-model="postForm.short_name" type="text" autosize placeholder="Please enter short team name" />
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Starting date:">
              <el-date-picker v-model="postForm.starting_date" type="datetime" format="yyyy-MM-dd HH:mm:ss" placeholder="Please enter starting date" />
            </el-form-item>
          </el-col>

        </el-row>

        <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Description:">
          <el-input v-model="postForm.description" :rows="2" type="textarea" class="team-textarea" autosize placeholder="Please enter the description" />
        </el-form-item>

        <el-row>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="World rank:">
              <el-input v-model="postForm.world_rank" type="text" autosize placeholder="Please enter world rank" />
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Region rank:">
              <el-input v-model="postForm.region_rank" type="text" autosize placeholder="Please enter region rank" />
            </el-form-item>
          </el-col>

        </el-row>

        <el-row>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Total earnings:">
              <el-input v-model="postForm.total_earnings" type="text" autosize placeholder="Please enter total earnings" />
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Win rate (%):">
              <el-input v-model="postForm.win_rate" type="text" autosize placeholder="Please enter win rate" />
            </el-form-item>
          </el-col>

        </el-row>

        <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Region:">
          <RegionDropdown :parentValue="this.postForm.team_region" v-model="postForm.team_region" @onRegionChange="onRegionChange"/>
        </el-form-item>

        <el-form-item hidden prop="image_uri" style="margin-bottom: 30px;">
          <Upload v-model="postForm.banner_in_list_uri" />
        </el-form-item>

        <el-form-item hidden prop="image_uri" style="margin-bottom: 30px;">
          <Upload v-model="postForm.banner_in_detail_uri" />
        </el-form-item>

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
  import Tinymce from '@/components/Tinymce'
  import Upload from '@/components/Upload/SingleImage3'
  import MDinput from '@/components/MDinput'
  import Sticky from '@/components/Sticky'
  import { validURL } from '@/utils/validate'
  import { fetchTeam, createTeam, updateTeam } from '@/api/team'
  import { searchUser } from '@/api/remote-search'
  import { RegionDropdown, PlatformDropdown, SourceUrlDropdown } from './Dropdown'

  const defaultForm = {
    team_id: undefined,
    name: null,
    short_name: null,
    uri_name: null,
    description: null,
    world_rank: null,
    region_rank: null,
    total_earnings: null,
    win_rate: null,
    starting_date: null,
    banner_in_list_uri: undefined,
    banner_in_detail_uri: undefined,
    team_region: null,
    is_active: true,
    is_delete: false
  }

  export default {
    name: 'TeamDetail',
    components: { Tinymce, MDinput, Upload, Sticky, RegionDropdown },
    props: {
      isEdit: {
        type: Boolean,
        default: false
      }
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
        const team_id = this.$route.params && this.$route.params.id
        this.fetchData(team_id)
      }

      // Why need to make a copy of this.$route here?
      // Because if you enter this page and quickly switch tag, may be in the execution of the setTagsViewTitle function, this.$route is no longer pointing to the current page
      // https://github.com/PanJiaChen/vue-element-admin/issues/1221
      this.tempRoute = Object.assign({}, this.$route)
    },
    methods: {
      fetchData(team_id) {
        fetchTeam(team_id).then(response => {
          this.postForm = response.data

          // just for test
          // this.postForm.title += `   Team Id:${this.postForm.team_id}`
          // this.postForm.content_short += `   Team Id:${this.postForm.team_id}`

          // set tagsview title
          this.setTagsViewTitle()

          // set page title
          this.setPageTitle()
        }).catch(err => {
          console.log(err)
        })
      },
      setTagsViewTitle() {
        const title = 'Edit Team'
        const route = Object.assign({}, this.tempRoute, { title: `${title}-${this.postForm.team_id}` })
        this.$store.dispatch('tagsView/updateVisitedView', route)
      },
      setPageTitle() {
        const title = 'Edit Team'
        document.title = `${title} - ${this.postForm.team_id}`
      },
      submitForm() {
        this.$refs.postForm.validate(valid => {
          console.log(this.postForm)
          if (valid) {
            if (this.isEdit) {
              updateTeam(this.postForm).then(response => {
                this.$notify({
                  title: 'Success',
                  message: 'Success update team',
                  type: 'success',
                  duration: 2000
                })
                this.$router.push({ path: '/team/list' })
              }).catch(err => {
                console.log(err)
              })
            }
            else {
              createTeam(this.postForm).then(response => {
                if (response.data.team_id) {
                  this.$notify({
                    title: 'Success',
                    message: 'Success create new team',
                    type: 'success',
                    duration: 2000
                  })
                  this.$router.push({ path: '/team/list' })
                } else {
                  this.$notify({
                    title: 'Error',
                    message: 'Duplicate team info',
                    type: 'error',
                    duration: 2000
                  })
                }
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
      changeUriName(form) {
        form.uri_name = form.name.replace(/ /g, "-").toLowerCase()
      },
      onRegionChange(value) {
        this.postForm.team_region = value
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

  .team-textarea /deep/ {
    textarea

  {
    padding-right: 40px;
    resize: none;
    border: none;
    border-radius: 0px;
    border-bottom: 1px solid #bfcbd9;
  }
  }

  .el-form-item__label{text-align:left}
</style>
