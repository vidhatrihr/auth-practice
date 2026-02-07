import { reactive } from 'vue';

const storedUser = JSON.parse(localStorage.getItem('user')) || {};

export const authStore = reactive({
  user: {
    name: storedUser.name || null,
    role: storedUser.role || null,
  },
  session: {
    token: localStorage.getItem('token') || null,
  },

  setUser(name, role) {
    this.user = { name, role };
    localStorage.setItem('user', JSON.stringify(this.user));
  },

  setToken(token) {
    this.session.token = token;
    localStorage.setItem('token', token);
  },

  logout() {
    this.user = {
      name: null,
      role: null,
    };
    this.session.token = null;
    localStorage.removeItem('user');
    localStorage.removeItem('token');
  },

  get isLoggedIn() {
    return !!this.session.token;
  },
});
