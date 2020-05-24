<template>
  <div class="app-container">
    <el-table v-loading="listLoading" :data="list" border fit highlight-current-row style="width: 100%">
      <el-table-column align="center" label="ID" width="180">
        <template slot-scope="scope">
          <span>{{ scope.row.region_id }}</span>
        </template>
      </el-table-column>

      <el-table-column min-width="300px" label="Title">
        <template slot-scope="{row}">
          <router-link :to="'/region/edit/'+row.region_id" class="link-type">
            <span>{{ row.name }}</span>
          </router-link>
        </template>
      </el-table-column>

      <el-table-column width="180px" align="center" label="Active">
        <template slot-scope="scope">
          <span>{{ scope.row.is_active }}</span>
        </template>
      </el-table-column>

      <el-table-column width="180px" align="center" label="Deleted">
        <template slot-scope="scope">
          <span>{{ scope.row.is_delete }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="Actions" width="240">
        <template slot-scope="scope">
          <router-link :to="'/region/edit/'+scope.row.region_id">
            <el-button type="primary" size="mini" icon="el-icon-edit">
              Edit
            </el-button>
          </router-link>
          <el-button v-if="!scope.row.is_delete" size="mini" type="danger" icon="el-icon-delete" @click="handleDelete(scope.row, scope.$index)">
            Delete
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />
  </div>
</template>

<script>
  import { fetchList, updateRegion } from '@/api/region'
  import Pagination from '@/components/Pagination' // Secondary package based on el-pagination
  import moment from 'moment'

  export default {
    name: 'RegionList',
    components: { Pagination },
    data() {
      return {
        list: null,
        total: 0,
        listLoading: true,
        listQuery: {
          page: 1,
          limit: 20
        }
      }
    },
    created() {
      this.getList()
    },
    methods: {
      format_date(value){
         if (value) {
           return moment(String(value)).format('DD/MM/YYYY hh:mm')
         }
      },
      getList() {
        this.listLoading = true
        fetchList(this.listQuery).then(response => {
          this.list = response.data.results
          this.total = response.data.count
          this.listLoading = false
        })
      },
      handleDelete(row, index) {
        updateRegion({region_id:row.region_id, name:row.name, is_active:row.is_active, is_delete:true}).then(response => {
          this.$notify({
            title: 'Success',
            message: 'Delete Successfully',
            type: 'success',
            duration: 2000
          })
          this.list.splice(index, 1)
        }).catch(err => {
          console.log(err)
        })
      }
    }
  }
</script>

<style scoped>
  .edit-input {
    padding-right: 100px;
  }

  .cancel-btn {
    position: absolute;
    right: 15px;
    top: 10px;
  }
</style>
