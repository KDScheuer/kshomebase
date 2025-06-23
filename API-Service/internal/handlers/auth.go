package handlers

import (
	"api-service/internal/tools"
    "encoding/json"
    "net/http"
    "strings"
)

func LoginHandler(w http.ResponseWriter, r *http.Request) {
    if r.Method != http.MethodPost {
        http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
        return
    }

    auth := r.Header.Get("Authorization")
    if !strings.HasPrefix(auth, "Bearer ") {
        http.Error(w, "Missing token", http.StatusUnauthorized)
        return
    }

    idToken := strings.TrimPrefix(auth, "Bearer ")

    claims, err := tools.VerifyGoogleToken(idToken)
    if err != nil {
        http.Error(w, "Token invalid: "+err.Error(), http.StatusUnauthorized)
        return
    }

    // Check email
    allowed := map[string]bool{
        "kdscheuer97@gmail.com":  true,
        "scheuerkayla@gmail.com": true,
    }
    if !allowed[claims.Email] || !claims.EmailVerified {
        http.Error(w, "Access denied", http.StatusForbidden)
        return
    }

    json.NewEncoder(w).Encode(map[string]string{
        "message": "Welcome, " + claims.Email,
    })
}
