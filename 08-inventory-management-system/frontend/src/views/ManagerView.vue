<script setup>
import { ref, computed, onMounted } from 'vue';
import { api } from '@/utils/api';
import { authStore } from '@/stores/auth';
import { Icon } from '@iconify/vue';
import { useRouter } from 'vue-router';

const router = useRouter();

async function logout(everywhere = false) {
  await api('get', `/auth/logout${everywhere ? '-everywhere' : ''}`);
  authStore.logout();
  router.push('/login');
}

const orders = ref([]);

const incomingOrders = computed(() => orders.value.filter(o => o.type === 'incoming'));
const outgoingOrders = computed(() => orders.value.filter(o => o.type === 'outgoing'));

onMounted(async () => {
  await loadOrders();
});

async function loadOrders() {
  const res = await api('get', '/orders');
  if (res.success) orders.value = res.payload.orders;
}

async function deleteOrder(id) {
  const res = await api('delete', `/orders/${id}`);
  if (res.success) await loadOrders();
  else alert(res.message);
}

async function markDelivered(id) {
  const res = await api('patch', `/orders/${id}/deliver`);
  if (res.success) await loadOrders();
  else alert(res.message);
}

function formatDate(iso) {
  if (!iso) return '-';
  return new Date(iso).toLocaleDateString();
}
</script>

<template>
  <div class="page">
    <div class="container" style="max-width: 1000px">
      <h1>
        <span class="icon-text"
          ><Icon icon="mdi:view-dashboard" /> Manager Dashboard</span
        >
      </h1>
      <p class="muted mb-sm">Welcome, {{ authStore.user.name }}</p>
      <div class="flex gap-sm mb-sm">
        <button class="btn btn-sm" @click="logout()">Log out</button>
        <button class="btn btn-sm btn-danger" @click="logout(true)">
          Log out everywhere
        </button>
      </div>

      <!-- INCOMING ORDERS -->
      <section>
        <h2>
          <span class="icon-text"
            ><Icon icon="mdi:truck-delivery" /> Incoming Orders (from Suppliers)</span
          >
        </h2>
        <table>
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
                <span
                  :class="[
                    'status',
                    order.status === 'pending' ? 'status-pending' : 'status-delivered',
                  ]"
                >
                  {{ order.status }}
                </span>
              </td>
              <td>{{ formatDate(order.dateCreated) }}</td>
              <td>{{ formatDate(order.dateDelivered) }}</td>
              <td>
                <template v-if="order.status === 'pending'">
                  <button class="btn btn-sm btn-success" @click="markDelivered(order.id)">
                    <span class="icon-text"><Icon icon="mdi:check" /> Delivered</span>
                  </button>
                  <button class="btn btn-sm btn-danger" @click="deleteOrder(order.id)">
                    <span class="icon-text"><Icon icon="mdi:delete" /> Delete</span>
                  </button>
                </template>
                <span v-else style="color: #2c5"><Icon icon="mdi:check-circle" /></span>
              </td>
            </tr>
            <tr v-if="incomingOrders.length === 0">
              <td colspan="7" class="empty">No incoming orders</td>
            </tr>
          </tbody>
        </table>
      </section>

      <!-- OUTGOING ORDERS -->
      <section>
        <h2>
          <span class="icon-text"
            ><Icon icon="mdi:cart-arrow-right" /> Outgoing Orders (to Customers)</span
          >
        </h2>
        <table>
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
                <span
                  :class="[
                    'status',
                    order.status === 'pending' ? 'status-pending' : 'status-delivered',
                  ]"
                >
                  {{ order.status }}
                </span>
              </td>
              <td>{{ formatDate(order.dateCreated) }}</td>
              <td>{{ formatDate(order.dateDelivered) }}</td>
              <td>
                <template v-if="order.status === 'pending'">
                  <button class="btn btn-sm btn-success" @click="markDelivered(order.id)">
                    <span class="icon-text"><Icon icon="mdi:check" /> Delivered</span>
                  </button>
                  <button class="btn btn-sm btn-danger" @click="deleteOrder(order.id)">
                    <span class="icon-text"><Icon icon="mdi:delete" /> Delete</span>
                  </button>
                </template>
                <span v-else style="color: #2c5"><Icon icon="mdi:check-circle" /></span>
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
