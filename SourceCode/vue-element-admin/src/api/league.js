import request from '@/utils/request'
import { getToken } from '@/utils/auth'
import baseApiUrl from '@/api/base-api-url'

export function fetchList(query) {
  return request({
    url: `${baseApiUrl}leagues/`,
    method: 'get',
    params: query,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchActiveLeagues() {
  return request({
    url: `${baseApiUrl}leagues/get_active_leagues/`,
    method: 'get',
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchLeagues(id) {
  return request({
    url: `${baseApiUrl}leagues/${id}/`,
    method: 'get',
    params: { id },
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function createLeagues(data) {
  return request({
    url: `${baseApiUrl}leagues/`,
    method: 'post',
    data,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function updateLeagues(data) {
  return request({
    url: `${baseApiUrl}leagues/${data.team_id}/`,
    method: 'put',
    data,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function removeLeagues(data) {
  return request({
    url: `${baseApiUrl}leagues/${data.team_id}/`,
    method: 'delete',
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}
