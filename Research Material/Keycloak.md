# KEYCLOAK

TAGS: #WebDevelopment 
BUILT-ON:
ENABLES:
PREREQUSIES:

---
## KEYCLOAK
**Keycloak** is your **Identity and Access Management (IAM)** server. It is the "Master Registry" of every person and device in your 185-store network.
It supports **Single Sign-On (SSO)**. A manager logs into the PWA once and can access the Inventory, Payroll, and BI dashboards without logging in again for each service.
- **The Problem:** You have 1,000+ employees (Pharmacists, Managers, Controllers). If you store passwords in your `users` table in PostgreSQL, you are responsible for hashing, salts, password resets, Multi-Factor Authentication (MFA), and social logins. If that DB leaks, you're in legal trouble.
- **The Solution:** You outsource all "Identity" to Keycloak. Your Python services never see a user's password. They only see a **signed digital passport (JWT)** that says "I am John, and I am a Store Manager."

## KEY POINTS
- LOCATION: Parallel to your API Gateway (Kong).
- INTERACTIONS:
	- **PWA:** Redirects the user to Keycloak’s login page.
	- **Kong:** Receives a token from the PWA and asks Keycloak (or its public key) if the token is faked.
	- **FastAPI:** Checks the "Roles" inside the token to decide if a user can "Delete an Order" or just "View" it.
- **Data Flow:** 
  `User Login` → `Keycloak Issues Token` → `PWA Token to Kong` → `Kong Authorizes` → `FastAPI Executes`.

## CORE CONCEPTS
- Realm: A "silo" for your project. You might have a "Staff" realm and a "Patient" realm. They are totally separate.
- **Client:** Any application that wants to use Keycloak. Your **PWA** is a client; your **FastAPI** services are clients.
- **Roles (RBAC):** "Pharmacist", "Admin", "Driver". You assign these to users.
- **Attributes (ABAC):** Extra data, like `store_id: 101`. This allows you to say "John is a manager, but _only_ for Store 101."
- **Tokens (JWT):** The small, encrypted JSON snippet that travels with every request.

## BEST PRACTISES
- **Token Exchange:** Use short-lived **Access Tokens** (5 mins) and longer **Refresh Tokens**. If a tablet is stolen in a store, you can revoke the session in the Keycloak admin panel immediately.
- **MFA for Managers:** Force "Corporate Admins" to use an Authenticator App, while "Associates" might just use a PIN for speed at the POS.
- **New Device Alerts:** Keycloak can trigger an event when a user logs in from a new IP/Browser. You can hook this to your **Notification Service** to alert the manager.

## ADVANCED USAGE
**Fine-Grained Authorization (AuthZ):** Go beyond roles. Use Keycloak's **Policy Enforcer**. You can write a rule: "A Pharmacist can only approve a prescription if it is assigned to their specific `store_id` AND it is currently within business hours."

## CONNECTION TO TOOLS
- **Kong:** Kong's `jwt` plugin uses Keycloak’s "Public Key" to ensure no one has tampered with the token.
-  **PostgreSQL:** Keycloak uses its own Postgres database to store user credentials. Your business Postgres is kept clean for pharmacy data.
- **PWA:** The PWA uses a library like `keycloak-js` to handle the "Login" button and token refreshing.

## INTERVIEW / SYSTEM DESIGN ANGLE
**Question:** "How do you handle Role-Based Access across 185 stores?" **Answer:** "We use **Keycloak for Centralized Identity**. We implement **RBAC** for job functions and **ABAC** (Attributes) for store-level isolation. By using **OIDC (OpenID Connect)**, we ensure that every microservice can independently verify a user's permissions by simply validating the JWT signature, without hitting the database every time."
