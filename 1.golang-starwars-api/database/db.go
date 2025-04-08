package database

import (
	"database/sql"
	"fmt"
	"log"
	"os"

	"starwars-api/models"

	_ "github.com/lib/pq"
)

var db *sql.DB

// Connect establishes a connection with PostgreSQL
func Connect() error {
	var err error

	host := os.Getenv("DB_HOST")
	port := os.Getenv("DB_PORT")
	user := os.Getenv("DB_USER")
	password := os.Getenv("DB_PASSWORD")
	dbname := os.Getenv("DB_NAME")

	connStr := fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=disable",
		host, port, user, password, dbname)

	db, err = sql.Open("postgres", connStr)
	if err != nil {
		return err
	}

	err = db.Ping()
	if err != nil {
		return err
	}

	log.Println("Successfully connected to PostgreSQL")
	return nil
}

// Close closes the database connection
func Close() {
	if db != nil {
		db.Close()
	}
}

// GetCharacters returns all characters
func GetCharacters() ([]models.Character, error) {
	query := "SELECT id, name, species, homeworld, birth_year, force_user FROM characters"
	rows, err := db.Query(query)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var characters []models.Character
	for rows.Next() {
		var c models.Character
		if err := rows.Scan(&c.ID, &c.Name, &c.Species, &c.Homeworld, &c.BirthYear, &c.ForceUser); err != nil {
			return nil, err
		}
		characters = append(characters, c)
	}

	return characters, nil
}

// GetCharacter returns a character by ID
func GetCharacter(id int) (models.Character, error) {
	var c models.Character
	query := "SELECT id, name, species, homeworld, birth_year, force_user FROM characters WHERE id = $1"
	err := db.QueryRow(query, id).Scan(&c.ID, &c.Name, &c.Species, &c.Homeworld, &c.BirthYear, &c.ForceUser)
	return c, err
}

// CreateCharacter adds a new character
func CreateCharacter(c models.Character) (models.Character, error) {
	query := `
		INSERT INTO characters (name, species, homeworld, birth_year, force_user)
		VALUES ($1, $2, $3, $4, $5)
		RETURNING id
	`
	err := db.QueryRow(query, c.Name, c.Species, c.Homeworld, c.BirthYear, c.ForceUser).Scan(&c.ID)
	return c, err
}

// UpdateCharacter updates an existing character
func UpdateCharacter(c models.Character) error {
	query := `
		UPDATE characters
		SET name = $1, species = $2, homeworld = $3, birth_year = $4, force_user = $5
		WHERE id = $6
	`
	_, err := db.Exec(query, c.Name, c.Species, c.Homeworld, c.BirthYear, c.ForceUser, c.ID)
	return err
}

// DeleteCharacter removes a character
func DeleteCharacter(id int) error {
	query := "DELETE FROM characters WHERE id = $1"
	_, err := db.Exec(query, id)
	return err
}
