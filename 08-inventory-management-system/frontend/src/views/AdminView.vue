<script setup>
import { ref, reactive, onMounted } from 'vue';
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
  const res = await api('get', '/products');
  if (res.success) products.value = res.payload.products;
}

async function submitProduct() {
  if (editingProductId.value) {
    await api('patch', `/products/${editingProductId.value}`, productForm);
  } else {
    await api('post', '/products', productForm);
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
  const res = await api('delete', `/products/${id}`);
  if (res.success) await loadProducts();
  else alert(res.message);
}

// ========== CUSTOMERS ==========
async function loadCustomers() {
  const res = await api('get', '/customers');
  if (res.success) customers.value = res.payload.customers;
}

async function submitCustomer() {
  await api('post', '/customers', customerForm);
  customerForm.name = '';
  await loadCustomers();
}

async function deleteCustomer(id) {
  const res = await api('delete', `/customers/${id}`);
  if (res.success) await loadCustomers();
  else alert(res.message);
}

// ========== SUPPLIERS ==========
async function loadSuppliers() {
  const res = await api('get', '/suppliers');
  if (res.success) suppliers.value = res.payload.suppliers;
}

async function submitSupplier() {
  await api('post', '/suppliers', supplierForm);
  supplierForm.name = '';
  await loadSuppliers();
}

async function deleteSupplier(id) {
  const res = await api('delete', `/suppliers/${id}`);
  if (res.success) await loadSuppliers();
  else alert(res.message);
}
</script>

<template>
  <div class="page">
    <div class="container">
      <h1>
        <span class="icon-text"><Icon icon="mdi:view-dashboard" /> Admin Dashboard</span>
      </h1>
      <p class="muted mb-sm">Welcome, {{ authStore.user.name }}</p>
      <div class="flex gap-sm mb-sm">
        <button class="btn btn-sm" @click="logout()">Log out</button>
        <button class="btn btn-sm btn-danger" @click="logout(true)">
          Log out everywhere
        </button>
      </div>

      <!-- PRODUCTS SECTION -->
      <section>
        <h2>
          <span class="icon-text"><Icon icon="mdi:package-variant" /> Products</span>
        </h2>
        <details>
          <summary>{{ editingProductId ? 'Update Product' : 'Create Product' }}</summary>
          <form @submit.prevent="submitProduct" class="form-row">
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
            <div class="flex gap-sm" style="width: 100%">
              <button type="submit" class="btn btn-primary">
                <span class="icon-text">
                  <Icon :icon="editingProductId ? 'mdi:content-save' : 'mdi:plus'" />
                  {{ editingProductId ? 'Update' : 'Create' }}
                </span>
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
        <ul>
          <li v-for="product in products" :key="product.id" class="list-item">
            <div class="flex-col">
              <strong>{{ product.name }}</strong>
              <span class="muted" style="font-size: 0.85rem">
                Cost: ₹{{ product.costPrice }} | Sell: ₹{{ product.sellingPrice }} | Qty:
                {{ product.qtyAvailable }}
              </span>
            </div>
            <div class="flex gap-sm">
              <button class="btn btn-sm" @click="editProduct(product)">
                <span class="icon-text"><Icon icon="mdi:pencil" /> Edit</span>
              </button>
              <button class="btn btn-sm btn-danger" @click="deleteProduct(product.id)">
                <span class="icon-text"><Icon icon="mdi:delete" /> Delete</span>
              </button>
            </div>
          </li>
        </ul>
      </section>

      <!-- CUSTOMERS SECTION -->
      <section>
        <h2>
          <span class="icon-text"><Icon icon="mdi:account-multiple" /> Customers</span>
        </h2>
        <details>
          <summary>Create Customer</summary>
          <form @submit.prevent="submitCustomer" class="form-row">
            <input v-model="customerForm.name" placeholder="Customer Name" required />
            <button type="submit" class="btn btn-primary">
              <span class="icon-text"><Icon icon="mdi:plus" /> Create</span>
            </button>
          </form>
        </details>
        <ul>
          <li v-for="customer in customers" :key="customer.id" class="list-item">
            <strong>{{ customer.name }}</strong>
            <button class="btn btn-sm btn-danger" @click="deleteCustomer(customer.id)">
              <span class="icon-text"><Icon icon="mdi:delete" /> Delete</span>
            </button>
          </li>
        </ul>
      </section>

      <!-- SUPPLIERS SECTION -->
      <section>
        <h2>
          <span class="icon-text"><Icon icon="mdi:truck-delivery" /> Suppliers</span>
        </h2>
        <details>
          <summary>Create Supplier</summary>
          <form @submit.prevent="submitSupplier" class="form-row">
            <input v-model="supplierForm.name" placeholder="Supplier Name" required />
            <button type="submit" class="btn btn-primary">
              <span class="icon-text"><Icon icon="mdi:plus" /> Create</span>
            </button>
          </form>
        </details>
        <ul>
          <li v-for="supplier in suppliers" :key="supplier.id" class="list-item">
            <strong>{{ supplier.name }}</strong>
            <button class="btn btn-sm btn-danger" @click="deleteSupplier(supplier.id)">
              <span class="icon-text"><Icon icon="mdi:delete" /> Delete</span>
            </button>
          </li>
        </ul>
      </section>
    </div>
  </div>
</template>
