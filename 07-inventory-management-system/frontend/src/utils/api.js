import { authStore } from '@/stores/auth';

const BASE_URL = 'http://127.0.0.1:5000';

export async function api(method, path, params = {}) {
  const options = {
    method: method.toUpperCase(),
    headers: {},
  };

  // Add Authorization header if token exists
  if (authStore.session.token) {
    options.headers['Authorization'] = `Bearer ${authStore.session.token}`;
  }

  let url = `${BASE_URL}${path}`;

  if (method === 'get') {
    const query = new URLSearchParams({ ...params }).toString();
    if (query) url += `?${query}`;
  } else {
    // POST, PATCH, DELETE with JSON body
    options.headers['Content-Type'] = 'application/json';
    options.body = JSON.stringify(params);
  }

  const response = await fetch(url, options);
  const data = await response.json();

  if (data.success) {
    console.log(data);
  } else {
    console.error(data);
  }
  return data;
}
