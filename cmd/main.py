import os

from api.routes import APIRouter
from http.server import HTTPServer
from db.init_db import init_db


DB_PATH = "data/homebase.db"
SCHEMA_PATH = "data/schema.sql"


def main():
    try:
        # Check DB Exists if not create one
        if os.path.exists(DB_PATH):
            print("Database file found")
        else:
            print(f"Database file not found, Creating file {DB_PATH}")
            init_db(DB_PATH, SCHEMA_PATH)

         # Start HTTP API server
        server_address = ('127.0.0.1', 8000)
        httpd = HTTPServer(server_address, APIRouter)
        print("API server running at http://127.0.0.1:8000")
        httpd.serve_forever()                    

    except KeyboardInterrupt as e:
        print("Keyboard interrupt detected. Exiting program.")
        exit(1)
    except ValueError as e:
        print(e)
        exit(1)
    except FileNotFoundError as e:
        print(e)
        exit(1)
    except SystemError as e:
        print(e)
        exit(1)
    

if __name__=="__main__":
    main()
    