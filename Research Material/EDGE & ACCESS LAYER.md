# EDGE AND ACCESS LAYER

TAGS: #WebDevelopment 
BUILT-ON:
ENABLES:
PREREQUSIES:

---
## EDGE & ACCESS LAYER
### THE BIG PICTURE: THE "PASSPORT" ANALOGY
Think of your Access Layer like an **International Airport**:
- **OIDC/OAuth2:** The global standard for how Passports and Visas must look.
- **Keycloak:** The Government Office that verifies your face and issues the Passport. 
- **Kong:** The Security Gate at the terminal that checks your Passport before letting you onto the "FastAPI" flight.

### THE STEP-BY-STEP INTERACTION FLOW
Let’s trace a **Pharmacy Manager** named Sarah trying to view a **Demand Forecast** for her store.
STEP 1: The OIDC Handshake (Authentication)
1. **PWA → Keycloak:** The PWA redirects Sarah to the Keycloak Login Page (using the **OIDC** protocol).
2. **Challenge:** Keycloak asks for Username/Password + MFA.
3. **Success:** Keycloak verifies Sarah. It looks up her **RBAC** (Role: Manager) and **ABAC** (Attribute: `store_id=185`).
4. **Issuance:** Keycloak generates a **JWT (JSON Web Token)**. This is her "Digital Passport."

STEP 2: The OAuth2 Bearer Token (Authorization)
The PWA now holds this JWT.
1. **PWA → Kong:** When Sarah clicks "View Forecast," the PWA sends a request to `api.pharmacy.com/v1/forecasting`.
2. **The Header:** It attaches the JWT in the header: `Authorization: Bearer <JWT_data>`.

STEP 3: The Kong Gateway Check (The Filter)
Kong receives the request before it ever touches your Python code.
1. **Signature Check:** Kong uses Keycloak’s **Public Key** to verify the JWT hasn't been forged.
2. **Plugin Execution:**
    - **Rate Limiting:** Kong checks: "Has Sarah requested 100 forecasts in the last minute?" (Prevents bot attacks).
    - **IP Restriction:** Kong checks if the request is coming from a known Pharmacy VPN or an unauthorized country.

STEP 4: Downstream to FastAPI (The Execution)
If Kong is happy, it "forwards" the request to the `ai-insights-service`.
1. **Context Passing:** Kong strips the heavy security headers and passes the "Sarah is a Manager of Store 185" info to FastAPI.
2. **Logic:** FastAPI sees the `store_id=185` and filters the PostgreSQL query to only show data for that specific location.

## HOW RBAC & ABAC WORK TOGETHER
| **Feature** | **Logic Type**                | **Example in Your Pharmacy**                                                 |
| ----------- | ----------------------------- | ---------------------------------------------------------------------------- |
| **RBAC**    | **What** can you do?          | **Role:** `inventory_controller`. Permission: Can edit stock levels.         |
| **ABAC**    | **Where/When** can you do it? | **Attribute:** `store_id: 101`. Result: Can _only_ edit stock for Store 101. |
