<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { api } from '@/utils/api';
import { authStore } from '@/stores/auth';
import { Icon } from '@iconify/vue';

const router = useRouter();

const email = ref('');
const password = ref('');
const error = ref(null);

async function handleLogin() {
  error.value = null;

  const res = await api('post', '/auth/login', {
    email: email.value,
    password: password.value,
  });

  if (res.success) {
    authStore.setToken(res.data.token);
    authStore.setUser(res.data.name, res.data.role);

    // Redirect based on role
    if (res.data.role === 'admin') {
      router.push('/admin');
    } else if (res.data.role === 'manager') {
      router.push('/manager');
    } else {
      router.push('/');
    }
  } else {
    error.value = res.message;
  }
}
</script>

<template>
  <div class="login-container">
    <div class="login-card">
      <h1 class="title">Welcome Back</h1>
      <p class="subtitle">Sign in to your account</p>

      <form class="login-form" @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="email"
            ><span class="icon-text"><Icon icon="mdi:email" /> Email</span></label
          >
          <input v-model="email" type="email" id="email" placeholder="name@company.com" />
        </div>

        <div class="form-group">
          <label for="password"
            ><span class="icon-text"><Icon icon="mdi:lock" /> Password</span></label
          >
          <input
            v-model="password"
            type="password"
            id="password"
            placeholder="••••••••"
          />
        </div>

        <p v-if="error" class="error-message">{{ error }}</p>

        <button type="submit" class="btn-primary">
          <span class="icon-text"><Icon icon="mdi:login" /> Sign In</span>
        </button>
      </form>
    </div>
  </div>
</template>

<style scoped>
.login-container {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 2rem;
}

.login-card {
  width: 100%;
  max-width: 450px;
  padding: 3rem;
  border: 1px solid var(--border-subtle);
  border-radius: 1rem;
  background: var(--bg-elevated);
  backdrop-filter: blur(10px);
  box-shadow: 0 25px 50px -12px var(--shadow-color);
}

.title {
  margin-bottom: 0.5rem;
  color: var(--text-primary);
  font-size: 2rem;
  font-weight: 700;
  text-align: center;
}

.subtitle {
  margin-bottom: 2.5rem;
  color: var(--text-secondary);
  text-align: center;
}

.form-group {
  margin-bottom: 1.5rem;
}

.icon-text {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: var(--text-tertiary);
  font-size: 0.9rem;
  font-weight: 500;
}

input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid var(--border-subtle);
  border-radius: 0.5rem;
  background: var(--bg-input);
  color: var(--text-primary);
  font-family: inherit;
  font-size: 1rem;
  transition:
    border-color 0.2s,
    box-shadow 0.2s;
}

input:focus {
  border-color: var(--accent-primary);
  box-shadow: 0 0 0 3px var(--focus-ring);
  outline: none;
}

.error-message {
  margin-bottom: 1rem;
  color: var(--color-danger);
  font-size: 0.875rem;
  text-align: center;
}

.btn-primary {
  width: 100%;
  margin-top: 1rem;
  padding: 0.875rem;
  border: none;
  border-radius: 0.5rem;
  background: var(--gradient-primary);
  color: var(--text-on-accent);
  font-size: 1rem;
  font-weight: 600;
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
