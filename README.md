# 🐳 Geek Containerization Projects

This repository contains a collection of containerized applications with geeky/nerdy themes, implemented in various programming languages. Each project demonstrates how to use Docker and Docker Compose to containerize and deploy applications.

## 🚀 Projects Overview

| Project | Language | Description |
|---------|----------|-------------|
| [Star Wars API](./1.golang-starwars-api/) | Go | REST API for Star Wars characters with PostgreSQL database |
| [Comics Catalog](./2.csharp-comics-catalog/) | C# | ASP.NET Core web application for managing comic book collections |
| [LOTR Quiz](./3.ruby-lotr-quiz/) | Ruby | Lord of the Rings quiz application with Redis for score tracking |
| [Stardate Converter](./4.rust-stardate-converter/) | Rust | Star Trek stardate conversion microservice |
| [Pokémon Battle Simulator](./5.python-pokemon-battle/) | Python | Pokémon battle simulation with Flask and MongoDB |

## 🔍 Key Features

- **Multi-language exploration**: Each project is built in a different programming language
- **Docker containerization**: All projects are containerized for consistent deployment
- **Docker Compose orchestration**: Multiple container services working together
- **Database integration**: Various databases (PostgreSQL, MongoDB, SQL Server, Redis)
- **Development best practices**: Each project demonstrates code organization and Docker best practices
- **Geeky themes**: Fun projects related to popular sci-fi and fantasy themes

## 🛠️ Prerequisites

To run any of these projects, you'll need:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

No need to install language-specific dependencies as everything runs in containers!

## 🏁 Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/swczk/geek-containerization.git
   cd geek-containerization
   ```

2. Navigate to any project folder:
   ```bash
   cd 1.golang-starwars-api
   ```

3. Start the application using Docker Compose:
   ```bash
   docker compose up -d
   ```

4. Check the project-specific README for details on how to use each application.

## 🎓 Learning Path

These projects demonstrate a progression in containerization skills:
1. **Basic containerization**: Single container applications
2. **Multi-container applications**: Using Docker Compose for orchestration
3. **Data persistence**: Managing volumes and database states
4. **Environment configuration**: Using environment variables and config files
5. **Networking**: Container communication in a networked environment

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ✨ Acknowledgements

These projects are for educational purposes to demonstrate how to containerize applications in various programming languages. The themes are inspired by popular sci-fi and fantasy franchises but are not affiliated with their respective owners.
