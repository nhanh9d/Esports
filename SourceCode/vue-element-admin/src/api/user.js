import request from '@/utils/request'
import { getToken } from '@/utils/auth'
import baseApiUrl from '@/api/base-api-url'

export function login(data) {
  return request({
    url: `${baseApiUrl}auth/login/`,
    method: 'post',
    data,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function create(email, password, first_name, last_name, telephone_number) {
  return request({
    url: `${baseApiUrl}users/`,
    method: 'post',
    data: {
      email,
      password,
      first_name,
      last_name,
      profile: {
        telephoneNumber: telephone_number
      }
    },
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function edit(id, email, password, first_name, last_name, telephone_number) {
  return request({
    url: `${baseApiUrl}users/${id}`,
    method: 'put',
    data: {
      password,
      first_name,
      last_name,
      profile: {
        telephoneNumber: telephone_number
      }
    },
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function getInfo(id) {
  return request({
    url: `${baseApiUrl}users/${id}/`,
    method: 'get',
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function logout() {
  return request({
    url: `${baseApiUrl}auth/logout/`,
    method: 'post',
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchList(query) {
  return request({
    url: `${baseApiUrl}users/`,
    method: 'get',
    params: query,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}
