<template>
  <div class="createPost-container">
    <el-form ref="postForm" :model="postForm" :rules="rules" class="form-container">

      <div class="createPost-main-container">
        <el-row>

          <el-col :span="24">

            <div class="postInfo-container">
              <el-row>

                <el-col :span="11">
                  <el-form-item style="margin-bottom: 40px;" prop="email">
                    <MDinput v-model="postForm.email" :maxlength="100" :type="'email'" name="name" required>
                      Email
                    </MDinput>
                  </el-form-item>
                </el-col>

                <el-col :span="1">
                  <el-form-item style="margin-bottom: 40px;">
                  </el-form-item>
                </el-col>
                <el-col :span="1">
                  <el-form-item style="margin-bottom: 40px;">
                  </el-form-item>
                </el-col>

                <el-col :span="11">
                  <el-form-item style="margin-bottom: 40px;" prop="password">
                    <MDinput v-model="postForm.password" :maxlength="100" :type="'password'" name="name" required>
                      Password
                    </MDinput>
                  </el-form-item>
                </el-col>

              </el-row>
            </div>

            <div class="postInfo-container">
              <el-row>

                <el-col :span="11">
                  <el-form-item style="margin-bottom: 40px;" prop="first_name">
                    <MDinput v-model="postForm.first_name" :maxlength="100" name="name" required>
                      First Name
                    </MDinput>
                  </el-form-item>
                </el-col>

                <el-col :span="1">
                  <el-form-item style="margin-bottom: 40px;">
                  </el-form-item>
                </el-col>
                <el-col :span="1">
                  <el-form-item style="margin-bottom: 40px;">
                  </el-form-item>
                </el-col>

                <el-col :span="11">
                  <el-form-item style="margin-bottom: 40px;" prop="last_name">
                    <MDinput v-model="postForm.last_name" :maxlength="100" name="name" required>
                      Last Name
                    </MDinput>
                  </el-form-item>
                </el-col>

              </el-row>
            </div>

            <div class="postInfo-container">
              <el-row>

                <el-col :span="11">
                  <el-form-item style="margin-bottom: 40px;" prop="telephone_number">
                    <MDinput v-model="postForm.telephone_number" :maxlength="100" :type="'tel'" name="name" required>
                      Telephone number
                    </MDinput>
                  </el-form-item>
                </el-col>

              </el-row>
            </div>

            <div class="postInfo-container">
              <el-row>

                <el-col :span="11">
                  <el-button v-loading="loading" type="success" @click="submitForm">
                    Submit
                  </el-button>
                </el-col>

              </el-row>
            </div>

          </el-col>
        </el-row>

      </div>
    </el-form>
  </div>
</template>

<script>
  import MDinput from '@/components/MDinput'
  import { getInfo } from '@/api/user'

  const defaultForm = {
    id: undefined,
    email: '',
    password: '',
    first_name: '',
    last_name: '',
    telephone_number: ''
  }

  export default {
    name: 'UsersDetail',
    components: { MDinput }, //Upload
    props: {
      isEdit: {
        type: Boolean,
        default: false
      },
      idEdit: {
        type: Number,
        default: -1
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
          email: [{ validator: validateRequire }],
          password: [{ validator: validateRequire }],
        },
        tempRoute: {}
      }
    },
    computed: {

    },
    created() {
      if (this.isEdit) {
        const id = this.$route.params && this.$route.params.id
        this.fetchData(id)
      }

      // Why need to make a copy of this.$route here?
      // Because if you enter this page and quickly switch tag, may be in the execution of the setTagsViewTitle function, this.$route is no longer pointing to the current page
      // https://github.com/PanJiaChen/vue-element-admin/issues/1221
      this.tempRoute = Object.assign({}, this.$route)
    },
    methods: {
      fetchData(id) {
        getInfo(id).then(response => {
          this.postForm = response.data
          this.postForm.id = id

          // just for test
          //this.postForm.title += `   Users Id:${this.postForm.id}`
          //this.postForm.content_short += `   Users Id:${this.postForm.id}`

          // set tagsview title
          this.setTagsViewTitle()

          // set page title
          this.setPageTitle()
        }).catch(err => {
          console.log(err)
        })
      },
      setTagsViewTitle() {
        const title = 'Edit User'
        const route = Object.assign({}, this.tempRoute, { title: `${title}-${this.postForm.email}` })
        this.$store.dispatch('tagsView/updateVisitedView', route)
      },
      setPageTitle() {
        const title = 'Edit User'
        document.title = `${title} - ${this.postForm.email}`
      },
      submitForm() {
        this.$refs.postForm.validate(valid => {
          if (valid) {
            this.loading = true
            this.$store.dispatch(this.isEdit ? 'user/edit' : 'user/create', this.postForm)
              .then(() => {
                const message = this.isEdit ? 'Success edit account' : 'Success register new account'
                this.$notify({
                  title: 'Success',
                  message: message,
                  type: 'success',
                  duration: 2000
                })
                this.$router.push({ path: '/users/list' })
              })
              .catch(() => {
                this.loading = false
              })
          } else {
            console.log('error submit!!')
            return false
          }
        })
      },
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

  .users-textarea /deep/ {
    textarea

  {
    padding-right: 40px;
    resize: none;
    border: none;
    border-radius: 0px;
    border-bottom: 1px solid #bfcbd9;
  }
  }
</style>
