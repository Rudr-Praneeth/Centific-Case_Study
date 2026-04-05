# DATA & EVENT BACKBONE

TAGS: #WebDevelopment 
BUILT-ON:
ENABLES:
PREREQUSIES:

---
# DATA BACKBONE 
## POSTGRESQL
It is ACID-compliant (Atomicity, Consistency, Isolation, Durability) Database. 
**Database-per-service**. The `inventory-service` has its own tables; the `pos-service` has its own. This prevents a bug in the "Reporting" service from crashing the "Sales" service.
**Advanced Tech:** * **Read Replicas:** You have one "Leader" DB for writing sales and several "Followers" for the AI/BI to read from so they don't slow down the cashiers.

## PGVECTOR
**pgvector:** This is a "Power-up" for Postgres. It stores AI "Embeddings" (mathematical representations of text). This allows your **Conversational BI** to understand that "Show me drugs for headaches" should include "Paracetamol."

## REDIS
An ultra-fast, "In-Memory" data store. It’s like a sticky note on a monitor—quick to read, but gone if you throw it away. Postgres is on a disk (slower); Redis is in RAM (instant).
- DISTRIBUTED LOCKING: When two pharmacists try to "Reconcile" the same warehouse shipment at once, Redis creates a **Lock**. The first person gets the lock; the second person is told to wait.
- CACHING: Instead of asking Postgres for the price of "Aspirin" 1,000 times a minute, you store it in Redis for 10 minutes.

# EVENT BACKBONE
## APACHE KAFKA
The "Central Nervous System." It’s a giant, unbreakable log of everything that happens in the business.
Unlike a direct API call where Service A talks to Service B, Kafka allows Service A to just "shout" an event into a **Topic**. Anyone who cares can listen.
TOPICS:
- `inventory-events`: When stock hits zero, this event is fired.
- `pos-events`: Every receipt generated goes here.
- `sync-events`: When a store comes back online, its offline data flows through here.
**Time-Travel Debugging:** If the `reporting-service` crashes on Tuesday, you can "replay" all Kafka events from Monday to rebuild the reports perfectly.

## CELERY
A task queue for things that take a long time.
If a manager clicks "Generate Monthly PDF Report," you shouldn't make them stare at a loading spinner for 2 minutes.
FastAPI tells Celery "Hey, build this PDF in the background." FastAPI immediately tells the manager "We're working on it!" Celery finishes the job and sends a notification when it's ready.

---
# DATA STRATEGIES
## **The Outbox Pattern (Reliability)**
What if you save a sale to Postgres, but the Wi-Fi dies before you can tell Kafka? Now the Warehouse thinks you still have the stock.
You save the Sale _and_ the "Message to Kafka" in the **same Postgres transaction**. A small "Relay" service then reads that table and pushes it to Kafka. **This guarantees the database and Kafka never get out of sync.**

## Event-Driven Architecture (EDA)
Instead of the POS Service telling the Inventory Service: "Hey, please update stock," the POS Service simply says: **"I sold an item."** 
- The **Inventory Service** hears it and updates stock.
- The **AI Service** hears it and updates the forecast.
- The **Audit Service** hears it and logs the tax.

## Materialized Views (For BI)
Calculating "Total Profit per Region" across 5 million rows is slow.
Postgres creates a "Snapshot" table (Materialized View) that pre-calculates this every hour. The BI dashboard loads instantly because the math is already done.

