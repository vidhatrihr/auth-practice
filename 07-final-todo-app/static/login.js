const html = String.raw;

const { createApp } = Vue;

const template = html`
  <section>
    <h2>Sign in</h2>
    <form @submit.prevent="handleLogin">
      <label>
        Email
        <input type="email" v-model="email" placeholder="you@example.com" />
      </label>

      <label>
        Password
        <input type="password" v-model="password" placeholder="••••••••" />
      </label>

      <button>
        <iconify-icon icon="mdi:arrow-right"></iconify-icon>
        Sign in
      </button>
    </form>

    <div v-if="authResult" class="auth-message">{{ authResult }}</div>
  </section>
`;

createApp({
  template,
  data() {
    return {
      email: 'vidu@example.com',
      password: 'qwerty',
      authResult: '',
    };
  },

  methods: {
    async handleLogin() {
      const data = await api('post', '/auth/login', {
        email: this.email,
        password: this.password,
      });

      if (data.success) {
        localStorage.setItem(
          'session',
          JSON.stringify({
            message: data.message,
            loggedIn: true,
          }),
        );
        window.location.href = '/app';
      } else {
        this.authResult = data.message;
      }
    },
  },
}).mount('#app');
