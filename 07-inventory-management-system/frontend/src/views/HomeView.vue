<script setup></script>

<template>
  <div class="home-container">
    <div class="hero-section">
      <h1 class="title">Inventory Management System</h1>
      <p class="subtitle">Secure, Efficient, and Scalable</p>

      <div class="cta-wrapper">
        <RouterLink to="/login" class="btn-cta">Login</RouterLink>
      </div>
    </div>

    <div class="features-grid">
      <div class="feature-card">
        <div class="icon-wrapper">
          <span class="icon">🛡️</span>
        </div>
        <h3>Robust Security</h3>
        <p>
          Implemented with JWT from scratch, featuring secure route protection and
          Role-Based Access Control (RBAC).
        </p>
      </div>

      <div class="feature-card">
        <div class="icon-wrapper">
          <span class="icon">👥</span>
        </div>
        <h3>User Management</h3>
        <p>
          Distinct roles for Admins to create products and Managers to oversee incoming
          and outgoing orders.
        </p>
      </div>

      <div class="feature-card">
        <div class="icon-wrapper">
          <span class="icon">🔄</span>
        </div>
        <h3>Session Control</h3>
        <p>
          Advanced session management with token regeneration, expiration handling, and
          global logout capabilities.
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-container {
  min-height: 100vh;
  background-color: var(--bg-primary);
  color: var(--text-primary);
  font-family: var(--font-family-base);
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 4rem 2rem;
}

.hero-section {
  text-align: center;
  margin-bottom: 4rem;
  animation: fadeInDown 0.8s ease-out;
}

.cta-wrapper {
  margin-top: 2.5rem;
}

.btn-cta {
  display: inline-block;
  background: linear-gradient(
    135deg,
    var(--color-blue-400) 0%,
    var(--color-violet-400) 100%
  );
  color: white;
  padding: 1rem 2.5rem;
  border-radius: 2rem;
  font-weight: 600;
  font-size: 1.1rem;
  box-shadow:
    0 4px 6px -1px rgba(0, 0, 0, 0.1),
    0 2px 4px -1px rgba(0, 0, 0, 0.06);
  transition:
    transform 0.2s,
    box-shadow 0.2s,
    opacity 0.2s;
}

.btn-cta:hover {
  transform: translateY(-2px);
  box-shadow:
    0 10px 15px -3px rgba(0, 0, 0, 0.1),
    0 4px 6px -2px rgba(0, 0, 0, 0.05);
  opacity: 0.95;
  background-color: transparent; /* fix for link hover style conflict if any */
}

.btn-cta:active {
  transform: translateY(0);
}

.title {
  font-size: 3.5rem;
  font-weight: 800;
  margin-bottom: 1rem;
  background: var(--gradient-title);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  letter-spacing: -0.05em;
}

.subtitle {
  font-size: 1.5rem;
  color: var(--text-secondary);
  font-weight: 400;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  width: 100%;
}

.feature-card {
  background: var(--card-bg);
  backdrop-filter: blur(10px);
  padding: 2.5rem;
  border-radius: 1rem;
  border: 1px solid var(--card-border);
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
  transform: translateY(-5px);
  box-shadow: 0 10px 30px -10px var(--card-hover-shadow);
  border-color: var(--card-hover-border);
}

.icon-wrapper {
  background: var(--icon-bg);
  width: 60px;
  height: 60px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
}

.icon {
  font-size: 1.8rem;
}

h3 {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: var(--text-heading);
}

p {
  color: var(--text-secondary);
  line-height: 1.6;
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
