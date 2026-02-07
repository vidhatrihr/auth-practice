async function api(method, path, params = {}) {
  const options = {
    method: method,
  };
  let url = path;

  if (method == 'post') {
    // POST - send params as JSON body
    options.headers = {
      'Content-Type': 'application/json',
    };
    options.body = JSON.stringify(params);
  } else {
    // GET, PATCH, DELETE - send params as query string
    const query = new URLSearchParams({
      ...params,
    }).toString();
    url += `?${query}`;
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
