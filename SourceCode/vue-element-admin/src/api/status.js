import request from '@/utils/request'
import { getToken } from '@/utils/auth'

export function fetchList(query) {
  return request({
    url: 'http://127.0.0.1:8000/api/status/',
    method: 'get',
    params: query,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchStatus(id) {
  return request({
    url: `http://127.0.0.1:8000/api/status/${id}/`,
    method: 'get',
    params: { id }
  })
}

export function createStatus(data) {
  return request({
    url: 'http://127.0.0.1:8000/api/status/',
    method: 'post',
    data
  })
}

export function updateStatus(data) {
  return request({
    url: `http://127.0.0.1:8000/api/status/${data.status_id}/`,
    method: 'put',
    data
  })
}
