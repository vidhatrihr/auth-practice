<script>
import { api } from '@/utils/api';
import { authStore } from '@/stores/auth';

export default {
  name: 'LoginView',
  data() {
    return {
      email: '',
      password: '',
      error: null,
    };
  },
  methods: {
    async handleLogin() {
      this.error = null;

      const data = await api('post', '/auth/login', {
        email: this.email,
        password: this.password,
      });

      if (data.success) {
        authStore.setToken(data.data.token);
        authStore.setUser(data.data.name, data.data.role);

        // Redirect based on role
        if (data.data.role === 'admin') {
          this.$router.push('/admin');
        } else if (data.data.role === 'manager') {
          this.$router.push('/manager');
        } else {
          this.$router.push('/');
        }
      } else {
        this.error = data.message;
      }
    },
  },
};
</script>

<template>
  <div class="login-container">
    <div class="login-card">
      <h1 class="title">Welcome Back</h1>
      <p class="subtitle">Sign in to your account</p>

      <form class="login-form" @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="email">Email</label>
          <input v-model="email" type="email" id="email" placeholder="name@company.com" />
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <input
            v-model="password"
            type="password"
            id="password"
            placeholder="••••••••"
          />
        </div>

        <p v-if="error" class="error-message">{{ error }}</p>

        <button type="submit" class="btn-primary">Sign In</button>
      </form>
    </div>
  </div>
</template>

<style scoped>
.login-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.login-card {
  background: var(--card-bg);
  backdrop-filter: blur(10px);
  padding: 3rem;
  border-radius: 1rem;
  border: 1px solid var(--card-border);
  width: 100%;
  max-width: 450px;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
}

.title {
  font-size: 2rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 0.5rem;
  color: var(--text-primary);
}

.subtitle {
  text-align: center;
  color: var(--text-secondary);
  margin-bottom: 2.5rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: var(--text-heading);
  font-size: 0.9rem;
  font-weight: 500;
}

input {
  width: 100%;
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
  border: 1px solid var(--card-border);
  background: rgba(15, 23, 42, 0.5);
  color: var(--text-primary);
  font-family: inherit;
  font-size: 1rem;
  transition:
    border-color 0.2s,
    box-shadow 0.2s;
}

input:focus {
  outline: none;
  border-color: var(--color-blue-400);
  box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.2);
}

.error-message {
  color: #ef4444;
  font-size: 0.875rem;
  margin-bottom: 1rem;
  text-align: center;
}

.btn-primary {
  width: 100%;
  padding: 0.875rem;
  margin-top: 1rem;
  border-radius: 0.5rem;
  border: none;
  background: linear-gradient(
    135deg,
    var(--color-blue-400) 0%,
    var(--color-violet-400) 100%
  );
  color: white;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition:
    opacity 0.2s,
    transform 0.1s;
}

.btn-primary:hover {
  opacity: 0.9;
}

.btn-primary:active {
  transform: translateY(1px);
}
</style>
