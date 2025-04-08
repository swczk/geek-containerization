# ⚡ Pokémon Battle Simulator

A web application built with Python and Flask that simulates battles between Pokémon. Select your favorite Pokémon, battle with others, and see the results based on type effectiveness, stats, and battle mechanics from the games.

## ✨ Features

- **Pokémon Selection**: Choose from a collection of Pokémon with accurate stats
- **Battle Simulation**: Simulate battles with game-accurate mechanics
- **Type Effectiveness**: Implementation of the Pokémon type chart
- **Battle Log**: Detailed turn-by-turn battle narration
- **Battle History**: View past battle results
- **Random Battles**: Quick battles with randomly selected Pokémon

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Database**: MongoDB
- **Containerization**: Docker & Docker Compose

## 🎮 Battle Mechanics

The battle simulator implements several core mechanics from the Pokémon games:

- **Type Effectiveness**: Damage multipliers based on type matchups
- **Physical/Special Split**: Attacks use either Attack/Defense or Special Attack/Special Defense
- **Critical Hits**: 6.25% chance of landing a critical hit for 1.5× damage
- **Random Damage Variation**: 85-100% of calculated damage
- **Speed-Based Turn Order**: Faster Pokémon attack first

## 🏁 Getting Started

### Prerequisites

- Docker and Docker Compose installed

### Running the Application

1. Navigate to the project directory:
   ```bash
   cd pokemon-battle
   ```

2. Start the containers:
   ```bash
   docker-compose up -d
   ```

3. The application will be available at `http://localhost:5000`

## 📋 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/pokemon` | GET | Get all Pokémon |
| `/api/pokemon/{name}` | GET | Get details for a specific Pokémon |
| `/api/battle/random` | GET | Start a random battle |
| `/api/battle` | POST | Start a custom battle between two Pokémon |
| `/api/battles/recent` | GET | Get recent battle results |
| `/api/battle/{id}` | GET | Get details of a specific battle |

See the `requests.http` file for example API requests that can be used with REST clients.

## 📝 License

This project is licensed under the MIT License.

## ⚠️ Disclaimer

This is a fan project for educational purposes. Pokémon and all related properties are owned by Nintendo, Game Freak, and The Pokémon Company. This project is not affiliated with or endorsed by these companies.
