import request from '@/utils/request'
import { getToken } from '@/utils/auth'

export function fetchList(query) {
  return request({
    url: 'http://127.0.0.1:8000/api/leagues/',
    method: 'get',
    params: query,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchActiveLeagues() {
  return request({
    url: `http://127.0.0.1:8000/api/leagues/get_active_leagues/`,
    method: 'get'
  })
}

export function fetchLeagues(id) {
  return request({
    url: `http://127.0.0.1:8000/api/leagues/${id}/`,
    method: 'get',
    params: { id }
  })
}

export function createLeagues(data) {
  return request({
    url: 'http://127.0.0.1:8000/api/leagues/',
    method: 'post',
    data
  })
}

export function updateLeagues(data) {
  return request({
    url: `http://127.0.0.1:8000/api/leagues/${data.team_id}/`,
    method: 'put',
    data
  })
}

export function removeLeagues(data) {
  return request({
    url: `http://127.0.0.1:8000/api/leagues/${data.team_id}/`,
    method: 'delete'
  })
}
