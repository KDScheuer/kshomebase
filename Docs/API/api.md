# API Design Overview

## Auth
| Method | Path        | Description           |
|--------|-------------|-----------------------|
| POST   | /auth/login | Exchange Google Token |

## Tasks
| Method | Path        | Description     |
|--------|-------------|-----------------|
| GET    | /tasks      | List all tasks  |
| POST   | /tasks      | Create new task |
| GET    | /tasks/{id} | Get task by ID  |
| PUT    | /tasks/{id} | Update task     |
| DELETE | /tasks/{id} | Delete task     |

## Grocery
| Method | Path          | Description       |
|--------|---------------|-------------------|
| GET    | /grocery      | List all items    |
| POST   | /grocery      | Add an item       |
| DELETE | /grocery      | Remove all items  |
| PATCH  | /grocery/{id} | Mark as purchased |
| DELETE | /grocery/{id} | Remove an Item    |

## Calendar
| Method | Path      | Description             |
|--------|-----------|-------------------------|
| GET    | /calendar | Get all calendar events |