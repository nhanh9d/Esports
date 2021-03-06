<template>
  <div class="createPost-container">
    <el-form ref="postForm" :model="postForm" :rules="rules" class="form-container">

      <sticky :z-index="10" :class-name="'sub-navbar '+postForm.status">
        <el-button v-loading="loading" style="margin-right: 25px;" type="success" @click="submitForm">
          Publish
        </el-button>
      </sticky>

      <div class="createPost-main-container">
        <el-row>

          <el-col :span="24">
            <el-form-item style="margin-bottom: 40px;" prop="title">
              <MDinput v-model="postForm.title" :maxlength="100" name="name" required>
                Title
              </MDinput>
            </el-form-item>

            <div class="postInfo-container">
              <el-row>
                <el-col :span="10">
                  <el-form-item label-width="120px" label="Publish Time:" class="postInfo-container-item">
                    <el-date-picker v-model="postForm.display_time" type="datetime" format="yyyy-MM-dd HH:mm:ss" placeholder="Select date and time" />
                  </el-form-item>
                </el-col>

                <el-col :span="6">
                  <el-form-item label-width="90px" label="Importance:" class="postInfo-container-item">
                    <el-rate v-model="postForm.importance"
                             :max="3"
                             :colors="['#99A9BF', '#F7BA2A', '#FF9900']"
                             :low-threshold="1"
                             :high-threshold="3"
                             style="display:inline-block" />
                  </el-form-item>
                </el-col>
              </el-row>
            </div>
          </el-col>
        </el-row>

        <el-form-item style="margin-bottom: 40px;" label-width="70px" label="Summary:">
          <el-input v-model="postForm.content_short" :rows="1" type="textarea" class="article-textarea" autosize placeholder="Please enter the content" />
          <span v-show="contentShortLength" class="word-counter">{{ contentShortLength }}words</span>
        </el-form-item>

        <el-form-item prop="content" style="margin-bottom: 30px;">
          <Tinymce ref="editor" v-model="postForm.content" :height="400" />
        </el-form-item>

        <el-form-item prop="image_uri" style="margin-bottom: 30px;">
          <Upload v-model="postForm.image_uri" />
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
  import { fetchArticle, createArticle, updateArticle } from '@/api/article'

  const defaultForm = {
    status: 'draft',
    title: '',
    content: '',
    content_short: '',
    source_uri: '',
    image_uri: '',
    display_time: undefined,
    article_id: undefined,
    importance: 0
  }

  export default {
    name: 'ArticleDetail',
    components: { Tinymce, MDinput, Upload, Sticky },
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
      contentShortLength() {
        return this.postForm.content_short.length
      },
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
        const article_id = this.$route.params && this.$route.params.id
        this.fetchData(article_id)
      }

      // Why need to make a copy of this.$route here?
      // Because if you enter this page and quickly switch tag, may be in the execution of the setTagsViewTitle function, this.$route is no longer pointing to the current page
      // https://github.com/PanJiaChen/vue-element-admin/issues/1221
      this.tempRoute = Object.assign({}, this.$route)
    },
    methods: {
      fetchData(article_id) {
        fetchArticle(article_id).then(response => {
          this.postForm = response.data

          // just for test
          // this.postForm.title += `   Article Id:${this.postForm.article_id}`
          // this.postForm.content_short += `   Article Id:${this.postForm.article_id}`

          // set tagsview title
          this.setTagsViewTitle()

          // set page title
          this.setPageTitle()
        }).catch(err => {
          console.log(err)
        })
      },
      setTagsViewTitle() {
        const title = 'Edit Article'
        const route = Object.assign({}, this.tempRoute, { title: `${title}-${this.postForm.article_id}` })
        this.$store.dispatch('tagsView/updateVisitedView', route)
      },
      setPageTitle() {
        const title = 'Edit Article'
        document.title = `${title} - ${this.postForm.article_id}`
      },
      submitForm() {
        this.$refs.postForm.validate(valid => {
          if (valid) {
            console.log(this.postForm)
            if (this.isEdit) {
              updateArticle(this.postForm).then(response => {
                this.$notify({
                  title: 'Success',
                  message: 'Success update article',
                  type: 'success',
                  duration: 2000
                })
                this.$router.push({ path: '/article/list' })
              }).catch(err => {
                console.log(err)
              })
            }
            else {
              createArticle(this.postForm).then(response => {
                this.$notify({
                  title: 'Success',
                  message: 'Success create new article',
                  type: 'success',
                  duration: 2000
                })
                this.$router.push({ path: '/article/list' })
              }).catch(err => {
                console.log(err)
              })
            }
          } else {
            console.log('error submit!!')
            return false
          }
        })
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

  .article-textarea /deep/ {
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
