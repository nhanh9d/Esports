import request from '@/utils/request'
import { getToken } from '@/utils/auth'

export function fetchList(query) {
  return request({
    url: 'http://127.0.0.1:8000/api/teams/',
    method: 'get',
    params: query,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchActiveTeams() {
  return request({
    url: `http://127.0.0.1:8000/api/teams/get_active_teams/`,
    method: 'get'
  })
}

export function fetchTeam(id) {
  return request({
    url: `http://127.0.0.1:8000/api/teams/${id}/`,
    method: 'get',
    params: { id }
  })
}

export function createTeam(data) {
  return request({
    url: 'http://127.0.0.1:8000/api/teams/',
    method: 'post',
    data
  })
}

export function updateTeam(data) {
  return request({
    url: `http://127.0.0.1:8000/api/teams/${data.team_id}/`,
    method: 'put',
    data
  })
}

export function removeTeam(data) {
  return request({
    url: `http://127.0.0.1:8000/api/teams/${data.team_id}/`,
    method: 'delete'
  })
}
