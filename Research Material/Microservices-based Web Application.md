# Microservices-based Web Application

TAGS: #
BUILT-ON:
ENABLES:
PREREQUSIES:

---
## DEFINITION
A **microservices-based web application** is a type of software architecture where a large application is built as a collection of **small, independent services** that work together. Each service focuses on a specific business function and communicates with other services through APIs.
In monolithic applications, everything is built as one large system. In contrast, **microservices break the application into smaller parts**, each running independently.

## KEY FEATURES 
Each microservice has:
- Separate logic and database.
- Can be developed, deployed, and scaled independently.
- Communicates via protocols like HTTP/REST, gRPC, or messaging queues
![[Pasted image 20260403193104.png]]

## KEY CHARACTERISTICS
- Independent Services
- Decentralized Data Management
- API-Based Communication
- Scalability
- Technology Diversity

## COMPONENTS
- Frontend
	Web browser or mobile app
- API Gateway
	Single entry point for all client requests
	Routes requests to appropriate services
- Microservices
	Independent backend services
- Databases
	Separate or shared depending on design
- Service Communication
	REST APIs or message queues (like Kafka, RabbitMQ)
- DevOps & Infrastructure
	Containers (Docker), orchestration (Kubernetes), CI/CD pipelines

## ADVANTAGES
- **Scalability**
- **Flexibility**
- **Fault Isolation**
- **Continuous Deployment**

## DISADVANTAGES
- **Complexity**
- **Network Latency**
- **Data Consistency Issues**
- **Deployment Overhead**
