# 🚀 Star Trek Stardate Converter

A microservice built with Rust that converts Earth calendar dates to Star Trek stardates across different series formats (TOS, TNG, Discovery, and Kelvin timeline).

## ✨ Features

- **Multiple Stardate Systems**: Support for different Star Trek series date formats
- **Current Date Conversion**: Get the current stardate in all supported formats
- **Custom Date Conversion**: Convert any Earth date to stardates
- **REST API**: Simple HTTP endpoints for integration with other applications
- **Rocket Framework**: Fast, secure Rust web server

## 🛠️ Technology Stack

- **Language**: Rust 1.68+
- **Web Framework**: Rocket 0.5.0-rc.2
- **JSON Processing**: Serde
- **Date Handling**: Chrono
- **Error Handling**: Thiserror
- **Containerization**: Docker & Docker Compose

## 📋 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Welcome message and API information |
| `/api/systems` | GET | List all available stardate systems |
| `/api/current` | GET | Convert current Earth date to all stardate formats |
| `/api/stardate` | POST | Convert a specific Earth date to stardates |

## 🏁 Getting Started

### Prerequisites

- Docker and Docker Compose installed

### Running the Microservice

1. Navigate to the project directory:
   ```bash
   cd rust-startrek
   ```

2. Start the container:
   ```bash
   docker-compose up -d
   ```

3. The API will be available at `http://localhost:8000`

See the `requests.http` file for example API requests that can be used with REST clients.

## 🚀 Stardate Systems

The application implements four different stardate calculation systems:

1. **TOS (The Original Series)**
   - Format: XXXX.X (e.g., 3817.5)
   - Somewhat random but based on the 1966-1969 era

2. **TNG (The Next Generation)**
   - Format: [4-digit year]XXX.X (e.g., 41072.5)
   - More structured system based on the 24th century

3. **Kelvin Timeline (2009 movies)**
   - Format: YYYYMM.DD (e.g., 2259.42)
   - Based on the actual Earth date in the new film series

4. **Discovery**
   - Format: Year plus decimal (e.g., 1308.9)
   - Based on the 23rd and 32nd centuries in the series

## 📝 License

This project is licensed under the MIT License.

## ⚠️ Disclaimer

This is a fan project implementing fictional date conversions from the Star Trek universe. It is not affiliated with CBS Studios, Paramount Pictures, or any Star Trek production.
