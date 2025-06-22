# Overview

| Table                  | Purpose                                                      |
|------------------------|--------------------------------------------------------------|
| users	                 | Store user info and auth tokens                              |
| tasks	                 | Store tasks, including recurring schedule info               |
| grocery_items	         | Store grocery list items                                     |
| task_recurrence        |	Define recurrence rules for tasks                           |
|calendar_events	Optional | store upcoming events (if not using Google Calendar)     |

# Table Schemas
## users
| Column        | Type       | Notes                                  |
|---------------|------------|----------------------------------------|
| id            | INTEGER PK | User ID                                |
| username      | TEXT       | Unique                                 |
| password_hash | TEXT       | Hashed password (if you do local auth) |
| token         | TEXT       | Optional auth token                    |

## tasks
| Column        | Type       | Notes                              |
|---------------|------------|------------------------------------|
| id            | INTEGER PK | Task ID                            |
| title         | TEXT       | Task description/title             |
| description   | TEXT       | Optional details                   |
| due_date      | DATE       | Next due date                      |
| completed     | BOOLEAN    | Is task done?                      |
| recurrence_id | INTEGER FK | Link to recurrence rule (nullable) |
| created_at    | DATETIME   | When created                       |
| updated_at    | DATETIME   | Last update                        |

## task_recurrence
| Column       | Type       | Notes                                     |
|--------------|------------|-------------------------------------------|
| id           | INTEGER PK | Recurrence rule ID                        |
| frequency    | TEXT       | e.g. daily, weekly, monthly               |
| interval     | INTEGER    | Every n days/weeks/months                 |
| days_of_week | TEXT       | e.g. "Mon,Wed,Fri" (if weekly recurrence) |
| end_date     | DATE       | When recurrence stops (nullable)          |

## grocery_items
| Column     | Type       | Notes                   |
|------------|------------|-------------------------|
| id         | INTEGER PK | Item ID                 |
| name       | TEXT       | Grocery item name       |
| quantity   | TEXT       | Optional quantity/notes |
| purchased  | BOOLEAN    | Has it been bought?     |
| created_at | DATETIME   | Timestamp               |
| updated_at | DATETIME   | Timestamp               |

## calendar_events (Optional)
| Column      | Type       | Notes            |
|-------------|------------|------------------|
| id          | INTEGER PK | Event ID         |
| title       | TEXT       | Event title      |
| start_time  | DATETIME   | Event start time |
| end_time    | DATETIME   | Event end time   |
| location    | TEXT       | Optional         |
| description | TEXT       | Optional         |