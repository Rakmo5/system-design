# 🌐 Cheat Sheet: Networking, HTTP & REST API Design

This document contains everything you need to master REST APIs and Web Networking for SDE technical interviews.

---

## 1. What Happens When You Type a URL in Your Browser? (Classic Interview Question)

1. **DNS Lookup**: Browser checks DNS cache (Browser $\to$ OS $\to$ Router $\to$ ISP $\to$ Authoritative DNS server) to convert `https://api.example.com` into an IP address (e.g., `192.0.2.1`).
2. **TCP 3-Way Handshake**:
   - `SYN`: Client sends Synchronize packet to Server.
   - `SYN-ACK`: Server acknowledges and sends Synchronize packet back.
   - `ACK`: Client acknowledges. Connection is established.
3. **SSL/TLS Handshake** (for HTTPS): Negotiates encryption cipher suites and exchanges cryptographic keys.
4. **HTTP Request Sent**: Browser sends `GET /index.html HTTP/1.1` with headers.
5. **Server Processing & Response**: Server processes request and returns HTTP `200 OK` with HTML/JSON body.
6. **Rendering**: Browser parses HTML, fetches CSS/JS, and renders DOM.

---

## 2. HTTP Methods & Idempotency

| Method | Purpose | Idempotent? | Safe? (Read-only) | Example |
| :--- | :--- | :---: | :---: | :--- |
| `GET` | Retrieve resource | **YES** | **YES** | `GET /api/v1/users/42` |
| `POST` | Create new resource | **NO** | **NO** | `POST /api/v1/orders` |
| `PUT` | Replace entire resource | **YES** | **NO** | `PUT /api/v1/users/42` |
| `PATCH`| Partial update | **NO** (usually) | **NO** | `PATCH /api/v1/users/42` |
| `DELETE`| Remove resource | **YES** | **NO** | `DELETE /api/v1/users/42` |

> **💡 What is Idempotency?**  
> An operation is **idempotent** if making the same request multiple times produces the **exact same result** on the server.
> * *Why `PUT` is idempotent*: Setting `name = 'Omkar'` 10 times results in `name = 'Omkar'`.
> * *Why `POST` is not idempotent*: Submitting `POST /orders` 10 times creates 10 separate orders (or double-charges a credit card!).

---

## 3. HTTP Status Codes Cheat Sheet

### 🟢 2xx: Success
* **`200 OK`**: Standard success (e.g., successful `GET` or `PUT`).
* **`201 Created`**: New resource created (standard for `POST /users`).
* **`204 No Content`**: Action succeeded, but no body to return (standard for `DELETE`).

### 🟡 3xx: Redirection
* **`301 Moved Permanently`**: URL permanently changed (SEO friendly).
* **`304 Not Modified`**: Client cached copy is still valid (saves bandwidth).

### 🔴 4xx: Client Errors (The caller made a mistake)
* **`400 Bad Request`**: Malformed JSON or validation error.
* **`401 Unauthorized`**: Authentication missing or invalid (User is not logged in).
* **`403 Forbidden`**: User is authenticated, but **does not have permission** to view this resource (Role-based access error).
* **`404 Not Found`**: Resource does not exist.
* **`429 Too Many Requests`**: Rate limit exceeded.

### ⚫ 5xx: Server Errors (The backend crashed)
* **`500 Internal Server Error`**: Unhandled exception in backend code.
* **`502 Bad Gateway`**: Upstream server / reverse proxy (Nginx) received an invalid response from app server.
* **`503 Service Unavailable`**: Server is overloaded or down for maintenance.
* **`504 Gateway Timeout`**: App server took too long to respond to Nginx / Load Balancer.

---

## 4. Real-Time Protocols: When to Use What?

| Protocol | Direction | Overhead | Best Use Case |
| :--- | :--- | :---: | :--- |
| **HTTP/REST** | Request $\to$ Response (Unary) | Medium | Standard CRUD APIs |
| **WebSockets** | Full-Duplex (2-way persistent) | Very Low | Live Chat (WhatsApp), Multiplayer Gaming |
| **Server-Sent Events (SSE)** | Server $\to$ Client only | Low | Stock Tickers, Live Scoreboards, AI stream responses |
| **Long Polling** | Client asks, Server holds until data | High | Fallback when WebSockets blocked |
