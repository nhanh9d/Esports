import request from '@/utils/request'
import { getToken } from '@/utils/auth'

export function login(data) {
  return request({
    url: 'http://127.0.0.1:8000/api/auth/login/',
    method: 'post',
    data
  })
}

export function create(email, password, first_name, last_name, telephone_number) {
  return request({
    url: 'http://127.0.0.1:8000/api/users/',
    method: 'post',
    data: {
      email,
      password,
      first_name,
      last_name,
      profile: {
        telephoneNumber: telephone_number
      }
    }
  })
}

export function edit(id, email, password, first_name, last_name, telephone_number) {
  return request({
    url: `http://127.0.0.1:8000/api/users/${id}`,
    method: 'put',
    data: {
      password,
      first_name,
      last_name,
      profile: {
        telephoneNumber: telephone_number
      }
    }
  })
}

export function getInfo(id) {
  return request({
    url: `http://127.0.0.1:8000/api/users/${id}/`,
    method: 'get',
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function logout() {
  return request({
    url: 'http://127.0.0.1:8000/api/auth/logout/',
    method: 'post'
  })
}

export function fetchList(query) {
  return request({
    url: 'http://127.0.0.1:8000/api/users/',
    method: 'get',
    params: query,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}
