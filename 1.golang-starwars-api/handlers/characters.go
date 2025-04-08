package handlers

import (
	"encoding/json"
	"net/http"
	"strconv"

	"starwars-api/database"
	"starwars-api/models"

	"github.com/gorilla/mux"
)

// GetCharacters returns all characters
func GetCharacters(w http.ResponseWriter, r *http.Request) {
	characters, err := database.GetCharacters()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(characters)
}

// GetCharacter returns a character by ID
func GetCharacter(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id, err := strconv.Atoi(vars["id"])
	if err != nil {
		http.Error(w, "Invalid ID", http.StatusBadRequest)
		return
	}

	character, err := database.GetCharacter(id)
	if err != nil {
		http.Error(w, "Character not found", http.StatusNotFound)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(character)
}

// CreateCharacter adds a new character
func CreateCharacter(w http.ResponseWriter, r *http.Request) {
	var character models.Character
	err := json.NewDecoder(r.Body).Decode(&character)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	character, err = database.CreateCharacter(character)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(character)
}

// UpdateCharacter updates a character
func UpdateCharacter(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id, err := strconv.Atoi(vars["id"])
	if err != nil {
		http.Error(w, "Invalid ID", http.StatusBadRequest)
		return
	}

	var character models.Character
	err = json.NewDecoder(r.Body).Decode(&character)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	character.ID = id
	err = database.UpdateCharacter(character)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusOK)
}

// DeleteCharacter removes a character
func DeleteCharacter(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id, err := strconv.Atoi(vars["id"])
	if err != nil {
		http.Error(w, "Invalid ID", http.StatusBadRequest)
		return
	}

	err = database.DeleteCharacter(id)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusNoContent)
}
