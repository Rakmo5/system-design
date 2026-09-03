# 🏛️ System Design: 0 to Hero Placement Roadmap

Welcome to my personal **System Design & Distributed Systems** learning repository! This repo contains a comprehensive, 40-module structured path designed for SDE placement interviews, technical drives, and scalable backend architecture mastery.

<p align="left">
  <img src="https://img.shields.io/badge/System%20Design-0%20%2F%2040%20Completed-red?style=for-the-badge&logo=youtube" alt="Modules Completed">
  <img src="https://img.shields.io/badge/Track-SDE%20Placement-blue?style=for-the-badge" alt="Track">
  <img src="https://img.shields.io/badge/Focus-REST%20%7C%20SQL%20%7C%20HLD%20%7C%20LLD-orange?style=for-the-badge" alt="Focus">
</p>

---

## 📊 Progress Dashboard

Track my interactive progress through the 5 phases of System Design below:

<p align="left">
  <img src="./progress.svg" alt="System Design Progress" width="400">
</p>

| Phase | Modules Completed | Progress Percentage | Status |
| :--- | :---: | :---: | :---: |
| **Phase 1** | 0 / 8 | 0.0% | ⚪ Not Started |
| **Phase 2** | 0 / 10 | 0.0% | ⚪ Not Started |
| **Phase 3** | 0 / 10 | 0.0% | ⚪ Not Started |
| **Phase 4** | 0 / 6 | 0.0% | ⚪ Not Started |
| **Phase 5** | 0 / 6 | 0.0% | ⚪ Not Started |
| **TOTAL** | **0 / 40** | **0.0%** | **🧠 Engineering Grind** |

---

## 🎯 Active Learning Module (Watch & Practice on the Go)

> **📱 Mobile Dashboard**: Watch your current video lesson and review the key concept flashcards straight from your phone!

### **Lesson #1: [How the Internet & Web Works](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=1)**
* **Phase:** `Phase 1` | **Category:** `Networking & Web`
* **Core Concepts:** `DNS, IP, TCP 3-Way Handshake, SSL/TLS Handshake`

#### 🎥 Video Resources
* ▶️ **Primary Video (Coder Army):** [Watch Video #1](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=1)
* 💡 **Supplementary Visual Guide:** [Watch Supplementary Deep-Dive](https://www.youtube.com/watch?v=7_LPdttKXPc)

#### 🛠️ Hands-On Practice Task
> **Assignment:** Write down step-by-step trace of typing 'google.com' in browser

---


## 📚 Repository Structure
```text
system-design/
├── notes/                # Comprehensive cheat-sheets for REST, SQL, Caching & HLD
├── practice/             # Hands-on API specifications, SQL queries & architecture tasks
├── lld-cpp/              # C++ implementations of SOLID design patterns and LRU Cache
├── System_Design_Roadmap.xlsx # Master tracking spreadsheet
└── generate_readme.py    # Auto-generates README and animated SVG
```

---

## 📂 Complete 40-Module Learning Path


<details>
<summary><b>🌐 Phase 1: Web, Networking & REST API Fundamentals (Lessons 1–8) (0/8 Completed)</b></summary>
<br>

| No. | Module Name | Key Concepts | Video Link | Practice Task | Status |
| :---: | :--- | :--- | :---: | :--- | :---: |
| 1 | How the Internet & Web Works | `DNS, IP, TCP 3-Way Handshake, SSL/TLS Handshake` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=1) | Write down step-by-step trace of typing 'google.com' in browser | ⚪ Not Started |
| 2 | Client-Server Architecture & OSI Model | `7 Layers, Client/Server roles, Request-Response cycle` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=2) | Map OSI layers to real web protocols (HTTP, TCP, IP, Ethernet) | ⚪ Not Started |
| 3 | HTTP Evolution: HTTP/1.1 vs HTTP/2 vs HTTP/3 | `Persistent connections, Multiplexing, Head-of-line blocking, QUIC/UDP` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=3) | Compare HTTP/1.1 vs HTTP/2 performance trade-offs in a table | ⚪ Not Started |
| 4 | WebSockets vs Long Polling vs SSE vs WebRTC | `Full-duplex real-time communication, Server-Sent Events, Video streaming` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=4) | Select the right protocol for: (1) Chat App, (2) Stock Ticker, (3) Video Call | ⚪ Not Started |
| 5 | REST Architecture & Constraints | `Statelessness, Uniform Interface, Client-Server, Cacheability` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=5) | Explain the 6 REST architectural constraints in plain English | ⚪ Not Started |
| 6 | HTTP Methods & Idempotency Deep Dive | `GET, POST, PUT, PATCH, DELETE. Why PUT is idempotent but POST is not` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=6) | Design REST endpoints for an E-Commerce Cart & Order Placement flow | ⚪ Not Started |
| 7 | HTTP Status Codes & Error Handling | `2xx (Success), 3xx (Redirects), 4xx (Client errors), 5xx (Server errors)` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=7) | Flashcard drill: Match 10 real-world API error scenarios to exact status codes | ⚪ Not Started |
| 8 | API Security, Headers, Pagination & Versioning | `JWT vs Sessions, OAuth 2.0, Offset vs Cursor Pagination, Rate limiting headers` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=8) | Draft a complete OpenAPI/Swagger JSON specification for a User Auth API | ⚪ Not Started |

