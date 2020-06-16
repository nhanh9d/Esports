import request from '@/utils/request'
import { getToken } from '@/utils/auth'
import baseApiUrl from '@/api/base-api-url'

export function fetchList(query) {
  return request({
    url: `${baseApiUrl}articles/`,
    method: 'get',
    params: query,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchArticle(id) {
  return request({
    url: `${baseApiUrl}articles/${id}/`,
    method: 'get',
    params: { id },
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/vue-element-admin/article/pv',
    method: 'get',
    params: { pv },
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function createArticle(data) {
  return request({
    url: `${baseApiUrl}articles/`,
    method: 'post',
    data,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function updateArticle(data) {
  return request({
    url: `${baseApiUrl}articles/${data.article_id}/`,
    method: 'put',
    data,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}
