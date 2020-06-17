<template>
  <div class="createPost-container">
    <el-form ref="postForm" :model="postForm" :rules="rules" class="form-container">

      <div class="createPost-main-container">

        <el-form-item style="margin-bottom: 40px;" label-width="150px" label="Region name:">
          <el-input v-model="postForm.name" type="text" autosize placeholder="Please enter the name of region" />
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
  import { fetchRegion, createRegion, updateRegion } from '@/api/region'

  const defaultForm = {
    region_id: undefined,
    name: 'region name',
    is_active: true,
    is_delete: false
  }

  export default {
    name: 'RegionDetail',
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
        const region_id = this.$route.params && this.$route.params.id
        this.fetchData(region_id)
      }

      // Why need to make a copy of this.$route here?
      // Because if you enter this page and quickly switch tag, may be in the execution of the setTagsViewTitle function, this.$route is no longer pointing to the current page
      // https://github.com/PanJiaChen/vue-element-admin/issues/1221
      this.tempRoute = Object.assign({}, this.$route)
    },
    methods: {
      fetchData(region_id) {
        fetchRegion(region_id).then(response => {
          this.postForm = response.data

          // just for test
          // this.postForm.title += `   Region Id:${this.postForm.region_id}`
          // this.postForm.content_short += `   Region Id:${this.postForm.region_id}`


          // set page title
          this.setPageTitle()
        }).catch(err => {
          console.log(err)
        })
      },
      setPageTitle() {
        const title = 'Edit Region'
        document.title = `${title} - ${this.postForm.region_id}`
      },
      submitForm() {
        this.$refs.postForm.validate(valid => {
          if (valid) {
            console.log(this.postForm)
            if (this.isEdit) {
              updateRegion(this.postForm).then(response => {
                this.$notify({
                  title: 'Success',
                  message: 'Success update region',
                  type: 'success',
                  duration: 2000
                })
                this.$router.push({ path: '/region/list' })
              }).catch(err => {
                console.log(err)
              })
            }
            else {
              createRegion(this.postForm).then(response => {
                this.$notify({
                  title: 'Success',
                  message: 'Success create new region',
                  type: 'success',
                  duration: 2000
                })
                this.$router.push({ path: '/region/list' })
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
      toggleIsActive(val) {
        val.is_active = !val.is_active
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

  .region-textarea /deep/ {
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
