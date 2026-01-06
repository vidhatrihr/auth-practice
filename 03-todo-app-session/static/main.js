const html = String.raw;

let sessionId = localStorage.getItem('sessionId');
let token = localStorage.getItem('token');

if (sessionId && token) {
  document.querySelector('#auth-result').textContent = 'already logged in';
}

document.querySelector('form').addEventListener('submit', handleLogin);

function renderTodos(todos) {
  document.querySelector('#todos').innerHTML = '';
  for (let todo of todos) {
    document.querySelector('#todos').insertAdjacentHTML(
      'beforeend',
      html`
        <li>
          <span class="${todo.isDone ? 'done' : ''}" onclick="markDone(${todo.id})"
            >${todo.text}
          </span>

          <span class="${todo.isStarred ? 'star' : ''}" onclick="markStarred(${todo.id})"
            >${todo.isStarred ? '★' : '☆'}
          </span>
        </li>
      `
    );
  }
}

async function api(method, path, params = {}) {
  const options = {
    method: method,
  };

  let url;

  if (method == 'get') {
    const query = new URLSearchParams({
      ...params,
      sessionId,
      token,
    }).toString();

    url = `http://127.0.0.1:5000${path}?${query}`;
  }

  if (method == 'post') {
    options.headers = {
      'Content-Type': 'application/json',
    };
    options.body = JSON.stringify(params);

    url = `http://127.0.0.1:5000${path}`;
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

async function handleLogin(event) {
  event.preventDefault();

  const response = await api('post', '/auth/login', {
    email: email.value,
    password: password.value,
  });

  const data = await response.json();

  if (data.success) {
    sessionId = data.payload.sessionId;
    token = data.payload.token;
    localStorage.setItem('sessionId', sessionId);
    localStorage.setItem('token', token);
  }

  document.querySelector('#auth-result').textContent = data.message;
}

async function fetchTodos() {
  const data = await api('get', '/todo/list');

  renderTodos(data.payload.todos);
}

async function markDone(id) {
  await api('get', '/todo/update', {
    todoId: id,
    action: 'markDone',
  });

  fetchTodos();
}

async function markStarred(id) {
  await api('get', '/todo/update', {
    todoId: id,
    action: 'markStarred',
  });
  fetchTodos();
}
