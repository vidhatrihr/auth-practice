import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import { authStore } from '../stores/auth';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue'),
    },
    {
      path: '/admin',
      name: 'admin',
      component: () => import('../views/AdminView.vue'),
      meta: { role: 'admin' },
    },
    {
      path: '/manager',
      name: 'manager',
      component: () => import('../views/ManagerView.vue'),
      meta: { role: 'manager' },
    },
  ],
});

router.beforeEach(to => {
  if (['login', 'home'].includes(to.name)) return true;
  if (!authStore.isLoggedIn || to.meta.role !== authStore.user.role)
    return { name: 'login' };
  return true;
});

export default router;
