# TanStack Query

TAGS: #WebDevelopment  
BUILT-ON:
ENABLES:
PREREQUSIES:

---
## TANSTACK QUERY
TanStack Query (TQ) is the **server‑state machine** that acts as a "Brain" that manages how your frontend talks to your backend. 
It sits in the React layer and glues your microservices to the UI
- It fetches data and managing caching
- It manages retries, background refetching, and optimistic updates so your offline‑first, high‑performance POS and dashboards don’t have to roll all that from scratch.
### PROBLEM SOLVED
Without it, you have to manually manage loading spinners, error states, and "stale" data (e.g., showing a medicine price that changed 5 minutes ago). You'd end up with messy `useEffect` hooks everywhere. )
### WHY OVER ALTERNATIVES
- **Redux** is for "Global State" (Is User logged in?)
  **TanStack Query** is for "Server State" (What is the stock level of Aspirin?)
- It handles **~={purple}caching=~, ~={purple}retries=~, and ~={purple}background updates=~** automatically, which is vital for a high-traffic POS system.

## KEY POINTS
- LOCATION: Experience Layer
- INTERATIONS: Wraps FastAPI calls
- DATA FLOW:
	- UI asks TanStack Query for "Inventory".
	- TanStack Query checks its **Cache**
	- If empty/old, it hits the **Kong API Gateway** → **FastAPI**.
	- It saves the result and hands it to the UI.

## CORE CONCEPTS
- **Query Keys**: Unique IDs for data. If the key changes, the data refreshes.
- **StaleTime**: How long data is "fresh."
	"Drug Categories" might have a high `staleTime` (1 hour)
	But "Stock Levels" should have 0 (always check for updates).
- **Mutations:** Used when you _change_ data (e.g., "Complete Sale").
- **Invalidation:** After a "Sale" mutation, you tell TanStack Query: "Hey, the stock for this item is now wrong, go fetch it again."
### USAGE EXAMPLE
1. Fetching Stock
``` ts
const { data, isLoading } = useQuery({
  queryKey: ['stock', storeId],
  queryFn: () => fetchInventory(storeId),
  staleTime: 1000 * 30, 
});
```
2. Processing a Sale
``` ts
   const mutation = useMutation({
  mutationFn: (newSale) => postSaleToApi(newSale),
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['stock'] });
  },
});
```

## CORE OPERATIONS
### Handling the "185-Store Storm" (Smart Throttling)
With 185 stores, thousands of staff members are clicking around simultaneously.
- **The Danger:** Every time a staff member switches from the "Billing" tab to the "Inventory" tab, your **FastAPI** backend would normally get hit with a new request. This "hammers" your **PostgreSQL** database.
- **The TanStack Solution:** It uses **Stale-While-Revalidate**. If 10 people in Store #42 look at the same "Aspirin" stock level within 1 minute, TanStack Query only hits the server **once**. The other 9 times, it serves the answer from the local cache. It turns a "storm" of traffic into a "drip."
### The "Offline-First" Glue
Your project requirement specifically mentions **intermittent connectivity** and **PWA**.
- **The Danger:** In a rural pharmacy, the Wi-Fi drops for 30 seconds. Without this tool, the "Stock Search" bar would break, showing a spinning wheel of death or a 404 error.
- **The TanStack Solution:** It integrates with **IndexedDB** (your local browser database). It "persists" the cache.    
    - **Scenario:** The internet dies. The pharmacist searches for "Amoxicillin." TanStack Query says, _"I can't reach the server, but here is the stock count from 2 minutes ago."_ The pharmacy keeps moving.
    - **Reconnection:** Once the Wi-Fi returns, TanStack Query notices and automatically triggers a "refetch" to sync the data without the user hitting refresh.
### "Optimistic" Sales (Speed = Profit)
In a busy pharmacy, a 2-second delay at the POS (Point of Sale) creates a line out the door.
- **The Danger:** Waiting for **FastAPI → Kafka → Postgres → Response** can take time during peak hours.
- **The TanStack Solution:** **Optimistic Updates.** When the cashier hits "Complete Sale," TanStack Query updates the UI immediately to show "Sale Successful" and deducts the stock locally. It sends the real data to the backend in the background. If the backend fails, it rolls back. This makes the app feel "local-speed" even though it's a web app.
### 4. Keeping the AI Layer Fed
You have **Agentic AI** and **Conversational BI** features.
- **The Logic:** AI features are "heavy." You don't want your LLM (via Kong Gateway) to re-run an expensive "Demand Forecast" every time a manager refreshes their dashboard.
- **The TanStack Solution:** You can set a long `staleTime` (e.g., 30 minutes) for AI insights. The manager sees the complex AI data instantly because TanStack Query "remembered" the result of the last expensive query.

## BEST PRACTISES
1. **Prefetching:** When a pharmacist hovers over a "Reconciliation" button, start fetching that data _before_ they even click it.
2. **Offline Support:** Since your stores have "intermittent connectivity," TanStack Query works with your **IndexedDB** to persist the cache so the UI doesn't go blank when the Wi-Fi drops.
3. **Retries:** Set `retry: 3` for network blips, but `retry: false` for 404 errors.

## CONNECTION TO TOOLS
- **FastAPI:** TanStack Query consumes the JSON output from your FastAPI endpoints.
- **Redis:** While Redis caches data on the **Server**, TanStack Query caches it on the **User's Device**.
- **Redis:** While Redis caches data on the **Server**, TanStack Query caches it on the **User's Device**.
