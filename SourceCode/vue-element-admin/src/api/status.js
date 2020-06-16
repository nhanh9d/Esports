import request from '@/utils/request'
import { getToken } from '@/utils/auth'
import baseApiUrl from '@/api/base-api-url'

export function fetchList(query) {
  return request({
    url: `${baseApiUrl}status/`,
    method: 'get',
    params: query,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchActiveStatus() {
  return request({
    url: `${baseApiUrl}status/get_active_status/`,
    method: 'get',
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchStatus(id) {
  return request({
    url: `${baseApiUrl}status/${id}/`,
    method: 'get',
    params: { id },
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function createStatus(data) {
  return request({
    url: `${baseApiUrl}status/`,
    method: 'post',
    data,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function updateStatus(data) {
  return request({
    url: `${baseApiUrl}status/${data.status_id}/`,
    method: 'put',
    data,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function removeStatus(data) {
  return request({
    url: `${baseApiUrl}status/${data.status_id}/`,
    method: 'delete',
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}
