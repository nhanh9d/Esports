<template>
  <div class="createPost-container">
    <el-form ref="postForm" :model="postForm" :rules="rules" class="form-container">

      <div class="createPost-main-container">

        <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Game name:">
          <el-input v-model="postForm.name" type="text" autosize placeholder="Please enter the name of game" @change="changeUriName(postForm)"/>
        </el-form-item>

        <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Uri name:">
          <el-input v-model="postForm.uri_name" type="text" readonly autosize placeholder="Please enter the uri of game" />
        </el-form-item>

        <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Description:">
          <el-input v-model="postForm.description" :rows="5" type="textarea" class="article-textarea" placeholder="Please enter the description of game" />
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
  import { fetchGame, createGame, updateGame } from '@/api/game'

  const defaultForm = {
    game_id: undefined,
    name: 'game name',
    uri_name: 'game-name',
    description: 'description',
    is_active: true,
    is_delete: false
  }

  export default {
    name: 'GameDetail',
    components: { },
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
          name: [{ validator: validateRequire }]
        },
        tempRoute: {}
      }
    },
    computed: {
    },
    created() {
      if (this.isEdit) {
        const game_id = this.$route.params && this.$route.params.id
        this.fetchData(game_id)
      }

      // Why need to make a copy of this.$route here?
      // Because if you enter this page and quickly switch tag, may be in the execution of the setTagsViewTitle function, this.$route is no longer pointing to the current page
      // https://github.com/PanJiaChen/vue-element-admin/issues/1221
      this.tempRoute = Object.assign({}, this.$route)
    },
    methods: {
      fetchData(game_id) {
        fetchGame(game_id).then(response => {
          this.postForm = response.data

          // just for test
          // this.postForm.title += `   Game Id:${this.postForm.game_id}`
          // this.postForm.content_short += `   Game Id:${this.postForm.game_id}`


          // set page title
          this.setPageTitle()
        }).catch(err => {
          console.log(err)
        })
      },
      setPageTitle() {
        const title = 'Edit Game'
        document.title = `${title} - ${this.postForm.game_id}`
      },
      submitForm() {
        this.$refs.postForm.validate(valid => {
          if (valid) {
            console.log(this.postForm)
            if (this.isEdit) {
              updateGame(this.postForm).then(response => {
                this.$notify({
                  title: 'Success',
                  message: 'Success update game',
                  type: 'success',
                  duration: 2000
                })
                this.$router.push({ path: '/game/list' })
              }).catch(err => {
                console.log(err)
              })
            }
            else {
              createGame(this.postForm).then(response => {
                this.$notify({
                  title: 'Success',
                  message: 'Success create new game',
                  type: 'success',
                  duration: 2000
                })
                this.$router.push({ path: '/game/list' })
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

  .game-textarea /deep/ {
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
