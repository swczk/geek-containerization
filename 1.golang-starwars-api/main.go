package main

import (
	"log"
	"net/http"
	"os"
	"time"

	"starwars-api/database"
	"starwars-api/handlers"

	"github.com/gorilla/mux"
)

func main() {
	// Wait for PostgreSQL to start
	time.Sleep(5 * time.Second)

	// Connect to database
	err := database.Connect()
	if err != nil {
		log.Fatalf("Error connecting to database: %v", err)
	}
	defer database.Close()

	// Configure routes
	r := mux.NewRouter()
	r.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Star Wars API - Use /api/characters to list characters"))
	})
	r.HandleFunc("/api/characters", handlers.GetCharacters).Methods("GET")
	r.HandleFunc("/api/characters/{id}", handlers.GetCharacter).Methods("GET")
	r.HandleFunc("/api/characters", handlers.CreateCharacter).Methods("POST")
	r.HandleFunc("/api/characters/{id}", handlers.UpdateCharacter).Methods("PUT")
	r.HandleFunc("/api/characters/{id}", handlers.DeleteCharacter).Methods("DELETE")

	// Start server
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	log.Printf("Server running on port %s", port)
	log.Fatal(http.ListenAndServe(":"+port, r))
}
