# 🏛️ System Design: 0 to Hero Placement Roadmap

Welcome to my personal **System Design & Distributed Systems** learning repository! This repo contains a comprehensive, 40-module structured path designed for SDE placement interviews, technical drives, and scalable backend architecture mastery.

<p align="left">
  <img src="https://img.shields.io/badge/System%20Design-3%20%2F%2040%20Completed-red?style=for-the-badge&logo=youtube" alt="Modules Completed">
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
| **Phase 1** | 3 / 8 | 37.5% | 🟢 Active |
| **Phase 2** | 0 / 10 | 0.0% | ⚪ Not Started |
| **Phase 3** | 0 / 10 | 0.0% | ⚪ Not Started |
| **Phase 4** | 0 / 6 | 0.0% | ⚪ Not Started |
| **Phase 5** | 0 / 6 | 0.0% | ⚪ Not Started |
| **TOTAL** | **3 / 40** | **7.5%** | **🧠 Engineering Grind** |

> 📱 **1-Tap Interactive Mobile Checklist**: You can directly tap & check off completed lessons on your phone here:  
> 👉 [**Open Interactive Checkbox Issue #1**](https://github.com/Rakmo5/system-design/issues/1)

---

## 🎯 Active Learning Module (Watch & Practice on the Go)

> **📱 Mobile Dashboard**: Watch your current video lesson and review the key concept flashcards straight from your phone!

### **Lesson #4: [HTTP & HTTPS: Evolution (HTTP/1.1 vs HTTP/2 vs HTTP/3) & SSL/TLS Handshake](https://www.youtube.com/watch?v=UMwQjFzTQXw)**
* **Phase:** `Phase 1` | **Category:** `Web Protocols`
* **Core Concepts:** `Multiplexing, Head-of-line blocking, QUIC protocol, Symmetric vs Asymmetric encryption, TLS Handshake`

#### 🎥 Video Resources
* ▶️ **Primary Video Resource:** [Watch Lesson #4 Video](https://www.youtube.com/watch?v=UMwQjFzTQXw)
* 💡 **Supplementary Visual Guide:** [Watch Supplementary Deep-Dive](https://www.youtube.com/watch?v=hExRDVZHhig)

#### 🛠️ Hands-On Practice Task
> **Assignment:** Create a comparison table showing how HTTP/2 multiplexing solves HTTP/1.1 HOL blocking

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
<summary><b>🌐 Phase 1: Web, Networking & REST API Fundamentals (Lessons 1–8) (3/8 Completed)</b></summary>
<br>

| No. | Module Name | Key Concepts | Video Link | Practice Task | Checkbox Status |
| :---: | :--- | :--- | :---: | :--- | :---: |
| 1 | Introduction to System Design: HLD vs LLD & Scalability Overview | `What is a System, Monolith vs Microservices, Vertical vs Horizontal scaling, System Design interview framework` | [Watch Video](https://www.youtube.com/watch?v=AK0hu0Zxua4) | Write down the core difference between High-Level Design (HLD) and Low-Level Design (LLD) | `[x]` ✅ Completed |
| 2 | How the Internet Works & Client-Server Architecture (DNS, IP, Routing) | `DNS resolution, IP routing, Ports, Client/Server roles, Request-Response lifecycle` | [Watch Video](https://www.youtube.com/watch?v=7_LPdttKXPc) | Write down the step-by-step trace of typing 'google.com' in a browser until the page renders | `[x]` ✅ Completed |
| 3 | OSI & TCP/IP Model: TCP 3-Way Handshake vs UDP | `7 Layers vs 4 Layers, TCP 3-Way Handshake (SYN, SYN-ACK, ACK), Connection-oriented TCP vs Fast UDP` | [Watch Video](https://www.youtube.com/watch?v=vv4y_uOneC0) | Map real web protocols (HTTP, TCP, IP, Ethernet) to their respective OSI layers | `[x]` ✅ Completed |
| 4 | HTTP & HTTPS: Evolution (HTTP/1.1 vs HTTP/2 vs HTTP/3) & SSL/TLS Handshake | `Multiplexing, Head-of-line blocking, QUIC protocol, Symmetric vs Asymmetric encryption, TLS Handshake` | [Watch Video](https://www.youtube.com/watch?v=UMwQjFzTQXw) | Create a comparison table showing how HTTP/2 multiplexing solves HTTP/1.1 HOL blocking | `[ ]` ⚪ Not Started |
| 5 | REST Architecture & 6 Guiding Constraints | `Statelessness, Client-Server separation, Cacheability, Uniform Interface, Layered System, Code-on-Demand` | [Watch Video](https://www.youtube.com/watch?v=-mN3VyJuCjM) | Explain why statelessness in REST makes horizontal backend scaling much easier | `[ ]` ⚪ Not Started |
| 6 | HTTP Methods & Idempotency Deep Dive (GET, POST, PUT, PATCH, DELETE) | `Safe vs Idempotent methods. Why PUT is idempotent but POST is not. Handling double-payment submissions` | [Watch Video](https://www.youtube.com/watch?v=tkfVQK6UxDI) | Design REST endpoints for an E-Commerce Cart & Checkout order flow with correct methods | `[ ]` ⚪ Not Started |
| 7 | HTTP Status Codes & API Error Handling (2xx, 3xx, 4xx, 5xx) | `200 OK, 201 Created, 204 No Content, 301 vs 302, 400, 401 vs 403, 404, 429, 500, 502 Bad Gateway, 504` | [Watch Video](https://www.youtube.com/watch?v=wJa5CTIFj7U) | Flashcard drill: Explain the difference between 401 Unauthorized and 403 Forbidden with examples | `[ ]` ⚪ Not Started |
| 8 | WebSockets vs Long Polling vs Server-Sent Events (SSE) vs WebRTC | `Full-duplex bidirectional communication, Server-Sent Events for one-way streams, WebRTC for P2P audio/video` | [Watch Video](https://www.youtube.com/watch?v=1BfCnjr_Vjg) | Select the optimal protocol for: (1) WhatsApp Chat, (2) Stock Ticker, (3) Live Video Call | `[ ]` ⚪ Not Started |

</details>

<details>
<summary><b>💾 Phase 2: Database Deep-Dive (SQL vs NoSQL & Indexing) (Lessons 9–18) (0/10 Completed)</b></summary>
<br>

| No. | Module Name | Key Concepts | Video Link | Practice Task | Checkbox Status |
| :---: | :--- | :--- | :---: | :--- | :---: |
| 9 | Relational Databases (SQL / RDBMS) Architecture | `PostgreSQL/MySQL storage engines, Tables, Foreign Keys, Schema integrity constraints` | [Watch Video](https://www.youtube.com/watch?v=zsjvFFKOm3c) | Design a normalized relational schema for a Food Delivery App (Users, Restaurants, Orders) | `[ ]` ⚪ Not Started |
| 10 | ACID Properties in Relational Databases | `Atomicity, Consistency, Isolation, Durability with banking money transfer transactions` | [Watch Video](https://www.youtube.com/watch?v=-GS0OxFJsYQ) | Explain how Write-Ahead Logging (WAL) guarantees Durability even if the power fails | `[ ]` ⚪ Not Started |
| 11 | Transaction Isolation Levels & Concurrency Anomalies | `Dirty Reads, Non-repeatable Reads, Phantom Reads. Read Committed vs Repeatable Read vs Serializable` | [Watch Video](https://www.youtube.com/watch?v=pomxJOFVcQs) | Simulate two concurrent banking transactions and show which isolation level prevents double spending | `[ ]` ⚪ Not Started |
| 12 | Database Indexing Deep Dive (How B+ Trees Work) | `How B+ Trees organize data on disk, Clustered Index (Primary Key) vs Non-Clustered (Secondary) Index` | [Watch Video](https://www.youtube.com/watch?v=fsG1XaZEa78) | Given a query with WHERE user_id = ? AND status = 'ACTIVE' ORDER BY created_at, design the composite index | `[ ]` ⚪ Not Started |
| 13 | Indexing Trade-offs & Query Optimization (EXPLAIN Plans) | `Why indexing speeds up SELECT queries but slows down INSERT/UPDATE/DELETE. Reading EXPLAIN query plans` | [Watch Video](https://www.youtube.com/watch?v=OhJ3xcjtpis) | Analyze a slow SQL query and explain why adding too many indexes degrades write throughput | `[ ]` ⚪ Not Started |
| 14 | Database Normalization (1NF to BCNF) vs Denormalization | `Eliminating data redundancy vs intentionally denormalizing data to eliminate expensive JOINs on reads` | [Watch Video](https://www.youtube.com/watch?v=5GDTIUVlHB8) | Demonstrate when you would denormalize a Comment Count column in a high-traffic Social Media post table | `[ ]` ⚪ Not Started |
| 15 | Introduction to NoSQL: Document, Key-Value, Columnar & Graph | `MongoDB (Document), Redis (Key-Value), Cassandra (Column-family), Neo4j (Graph). When to choose SQL vs NoSQL` | [Watch Video](https://www.youtube.com/watch?v=0buKQHokLK8) | Build a decision matrix comparing SQL vs MongoDB vs Redis vs Cassandra across 5 dimensions | `[ ]` ⚪ Not Started |
| 16 | Database Replication: Read Replicas & Master-Slave Sync | `Leader-Follower architecture, Synchronous vs Asynchronous replication, Handling Replication Lag` | [Watch Video](https://www.youtube.com/watch?v=bI8Ry6GhMSE) | Explain how to solve the 'Read-Your-Own-Writes' consistency problem when using read replicas | `[ ]` ⚪ Not Started |
| 17 | Database Sharding & Horizontal Partitioning | `Range-based, Hash-based, and Directory-based sharding. Handling cross-shard JOINs and hot partitions` | [Watch Video](https://www.youtube.com/watch?v=5faMjKuB9bc) | Choose the optimal shard key for a 500-million user Twitter Tweet database | `[ ]` ⚪ Not Started |
| 18 | Consistent Hashing & Distributed Hash Rings | `Virtual nodes, Minimizing key re-balancing when servers are added or removed in distributed caches` | [Watch Video](https://www.youtube.com/watch?v=UF9Iqmg94tk) | Trace what happens in a consistent hash ring when Server 2 crashes and goes offline | `[ ]` ⚪ Not Started |

</details>

<details>
<summary><b>🏗️ Phase 3: High-Level Design (HLD) Building Blocks (Lessons 19–28) (0/10 Completed)</b></summary>
<br>

| No. | Module Name | Key Concepts | Video Link | Practice Task | Checkbox Status |
| :---: | :--- | :--- | :---: | :--- | :---: |
| 19 | Vertical vs Horizontal Scaling & Stateless Architecture | `Scale-up limits, Scale-out benefits, Decoupling session state to Redis, Auto-scaling groups` | [Watch Video](https://www.youtube.com/watch?v=EWS_CIxttVw) | Explain why stateless servers enable auto-scaling in cloud environments | `[ ]` ⚪ Not Started |
| 20 | Load Balancers & Traffic Routing Algorithms (L4 vs L7) | `L4 Transport vs L7 Application load balancing. Round Robin, Least Connections, IP Hash algorithms` | [Watch Video](https://www.youtube.com/watch?v=LQuuoHTyYz8) | Draw a diagram showing HAProxy L7 load balancer routing traffic based on URL paths (/api vs /static) | `[ ]` ⚪ Not Started |
| 21 | Reverse Proxies (Nginx) & API Gateways | `SSL Termination, Response Compression, Rate Limiting, Authentication routing, Forward vs Reverse proxy` | [Watch Video](https://www.youtube.com/watch?v=4NB0NDtOwIQ) | Explain the 5 core responsibilities of an API Gateway in a microservices architecture | `[ ]` ⚪ Not Started |
| 22 | Caching Fundamentals: CDN, Edge Caching & In-Memory Redis | `Client Cache, CDN (Cloudflare), Reverse Proxy Cache, Application Cache, Redis/Memcached DB cache` | [Watch Video](https://www.youtube.com/watch?v=dGAgxozNWFE) | Calculate cache hit ratio and latency savings for a 95% cache hit rate system | `[ ]` ⚪ Not Started |
| 23 | Caching Strategies: Cache-Aside, Write-Through, Write-Back | `Lazy loading (Cache-Aside), Synchronous write-through, Asynchronous write-back buffer trade-offs` | [Watch Video](https://www.youtube.com/watch?v=dGAgxozNWFE) | Choose the right caching strategy for: (1) News Feed, (2) User Profile, (3) Video View Count | `[ ]` ⚪ Not Started |
| 24 | Cache Eviction Policies (LRU, LFU, FIFO, TTL) | `Least Recently Used (LRU), Least Frequently Used (LFU), Time To Live (TTL) expiration strategies` | [Watch Video](https://www.youtube.com/watch?v=R0UkJSzM_4k) | Explain why Hash Map + Doubly Linked List enables O(1) LRU Cache get and put operations | `[ ]` ⚪ Not Started |
| 25 | Cache Pitfalls: Penetration, Avalanche & Stampede (Thundering Herd) | `Null caching, Bloom filters, Jittered TTLs, Mutex locking to prevent DB crashes` | [Watch Video](https://www.youtube.com/watch?v=1nENigGr-a0) | Propose a concrete architectural fix for Cache Avalanche when 100,000 keys expire at midnight | `[ ]` ⚪ Not Started |
| 26 | Message Queues & Decoupled Event-Driven Architecture | `Point-to-point queues, Pub-Sub, Backpressure handling, Decoupling producers and consumers` | [Watch Video](https://www.youtube.com/watch?v=oUJbuFMyBDk) | Design an asynchronous Order Processing pipeline with payment, email, and shipping workers | `[ ]` ⚪ Not Started |
| 27 | RabbitMQ vs Apache Kafka Deep Dive | `Traditional push queue model vs Distributed append-only log pull model, Topic partitions, Consumer groups` | [Watch Video](https://www.youtube.com/watch?v=Ch5VhJzaoaI) | Create a comparison table: RabbitMQ vs Kafka throughput, latency, ordering, and retention | `[ ]` ⚪ Not Started |
| 28 | CAP Theorem & PACELC Theorem | `Consistency vs Availability over network partitions. Why P is mandatory. Real-world CP vs AP systems` | [Watch Video](https://www.youtube.com/watch?v=k-Yaq8AHlFA) | Classify MySQL, MongoDB, Cassandra, and Spanner into CP vs AP models with justification | `[ ]` ⚪ Not Started |

</details>

<details>
<summary><b>📐 Phase 4: Low-Level Design (LLD) & OOP Design Patterns (Lessons 29–34) (0/6 Completed)</b></summary>
<br>

| No. | Module Name | Key Concepts | Video Link | Practice Task | Checkbox Status |
| :---: | :--- | :--- | :---: | :--- | :---: |
| 29 | SOLID Principles: Single Responsibility & Open-Closed | `Single Responsibility (SRP) and Open/Closed (OCP) principles with clean C++ examples` | [Watch Video](https://www.youtube.com/watch?v=pTB30aXS77U) | Refactor a messy C++ Invoice generator class to strictly adhere to SRP and OCP | `[ ]` ⚪ Not Started |
| 30 | SOLID Principles: Liskov, Interface Segregation & Dependency Inversion | `Liskov Substitution (LSP), Interface Segregation (ISP), Dependency Inversion (DIP) & Dependency Injection` | [Watch Video](https://www.youtube.com/watch?v=J1f5b4vcxCQ) | Demonstrate a classic LSP violation with Rectangle and Square classes in C++ | `[ ]` ⚪ Not Started |
| 31 | Creational Patterns: Singleton & Factory Method in C++ | `Thread-safe Meyers' Singleton in C++, Factory Method, Abstract Factory for decoupling object creation` | [Watch Video](https://www.youtube.com/watch?v=PPup1yeU45I) | Write a thread-safe Logger class in C++ using Meyers' Singleton pattern | `[ ]` ⚪ Not Started |
| 32 | Creational Patterns: Builder & Prototype Pattern | `Constructing complex objects step-by-step, method chaining, cloning objects` | [Watch Video](https://www.youtube.com/watch?v=v9ejT8FO-7I) | Implement the Builder pattern for a custom HTTP Request object in C++ | `[ ]` ⚪ Not Started |
| 33 | Structural Patterns: Adapter, Decorator & Facade | `Wrapping incompatible interfaces, adding dynamic behavior at runtime, simplifying complex subsystems` | [Watch Video](https://www.youtube.com/watch?v=2PKQtNXTEVU) | Implement a Coffee/Pizza pricing calculator in C++ using the Decorator pattern | `[ ]` ⚪ Not Started |
| 34 | Behavioral Patterns: Strategy & Observer (Pub-Sub) Pattern | `Interchangeable algorithms at runtime, Event listener / Pub-Sub pattern for decoupling` | [Watch Video](https://www.youtube.com/watch?v=_BpmXJYXWU4) | Implement a Payment Processor in C++ using Strategy pattern (CreditCard, UPI, PayPal) | `[ ]` ⚪ Not Started |

</details>

<details>
<summary><b>🎯 Phase 5: Real-World Case Studies & Capstones (Lessons 35–40) (0/6 Completed)</b></summary>
<br>

| No. | Module Name | Key Concepts | Video Link | Practice Task | Checkbox Status |
| :---: | :--- | :--- | :---: | :--- | :---: |
| 35 | The 4-Step System Design Interview Framework | `Step 1 Requirements, Step 2 Capacity Estimations, Step 3 High-Level Design, Step 4 Component Deep-Dives` | [Watch Video](https://www.youtube.com/watch?v=i7twT3x5yv8) | Create a standardized template for tackling any 45-minute System Design interview | `[ ]` ⚪ Not Started |
| 36 | Design a URL Shortener (TinyURL / Bitly) | `Base62 encoding, Hash collisions, Relational DB Schema, Redis Redirection Caching` | [Watch Video](https://www.youtube.com/watch?v=JQDHz72OA3c) | Draw full architecture diagram and calculate 5-year storage for 100M URLs/month | `[ ]` ⚪ Not Started |
| 37 | Design an API Rate Limiter | `Token Bucket, Leaky Bucket, Sliding Window Counter algorithms with Redis` | [Watch Video](https://www.youtube.com/watch?v=FU4WlwfS3G0) | Implement a Token Bucket Rate Limiter in C++ | `[ ]` ⚪ Not Started |
| 38 | Design a Real-Time Chat App (WhatsApp / Messenger) | `WebSockets, Gateway servers, Cassandra message storage, Online/Offline presence indicator` | [Watch Video](https://www.youtube.com/watch?v=vvhC64hQZMk) | Diagram how messages route from Sender -> WebSocket Gateway -> Kafka -> Receiver | `[ ]` ⚪ Not Started |
| 39 | Design a Social Media News Feed (Instagram / Twitter) | `Fan-out on write vs Fan-out on read, Hybrid fan-out for celebrities, News Feed ranking, CDN media delivery` | [Watch Video](https://www.youtube.com/watch?v=KmAyPUv97nM) | Explain how to handle celebrity posts with 100 million followers using hybrid fan-out | `[ ]` ⚪ Not Started |
| 40 | Design a Ride-Sharing System (Uber / Ola) | `Geohashing, QuadTrees for spatial proximity, Driver location tracking, Matching engine` | [Watch Video](https://www.youtube.com/watch?v=umWABit-wbk) | Draw architecture showing Driver GPS ping ingestion, QuadTree updates, and Rider matching | `[ ]` ⚪ Not Started |

</details>

---

## 🚀 How to Sync Progress

Whenever you check off an item on your phone via [Issue #1](https://github.com/Rakmo5/system-design/issues/1) or finish an Excel task:
1. Double-click **`sync.bat`** (or run `python generate_readme.py && git push`).
2. Your local Excel sheet, README, and animated progress bar will automatically synchronize in seconds!

*“Simplicity is prerequisite for reliability.” – Edsger W. Dijkstra.* 💻🚀
