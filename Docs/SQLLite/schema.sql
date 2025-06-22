CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    token_hash TEXT,
    token_expires_at TEXT,
    token_issued_at TEXT,
    token_last_used_at TEXT
);
 
CREATE TABLE task_templates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    interval_frequency TEXT NOT NULL,         
    interval INTEGER NOT NULL,       
    days_of_week TEXT,               
    start_date TEXT NOT NULL,        
    end_date TEXT,                   
    last_generated_at TEXT           
);

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    template_id INTEGER,             
    title TEXT NOT NULL,
    description TEXT,
    display_on TEXT NOT NULL,        
    due_date TEXT,                   
    completed INTEGER DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (template_id) REFERENCES task_templates(id)
);

CREATE TABLE grocery_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    quantity INTEGER DEFAULT 1,
    purchased INTEGER DEFAULT 0,          
    added_on TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE calendar_events (
    id TEXT PRIMARY KEY,            
    title TEXT NOT NULL,
    start_time TEXT NOT NULL,       
    end_time TEXT NOT NULL,         
    location TEXT,
    description TEXT
);