</details>

<details>
<summary><b>💾 Phase 2: Database Deep-Dive (SQL vs NoSQL & Indexing) (Lessons 9–18) (0/10 Completed)</b></summary>
<br>

| No. | Module Name | Key Concepts | Video Link | Practice Task | Status |
| :---: | :--- | :--- | :---: | :--- | :---: |
| 9 | Relational Databases (SQL / RDBMS) Overview | `PostgreSQL/MySQL architecture, Tables, Foreign Keys, Schema constraints` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=9) | Design a normalized relational schema for a Food Delivery App | ⚪ Not Started |
| 10 | ACID Properties in Relational Databases | `Atomicity, Consistency, Isolation, Durability with banking transactions` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=10) | Explain how Rollback and Write-Ahead Logging (WAL) ensure Atomicity and Durability | ⚪ Not Started |
| 11 | Transaction Isolation Levels & Concurrency | `Dirty Reads, Non-repeatable Reads, Phantom Reads. Read Committed vs Repeatable Read` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=11) | Simulate two concurrent bank transfers and show which isolation level prevents double spending | ⚪ Not Started |
| 12 | Database Indexing Deep Dive (B-Trees & B+ Trees) | `How B+ Trees store data, Clustered vs Non-Clustered index, range query speed` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=12) | Given a query with WHERE user_id = 5 AND status = 'ACTIVE' ORDER BY created_at, design optimal composite index | ⚪ Not Started |
| 13 | Indexing Trade-offs & Query Optimization | `Why indexing slows down INSERT/UPDATE/DELETE, EXPLAIN ANALYZE queries` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=13) | Analyze a slow SQL query with EXPLAIN plan and fix it using indexing | ⚪ Not Started |
| 14 | Database Normalization (1NF to BCNF) vs Denormalization | `Reducing data redundancy vs optimizing high-throughput reads` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=14) | Demonstrate when you would denormalize a Comment count in a Social Media post table | ⚪ Not Started |
| 15 | Introduction to NoSQL & The 4 Main Types | `Document (MongoDB), Key-Value (Redis), Columnar (Cassandra), Graph (Neo4j)` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=15) | Create a decision matrix: SQL vs MongoDB vs Redis vs Cassandra | ⚪ Not Started |
| 16 | Database Replication (Master-Slave / Leader-Follower) | `Read Replicas, Synchronous vs Asynchronous replication, Replication lag` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=16) | Explain how to solve 'Read-Your-Own-Writes' consistency problem with read replicas | ⚪ Not Started |
| 17 | Database Sharding & Horizontal Partitioning | `Range-based, Hash-based, Directory-based sharding, Cross-shard queries` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=17) | Choose the optimal shard key for a 500-million user Twitter Tweet database | ⚪ Not Started |
| 18 | Consistent Hashing & Hash Rings | `Virtual nodes, Minimizing re-balancing keys during node additions/failures` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=18) | Implement basic Consistent Hashing logic in C++ / Python | ⚪ Not Started |

</details>

<details>
<summary><b>🏗️ Phase 3: High-Level Design (HLD) Building Blocks (Lessons 19–28) (0/10 Completed)</b></summary>
<br>

| No. | Module Name | Key Concepts | Video Link | Practice Task | Status |
| :---: | :--- | :--- | :---: | :--- | :---: |
| 19 | Vertical vs Horizontal Scaling & Stateless Architecture | `Scale-up limits, Scale-out benefits, Decoupling session state to Redis` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=19) | Explain why stateless servers enable auto-scaling in cloud environments | ⚪ Not Started |
| 20 | Load Balancers & Routing Algorithms | `L4 vs L7, Round Robin, Least Connections, IP Hash, Health checks` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=20) | Draw a diagram showing HAProxy L7 load balancer routing traffic based on URL path | ⚪ Not Started |
| 21 | Reverse Proxies (Nginx) & API Gateways | `SSL Termination, Compression, Rate Limiting, Authentication routing` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=21) | Explain the 5 core responsibilities of an API Gateway in Microservices | ⚪ Not Started |
| 22 | Caching Fundamentals & Caching Locations | `Client Cache, CDN (Edge), Reverse Proxy Cache, Redis, DB Cache` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=22) | Calculate cache hit ratio and latency savings for a 95% cache hit rate | ⚪ Not Started |
| 23 | Caching Strategies: Cache-Aside, Write-Through, Write-Back | `Read-heavy vs Write-heavy patterns, Cache-Aside (Lazy loading), Write-Back dirty buffer` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=23) | Choose the right caching strategy for: (1) News Feed, (2) User Profile, (3) Video View Count | ⚪ Not Started |
| 24 | Cache Eviction Policies (LRU, LFU, FIFO, TTL) | `Least Recently Used, Least Frequently Used, TTL expirations` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=24) | Explain why Hash Map + Doubly Linked List enables O(1) LRU Cache operations | ⚪ Not Started |
| 25 | Cache Pitfalls: Penetration, Avalanche, Stampede (Thundering Herd) | `Null caching, Bloom filters, Jittered TTLs, Mutex locking` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=25) | Propose a concrete solution for Cache Avalanche when 100,000 keys expire at midnight | ⚪ Not Started |
| 26 | Message Queues & Decoupled Architecture | `Point-to-point queues, Pub-Sub, Backpressure, Consumer groups` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=26) | Design an asynchronous Order Processing pipeline with payment, email, and shipping workers | ⚪ Not Started |
| 27 | RabbitMQ vs Apache Kafka Deep Dive | `Queue-based push model vs Distributed log-based pull model, Topic partitions, Offsets` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=27) | Create a comparison table: RabbitMQ vs Kafka throughput, latency, and retention | ⚪ Not Started |
| 28 | CAP Theorem & PACELC Theorem | `Consistency vs Availability over network partitions. Real-world CP vs AP systems` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=28) | Classify MySQL, MongoDB, Cassandra, and Spanner into CP vs AP models | ⚪ Not Started |

