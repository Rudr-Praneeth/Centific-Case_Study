# KONG API GATEWAY

TAGS: #WebDevelopment  
BUILT-ON:
ENABLES:
PREREQUSIES:

---
## KONG API GATEWAY
Kong API Gateway acts as a traffic controller for the microservices. It’s built on **Nginx**, meaning it’s incredibly fast (sub-millisecond latency) and uses a "Plugin" architecture to add features.
**The Problem:** 8+ microservices (Inventory, Billing, AI, etc.). If every service had to handle its own security, rate limiting, and logging, you’d be writing the same code 10 times. Plus, exposing all those services directly to the internet is a massive security risk.
**The Solution:** You put Kong at the very front. Every request from your PWA hits Kong first. Kong checks: "Are you logged in? Are you allowed to see this? Are you sending too many requests?" If everything is fine, it passes the request to the correct Python service.

## KEY POINTS
- LOCATION: Between the Public Internet (PWA) and your Private Network (FastAPI services).
- INTERACTIONS:
	- **Inbound:** Receives HTTPS requests from the PWA.
	- **Identity:** Talks to **Keycloak** to verify JWT tokens.
	- **Outbound:** Routes requests to **FastAPI** services.
	- **Observability:** Sends metrics to **Prometheus/Grafana**.
- **Data Flow:** `PWA Request` → `Kong (Checks Auth)` → `Kong (Rate Limits)` → `Inventory Service`

## CORE CONCEPTS
- Route
- Service: Internal address of the microservice
- Plugins: Modular "power-ups" you toggle on/off (e.g., `rate-limiting`, `cors`, `key-auth`).
- **Upstream/Target:** How Kong handles load balancing between multiple instances of your FastAPI containers.
- **Declarative Config (decK):** Managing Kong using YAML files instead of clicking buttons, making it reproducible.
### EXAMPLE USAGE
The Config (Simplified YAML):
``` yaml
_format_version: "3.0"
services:
  - name: ai-service
    url: http://ai-insights-service:8000
    routes:
      - name: ai-forecasting-route
        paths:
          - /ai/forecast
    plugins:
      - name: rate-limiting
        config:
          minute: 5  
      - name: jwt
        config:
          claims_to_verify:
            - exp 
```

### BEST PRACTISES
- **Centralized Logging:** Use the `http-log` plugin to send every single request/response metadata to your ELK stack for auditing
- **Circuit Breaking:** If the `reconciliation-service` is crashing, Kong can stop sending traffic to it automatically to prevent the whole system from slowing down.
- **Secret Masking:** Use plugins to ensure sensitive patient PII in logs is masked before it reaches your monitoring tools.

### ADVANCED USAGES
- **The AI Gateway Pattern:** Since you have AI features, you can use Kong as an **AI Proxy**. You can use a plugin to log the _cost_ of LLM tokens used by different pharmacy branches or to strip out PII (Patient Names) _before_ the request even hits OpenAI/OSS models.

## CONNECTION TO TOOLS
- **Keycloak:** Kong acts as the "Enforcement Point" for the tokens Keycloak issues.
- **FastAPI:** FastAPI doesn't have to worry about "who is this user?"—it trusts that if a request reached it, Kong already verified it.
- **Redis:** Kong often uses Redis to keep track of rate-limiting counters across multiple instances.

