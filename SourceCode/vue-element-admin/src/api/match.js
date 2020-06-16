import request from '@/utils/request'
import { getToken } from '@/utils/auth'
import baseApiUrl from '@/api/base-api-url'

export function fetchList(query) {
  return request({
    url: `${baseApiUrl}matches/`,
    method: 'get',
    params: query,
    headers: {
      "Authorization": `Bearer ${getToken()}`
    }
  })
}

export function fetchMatches(id) {
  return request({
    url: `${baseApiUrl}matches/${id}/`,
    method: 'get',
    params: { id },
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function createMatches(data) {
	console.log(data)
  return request({
    url: `${baseApiUrl}matches/`,
    method: 'post',
    data,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function updateMatches(data) {
  return request({
    url: `${baseApiUrl}matches/${data.team_id}/`,
    method: 'put',
    data,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function removeMatches(data) {
  return request({
    url: `${baseApiUrl}matches/${data.team_id}/`,
    method: 'delete',
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}
