import sqlite3

DB_PATH = "data/homebase.db"

def sql_helper(method: str, cmd: str, params: tuple = ()):
    method = method.lower()
    results = None

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(cmd, params)

        if method == "fetchall":
            results = cursor.fetchall()
            print(results)
        elif method == "fetchone":
            results = cursor.fetchone()
        elif method in ("insert", "update"):
            conn.commit()
            if method == "insert":
                results = cursor.lastrowid
            elif method == "update":
                results = cursor.rowcount

        conn.close()
        return results

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return None
