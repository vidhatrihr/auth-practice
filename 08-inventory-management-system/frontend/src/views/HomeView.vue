<script setup>
import { Icon } from '@iconify/vue';
</script>

<template>
  <div class="page">
    <div class="container" style="text-align: center">
      <h1>Inventory Management System</h1>
      <p class="muted">Secure, Efficient, and Scalable</p>

      <div class="mt-sm mb-sm">
        <RouterLink to="/login" class="btn btn-primary">
          <span class="icon-text"><Icon icon="mdi:login" /> Login</span>
        </RouterLink>
      </div>
    </div>

    <div
      class="container"
      style="
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin-top: 2rem;
      "
    >
      <div style="padding: 1.5rem; border: 1px solid #333">
        <Icon icon="mdi:shield-lock" style="font-size: 1.5rem" />
        <h2 style="margin-top: 0.5rem">Robust Security</h2>
        <ul>
          <li class="muted"><Icon icon="mdi:key" /> JWT authentication from scratch</li>
          <li class="muted"><Icon icon="mdi:shield-check" /> Secure route protection</li>
          <li class="muted">
            <Icon icon="mdi:account-lock" /> Role-Based Access Control (RBAC)
          </li>
        </ul>
      </div>

      <div style="padding: 1.5rem; border: 1px solid #333">
        <Icon icon="mdi:account-group" style="font-size: 1.5rem" />
        <h2 style="margin-top: 0.5rem">User Management</h2>
        <ul>
          <li class="muted">
            <Icon icon="mdi:shield-crown" /> Admin role for product creation
          </li>
          <li class="muted">
            <Icon icon="mdi:clipboard-account" /> Manager role for order oversight
          </li>
          <li class="muted">
            <Icon icon="mdi:arrow-left-right" /> Incoming & outgoing order tracking
          </li>
        </ul>
      </div>

      <div style="padding: 1.5rem; border: 1px solid #333">
        <Icon icon="mdi:sync" style="font-size: 1.5rem" />
        <h2 style="margin-top: 0.5rem">Session Control</h2>
        <ul>
          <li class="muted"><Icon icon="mdi:autorenew" /> Token regeneration</li>
          <li class="muted"><Icon icon="mdi:clock-alert" /> Expiration handling</li>
          <li class="muted"><Icon icon="mdi:logout-variant" /> Logout from everywhere</li>
        </ul>
      </div>
    </div>
  </div>
</template>