</details>

<details>
<summary><b>📐 Phase 4: Low-Level Design (LLD) & OOP Design Patterns (Lessons 29–34) (0/6 Completed)</b></summary>
<br>

| No. | Module Name | Key Concepts | Video Link | Practice Task | Status |
| :---: | :--- | :--- | :---: | :--- | :---: |
| 29 | SOLID Principles: Single Responsibility & Open-Closed | `S and O principles with code examples, decoupling business logic` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=29) | Refactor a messy C++ Invoice generator class to adhere to SRP and OCP | ⚪ Not Started |
| 30 | SOLID Principles: Liskov, Interface Segregation & Dependency Inversion | `L, I, D principles, Dependency Injection, Interface segregation` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=30) | Demonstrate a classic LSP violation with Rectangle and Square classes in C++ | ⚪ Not Started |
| 31 | Creational Patterns: Singleton & Factory Pattern | `Thread-safe Singleton in C++, Factory Method, Abstract Factory` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=31) | Write a thread-safe Logger class in C++ using Meyers' Singleton pattern | ⚪ Not Started |
| 32 | Creational Patterns: Builder & Prototype Pattern | `Constructing complex objects step-by-step, cloning objects` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=32) | Implement the Builder pattern for a custom HTTP Request object in C++ | ⚪ Not Started |
| 33 | Structural Patterns: Adapter, Decorator & Facade | `Wrapping incompatible interfaces, adding dynamic behavior, simplifying APIs` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=33) | Implement a Pizza pricing calculator in C++ using the Decorator pattern | ⚪ Not Started |
| 34 | Behavioral Patterns: Strategy & Observer Pattern | `Interchangeable algorithms, Event listener / Pub-Sub pattern` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=34) | Implement a Payment Processor in C++ using Strategy (CreditCard, UPI, PayPal) | ⚪ Not Started |

</details>

<details>
<summary><b>🎯 Phase 5: Real-World Case Studies & Capstones (Lessons 35–40) (0/6 Completed)</b></summary>
<br>

| No. | Module Name | Key Concepts | Video Link | Practice Task | Status |
| :---: | :--- | :--- | :---: | :--- | :---: |
| 35 | The 4-Step System Design Interview Framework | `Requirements, Capacity Estimations, High-Level Design, Deep Dives` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=35) | Create a standardized template for tackling any 45-minute System Design interview | ⚪ Not Started |
| 36 | Design a URL Shortener (TinyURL / Bitly) | `Base62 encoding, Hash collisions, DB Schema, Redirection Caching` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=36) | Draw full architecture diagram and calculate 5-year storage for 100M URLs/month | ⚪ Not Started |
| 37 | Design an API Rate Limiter | `Token Bucket, Leaky Bucket, Sliding Window Counter with Redis` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=37) | Implement a Token Bucket Rate Limiter in C++ | ⚪ Not Started |
| 38 | Design a Chat Application (WhatsApp / Messenger) | `WebSockets, Gateway servers, Cassandra message storage, Online/Offline presence` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=38) | Diagram how messages route from Sender -> WebSocket Gateway -> Kafka -> Receiver | ⚪ Not Started |
| 39 | Design a Social Media News Feed (Instagram / Twitter) | `Fan-out on write vs Fan-out on read, News Feed ranking, CDN caching for media` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=39) | Explain how to handle celebrity posts with 100 million followers using hybrid fan-out | ⚪ Not Started |
| 40 | Design a Ride-Sharing System (Uber / Ola) | `Geohashing, QuadTrees for spatial proximity, Driver location tracking, Matching service` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=40) | Draw architecture showing Driver GPS ping ingestion, QuadTree updates, and Rider matching | ⚪ Not Started |

</details>

---

## 🚀 How to Sync Progress

Whenever you finish a video or practice task:
1. Open `System_Design_Roadmap.xlsx` and change the Status to `Completed`.
2. Double-click `sync.bat` (or run `python generate_readme.py` and `git push`).

*“Simplicity is prerequisite for reliability.” – Edsger W. Dijkstra.* 💻🚀
