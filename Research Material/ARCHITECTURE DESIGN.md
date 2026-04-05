
## PROBLEM STATEMENT
## Omnichannel Pharmacy Operations Mobile Web Platform
Design and develop a responsive **Microservices-based Web Application** for a regional pharmacy retailer operating across **185 stores, 2 central warehouses, and a growing** 
**e-commerce fulfilment network**. 
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

## ARCHITECTURE

### MICROSERVICES
Each Microservice strictly owns data + business logic (DDD aligned)
1. Identity Policy Service
2. Catalog & Pricing Service
3. Inventory & Replenishment Service
4. POS Billing Service
5. Reconciliation Service
6. Reporting & BI Service
7. AI Insights Service
8. Sync Office Service