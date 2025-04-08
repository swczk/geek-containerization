# 📚 Comic Book Catalog

A web application built with ASP.NET Core for managing comic book collections. The application allows users to add, view, edit, and delete comic books in their collection.

## ✨ Features

- **Comic Book Management**: CRUD operations for your comic collection
- **Responsive UI**: Bootstrap-based interface that works on mobile and desktop
- **Data Persistence**: SQL Server database for storing comic information
- **Entity Framework Core**: ORM for database operations
- **MVC Architecture**: Clean separation of concerns
- **Docker Deployment**: Fully containerized application

## 🛠️ Technology Stack

- **Backend**: C# / ASP.NET Core 6.0
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: Microsoft SQL Server
- **ORM**: Entity Framework Core
- **Containerization**: Docker & Docker Compose

## 🏁 Getting Started

### Prerequisites

- Docker and Docker Compose installed

### Running the Application

1. Navigate to the project directory:
   ```bash
   cd csharp-comics
   ```

2. Start the containers:
   ```bash
   docker-compose up -d
   ```

3. The application will be available at `http://localhost:8000`

### Default Data

The application comes pre-populated with some comic books including:
- Batman: The Dark Knight Returns
- Watchmen
- Saga
- Spider-Man: Maximum Carnage

## 🐳 Docker Configuration

The project uses two Docker containers:

1. **Web Application Container**
   - Built from the .NET SDK
   - Publishes and runs the ASP.NET Core application
   - Exposes port 8000

2. **SQL Server Container**
   - Uses Microsoft SQL Server 2019
   - Persists data in a Docker volume
   - Secured with an environment-defined password

## 📝 License

This project is licensed under the MIT License.
