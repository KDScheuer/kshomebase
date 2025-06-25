import os
import sqlite3

def init_db(dbPath: str = None, schemaPath: str = None) -> None:
    if dbPath == None or schemaPath == None:
        raise ValueError("Database path or Schema path were not declared")

    if not os.path.exists(schemaPath):
        raise FileNotFoundError(f"Schema file not found: {schemaPath}") 

    print(f"Initilizing DB at {dbPath} with schema: {schemaPath}")

    with open(schemaPath, 'r') as f:
        schema = f.read()
    
    conn = sqlite3.connect(dbPath)
    try:
        conn.executescript(schema)
        print("DB Successfully initialized")
    except:
        raise SystemError("Unable to initilize sqlite database")
    finally:
        conn.close()