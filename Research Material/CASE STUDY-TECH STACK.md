# OMNICHANNEL PHARMACY PLATFORM — TECH STACK

---

## 1. EXPERIENCE LAYER 
- [ ] Next.js (App Router)
- [x] React + TypeScript
- [x] Tailwind CSS
- [x] shadcn/ui (accessible component system)
- [x] [[TanStack Query]] (server state + caching)
- [x] [[Progressive Web App]] (PWA shell)
- [x] Service Workers (offline caching + request interception)
- [x] IndexedDB (local persistence for offline transactions)
### Responsibilities
- POS (cashier workflows)
- Store manager dashboards
- Warehouse console
- Replenishment + reconciliation UIs
- Corporate BI entry points
### Advanced Capabilities
- Offline-first transaction queueing
- Background sync on reconnect
- Optimistic UI updates for POS speed
- Multi-language support (i18n ready)
---

## 2. [[EDGE & ACCESS LAYER]] (Secure API Entry)
- [x] [[Kong API Gateway]]
- [x] [[Keycloak]] 
      (Identity Provider) + RBAC+ ABAC
- [x] [[OIDC OAuth2]]
- [ ] Device Risk Engine (custom rules)
### Responsibilities
- API routing & rate limiting
- Authentication & token issuance (JWT)
- Authorization (roles + policies)
- New-device login alerts
- Step-up authentication (risk-based)
### Advanced Capabilities
- API analytics + throttling
- AI Gateway (LLM request governance via Kong)
- Centralized audit logging
---

## 3. BACKEND — TRANSACTION DOMAIN SERVICES (Python Core)
### Core Stack
- [x] FastAPI (primary microservices framework)
- [x] Django + Django REST Framework (select transactional domains / admin)
      [[FastAPI & Django]]
- [x] Pydantic (data validation)
- [x] [[SQLAlchemy]] (ORM / query layer)
### API Strategy
- [ ] REST (external APIs)
- [ ] gRPC (internal service-to-service communication)
### Responsibilities
- Inventory management
- POS & billing
- Catalog & pricing
- Stock transfers & adjustments
- Reconciliation workflows
- Notifications
### Advanced Capabilities
- Strict service boundaries (domain-driven design)
- Idempotent APIs for offline replay
- Schema-first API contracts (OpenAPI)
---

## 4. [[DATA & EVENT BACKBONE]]
- [x] PostgreSQL (system of record)
- [x] Redis (cache, locks, ephemeral state)
- [x] Apache Kafka (event streaming backbone)
- [x] Celery (limited async jobs)
- [x] pgvector (AI embeddings inside Postgres)
### Data Strategy
- Database-per-service (logical separation)
- Read replicas for analytics
- Materialized views for BI
- Logical replication for scaling
### Event Strategy
- Kafka topics:
  - inventory-events
  - pos-events
  - audit-events
  - sync-events
### Advanced Capabilities
- Outbox pattern (reliable event publishing)
- Event-driven architecture (EDA)
- Time-travel debugging via event logs
---

## 5. OFFLINE & SYNC ARCHITECTURE (CRITICAL DIFFERENTIATOR)
- [x] Sync Service (dedicated microservice)
- [x] IndexedDB (client-side storage)
- [x] Background Sync API
### Responsibilities
- Offline transaction capture
- Replay on reconnect
- Conflict detection & resolution
- Idempotency enforcement
### Conflict Strategy
- Versioning + timestamps
- Vector-clock style resolution (advanced)
- Manual reconciliation fallback

---
## 6. AI & INSIGHTS LAYER
- [ ] Darts / Prophet (demand forecasting)
- [ ] PyOD (anomaly detection)
- [ ] LLM APIs (OpenAI / OSS models)
- [ ] pgvector (semantic search)
- [ ] Feature store (Postgres / Redis)
### Capabilities
- Demand forecasting (SKU/store/day)
- Replenishment recommendations
- Shrinkage & anomaly detection
- Workforce optimization
- Conversational BI
### Query Flow
User 
→ Natural Language  
→ Embedding (pgvector)  
→ SQL generation  
→ LLM explanation  
### Guardrails
- Prompt filtering
- No PII leakage
- Explainable outputs
- Audit logging of AI responses
---

## 7. DEPLOYMENT & RUNTIME
- [ ] Docker (containerization)
- [ ] Kubernetes (orchestration)
- [ ] Helm (deployment management)
- [ ] GitHub Actions (CI/CD)
### Responsibilities
- Service isolation
- Horizontal scaling
- Rolling deployments
- Environment consistency
### Advanced Capabilities
- Multi-region deployment
- Auto-scaling (HPA)
- Blue/Green deployments
---

## 8. OBSERVABILITY & SUPPORTABILITY
- [ ] OpenTelemetry (traces + metrics)
- [ ] Prometheus (metrics collection)
- [ ] Grafana (dashboards)
- [ ] Jaeger / Tempo (distributed tracing)
- [ ] Loki / ELK (log aggregation)
### Monitoring
- API latency
- Error rates
- Kafka lag
- DB performance
### SLOs
- POS latency < 1s
- 99.9% transaction success rate
---

## 9. SECURITY & COMPLIANCE
- [ ] TLS everywhere
- [x] JWT-based authentication
- [ ] Audit logs (immutable)
- [ ] Secrets management (Vault / K8s secrets)
### Advanced Controls
- Behavior-based anomaly detection
- Device fingerprinting
- Fine-grained access policies
---

## 10. PERFORMANCE & SCALABILITY STRATEGY
- [x] Redis caching (hot paths)
- [x] Read replicas (Postgres)
- [x] Kafka buffering (traffic spikes)
- [x] Async processing (non-blocking flows)
### Patterns
- CQRS (for reporting vs transactions)
- Event-driven scaling
- Region-aware routing
---

## 12. PROFIT-DRIVEN DIFFERENTIATORS
- [ ] Demand-based replenishment ranking
- [ ] Substitution engine at POS
- [ ] Basket uplift recommendations
- [ ] Shrinkage anomaly detection
- [ ] Workforce optimization engine
- [ ] Conversational analytics
---

## FINAL ARCHITECTURE PRINCIPLES
- Offline-first, cloud-synced
- Event-driven microservices
- Strong domain boundaries
- AI as augmentation (not replacement)
- Observability-first design
- Security by default
