<template>
  <div class="app-container">
    <el-table v-loading="listLoading" :data="list" border fit highlight-current-row style="width: 100%">
      <el-table-column align="center" label="ID">
        <template slot-scope="scope">
          <span>{{ scope.row.team_id }}</span>
        </template>
      </el-table-column>

      <el-table-column min-width="300px" label="Team name">
        <template slot-scope="{row}">
          <router-link :to="'/team/edit/'+row.team_id" class="link-type">
            <span>{{ row.name }}</span>
          </router-link>
        </template>
      </el-table-column>

      <el-table-column align="center" label="Team short name">
        <template slot-scope="{row}">
          <span>{{ row.short_name }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="World rank">
        <template slot-scope="{row}">
          <span>{{ row.world_rank }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="Region rank">
        <template slot-scope="{row}">
          <span>{{ row.region_rank }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="Total earning">
        <template slot-scope="{row}">
          <span>{{ row.total_earnings }}$</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="Win rate">
        <template slot-scope="{row}">
          <span>{{ row.win_rate }}%</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="Starting Date">
        <template slot-scope="scope">
          <span>{{ format_date(scope.row.starting_date) }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="Actions" width="120">
        <template slot-scope="scope">
          <router-link :to="'/team/edit/'+scope.row.team_id">
            <el-button type="primary" size="small" icon="el-icon-edit">
              Edit
            </el-button>
          </router-link>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />
  </div>
</template>

<script>
  import { fetchList } from '@/api/team'
  import Pagination from '@/components/Pagination' // Secondary package based on el-pagination
  import moment from 'moment'

  export default {
    name: 'TeamList',
    components: { Pagination },
    filters: {
      statusFilter(status) {
        const statusMap = {
          published: 'success',
          draft: 'info',
          deleted: 'danger'
        }
        return statusMap[status]
      }
    },
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
