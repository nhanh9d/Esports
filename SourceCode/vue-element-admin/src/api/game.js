import request from '@/utils/request'
import { getToken } from '@/utils/auth'

export function fetchList(query) {
  return request({
    url: 'http://127.0.0.1:8000/api/games/',
    method: 'get',
    params: query,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchGame(id) {
  return request({
    url: `http://127.0.0.1:8000/api/games/${id}/`,
    method: 'get',
    params: { id }
  })
}

export function createGame(data) {
  return request({
    url: 'http://127.0.0.1:8000/api/games/',
    method: 'post',
    data
  })
}

export function updateGame(data) {
  return request({
    url: `http://127.0.0.1:8000/api/games/${data.game_id}/`,
    method: 'put',
    data
  })
}

export function removeGame(data) {
  return request({
    url: `http://127.0.0.1:8000/api/games/${data.game_id}/`,
    method: 'delete'
  })
}
