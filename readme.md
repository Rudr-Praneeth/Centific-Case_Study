# Omnichannel Pharmacy Operations Platform

## Overview
This project presents a scalable, offline-capable microservices-based web platform designed for a regional pharmacy and wellness retail network. The system supports store operations, warehouse management, and e-commerce workflows while ensuring reliability in environments with intermittent connectivity.

The solution is based on real-world observations from pharmacy retail outlets such as MedPlus and Apollo Pharmacy, combined with system design research and distributed systems principles.

---

## Key Objectives
- Enable seamless point-of-sale (POS) operations across stores
- Maintain accurate, real-time inventory visibility
- Support offline-first workflows with reliable synchronization
- Provide analytics and business intelligence dashboards
- Integrate AI-driven insights for operational optimization
- Ensure security, scalability, and auditability

---

## System Architecture

### High-Level Design
The platform follows a Domain-Driven Design (DDD) approach with independently deployable microservices and decentralized data ownership.

Core architectural components:
- API Gateway for routing, authentication, and rate limiting
- Microservices for domain-specific responsibilities
- Event-driven communication using Kafka
- PostgreSQL databases per service
- Redis for caching and distributed coordination
- Sync Service for offline-first resilience

### Core Services
- **POS Billing Service**: Cart lifecycle, checkout, payments, invoices, returns
- **Inventory Service**: Stock tracking, reservations, replenishment, transfers
- **Catalog & Pricing Service**: Product management, pricing, promotions
- **Identity Policy Service**: Authentication, authorization, device trust
- **Inventory Reconciliation Service**: Variance detection and audit workflows
- **Reporting BI Service**: Aggregated analytics and dashboards
- **Agentic AI Service**: Forecasting, anomaly detection, conversational insights
- **Sync Service**: Offline transaction ingestion, replay, and conflict resolution

---

## Checkout Flow (Online)
1. Product scanned or searched
2. Pricing and promotions resolved
3. Inventory reserved
4. Payment processed
5. Transaction committed
6. Events published for downstream processing

Consistency is ensured using:
- Idempotent APIs
- Transactional outbox pattern
- TTL-based inventory reservations
- Compensation handling for failures

---

## Offline-First Design

### Key Features
- Local storage using IndexedDB
- Cached product and pricing data with TTL
- Offline transaction capture
- Background synchronization on connectivity restoration

### Sync Workflow
- Batch upload of offline transactions
- Idempotent replay with deduplication
- Conflict detection using versioning
- Automated and manual conflict resolution strategies
- Dead-letter queue for failed events

---

## Data Model

### Design Principles
- Database per service
- No cross-service joins
- Event-driven data propagation
- Global identifiers for correlation (store_id, sku, transaction_id)

### Key Entities
- Product, SKU, PriceBook, Promotion
- InventoryItem, BatchLot, StockLedger, Reservation
- Cart, SaleTransaction, Payment, Invoice
- UserProfile, DeviceProfile, LoginEvent
- SyncBatch, SyncEvent, ConflictLog

---

## AI Capabilities

### Features
- Demand forecasting for SKU-level planning
- Inventory anomaly detection (shrinkage and irregular movement)
- Conversational querying for business insights

### Design Approach
- Feature extraction from event streams and BI models
- Model inference via API layer
- Human-in-the-loop approval for critical decisions
- Confidence scoring and audit logging

---

## Technology Stack

### Backend
- Python (FastAPI / Flask)
- PostgreSQL
- Kafka
- Redis

### Frontend
- React.js with TypeScript
- Tailwind CSS
- Progressive Web Application (PWA)
- IndexedDB for offline storage

### Infrastructure
- Kubernetes (container orchestration)
- Docker
- Helm (deployment management)

### Observability
- OpenTelemetry (distributed tracing)
- Prometheus (metrics)
- Grafana (dashboards)
- Loki (logging)

---

## Security

- JWT-based authentication using Keycloak
- Role-Based and Attribute-Based Access Control (RBAC + ABAC)
- Device trust and anomaly detection
- mTLS for secure service-to-service communication
- Audit logging for all critical actions

---

## Non-Functional Considerations

### Performance
- Redis caching for hot data
- Optimized checkout path for low latency
- Connection pooling

### Scalability
- Horizontal Pod Autoscaling (HPA)
- Kafka partitioning by store_id
- Stateless service design

### Reliability
- Retry mechanisms with exponential backoff
- Circuit breakers
- Idempotent operations
- Sync replay tracking

### Observability
- End-to-end trace correlation
- Defined SLOs for critical operations

---

## Prototype Status

A working prototype is currently under development to demonstrate:
- Core service interactions
- POS checkout workflow
- Offline-to-online synchronization

This repository will be updated iteratively with:
- Service implementations
- API contracts
- Sample datasets and test scenarios

---

## Research and References

This solution is informed by:
- Field observations from pharmacy retail stores: MedPlus, Apollo Pharmacy
- Distributed systems design patterns
- Event-driven architecture principles
- Offline-first application design strategies

Detailed research notes and supporting materials are included in this repository.

---

## Future Enhancements
- Advanced forecasting models with continuous learning
- Automated replenishment workflows
- Enhanced fraud detection mechanisms
- Multi-region data replication improvements
- Full production-grade deployment pipelines

---

## Author
Praneeth Narayan  
Final Year B.Tech Student (Graduating July)

---

## License
This project is intended for academic and evaluation purposes.