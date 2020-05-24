import request from '@/utils/request'
import { getToken } from '@/utils/auth'

export function fetchList(query) {
  return request({
    url: 'http://127.0.0.1:8000/api/articles/',
    method: 'get',
    params: query,
    headers: {
      "Authorization": "Bearer " + getToken()
    }
  })
}

export function fetchArticle(id) {
  return request({
    url: `http://127.0.0.1:8000/api/articles/${id}/`,
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/vue-element-admin/article/pv',
    method: 'get',
    params: { pv }
  })
}

export function createArticle(data) {
  return request({
    url: 'http://127.0.0.1:8000/api/articles/',
    method: 'post',
    data
  })
}

export function updateArticle(data) {
  return request({
    url: `http://127.0.0.1:8000/api/articles/${data.article_id}/`,
    method: 'put',
    data
  })
}
