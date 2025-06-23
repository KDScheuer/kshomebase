package middleware

import (
    "net/http"
    "strings"
)

func AuthMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        auth := r.Header.Get("Authorization")
        if !strings.HasPrefix(auth, "Bearer ") {
            http.Error(w, "Unauthorized", http.StatusUnauthorized)
            return
        }

        // token := strings.TrimPrefix(auth, "Bearer ")
        token := strings.TrimPrefix(auth, "Bearer ")
        if token != "example-token" { // You’ll replace this later with real logic
            http.Error(w, "Invalid token", http.StatusUnauthorized)
            return
        }

        next.ServeHTTP(w, r)
    })
}
