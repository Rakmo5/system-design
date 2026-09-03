# 🏗️ Cheat Sheet: High-Level Design (HLD) Building Blocks

This document summarizes core distributed systems components used in system design interviews.

---

## 1. Caching Strategies (Redis & Memcached)

### Cache Eviction Policies
1. **LRU (Least Recently Used)**: Evicts the item that hasn't been accessed for the longest time. (Implemented via `unordered_map` + Doubly Linked List in $O(1)$).
2. **LFU (Least Frequently Used)**: Evicts the item with the lowest access count.
3. **TTL (Time to Live)**: Items expire after a fixed duration (e.g. 5 minutes).

### Caching Write Strategies
* **Cache-Aside (Lazy Loading)**: App reads from Cache. On Cache Miss, App queries DB, writes to Cache, and returns data.
* **Write-Through**: App writes data to Cache, and Cache synchronously writes to DB before returning.
* **Write-Back (Write-Behind)**: App writes to Cache immediately; Cache batches writes and saves to DB asynchronously (super fast, but risk of data loss if cache crashes).

### Cache Pitfalls (Interview Traps!)
* **Cache Penetration**: Malicious queries for non-existent IDs bypass cache and hit DB repeatedly.  
  * *Fix*: Cache `null` values with short TTL, or use a **Bloom Filter**.
* **Cache Avalanche**: Hundreds of thousands of cache keys expire simultaneously at midnight, crashing the DB.  
  * *Fix*: Add random jitter to TTLs (e.g., `TTL = 300s + rand(0, 60s)`).
* **Cache Stampede (Thundering Herd)**: A high-traffic key expires, and 10,000 concurrent requests all miss and hit DB at the exact same millisecond.  
  * *Fix*: Mutex locks (only 1 thread regenerates cache).

---

## 2. Load Balancers & Proxies

* **L4 Load Balancing**: Operates at Transport Layer (TCP/UDP, routing based on IP and Port). Fast, but unaware of content.
* **L7 Load Balancing**: Operates at Application Layer (HTTP/HTTPS, routing based on URL path, headers, cookies).
* **Algorithms**:
  * **Round Robin**: Distributes requests sequentially.
  * **Least Connections**: Sends traffic to the server with fewest active connections.
  * **IP Hash**: Ensures a user consistently hits the same backend server (useful for in-memory sessions).

---

## 3. Message Queues: RabbitMQ vs Apache Kafka

| Feature | RabbitMQ | Apache Kafka |
| :--- | :--- | :--- |
| **Model** | Traditional Message Queue (Push model) | Distributed Commit Log (Pull model) |
| **Message Retention**| Deleted once consumed | Persisted on disk for days/weeks |
| **Throughput** | High (tens of thousands msgs/sec) | Ultra-High (millions of msgs/sec) |
| **Best Used For** | Task background jobs, complex routing | Event streaming, log aggregation, real-time analytics |

---

## 4. CAP Theorem (The Golden Law)

In any distributed network, you can only guarantee **2 out of 3**:
* **C (Consistency)**: Every read receives the most recent write or an error.
* **A (Availability)**: Every non-failing request receives a non-error response.
* **P (Partition Tolerance)**: The system continues to operate despite network packet loss/partition.

> **💡 Note**: Since network partitions are an inevitable physical reality of distributed systems, **you MUST choose P**. Therefore, your real-world architectural choice is always between **CP (Consistency)** vs **AP (Availability)**.
