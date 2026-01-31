import { authStore } from '@/stores/auth';

const BASE_URL = 'http://127.0.0.1:5000';

export async function api(method, path, params = {}) {
  const options = {
    method: method,
    headers: {},
  };

  // Add Authorization header if token exists
  if (authStore.session.token) {
    options.headers['Authorization'] = `Bearer ${authStore.session.token}`;
  }

  let url;

  if (method == 'get') {
    const query = new URLSearchParams({
      ...params,
    }).toString();

    url = `${BASE_URL}${path}?${query}`;
  }

  if (method == 'post') {
    options.headers['Content-Type'] = 'application/json';
    options.body = JSON.stringify(params);

    url = `${BASE_URL}${path}`;
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
