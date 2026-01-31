<script>
import { authStore } from '@/stores/auth';

export default {
  name: 'ManagerView',
  data() {
    return {
      authStore,
    };
  },
};
</script>

<template>
  <div class="manager-container">
    <div class="manager-card">
      <h1 class="title">Manager Dashboard</h1>
      <p class="subtitle">Welcome, {{ authStore.user.name }}</p>

      <div class="info-section">
        <h2>Manager Capabilities</h2>
        <ul>
          <li>View & Manage Orders</li>
          <li>Manage Products & Inventory</li>
          <li>Manage Customers</li>
          <li>Manage Suppliers</li>
          <li>View Reports</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
.manager-container {
  min-height: 100vh;
  padding: 2rem;
}

.manager-card {
  background: var(--card-bg);
  backdrop-filter: blur(10px);
  padding: 2rem;
  border-radius: 1rem;
  border: 1px solid var(--card-border);
  max-width: 800px;
  margin: 0 auto;
}

.title {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: var(--text-primary);
}

.subtitle {
  color: var(--text-secondary);
  margin-bottom: 2rem;
}

.info-section h2 {
  font-size: 1.25rem;
  margin-bottom: 1rem;
  color: var(--text-heading);
}

.info-section ul {
  list-style: none;
  padding: 0;
}

.info-section li {
  padding: 0.75rem 0;
  border-bottom: 1px solid var(--card-border);
  color: var(--text-secondary);
}

.info-section li:last-child {
  border-bottom: none;
}
</style>
