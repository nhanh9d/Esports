import request from '@/utils/request'
import { getToken } from '@/utils/auth'
import baseApiUrl from '@/api/base-api-url'

export function fetchList(query) {
  return request({
    url: `${baseApiUrl}teams/`,
    method: 'get',
    params: query,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchActiveTeams() {
  return request({
    url: `${baseApiUrl}teams/get_active_teams/`,
    method: 'get',
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchTeam(id) {
  return request({
    url: `${baseApiUrl}teams/${id}/`,
    method: 'get',
    params: { id },
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function createTeam(data) {
  return request({
    url: `${baseApiUrl}teams/`,
    method: 'post',
    data,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function updateTeam(data) {
  return request({
    url: `${baseApiUrl}teams/${data.team_id}/`,
    method: 'put',
    data,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function removeTeam(data) {
  return request({
    url: `${baseApiUrl}teams/${data.team_id}/`,
    method: 'delete',
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}
