import request from '@/utils/request'
import { getToken } from '@/utils/auth'

export function fetchList(query) {
  return request({
    url: 'http://127.0.0.1:8000/api/region/',
    method: 'get',
    params: query,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchRegion(id) {
  return request({
    url: `http://127.0.0.1:8000/api/region/${id}/`,
    method: 'get',
    params: { id }
  })
}

export function createRegion(data) {
  return request({
    url: 'http://127.0.0.1:8000/api/region/',
    method: 'post',
    data
  })
}

export function updateRegion(data) {
  return request({
    url: `http://127.0.0.1:8000/api/region/${data.region_id}/`,
    method: 'put',
    data
  })
}
