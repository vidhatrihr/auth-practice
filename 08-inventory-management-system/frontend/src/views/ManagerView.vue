<script setup>
import { ref, computed, onMounted } from 'vue';
import { api } from '@/utils/api';
import { authStore } from '@/stores/auth';
import { Icon } from '@iconify/vue';

const orders = ref([]);

const incomingOrders = computed(() => orders.value.filter(o => o.type === 'incoming'));
const outgoingOrders = computed(() => orders.value.filter(o => o.type === 'outgoing'));

onMounted(async () => {
  await loadOrders();
});

async function loadOrders() {
  const res = await api('get', '/manager/orders');
  if (res.success) orders.value = res.payload.orders;
}

async function deleteOrder(id) {
  const res = await api('delete', `/manager/orders/${id}`);
  if (res.success) await loadOrders();
  else alert(res.message);
}

async function markDelivered(id) {
  const res = await api('patch', `/manager/orders/${id}/deliver`);
  if (res.success) await loadOrders();
  else alert(res.message);
}

function formatDate(iso) {
  if (!iso) return '-';
  return new Date(iso).toLocaleDateString();
}
</script>

<template>
  <div class="manager-container">
    <div class="manager-card">
      <h1 class="title">
        <span class="icon-text"
          ><Icon icon="mdi:view-dashboard" /> Manager Dashboard</span
        >
      </h1>
      <p class="subtitle">Welcome, {{ authStore.user.name }}</p>

      <!-- INCOMING ORDERS -->
      <section class="section">
        <h2>
          <span class="icon-text"
            ><Icon icon="mdi:truck-delivery" /> Incoming Orders (from Suppliers)</span
          >
        </h2>
        <table class="orders-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Supplier</th>
              <th>Items</th>
              <th>Status</th>
              <th>Created</th>
              <th>Delivered</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="order in incomingOrders" :key="order.id">
              <td>{{ order.id }}</td>
              <td>{{ order.supplierName || '-' }}</td>
              <td>
                <span v-for="(item, idx) in order.items" :key="item.id">
                  {{ item.productName }} ({{ item.qty }})<span
                    v-if="idx < order.items.length - 1"
                    >,
                  </span>
                </span>
              </td>
              <td>
                <span :class="['status', order.status]">{{ order.status }}</span>
              </td>
              <td>{{ formatDate(order.dateCreated) }}</td>
              <td>{{ formatDate(order.dateDelivered) }}</td>
              <td>
                <template v-if="order.status === 'pending'">
                  <button
                    class="btn btn-small btn-success"
                    @click="markDelivered(order.id)"
                  >
                    <span class="icon-text"
                      ><Icon icon="mdi:check" /> Mark Delivered</span
                    >
                  </button>
                  <button class="btn btn-small btn-danger" @click="deleteOrder(order.id)">
                    <span class="icon-text"><Icon icon="mdi:delete" /> Delete</span>
                  </button>
                </template>
                <span v-else class="done"><Icon icon="mdi:check-circle" /></span>
              </td>
            </tr>
            <tr v-if="incomingOrders.length === 0">
              <td colspan="7" class="empty">No incoming orders</td>
            </tr>
          </tbody>
        </table>
      </section>

      <!-- OUTGOING ORDERS -->
      <section class="section">
        <h2>
          <span class="icon-text"
            ><Icon icon="mdi:cart-arrow-right" /> Outgoing Orders (to Customers)</span
          >
        </h2>
        <table class="orders-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Customer</th>
              <th>Items</th>
              <th>Status</th>
              <th>Created</th>
              <th>Delivered</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="order in outgoingOrders" :key="order.id">
              <td>{{ order.id }}</td>
              <td>{{ order.customerName || '-' }}</td>
              <td>
                <span v-for="(item, idx) in order.items" :key="item.id">
                  {{ item.productName }} ({{ item.qty }})<span
                    v-if="idx < order.items.length - 1"
                    >,
                  </span>
                </span>
              </td>
              <td>
                <span :class="['status', order.status]">{{ order.status }}</span>
              </td>
              <td>{{ formatDate(order.dateCreated) }}</td>
              <td>{{ formatDate(order.dateDelivered) }}</td>
              <td>
                <template v-if="order.status === 'pending'">
                  <button
                    class="btn btn-small btn-success"
                    @click="markDelivered(order.id)"
                  >
                    <span class="icon-text"
                      ><Icon icon="mdi:check" /> Mark Delivered</span
                    >
                  </button>
                  <button class="btn btn-small btn-danger" @click="deleteOrder(order.id)">
                    <span class="icon-text"><Icon icon="mdi:delete" /> Delete</span>
                  </button>
                </template>
                <span v-else class="done"><Icon icon="mdi:check-circle" /></span>
              </td>
            </tr>
            <tr v-if="outgoingOrders.length === 0">
              <td colspan="7" class="empty">No outgoing orders</td>
            </tr>
          </tbody>
        </table>
      </section>
    </div>
  </div>
</template>

<style scoped>
.manager-container {
  min-height: 100vh;
  padding: 2rem;
}

.manager-card {
  max-width: 1100px;
  margin: 0 auto;
  padding: 2rem;
  border: 1px solid var(--border-subtle);
  border-radius: 1rem;
  background: var(--bg-elevated);
  backdrop-filter: blur(10px);
}

.icon-text {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.title {
  margin-bottom: 0.5rem;
  color: var(--text-primary);
  font-size: 2rem;
  font-weight: 700;
}

.subtitle {
  margin-bottom: 2rem;
  color: var(--text-secondary);
}

.section {
  margin-bottom: 2rem;
}

.section h2 {
  margin-bottom: 1rem;
  color: var(--text-tertiary);
  font-size: 1.25rem;
}

/* Table */
.orders-table {
  width: 100%;
  border-collapse: collapse;
}

.orders-table th,
.orders-table td {
  padding: 0.75rem 0.5rem;
  border-bottom: 1px solid var(--border-subtle);
  text-align: left;
}

.orders-table th {
  color: var(--text-secondary);
  font-size: 0.875rem;
  font-weight: 600;
}

.orders-table td {
  color: var(--text-primary);
}

.empty {
  color: var(--text-secondary);
  font-style: italic;
  text-align: center;
}

/* Status badges */
.status {
  display: inline-block;
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
}

.status.pending {
  background: var(--color-warning);
  color: var(--text-inverse);
}

.status.delivered {
  background: var(--color-success);
  color: var(--text-on-accent);
}

.done {
  color: var(--color-success);
  font-weight: bold;
}

/* Buttons */
.btn {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.375rem;
  font-weight: 500;
  cursor: pointer;
  transition: opacity 0.2s;
}

.btn:hover {
  opacity: 0.9;
}

.btn-small {
  margin-right: 0.25rem;
  padding: 0.25rem 0.5rem;
  font-size: 0.875rem;
}

.btn-success {
  background: var(--color-success);
  color: var(--text-on-accent);
}

.btn-danger {
  background: var(--color-danger);
  color: var(--text-on-accent);
}
</style>
