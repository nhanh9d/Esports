import request from '@/utils/request'
import { getToken } from '@/utils/auth'
import baseApiUrl from '@/api/base-api-url'

export function getRoutes() {
  return request({
    url: `${baseApiUrl}/routes`,
    method: 'get',
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function getRoles() {
  return request({
    url: `${baseApiUrl}/roles`,
    method: 'get',
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function addRole(data) {
  return request({
    url: `${baseApiUrl}/role`,
    method: 'post',
    data,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function updateRole(id, data) {
  return request({
    url: `${baseApiUrl}/role/${id}`,
    method: 'put',
    data,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function deleteRole(id) {
  return request({
    url: `${baseApiUrl}/role/${id}`,
    method: 'delete',
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}
