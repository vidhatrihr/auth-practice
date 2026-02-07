# Session and JWT Authentication in Flask

A learning journey through 8 progressive tasks.

---

## Slide 1: Why I Started This

I wanted to refresh my Flask skills. And I had a question in my mind.

**Why do we need authentication?**

Every time you visit a website, the server forgets who you are. That's how the internet works. So if you log in once, you don't want to enter your password again and again.

We need a way to remember the user. That's what this project is about.

I decided to explore step by step. I created numbered folders. Each folder is one small experiment.

---

## Slide 2: The Beginning (Tasks 1, 2.1, 2.2)

### Task 01 - The Missile Button

I started with something fun. A button that "launches a missile." Only an authorized person should be able to press it.

This was my first taste of authentication. I stored a token in the database. The user sends this token with every request. It worked. But storing tokens in the URL is not safe. I learned that.

### Task 02.1 and 02.2 - Learning CRUD

Before going deeper into authentication, I needed a practice ground. So I built a simple to-do app. No login. Just create, read, update, delete.

First version stored todos as plain text. Second version used proper objects. Now I had a playground to test authentication ideas.

**Expectation for next step:** Let me add login to this to-do app.

---

## Slide 3: Sessions and Where to Store Them (Tasks 3, 4)

### Task 03 - Session in Local Storage

I added login to my to-do app. After login, the server gives a session ID. I stored it in the browser's local storage.

It worked. But I realized a problem. Any script on the page can read local storage. That's not safe.

**Expectation for next step:** Find a safer place to store the session.

### Task 04 - Session in Cookies

I moved the session to HTTP-only cookies. The browser sends cookies automatically. And scripts cannot read them.

I also added a logout feature. And a "logout from everywhere" feature. If someone steals your phone, you can logout all your sessions.

This felt more secure. But I was curious. Do I really need to store sessions on the server?

**Expectation for next step:** Can I make authentication stateless?

---

## Slide 4: Going Stateless with JWT (Tasks 5, 6)

### Task 05 - JWT Without Database

I discovered JWT. It's like a signed note. The server signs the token. Later, the server can verify the signature without checking any database.

I implemented JWT from scratch. I learned about Base64 encoding. I learned about signatures. It felt like magic.

But there was a problem. How do you logout? The token is valid until it expires. No way to revoke it.

**Expectation for next step:** Fix the logout problem.

### Task 06 - JWT with Session Backup

I found a balance. JWT tokens are short-lived. They expire in 10 minutes. When they expire, the server checks the database. If the session is still valid, it gives a new token.

Now logout works. Delete the session from database. The token won't renew. User is logged out.

I liked this approach. Best of both worlds.

**Expectation for next step:** Build a real app with all these learnings.

---

## Slide 5: The Final Apps (Tasks 7, 8)

### Task 07 - Final To-Do App

I combined everything I learned. JWT authentication with session backup. HTTP-only cookies. Logout everywhere.

I also upgraded the frontend. I used Vue.js. The app looks modern now. It has a landing page. Separate login page. Nice icons.

This felt complete. A simple to-do app. But with proper security.

### Task 08 - Inventory Management System

I wanted to go further. Not everyone should have the same permissions. An admin can manage products. A manager can manage orders.

This is role-based access control. I added roles to users. The login decorator checks if the user has the right role.

I also used Vite and Vue.js for a proper frontend. This project is still in progress. But the foundation is solid.

---

## What I Learned

1. Authentication is about remembering users.
2. Where you store tokens matters a lot.
3. HTTP-only cookies are your friend.
4. JWT is powerful but needs careful handling.
5. Sometimes a hybrid approach works best.
6. Building step by step helps you understand deeply.
