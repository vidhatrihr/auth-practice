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
  <div class="page-center">
    <div class="container-sm">
      <h1>Welcome Back</h1>
      <p class="muted mb-sm">Sign in to your account</p>

      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="email">
            <span class="icon-text"><Icon icon="mdi:email" /> Email</span>
          </label>
          <input v-model="email" type="email" id="email" placeholder="name@company.com" />
        </div>

        <div class="form-group">
          <label for="password">
            <span class="icon-text"><Icon icon="mdi:lock" /> Password</span>
          </label>
          <input
            v-model="password"
            type="password"
            id="password"
            placeholder="••••••••"
          />
        </div>

        <p v-if="error" class="error mb-sm">{{ error }}</p>

        <button type="submit" class="btn btn-primary btn-block">
          <span class="icon-text"><Icon icon="mdi:login" /> Sign In</span>
        </button>
      </form>
    </div>
  </div>
</template>
