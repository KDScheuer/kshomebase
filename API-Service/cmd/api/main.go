package main

import (
	"fmt"
	"net/http"
	
	"github.com/go-chi/chi"
	"github.com/KDScheuer/kshomebase/API-Service/handlers"
	log "github.com/sirupsen/logrus"
)

func main() {

	log.SetReportCaller(true)
	var r *chi.Mux = chi.NewRouter()
	handlers.Handler(r)

	fmt.Println("Starting GO API Service...")

	fmt.Println('
   _____    ____                 _____    _____ 
  / ____|  / __ \        /\     |  __ \  |_   _|
 | |  __  | |  | |      /  \    | |__) |   | |  
 | | |_ | | |  | |     / /\ \   |  ___/    | |  
 | |__| | | |__| |    / ____ \  | |       _| |_ 
  \_____|  \____/    /_/    \_\ |_|      |_____|
	')

	err := http.ListenAndServe("localhost:8000", r)
	if err != nil {
		log.Error(err)
	}
}