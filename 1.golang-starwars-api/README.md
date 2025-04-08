# 🌌 Star Wars Characters API

A RESTful API built with Go that provides information about Star Wars characters. The application uses PostgreSQL as its database.

## ✨ Features

- **Character CRUD Operations**: Create, Read, Update, and Delete Star Wars characters
- **PostgreSQL Database**: Persistent storage with PostgreSQL
- **RESTful Endpoints**: Well-structured API following REST principles
- **Docker Deployment**: Containerized for easy deployment
- **Initialization Data**: Pre-populated with famous Star Wars characters

## 🛠️ Technology Stack

- **Backend**: Go (Golang)
- **Database**: PostgreSQL
- **Containerization**: Docker & Docker Compose
- **Packages**: Gorilla Mux, lib/pq

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/characters` | Get all characters |
| GET | `/api/characters/{id}` | Get character by ID |
| POST | `/api/characters` | Create a new character |
| PUT | `/api/characters/{id}` | Update a character |
| DELETE | `/api/characters/{id}` | Delete a character |

## 🏁 Getting Started

### Prerequisites

- Docker and Docker Compose installed

### Running the Application

1. Navigate to the project directory:
   ```bash
   cd golang-starwars
   ```

2. Start the containers:
   ```bash
   docker-compose up -d
   ```

3. The API will be available at `http://localhost:8080`

### Example API Requests

See the `requests.http` file for example API requests that can be used with REST clients like VS Code's REST Client extension or Postman.

## 📝 License

This project is licensed under the MIT License.
