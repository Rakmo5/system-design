# 💾 Cheat Sheet: Databases (SQL vs NoSQL, ACID, Indexing & Sharding)

This document covers high-frequency database interview concepts for SDE technical drives.

---

## 1. SQL vs NoSQL Decision Matrix

| Dimension | SQL (RDBMS) | NoSQL |
| :--- | :--- | :--- |
| **Data Schema** | Rigid, Structured Tables | Flexible, Schema-less (JSON, Key-Value) |
| **Relationships** | Complex JOINs supported | Denormalized (embedded documents) |
| **Scaling** | Vertical (Scale-up) primarily; Read Replicas | Horizontal (Scale-out) by default (Sharded) |
| **Transactions** | Strong ACID compliance | BASE (Eventual Consistency) |
| **Best Used For** | Finance, E-Commerce transactions, ERP | Big Data, Social Media feeds, Real-time analytics |
| **Examples** | PostgreSQL, MySQL, SQLite | MongoDB, Redis, Cassandra, DynamoDB |

---

## 2. ACID Properties (Explained with Bank Transfer)

Imagine Transferring \$100 from Account A to Account B:
1. **Atomicity ("All or Nothing")**: Either both steps (Deduct \$100 from A AND Add \$100 to B) succeed, or if the server crashes in between, the transaction rolls back completely.
2. **Consistency**: The database transitions from one valid state to another. Constraints (e.g. Account balance $\ge 0$) are never violated.
3. **Isolation**: If another transaction checks Account A's balance simultaneously, it won't see half-updated intermediate data.
4. **Durability**: Once the transaction is committed, the changes are recorded permanently on non-volatile storage (WAL log / disk), surviving power outages.

---

## 3. Database Indexing (B+ Trees) Deep Dive

### How B+ Trees Work
* Database indexes use **B+ Trees** (balanced trees where all values reside at the leaf nodes, connected as a linked list).
* Lookups, Insertions, and Range Queries take **$O(\log N)$** time instead of an $O(N)$ full table scan.

### Clustered vs Non-Clustered Indexes
* **Clustered Index**: Determines the physical order of data on disk (usually the Primary Key `id`). There can only be **one** clustered index per table.
* **Non-Clustered (Secondary) Index**: A separate B+ Tree that maps the indexed column to the Primary Key pointer.

> **⚠️ The Indexing Trade-Off (Interview Question)**:  
> *Why not put an index on every single column?*  
> Because every `INSERT`, `UPDATE`, and `DELETE` must update the primary table **PLUS all index B+ Trees** on disk. Too many indexes severely degrade write throughput!

---

## 4. Database Scaling Techniques

1. **Read Replicas (Leader-Follower)**:
   * All `INSERT`/`UPDATE` writes go to the **Primary/Leader** database.
   * Multiple **Read Replicas** sync asynchronously to handle high read traffic.
   * *Problem*: **Replication Lag** (user writes data and immediately refreshes, but read replica hasn't received it yet).

2. **Database Sharding (Horizontal Partitioning)**:
   * Splitting rows across multiple physical database instances using a **Shard Key** (e.g. `hash(user_id) % num_shards`).
   * Allows databases to scale horizontally to petabytes of data.
