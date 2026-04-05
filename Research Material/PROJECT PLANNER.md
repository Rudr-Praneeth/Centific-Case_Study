# CENTRIFIC CASE STUDY


[[ARCHITECTURE DESIGN]]
## Problem Statement
## Omnichannel Pharmacy Operations Mobile Web Platform
Design and develop a responsive [[Microservices-based Web Application]] for a regional pharmacy retailer operating across 185 stores, 2 central warehouses, and a growing 
e-commerce fulfilment network. 
The solution should support secure authentication and role-based access for 
- corporate administrators
- pharmacy managers
- Inventory controllers
- Front-line associates. 
### FUNCTIONAL REQUIREMENTS
- Product and prescription-adjacent inventory tracking
- Point-of-sale sales and billing workflows
- Real-time stock visibility with replenishment alerts
- Store-level and warehouse-level reconciliation
- BI reporting dashboards for operational and commercial decision-making.
- Agentic AI features
	- Demand forecasting recommendations
	- Anomaly detection for shrinkage and stock movement
	- Conversational querying for managers
	- Workforce optimisation
	- Multi-language & multi-region support
- Behaviour Based access monitoring
	 New device login alters.
- Designed for deployment in a hybrid environment where stores have intermittent connectivity, requiring offline-tolerant workflows and reliable sync once connectivity is restored.
### NON FUNCTIONAL REQUIREMENTS
- Performance under peak activity.
- Scalability across regions
- Security and Auditability
- Reliability
- Observability
- Responsible AI
### TECH STACK
[[CASE STUDY-TECH STACK]]
- Experience Layer
	- [ ] NextJs
	- [ ] ReactJs + TypeScript
	- [ ] Tailwindcss
	- [ ] TanStack Query
	- [ ] PWA Shell
	- [ ] Service Workers
	- [ ] IndexedDB
- Edge and Access Layer
	- [ ] Kong API Gateway
	- [ ] Keycloak
	- [ ] OIDC/OAuth2
	- [ ] RBAC
	- [ ] Device risk rules
- Transaction domain services: Python core 
	- [ ] FastAPI
	- [ ] Django + Django REST Framework
- Data and event backbone
	- [ ] PostgreSQL
	- [ ] Redis
	- [ ] Kafka
	- [ ] Celery
	- [ ] pgvector
- Deployment and Runtime
	- [ ] Docker
	- [ ] Kubernetes
- Observability and Supportability
	- [ ] OpenTelemetry
	- [ ] Prometheus
	- [ ] Grafana
### MICROSERVICES
1. Identity Policy Service
	Handles user profile metadata, store assignment, role mappings, device trust, login anomaly events, and audit pointers. Keycloak remains the identity source; this service holds your business-side policy state.
2. Catalog Pricing Service
	Owns product master, pack sizes, substitutes, price books, promotions, tax rules, margin constraints, and assortment. This is where you add profit features like promo optimization and substitution prompts at checkout.
3. Inventory Replenishment Service
	Owns store stock, warehouse stock, batch/lot, expiry, adjustments, cycle counts, transfer orders, reorder points, and replenishment alerts. This is your shrink-control and in-stock engine.
4. POS Billing Service
	Owns carts, sale headers, sale lines, tenders, invoices, returns, voids, discounts, and receipt generation. This is the offline-tolerant cashier path.
5. Reconciliation Service
	Owns stock snapshots, variance cases, audit trails, warehouse-to-store reconciliation, and mismatch workflows. This is where loss-prevention and close-of-day controls live.
6. Reporting BI Service
	Owns denormalized read models, KPI marts, materialized views, and export endpoints for corporate dashboards. PostgreSQL materialized views fit here well because they persist query results and can be refreshed on demand
7. AI Insights Service
	Owns demand forecasting, anomaly detection, conversational analytics, and recommendation APIs. It should not write directly to transactional tables; it reads from curated events and read models.
8. Sync Office Service
	Owns local transaction replay, conflict detection, idempotency handling, and store connectivity recovery. This is the bridge between the offline PWA and the online services.


### DELIVERABLES:
- A working prototype
- Detailed technical solution
	- [x] Architecture
	- [x] UI flows
	- [x] APIs
	- [x] Data model
	- [x] AI features
	- [x] Deployment approach
	- [ ] Non-functional controls
### **EVALUATION CRITERIA:**
- Clear microservices architecture with well-defined separation between UI, services, and PostgreSQL data layer
- Responsive mobile-first design that works across phones, tablets, and desktops
- Secure authentication and role-based access control for multiple user roles
- Robust inventory, sales, billing, replenishment, and reporting functionality
- Practical handling of hybrid/offline store connectivity and sync resilience
- Meaningful BI dashboards and operational analytics for store and corporate users
- Agentic AI capabilities including recommendations, anomaly detection, and conversational querying
- Use of Python technologies and PostgreSQL with sound API design
- Attention to performance, scalability, reliability, security, and observability
- Appropriate guardrails for safe, explainable, and compliant AI-assisted development

## RESOURCES 
- [NextJs Django FastAPI](https://damianhodgkiss.com/tutorials/fullstack-django-fastapi-nextjs).
	Notes: [[NextJS Django FastAPI]]
- 