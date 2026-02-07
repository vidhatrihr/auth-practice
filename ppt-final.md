# Session and JWT Authentication in Flask

A learning journey through 8 progressive tasks.

---

## Slide 1: Introduction & Why Authentication

**Title:** Session and JWT Authentication in Flask

**The Project:**

- Learning project to understand authentication mechanisms
- Progressive approach: 8 demo applications
- Technologies: Flask, SQLAlchemy, Vue.js
- Includes from-scratch Base64 and JWT implementations

**The Problem:**

- HTTP is stateless - server forgets users after each request
- User logs in once, shouldn't enter password again
- Solution: Remember the user across requests
- Key concepts: Tokens, Sessions, Cookies, JWT

---

## Slide 2: Tasks 01 & 02 - Getting Started

**Image:** Screenshot of missile button + basic to-do app

### Task 01 - The Missile Button

- First taste of authentication
- "Launch Missile" - only authorized users can press
- Token stored in database, sent via URL
- **Problem:** Token visible in URL = Not secure

### Task 02 - Basic CRUD (To-Do App)

- Practice ground for authentication experiments
- Simple to-do app without login
- CRUD operations: Create, Read, Update, Delete
- **Purpose:** Foundation for adding authentication

---

## Slide 3: Tasks 03 & 04 - Session Storage

**Image:** Screenshot of to-do app with login

### Task 03 - Session in Local Storage

- Session ID generated after login
- Stored in browser's Local Storage
- **Problem:** Any script can read it (XSS vulnerability)

### Task 04 - Session in Cookies

- Moved to HTTP-only cookies
- Browser sends cookies automatically
- JavaScript cannot access HTTP-only cookies
- Added logout + "logout everywhere" features
- **Security:** Mitigates XSS attacks

---

## Slide 4: Base64 Encoding/Decoding

**Title:** Understanding Base64 (From Scratch)

### Encoding Steps:

1. **bytes → binary string** - Each byte to 8-bit binary
2. **Add padding bits** - Make length divisible by 6
   - 1B remaining: +4 bits (==)
   - 2B remaining: +2 bits (=)
3. **Split into 6-bit chunks** - Binary string to chunks
4. **chunks → nums** - Each 6-bit chunk to number (0-63)
5. **nums → symbols** - Map to Base64 alphabet (A-Z, a-z, 0-9, +, /)
6. **Add padding (=)** - Indicate padding bits added

### Decoding Steps:

1. **Remove padding (=)** - Count and strip = symbols
2. **symbols → nums** - Map back to numbers
3. **nums → 6-bit chunks** - Convert to binary
4. **Join chunks** - Create full binary string
5. **Drop padding bits** - Remove added bits (2 or 4)
6. **Split into 8-bit chunks** - Group for bytes
7. **chunks → nums** - Convert to decimal
8. **nums → bytes** - Reconstruct original data

---

## Slide 5: JWT Implementation

**Title:** JSON Web Token (From Scratch)

### JWT Structure:

- **Header** - Algorithm (HS256), Type (JWT)
- **Payload** - User data (sub, iat)
- **Signature** - HMAC-SHA256 hash

### Encoding Steps:

1. **Create header dict** - {alg: "HS256", typ: "JWT"}
2. **Create payload dict** - {sub: user_id, iat: timestamp}
3. **Encode header** - JSON → Base64URL
4. **Encode payload** - JSON → Base64URL
5. **Create message** - header.payload
6. **Sign message** - HMAC-SHA256 with secret key
7. **Build token** - header.payload.signature

### Decoding/Verification Steps:

1. **Split token** - Separate header, payload, signature
2. **Recreate message** - header.payload
3. **Calculate signature** - Sign with secret key
4. **Compare signatures** - Must match exactly
5. **Decode payload** - Base64URL → JSON → dict
6. **Trust payload** - Only if signature verified

---

## Slide 6: Task 05 - JWT (Stateless)

**Image:** Screenshot of JWT-based to-do app

**Key Points:**

- Implemented JWT from scratch
- Stateless authentication - no database lookup
- Token contains user ID and timestamp
- Server verifies signature without database
- Token stored in HTTP-only cookie
- **Problem:** Cannot logout - token valid until expiry
- **Learning:** Pure JWT lacks revocation capability

---

## Slide 7: Task 06 - JWT with Session Backup

**Image:** Screenshot of hybrid authentication system

**Key Points:**

- Hybrid approach: JWT + Database sessions
- JWT tokens expire in 10 minutes
- On expiry: Check database for valid session
- If session valid: Issue new token
- Logout: Delete session from database
- Token won't renew → User logged out
- **Best of both:** Scalability + Revocation

---

## Slide 8: Task 07 - Final To-Do App

**Image:** Screenshot of Vue.js to-do app

**Key Points:**

- Combined all learnings
- JWT with session backup
- HTTP-only cookies
- Vue.js frontend (Options API)
- Modern UI with icons
- Full CRUD operations
- Landing page + Login page
- Logout + Logout everywhere

---

## Slide 9: Task 08 - Inventory Management System

**Image:** Screenshot of inventory management dashboard

**Key Points:**

- Role-Based Access Control (RBAC)
- Two roles: Admin, Manager
- **Admin:** Manage products, customers, suppliers
- **Manager:** Manage orders (incoming/outgoing)
- JWT via Authorization Bearer header
- Vite + Vue.js frontend
- SQLAlchemy models with relationships
- Real-world scenario application

---

## Slide 10: Summary

**Title:** Key Takeaways

- **Authentication** = Remembering users across requests
- **Token storage matters** - URL < Local Storage < HTTP-only Cookies
- **HTTP-only cookies** - Mitigate XSS attacks
- **JWT** - Powerful for stateless auth, needs careful handling
- **Hybrid approach** - JWT + Sessions = Best of both worlds
- **RBAC** - Essential for multi-user applications
- **Step-by-step learning** - Builds deep understanding
