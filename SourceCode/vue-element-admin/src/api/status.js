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

export function fetchActiveStatus() {
  return request({
    url: `http://127.0.0.1:8000/api/status/get_active_status/`,
    method: 'get'
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

export function removeStatus(data) {
  return request({
    url: `http://127.0.0.1:8000/api/status/${data.status_id}/`,
    method: 'delete'
  })
}
