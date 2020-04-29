### Kubecaf
A simple budget app.

Consists of the following services:
- MySQL Database
- Flask Backend
- Flask Authenticator
- React Frontend

# Functionality

1. Frontend -> auth info -> Authenticator
2. Frontend <- token <- Authenticator
3. Frontend -> (query, token) -> Backend
4. Frontend <- query results <- Backend
