import { login, logout, getInfo, create, edit } from '@/api/user'
import { getToken, setToken, removeToken, getId, setId, removeId } from '@/utils/auth'
import router, { resetRouter } from '@/router'

const state = {
  id: getId(),
  token: getToken(),
  name: '',
  avatar: '',
  introduction: '',
  roles: []
}

const mutations = {
  SET_ID: (state, id) => {
    state.id = id
  },
  SET_TOKEN: (state, token) => {
    state.token = token
  },
  SET_INTRODUCTION: (state, introduction) => {
    state.introduction = introduction
  },
  SET_NAME: (state, name) => {
    state.name = name
  },
  SET_AVATAR: (state, avatar) => {
    state.avatar = avatar
  },
  SET_ROLES: (state, roles) => {
    state.roles = roles
  }
}

const actions = {
  // user login
  login({ commit }, userInfo) {
    const { email, password } = userInfo
    return new Promise((resolve, reject) => {
      login({ username: '', email: email.trim(), password: password }).then(response => {
        const { data } = response
        commit('SET_TOKEN', data.token)
        commit('SET_ID', data.user.pk)
        setToken(data.token)
        setId(data.user.pk)
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get user info
  getInfo({ commit, state }) {
    return new Promise((resolve, reject) => {
      getInfo(state.id).then(response => {
        const { data } = response

        if (!data) {
          reject('Verification failed, please Login again.')
        }

        //const { roles, name, avatar, introduction } = data
        const dataFake = {
          roles: ['admin'],
          introduction: 'I am a super administrator',
          avatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
          name: 'Super Admin'
        }
        const { roles, name, avatar, introduction } = dataFake

        // roles must be a non-empty array
        //if (!roles || roles.length <= 0) {
        //  reject('getInfo: roles must be a non-null array!')
        //}

        commit('SET_ROLES', roles)
        commit('SET_NAME', name)
        commit('SET_AVATAR', avatar)
        commit('SET_INTRODUCTION', introduction)
        resolve(dataFake)
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user create
  create({ commit }, postForm) {
    const { email, password, first_name, last_name, telephone_number } = postForm
    return new Promise((resolve, reject) => {
      create(email, password, first_name, last_name, telephone_number).then(() => {
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user edit
  edit({ commit }, postForm) {
    const { email, password, first_name, last_name, telephone_number } = postForm
    return new Promise((resolve, reject) => {
      edit(email, password, first_name, last_name, telephone_number).then(() => {
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user logout
  logout({ commit, state, dispatch }) {
    return new Promise((resolve, reject) => {
      logout(state.token).then(() => {
        commit('SET_TOKEN', '')
        commit('SET_ROLES', [])
        removeToken()
        resetRouter()

        // reset visited views and cached views
        // to fixed https://github.com/PanJiaChen/vue-element-admin/issues/2485
        dispatch('tagsView/delAllViews', null, { root: true })

        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // remove token
  resetToken({ commit }) {
    return new Promise(resolve => {
      commit('SET_TOKEN', '')
      commit('SET_ROLES', [])
      removeToken()
      resolve()
    })
  },

  // dynamically modify permissions
  changeRoles({ commit, dispatch }, role) {
    return new Promise(async resolve => {
      const token = role + '-token'

      commit('SET_TOKEN', token)
      setToken(token)

      const { roles } = await dispatch('getInfo')

      resetRouter()

      // generate accessible routes map based on roles
      const accessRoutes = await dispatch('permission/generateRoutes', roles, { root: true })

      // dynamically add accessible routes
      router.addRoutes(accessRoutes)

      // reset visited views and cached views
      dispatch('tagsView/delAllViews', null, { root: true })

      resolve()
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
