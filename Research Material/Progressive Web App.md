# Progressive Web App

TAGS: #WebDevelopment  
BUILT-ON:
ENABLES:
PREREQUSIES:

---
## PROGRESSIVE WEB APPLICATION
A **PWA (Progressive Web App)** is a website that acts like a native mobile app.
- **The Problem:** In your 185-store pharmacy network, a pharmacist in a rural area might lose internet mid-transaction. A standard website would "white-screen" and lose the prescription data. A native app (iOS/Android) is expensive to maintain across different devices (tablets, PCs, handhelds).
-  **The Solution:** The PWA "shells" your app. It downloads the UI (HTML/CSS/JS) once and keeps it on the device. Even if the Wi-Fi dies, the UI stays visible, and data is saved to a local database (IndexedDB) until the connection returns.
- **Alternatives:** 
	  ***Native Apps:** High dev cost; harder to update 185 stores simultaneously.
	  **Standard Web App:** Fails instantly without internet.

## KEY POINTS
- LOCATION: Experience Layer (Device Local)
- **Interactions:** 
	  **Frontend:** React/Next.js UI.
	  **Local Storage:** IndexedDB (The "Offline Brain").
	  **Network:** Interacts with the **Kong API Gateway**.
- **Data Flow:** 
	1. User scans a drug barcode. 
	2. PWA checks **IndexedDB** for local stock. 
	3. PWA sends a "Sync Event" to the **Sync Service** via the **Service Worker**.

## CORE CONCEPTS
1. **Service Worker (The Proxy):** A script that runs in the background. It intercepts network calls. If the network is down, it pulls data from the cache.
2. **IndexedDB:** A heavy-duty database inside the browser. It stores thousands of SKUs and pending prescriptions locally.
3. **Workbox:** The industry-standard library (by Google) you'll use to manage these background scripts.

## WORKFLOW
1. Pharmacist hits "Complete Sale."
2. The PWA shows a "Pending Sync" yellow badge.
3. The receipt is printed (via local Bluetooth/USB).
4. **When Wi-Fi returns:** The Service Worker "replays" the sale to your FastAPI `pos-billing-service`.

## BEST PRACTICES
- **Cache-First for Assets:** Store the UI (CSS/Images) locally so the app opens in <1 second.
- **Network-First for Pricing:** Always try to get the latest price from the server; fallback to local price only if offline.
- **Background Sync API:** Use this so the browser syncs your data even if the pharmacist closes the tab.

## ADVANCED USAGE
**Differential Sync:** Instead of sending the whole "Order" object back, only send the "Changes" (the Delta). This saves bandwidth on slow 3G/Satellite links common in regional warehouses.

## CONNECTION TO TOOLS
- **FastAPI:** Receives the "Replayed" transactions from the PWA.
- **PostgreSQL:** The final home for the data once synced.
- **Kafka:** The `sync-service` pushes a message to Kafka (`pos-events`) once the PWA upload is successful.
- **Redis:** Stores the "Session Token" which the PWA must keep in `localStorage` to stay logged in while offline.
