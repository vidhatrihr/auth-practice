const html = String.raw;

const { createApp } = Vue;

const template = html`
  <section>
    <details>
      <summary class="icon-text" v-if="isAuthenticated">
        <iconify-icon icon="mdi:check-circle"></iconify-icon> {{ authResult }}
      </summary>
      <summary class="icon-text" v-else-if="authChecked">
        <iconify-icon icon="mdi:alert-circle"></iconify-icon> Please
        <a href="/login">sign in</a> to continue
      </summary>
      <summary class="icon-text" v-else>
        <iconify-icon icon="eos-icons:loading"></iconify-icon> Checking...
      </summary>
      <div class="button-group">
        <button @click="logout">
          <iconify-icon icon="mdi:logout"></iconify-icon> Logout
        </button>
        <button @click="logoutEverywhere">
          <iconify-icon icon="mdi:logout-variant"></iconify-icon> All devices
        </button>
      </div>
    </details>
  </section>

  <section>
    <form @submit.prevent="createTodo">
      <label>
        New todo
        <input type="text" v-model="todoText" placeholder="What needs to be done?" />
      </label>

      <button>
        <iconify-icon icon="mdi:plus"></iconify-icon>
        Add todo
      </button>
    </form>
  </section>

  <section>
    <p v-if="todos.length === 0">No todos yet</p>
    <ul v-else>
      <li v-for="todo in todos" :key="todo.id">
        <span @click="deleteTodo(todo.id)">×</span>
        <span :class="{ done: todo.isDone }" @click="markDone(todo.id)">
          {{ todo.text }}
        </span>
        <span :class="{ star: todo.isStarred }" @click="markStarred(todo.id)">
          {{ todo.isStarred ? '★' : '☆' }}
        </span>
      </li>
    </ul>
  </section>
`;

createApp({
  template,
  data() {
    return {
      todos: [],
      todoText: 'Drink coffee',
      authResult: 'Loading...',
      isAuthenticated: false,
      authChecked: false,
    };
  },

  mounted() {
    this.checkAuth();
  },

  methods: {
    async checkAuth() {
      const data = await api('get', '/auth/whoami');
      this.authResult = data.message;
      this.authChecked = true;
      if (data.success) {
        this.isAuthenticated = true;
        this.fetchTodos();
      }
    },

    async fetchTodos() {
      const data = await api('get', '/todo/list');
      if (data.success) {
        this.todos = data.payload.todos;
      }
    },

    async createTodo() {
      await api('post', '/todo/create', { text: this.todoText });
      this.fetchTodos();
    },

    async markDone(todoId) {
      await api('patch', '/todo/update', { todoId, action: 'markDone' });
      this.fetchTodos();
    },

    async markStarred(todoId) {
      await api('patch', '/todo/update', { todoId, action: 'markStarred' });
      this.fetchTodos();
    },

    async deleteTodo(todoId) {
      await api('delete', '/todo/delete', { todoId });
      this.fetchTodos();
    },

    async logout() {
      const data = await api('get', '/auth/logout');
      this.authResult = data.message;
    },

    async logoutEverywhere() {
      const data = await api('get', '/auth/logout-everywhere');
      this.authResult = data.message;
    },
  },
}).mount('#app');
