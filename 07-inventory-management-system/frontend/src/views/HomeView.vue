<script setup>
import { Icon } from '@iconify/vue';
</script>

<template>
  <div class="home-container">
    <div class="hero-section">
      <h1 class="title">Inventory Management System</h1>
      <p class="subtitle">Secure, Efficient, and Scalable</p>

      <div class="cta-wrapper">
        <RouterLink to="/login" class="btn-cta">
          <span class="icon-text"><Icon icon="mdi:login" /> Login</span>
        </RouterLink>
      </div>
    </div>

    <div class="features-grid">
      <div class="feature-card">
        <div class="icon-wrapper">
          <Icon icon="mdi:shield-lock" class="icon" />
        </div>
        <h3>Robust Security</h3>
        <ul class="feature-list">
          <li>
            <Icon icon="mdi:key" class="list-icon" /> JWT authentication from scratch
          </li>
          <li>
            <Icon icon="mdi:shield-check" class="list-icon" /> Secure route protection
          </li>
          <li>
            <Icon icon="mdi:account-lock" class="list-icon" /> Role-Based Access Control
            (RBAC)
          </li>
        </ul>
      </div>

      <div class="feature-card">
        <div class="icon-wrapper">
          <Icon icon="mdi:account-group" class="icon" />
        </div>
        <h3>User Management</h3>
        <ul class="feature-list">
          <li>
            <Icon icon="mdi:shield-crown" class="list-icon" /> Admin role for product
            creation
          </li>
          <li>
            <Icon icon="mdi:clipboard-account" class="list-icon" /> Manager role for order
            oversight
          </li>
          <li>
            <Icon icon="mdi:arrow-left-right" class="list-icon" /> Incoming & outgoing
            order tracking
          </li>
        </ul>
      </div>

      <div class="feature-card">
        <div class="icon-wrapper">
          <Icon icon="mdi:sync" class="icon" />
        </div>
        <h3>Session Control</h3>
        <ul class="feature-list">
          <li><Icon icon="mdi:autorenew" class="list-icon" /> Token regeneration</li>
          <li><Icon icon="mdi:clock-alert" class="list-icon" /> Expiration handling</li>
          <li>
            <Icon icon="mdi:logout-variant" class="list-icon" /> Logout from everywhere
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  padding: 4rem 2rem;
  background-color: var(--bg-primary);
  color: var(--text-primary);
}

.hero-section {
  margin-bottom: 4rem;
  text-align: center;
  animation: fadeInDown 0.8s ease-out;
}

.cta-wrapper {
  margin-top: 2.5rem;
}

.btn-cta {
  display: inline-block;
  padding: 1rem 2.5rem;
  border-radius: 2rem;
  background: var(--gradient-primary);
  color: var(--text-on-accent);
  box-shadow:
    0 4px 6px -1px var(--shadow-sm),
    0 2px 4px -1px var(--shadow-xs);
  font-size: 1.1rem;
  font-weight: 600;
  transition:
    transform 0.2s,
    box-shadow 0.2s,
    opacity 0.2s;
}

.btn-cta .icon-text {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.btn-cta:hover {
  background-color: transparent;
  box-shadow:
    0 10px 15px -3px var(--shadow-sm),
    0 4px 6px -2px var(--shadow-xs);
  opacity: 0.95;
  transform: translateY(-2px);
}

.btn-cta:active {
  transform: translateY(0);
}

.title {
  margin-bottom: 1rem;
  background: var(--gradient-primary);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-size: 3.5rem;
  font-weight: 800;
  letter-spacing: -0.05em;
}

.subtitle {
  color: var(--text-secondary);
  font-size: 1.5rem;
  font-weight: 400;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  width: 100%;
  max-width: 1200px;
}

.feature-card {
  padding: 2.5rem;
  border: 1px solid var(--border-subtle);
  border-radius: 1rem;
  background: var(--bg-elevated);
  backdrop-filter: blur(10px);
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
  animation: fadeInUp 0.8s ease-out backwards;
}

.feature-card:nth-child(1) {
  animation-delay: 0.2s;
}
.feature-card:nth-child(2) {
  animation-delay: 0.4s;
}
.feature-card:nth-child(3) {
  animation-delay: 0.6s;
}

.feature-card:hover {
  border-color: var(--border-accent);
  box-shadow: 0 10px 30px -10px var(--shadow-color);
  transform: translateY(-5px);
}

.icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 60px;
  height: 60px;
  margin-bottom: 1.5rem;
  border-radius: 50%;
  background: rgba(96, 165, 250, 0.1);
}

.icon {
  font-size: 1.8rem;
}

h3 {
  margin-bottom: 1rem;
  color: var(--text-tertiary);
  font-size: 1.5rem;
  font-weight: 600;
}

p {
  color: var(--text-secondary);
  line-height: 1.6;
}

.feature-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  padding: 0;
  margin: 0;
  list-style: none;
}

.feature-list li {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--text-secondary);
  line-height: 1.5;
}

.list-icon {
  flex-shrink: 0;
  color: var(--text-tertiary);
  font-size: 1.1rem;
}

@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
