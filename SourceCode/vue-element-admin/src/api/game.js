import request from '@/utils/request'
import { getToken } from '@/utils/auth'
import baseApiUrl from '@/api/base-api-url'

export function fetchList(query) {
  return request({
    url: `${baseApiUrl}games/`,
    method: 'get',
    params: query,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchActiveGame() {
  return request({
    url: `${baseApiUrl}games/get_active_games/`,
    method: 'get',
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchGame(id) {
  return request({
    url: `${baseApiUrl}games/${id}/`,
    method: 'get',
    params: { id },
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function createGame(data) {
  return request({
    url: `${baseApiUrl}games/`,
    method: 'post',
    data,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function updateGame(data) {
  return request({
    url: `${baseApiUrl}games/${data.game_id}/`,
    method: 'put',
    data,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function removeGame(data) {
  return request({
    url: `${baseApiUrl}games/${data.game_id}/`,
    method: 'delete',
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}
