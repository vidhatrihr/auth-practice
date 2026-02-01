async function api(method, path, params = {}) {
  const baseUrl = 'http://127.0.0.1:5000';
  const options = {
    method: method,
  };
  let url;

  if (method == 'post') {
    // POST - send params as JSON body
    options.headers = {
      'Content-Type': 'application/json',
    };
    options.body = JSON.stringify(params);
    url = `${baseUrl}${path}`;
  } else {
    // GET, PATCH, DELETE - send params as query string
    const query = new URLSearchParams({
      ...params,
    }).toString();
    url = `${baseUrl}${path}?${query}`;
  }

  const response = await fetch(url, options);
  const data = await response.json();

  const emoji = data.success ? '✅' : '💀';
  console.log(
    `${emoji} ${method.toUpperCase()} ${path}\n ${response.status} ${response.statusText}\n`,
    data,
  );

  return data;
}
