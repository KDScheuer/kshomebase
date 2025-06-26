import os

from config.config import Config
from api.routes import APIRouter
from http.server import HTTPServer
from db.init_db import init_db


def main():
    try:
        # Check DB Exists if not create one
        if os.path.exists(Config.DB_PATH):
            print("Database file found")
        else:
            print(f"Database file not found, Creating file {Config.DB_PATH}")
            init_db(Config.DB_PATH, Config.SCHEMA_PATH)

         # Start HTTP API server
        server_address = (Config.LISTEN_ADDR, int(Config.LISTEN_PORT))
        httpd = HTTPServer(server_address, APIRouter)
        print(f"API server running at http://{Config.LISTEN_ADDR}:{Config.LISTEN_PORT}")
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
    