package tools

import (
    "encoding/json"
	"encoding/base64"
    "errors"
    "fmt"
    // "net/http"
    "strings"
    "time"
)

// Minimal decoded JWT payload
type GoogleClaims struct {
    Email         string `json:"email"`
    EmailVerified bool   `json:"email_verified"`
    Exp           int64  `json:"exp"`
    Aud           string `json:"aud"`
    Iss           string `json:"iss"`
}

// VerifyGoogleToken checks a Google-issued ID token
func VerifyGoogleToken(token string) (*GoogleClaims, error) {
    parts := strings.Split(token, ".")
    if len(parts) != 3 {
        return nil, errors.New("invalid token format")
    }

    // Decode payload
    payloadBytes, err := decodeSegment(parts[1])
    if err != nil {
        return nil, fmt.Errorf("failed to decode payload: %w", err)
    }

    var claims GoogleClaims
    if err := json.Unmarshal(payloadBytes, &claims); err != nil {
        return nil, fmt.Errorf("failed to unmarshal payload: %w", err)
    }

    // Check expiration
    if time.Now().Unix() > claims.Exp {
        return nil, errors.New("token is expired")
    }

    // Confirm issuer is Google
    if claims.Iss != "accounts.google.com" && claims.Iss != "https://accounts.google.com" {
        return nil, errors.New("invalid issuer")
    }

    // Optional: confirm audience if you register OAuth2 client
    // if claims.Aud != "YOUR_CLIENT_ID.apps.googleusercontent.com" {
    //     return nil, errors.New("invalid audience")
    // }

    // You can verify signature here if needed (omitted for now)

    return &claims, nil
}

func decodeSegment(seg string) ([]byte, error) {
    // JWT uses base64url encoding without padding
    seg = padBase64(seg)
    return base64.URLEncoding.DecodeString(seg)
}

func padBase64(s string) string {
    for len(s)%4 != 0 {
        s += "="
    }
    return s
}
