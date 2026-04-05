# SQLAlchemy

TAGS: #WebDevelopment  
BUILT-ON:
ENABLES:
PREREQUSIES:

---
## SQLAlchemy
**SQLAlchemy** is the "Translator" (ORM - Object Relational Mapper) between your Python code and your **PostgreSQL** database.
- Databases speak **SQL** (`SELECT * FROM inventory...`), but Python speaks **Objects** (`inventory.item_name`). Writing raw SQL inside Python is messy, prone to "SQL Injection" hacks, and doesn't give you autocomplete in your code editor.
- SQLAlchemy allows you to define your pharmacy tables as Python Classes. When you save a Python object, SQLAlchemy automatically writes the complex SQL to put it into Postgres.
- In a 185-store system, your queries get complex (e.g., "Find all insulin batches expiring in 30 days across Region X"). SQLAlchemy handles this complexity safely and efficiently

## KEY POINTS
- LOCATION: The "Data Access Layer" of your Backend Services.
- INTERACTIONS:
	- **FastAPI:** Takes a request (e.g., "Add Stock").
	- **SQLAlchemy:** Converts that request into a Database Command.
	- **PostgreSQL:** Executes the command and stores the data.
- DATA FLOW:
	- `FastAPI Route` → `SQLAlchemy Session` → `Postgres Tables`

## CORE CONCEPTS
- **The Model:** A Python class representing a table (e.g., `class Prescription`).
- **The Engine:** The actual connection "pipe" to Postgres.
- **The Session:** A "transaction." Think of it as a shopping cart—you add several changes, then hit "Commit" to save them all at once.
- **Declarative Base:** The starting point that tracks all your pharmacy models.
- **Alembic:** The "Time Machine" for your database. If you add a new column (like `is_refrigerated`), Alembic manages that change across all 185 store databases.

## BEST PRACTISES
- **Connection Pooling:** Don't open/close a connection for every pill sold. SQLAlchemy keeps a "pool" of open connections ready to go, which is vital for high-traffic POS systems.
- **Async Sessions:** Since you are using **FastAPI**, use the `ext.asyncio` version of SQLAlchemy. This prevents the "I'm waiting for the DB" bottleneck.
- **Eager Loading:** If you fetch an "Order," tell SQLAlchemy to fetch the "Order Items" at the same time to avoid the "N+1 Problem" (making 100 separate DB calls for 100 items).

## ADVANCED USAGE
**Hybrid Attributes:** You can create "calculated" fields that work in Python _and_ SQL.
- _Example:_ A field called `needs_replenishment` that automatically calculates `(current_stock < minimum_threshold)`. You can query this directly: `session.query(Medicine).filter(Medicine.needs_replenishment == True)`.