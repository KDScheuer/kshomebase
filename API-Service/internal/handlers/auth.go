package handlers

import (
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

    // TODO: Validate Google token (you’ll add this later)
    if !isAllowedEmail("example@gmail.com") { // stub
        http.Error(w, "Access denied", http.StatusForbidden)
        return
    }

    json.NewEncoder(w).Encode(map[string]string{
        "message": "Token accepted",
    })
}

func isAllowedEmail(email string) bool {
    allowed := map[string]bool{
        "KDScheuer97@gmail.com":  true,
        "scheuerkayla@gmail.com": true,
    }
    return allowed[email]
}
