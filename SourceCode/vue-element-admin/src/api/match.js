import request from '@/utils/request'
import { getToken } from '@/utils/auth'

export function fetchList(query) {
  return request({
    url: 'http://127.0.0.1:8000/api/matches/',
    method: 'get',
    params: query,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchMatches(id) {
  return request({
    url: `http://127.0.0.1:8000/api/matches/${id}/`,
    method: 'get',
    params: { id }
  })
}

export function createMatches(data) {
  return request({
    url: 'http://127.0.0.1:8000/api/matches/',
    method: 'post',
    data
  })
}

export function updateMatches(data) {
  return request({
    url: `http://127.0.0.1:8000/api/matches/${data.team_id}/`,
    method: 'put',
    data
  })
}

export function removeMatches(data) {
  return request({
    url: `http://127.0.0.1:8000/api/matches/${data.team_id}/`,
    method: 'delete'
  })
}
