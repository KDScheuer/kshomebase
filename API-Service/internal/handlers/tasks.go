package handlers

import (
    "encoding/json"
    "net/http"
)

type Task struct {
    ID          int    `json:"id"`
    Title       string `json:"title"`
    Description string `json:"description"`
    Completed   bool   `json:"completed"`
}

func GetTasksHandler(w http.ResponseWriter, r *http.Request) {
    if r.Method != http.MethodGet {
        http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
        return
    }

    // TODO: fetch from DB
    tasks := []Task{
        {ID: 1, Title: "Take out trash", Description: "Before 9am", Completed: false},
        {ID: 2, Title: "Do dishes", Description: "", Completed: true},
    }

    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(tasks)
}
