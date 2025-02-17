# Kutanga Hub

## Overview

Kutanga Hub is a comprehensive platform designed to manage game servers, monitor system resources, and provide role-based access control. The project is built using a microservices architecture with a Python backend and a React frontend.

## To-Do List

### 1. Project Initialization and Setup ✅ (Completed)

- [x] 1.1 Define the overall system architecture (Microservices chosen)
- [x] 1.2 Decide on folder structure for backend (Python) and frontend (React)
- [x] 1.3 Set up version control (e.g., Git repository)
- [x] 1.4 Create a virtual environment and install essential Python packages
- [x] 1.5 Initialize the React project

### 2. Database Setup (PostgreSQL with SQLAlchemy)

- [x] 2.1 Install and configure PostgreSQL locally (Docker-based setup chosen)
- [x] 2.2 Define tables and relationships in SQLAlchemy (Users, Roles, Game Servers, Resource Logs)
- [x] 2.3 Plan and set up migrations (Alembic) to handle schema changes
- [ ] 2.4 Create seeds/fixtures for initial data (admin user, default roles, test game servers)

### 3. Backend API Design

- [ ] 3.1 Plan REST or GraphQL endpoints for:
  - User management (login, registration, fetch user data)
  - Role and permissions management
  - Game server actions (create, start, stop, delete, status checks)
  - Resource usage data (create/fetch system stats logs)
- [ ] 3.2 Define data validation and schemas (Pydantic, Marshmallow)
- [ ] 3.3 Decide on API authentication strategy (JWT, session-based, OAuth2)

### 4. User Authentication Mechanism

- [ ] 4.1 Implement secure user registration (password hashing, email uniqueness)
- [ ] 4.2 Implement login flow (token generation, session management)
- [ ] 4.3 Configure session/token storage (Redis, in-memory, JWT)
- [ ] 4.4 Ensure logout and refresh logic is accounted for

### 5. Role-Based Access Control (RBAC)

- [ ] 5.1 Create a roles table (Admin, Moderator, User, etc.)
- [ ] 5.2 Define permissions for each role (who can start/stop servers, view logs, etc.)
- [ ] 5.3 Implement middleware/decorators to enforce role permissions

### 6. Game Server Management Logic

- [ ] 6.1 Outline how to start a game server on Linux (launch commands, env vars)
- [ ] 6.2 Implement a background service to:
  - Create and configure a new server instance
  - Start and stop a server instance
  - Delete a server instance
  - Check server status periodically
- [ ] 6.3 Define error handling strategies (logs if server fails to start)

### 7. System Resource Monitoring

- [ ] 7.1 Determine how to collect CPU, RAM, and disk usage (psutil, shell commands)
- [ ] 7.2 Implement scheduled/on-demand tasks to store resource usage
- [ ] 7.3 Plan a strategy for real-time vs. historical data storage
- [ ] 7.4 Develop an API endpoint to retrieve resource usage data for graphs

### 8. Logging and Auditing

- [ ] 8.1 Set up a logging framework (log levels, rotation, format)
- [ ] 8.2 Establish audit trails for critical actions (server start/stop, role changes)
- [ ] 8.3 Configure integration with external tools (log aggregation, monitoring)

### 9. Frontend Integration with Backend

- [ ] 9.1 Define wireframes or UI components for the React interface
- [ ] 9.2 Create a service layer in React for API calls (Axios, Fetch)
- [ ] 9.3 Implement pages for:
  - Login/Registration
  - Dashboard (overview of servers, usage graphs)
  - User Management (admin panel to manage roles)
  - Server Management (list servers, start/stop controls)
  - Resource Usage Visualization (graphs/charts)

### 10. Graphs and Data Visualization

- [ ] 10.1 Choose a charting library (Chart.js, Recharts, etc.)
- [ ] 10.2 Implement CPU, RAM, disk usage graphs
- [ ] 10.3 Ensure real-time updates (WebSockets, polling)
- [ ] 10.4 Provide user controls for time ranges

### 11. Security and Hardening

- [ ] 11.1 Review authentication flows for vulnerabilities (CSRF, XSS, etc.)
- [ ] 11.2 Implement HTTPS/SSL certificates if externally exposed
- [ ] 11.3 Restrict internal endpoints (firewall, network rules)
- [ ] 11.4 Validate & sanitize all user inputs
- [ ] 11.5 Enforce password strength, implement password reset flow

### 12. Testing Strategy

- [ ] 12.1 Write unit tests for backend logic (authentication, server management)
- [ ] 12.2 Implement integration tests for API endpoints
- [ ] 12.3 Use a test database with seeded data for automated tests
- [ ] 12.4 Write frontend tests (React Testing Library, Cypress)

### 13. Deployment and Infrastructure

- [x] 13.1 Decide on hosting (on-prem, VM, Docker, etc.)
- [x] 13.2 Containerize backend with Docker
- [ ] 13.3 Containerize frontend with Docker/Nginx
- [ ] 13.4 Set up CI/CD pipeline
- [ ] 13.5 Configure production environment variables

### 14. Monitoring and Maintenance

- [ ] 14.1 Configure external monitoring (Prometheus, Grafana)
- [ ] 14.2 Set up alerts for high resource usage
- [ ] 14.3 Schedule PostgreSQL backups
- [ ] 14.4 Plan regular updates, patching, and maintenance
- [ ] 14.5 Monitor logs for suspicious activity

### 15. Documentation

- [ ] 15.1 Write or auto-generate API documentation (Swagger/OpenAPI)
- [ ] 15.2 Document environment variables and configuration options
- [ ] 15.3 Provide user/administrator guides
- [ ] 15.4 Include troubleshooting steps for common issues

## Progress So Far

✔ Step 1 (Project Setup) – ✅ Completed  
✔ Step 2.1 & 2.2 (Database & Models) – ✅ Completed  
✔ Step 2.3 (Alembic Migrations) – ✅ Completed  
✔ Step 13.2 (Backend Containerized) – ✅ Completed  
⏳ Next up: Step 2.4 (Database Seeding with Initial Data)
