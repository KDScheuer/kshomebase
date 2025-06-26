import sqlite3
from config.config import Config


conn = sqlite3.connect(Config.DB_PATH)
cursor = conn.cursor()
cursor.execute("UPDATE tasks SET completed = 0 WHERE completed = 1")
conn.commit()
conn.close()