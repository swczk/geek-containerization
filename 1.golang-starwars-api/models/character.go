package models

// Character represents a Star Wars character
type Character struct {
	ID        int    `json:"id"`
	Name      string `json:"name"`
	Species   string `json:"species"`
	Homeworld string `json:"homeworld"`
	BirthYear string `json:"birth_year"`
	ForceUser bool   `json:"force_user"`
}
