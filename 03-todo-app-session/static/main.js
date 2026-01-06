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
          <span class="${todo.isDone ? 'done' : 'empty'}" onclick="markDone(${todo.id})"
            >${todo.text}</span
          >
        </li>
      `
    );
  }
}

async function api(path, params = {}) {
  const query = new URLSearchParams({
    ...params,
    sessionId,
    token,
  }).toString();

  const response = await fetch(`http://127.0.0.1:5000${path}?${query}`);
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

  const response = await fetch('http://127.0.0.1:5000/auth/login', {
    method: 'post',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      email: document.querySelector('#email').value,
      password: document.querySelector('#password').value,
    }),
  });

  const data = await response.json();

  if (data.success) {
    console.log(data);
    sessionId = data.payload.sessionId;
    token = data.payload.token;
    localStorage.setItem('sessionId', sessionId);
    localStorage.setItem('token', token);
  } else {
    console.error(data);
  }
  document.querySelector('#auth-result').textContent = data.message;
}

async function markDone(id) {
  await api('/todo/update', {
    todoId: id,
    action: 'markDone',
  });

  fetchTodos();
}

async function fetchTodos() {
  const data = await api('/todo/list');

  renderTodos(data.payload.todos);
}
