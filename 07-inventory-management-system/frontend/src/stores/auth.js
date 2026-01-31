import { reactive } from 'vue';

export const authStore = reactive({
  user: {
    name: null,
    role: null,
  },
  session: {
    token: localStorage.getItem('token') || null,
  },

  setUser(name, role) {
    this.user.name = name;
    this.user.role = role;
  },

  setToken(token) {
    this.session.token = token;
    localStorage.setItem('token', token);
  },

  logout() {
    this.user.name = null;
    this.user.role = null;
    this.session.token = null;
    localStorage.removeItem('token');
  },

  get isLoggedIn() {
    return !!this.session.token;
  },
});
