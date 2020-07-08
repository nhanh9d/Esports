<template>
  <div class="createPost-container">
    <el-form ref="postForm" :model="postForm" :rules="rules" class="form-container">

      <div class="createPost-main-container">
        <el-row>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="League name:">
              <el-input v-model="postForm.name" type="text" autosize placeholder="Please enter league name" @change="changeUriName(postForm)"/>
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Uri name:">
              <el-input v-model="postForm.uri_name" type="text" autosize placeholder="Please enter league name to auto fill uri name" />
            </el-form-item>
          </el-col>

        </el-row>

        <el-row>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="League price pool:">
              <el-input v-model="postForm.price_pool" type="text" autosize placeholder="Please enter price pool" />
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Starting date:">
              <el-date-picker v-model="postForm.starting_date" type="datetime" format="yyyy-MM-dd HH:mm:ss" placeholder="Please enter starting date" />
            </el-form-item>
          </el-col>

        </el-row>

        <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Description:">
          <el-input v-model="postForm.description" :rows="2" type="textarea" class="league-textarea" autosize placeholder="Please enter the description" />
        </el-form-item>

        <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Status:">
          <StatusDropdown :parentValue="this.postForm.league_status" v-model="postForm.league_status" @onStatusChange="onStatusChange"/>
        </el-form-item>

        <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Game:">
          <GameDropdown :parentValue="this.postForm.league_game" v-model="postForm.league_game" @onGameChange="onGameChange"/>
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
  import { fetchLeagues, createLeagues, updateLeagues } from '@/api/league'
  import { searchUser } from '@/api/remote-search'
  import { StatusDropdown, GameDropdown, SourceUrlDropdown } from './Dropdown'

  const defaultForm = {
    league_id: undefined,
    name: null,
    uri_name: null,
    description: null,
    price_pool: null,
    starting_date: null,
    banner_in_list_uri: undefined,
    banner_in_detail_uri: undefined,
    league_status: null,
    league_game: null,
    is_active: true,
    is_delete: false
  }

  export default {
    name: 'LeagueDetail',
    components: { Tinymce, MDinput, Upload, Sticky, StatusDropdown, GameDropdown },
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
        const league_id = this.$route.params && this.$route.params.id
        this.fetchData(league_id)
      }

      // Why need to make a copy of this.$route here?
      // Because if you enter this page and quickly switch tag, may be in the execution of the setTagsViewTitle function, this.$route is no longer pointing to the current page
      // https://github.com/PanJiaChen/vue-element-admin/issues/1221
      this.tempRoute = Object.assign({}, this.$route)
    },
    methods: {
      fetchData(league_id) {
        fetchLeagues(league_id).then(response => {
          this.postForm = response.data

          // just for test
          // this.postForm.title += `   League Id:${this.postForm.league_id}`
          // this.postForm.content_short += `   League Id:${this.postForm.league_id}`

          // set tagsview title
          this.setTagsViewTitle()

          // set page title
          this.setPageTitle()
        }).catch(err => {
          console.log(err)
        })
      },
      setTagsViewTitle() {
        const title = 'Edit League'
        const route = Object.assign({}, this.tempRoute, { title: `${title}-${this.postForm.league_id}` })
        this.$store.dispatch('tagsView/updateVisitedView', route)
      },
      setPageTitle() {
        const title = 'Edit League'
        document.title = `${title} - ${this.postForm.league_id}`
      },
      submitForm() {
        this.$refs.postForm.validate(valid => {
          if (valid) {
            if (this.isEdit) {
              this.postForm.league_id = this.$route.params.id
              updateLeagues(this.postForm).then(response => {
                this.$notify({
                  title: 'Success',
                  message: 'Success update league',
                  type: 'success',
                  duration: 2000
                })
                this.$router.push({ path: '/league/list' })
              }).catch(err => {
                console.log(err)
              })
            }
            else {
              createLeagues(this.postForm).then(response => {
                this.$notify({
                  title: 'Success',
                  message: 'Success create new league',
                  type: 'success',
                  duration: 2000
                })
                this.$router.push({ path: '/league/list' })
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
      onStatusChange(value) {
        this.postForm.league_status = value
      },
      onGameChange(value) {
        this.postForm.league_game = value
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

  .league-textarea /deep/ {
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
