<script setup>
import { ref, reactive, onMounted } from 'vue';
import { api } from '@/utils/api';
import { authStore } from '@/stores/auth';
import { Icon } from '@iconify/vue';

const products = ref([]);
const customers = ref([]);
const suppliers = ref([]);

const productForm = reactive({
  name: '',
  costPrice: '',
  sellingPrice: '',
  qtyAvailable: '',
});
const customerForm = reactive({ name: '' });
const supplierForm = reactive({ name: '' });

const editingProductId = ref(null);

onMounted(async () => {
  await loadProducts();
  await loadCustomers();
  await loadSuppliers();
});

// ========== PRODUCTS ==========
async function loadProducts() {
  console.log('Loading products...');
  const res = await api('get', '/admin/products');
  console.log('Products response:', res);
  if (res.success) {
    products.value = res.payload.products;
    console.log('Products loaded:', products.value);
  } else {
    console.error('Failed to load products:', res.message);
  }
}

async function submitProduct() {
  if (editingProductId.value) {
    await api('patch', `/admin/products/${editingProductId.value}`, productForm);
  } else {
    await api('post', '/admin/products', productForm);
  }
  resetProductForm();
  await loadProducts();
}

function editProduct(product) {
  productForm.name = product.name;
  productForm.costPrice = product.costPrice;
  productForm.sellingPrice = product.sellingPrice;
  productForm.qtyAvailable = product.qtyAvailable;
  editingProductId.value = product.id;
}

function resetProductForm() {
  productForm.name = '';
  productForm.costPrice = '';
  productForm.sellingPrice = '';
  productForm.qtyAvailable = '';
  editingProductId.value = null;
}

async function deleteProduct(id) {
  const res = await api('delete', `/admin/products/${id}`);
  if (res.success) await loadProducts();
  else alert(res.message);
}

// ========== CUSTOMERS ==========
async function loadCustomers() {
  const res = await api('get', '/admin/customers');
  if (res.success) customers.value = res.payload.customers;
}

async function submitCustomer() {
  await api('post', '/admin/customers', customerForm);
  customerForm.name = '';
  await loadCustomers();
}

async function deleteCustomer(id) {
  const res = await api('delete', `/admin/customers/${id}`);
  if (res.success) await loadCustomers();
  else alert(res.message);
}

// ========== SUPPLIERS ==========
async function loadSuppliers() {
  const res = await api('get', '/admin/suppliers');
  if (res.success) suppliers.value = res.payload.suppliers;
}

async function submitSupplier() {
  await api('post', '/admin/suppliers', supplierForm);
  supplierForm.name = '';
  await loadSuppliers();
}

async function deleteSupplier(id) {
  const res = await api('delete', `/admin/suppliers/${id}`);
  if (res.success) await loadSuppliers();
  else alert(res.message);
}
</script>

