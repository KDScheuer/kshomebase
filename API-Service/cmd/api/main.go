package main

import (
    "log"
    "net/http"

    "api-service/internal/handlers"
    "api-service/internal/middleware"
)

func main() {
    mux := http.NewServeMux()

    // Auth route
    mux.HandleFunc("/auth/login", handlers.LoginHandler)

    // Protected routes
    mux.Handle("/tasks", middleware.AuthMiddleware(http.HandlerFunc(handlers.GetTasksHandler)))

    log.Println("API running on :8080")
    err := http.ListenAndServe("127.0.0.1:8080", mux)
    if err != nil {
        log.Fatalf("Server failed: %v", err)
    }
}
