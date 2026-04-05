# OIDC/OAuth2

TAGS: #WebDevelopment 
BUILT-ON:
ENABLES:
PREREQUSIES:

---
## OIDC/OAuth2
If **Keycloak** is the DMV office that issues your ID, **OIDC and OAuth2** are the official laws and protocols that dictate how that ID is designed and used.
- **OAuth2 (The Valet Key):** It is a framework for **Authorization**. It allows the PWA to act on your behalf (e.g., "The PWA is allowed to upload this inventory count to the server") without the server needing your password.
- **OIDC (The ID Card):** Built on top of OAuth2, it adds **Authentication**. It provides a standardized way to say "Who is this person?" (Name, Email, Role).

**The Problem:** Without these, every app would have its own "Login" logic, and sharing data between services would be a security nightmare.
**The Solution:** A universal "handshake" that everyone—the PWA, Kong, and FastAPI—understands.

## KEY POINTS
OIDC/OAuth2 is the **Communication Language** of your Access Layer.
- **Location:** It is the "protocol" used between the **PWA**, **Keycloak**, and **Kong**.
- **Interactions:**
    - **PWA:** Uses the **Authorization Code Flow** to get tokens.
    - **Kong/FastAPI:** Uses **Bearer Tokens** (JWTs) to authorize requests.
- **Data Flow:** 
	1. Pharmacist clicks "Login" (OIDC Request). 
	2. Keycloak gives a **Code**. 
	3. PWA trades that Code for an **Access Token** (OAuth2).
	4. PWA sends that Token in the header of every API call.

## CORE CONCEPTS
1. **Access Token:** A short-lived (5-15 min) "ticket" used to access data.
2. **ID Token:** A specific OIDC token that contains user profile info (Name, Email).
3. **Refresh Token:** A long-lived key used to get a _new_ Access Token when the old one expires (so the pharmacist isn't logged out mid-shift).
4. **Scopes:** The "Permissions" requested (e.g., `openid`, `profile`, `inventory:write`).
5. **PKCE (Proof Key for Code Exchange):** A security layer for PWAs that prevents hackers from intercepting the "Code" during login. **You must use this for your PWA.**

## BEST PRACTISES
- **Rotate Refresh Tokens:** Every time a refresh token is used, issue a new one and invalidate the old one.
- **Audience Validation:** Ensure the `aud` claim in the token matches your service so a token for "Pharmacy A" can't be used to access "Pharmacy B."

## ADVANCED USAGE