<template>
  <div class="admin-container">
    <div class="admin-card">
      <h1 class="title">
        <span class="icon-text"><Icon icon="mdi:view-dashboard" /> Admin Dashboard</span>
      </h1>
      <p class="subtitle">Welcome, {{ authStore.user.name }}</p>

      <!-- PRODUCTS SECTION -->
      <section class="section">
        <h2>
          <span class="icon-text"><Icon icon="mdi:package-variant" /> Products</span>
        </h2>
        <details class="accordion">
          <summary>{{ editingProductId ? 'Update Product' : 'Create Product' }}</summary>
          <form @submit.prevent="submitProduct" class="form">
            <input v-model="productForm.name" placeholder="Product Name" required />
            <input
              v-model.number="productForm.costPrice"
              type="number"
              step="0.01"
              placeholder="Cost Price"
              required
            />
            <input
              v-model.number="productForm.sellingPrice"
              type="number"
              step="0.01"
              placeholder="Selling Price"
              required
            />
            <input
              v-model.number="productForm.qtyAvailable"
              type="number"
              placeholder="Quantity"
              required
            />
            <div class="form-actions">
              <button type="submit" class="btn btn-primary">
                <span class="icon-text"
                  ><Icon :icon="editingProductId ? 'mdi:content-save' : 'mdi:plus'" />
                  {{ editingProductId ? 'Update' : 'Create' }}</span
                >
              </button>
              <button
                v-if="editingProductId"
                type="button"
                class="btn btn-secondary"
                @click="resetProductForm"
              >
                <span class="icon-text"><Icon icon="mdi:close" /> Cancel</span>
              </button>
            </div>
          </form>
        </details>
        <ul class="list">
          <li v-for="product in products" :key="product.id" class="list-item">
            <div class="item-info">
              <strong>{{ product.name }}</strong>
              <span class="meta"
                >Cost: ₹{{ product.costPrice }} | Sell: ₹{{ product.sellingPrice }} | Qty:
                {{ product.qtyAvailable }}</span
              >
            </div>
            <div class="item-actions">
              <button class="btn btn-small" @click="editProduct(product)">
                <span class="icon-text"><Icon icon="mdi:pencil" /> Edit</span>
              </button>
              <button class="btn btn-small btn-danger" @click="deleteProduct(product.id)">
                <span class="icon-text"><Icon icon="mdi:delete" /> Delete</span>
              </button>
            </div>
          </li>
        </ul>
      </section>

      <!-- CUSTOMERS SECTION -->
      <section class="section">
        <h2>
          <span class="icon-text"><Icon icon="mdi:account-multiple" /> Customers</span>
        </h2>
        <details class="accordion">
          <summary>Create Customer</summary>
          <form @submit.prevent="submitCustomer" class="form">
            <input v-model="customerForm.name" placeholder="Customer Name" required />
            <button type="submit" class="btn btn-primary">
              <span class="icon-text"><Icon icon="mdi:plus" /> Create</span>
            </button>
          </form>
        </details>
        <ul class="list">
          <li v-for="customer in customers" :key="customer.id" class="list-item">
            <div class="item-info">
              <strong>{{ customer.name }}</strong>
            </div>
            <div class="item-actions">
              <button
                class="btn btn-small btn-danger"
                @click="deleteCustomer(customer.id)"
              >
                <span class="icon-text"><Icon icon="mdi:delete" /> Delete</span>
              </button>
            </div>
          </li>
        </ul>
      </section>

      <!-- SUPPLIERS SECTION -->
      <section class="section">
        <h2>
          <span class="icon-text"><Icon icon="mdi:truck-delivery" /> Suppliers</span>
        </h2>
        <details class="accordion">
          <summary>Create Supplier</summary>
          <form @submit.prevent="submitSupplier" class="form">
            <input v-model="supplierForm.name" placeholder="Supplier Name" required />
            <button type="submit" class="btn btn-primary">
              <span class="icon-text"><Icon icon="mdi:plus" /> Create</span>
            </button>
          </form>
        </details>
        <ul class="list">
          <li v-for="supplier in suppliers" :key="supplier.id" class="list-item">
            <div class="item-info">
              <strong>{{ supplier.name }}</strong>
            </div>
            <div class="item-actions">
              <button
                class="btn btn-small btn-danger"
                @click="deleteSupplier(supplier.id)"
              >
                <span class="icon-text"><Icon icon="mdi:delete" /> Delete</span>
              </button>
            </div>
          </li>
        </ul>
      </section>
    </div>
  </div>
</template>

<style scoped>
.admin-container {
  min-height: 100vh;
  padding: 2rem;
}

.admin-card {
  max-width: 900px;
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

/* Accordion */
.accordion {
  margin-bottom: 1rem;
  border: 1px solid var(--border-subtle);
  border-radius: 0.5rem;
  background: var(--bg-secondary);
}

.accordion summary {
  padding: 0.75rem 1rem;
  color: var(--text-primary);
  font-weight: 600;
  cursor: pointer;
}

.accordion[open] summary {
  border-bottom: 1px solid var(--border-subtle);
}

/* Form */
.form {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  padding: 1rem;
}

.form input {
  flex: 1 1 150px;
  padding: 0.5rem 0.75rem;
  border: 1px solid var(--border-subtle);
  border-radius: 0.375rem;
  background: var(--bg-primary);
  color: var(--text-primary);
}

.form input:focus {
  border-color: var(--accent-primary);
  outline: none;
}

.form-actions {
  display: flex;
  flex: 1 1 100%;
  gap: 0.5rem;
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

.btn-primary {
  background: var(--accent-primary);
  color: var(--text-on-accent);
}

.btn-secondary {
  background: var(--bg-secondary);
  color: var(--text-primary);
}

.btn-danger {
  background: var(--color-danger);
  color: var(--text-on-accent);
}

.btn-small {
  padding: 0.25rem 0.5rem;
  font-size: 0.875rem;
}

/* List */
.list {
  padding: 0;
  list-style: none;
}

.list-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 0;
  border-bottom: 1px solid var(--border-subtle);
}

.list-item:last-child {
  border-bottom: none;
}

.item-info {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.item-info strong {
  color: var(--text-primary);
}

.meta {
  color: var(--text-secondary);
  font-size: 0.875rem;
}

.item-actions {
  display: flex;
  gap: 0.5rem;
}
</style>
