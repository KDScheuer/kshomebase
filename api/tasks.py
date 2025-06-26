import sqlite3
from db.db_helper import sql_helper

def getTasks():
    rows = sql_helper(method="fetchall", cmd="SELECT id, title, description, due_date FROM tasks WHERE completed = 0")
    
    if rows == None:
        return "</p> All tasks Complete </p>"

    html = "<ul>"
    for row in rows:
        id, title, description, due_date = row
        
        html += f"""
            <li hx-get="http://127.0.0.1:8000/api/tasks/{id}" hx-target="#content" hx-swap="innerHTML">
                <h3>{title}</h3>
                <p>{description}</p>
                <i>Due: {due_date}</i>
                </li>"""
    html += "</ul>"
    return html


def get_task_detail(task_id):
    row = sql_helper(method="fetchone", cmd="SELECT title, description, due_date, completed FROM tasks WHERE id = ?", params= (task_id,))
    if not row:
        print(task_id)
        return "<p>Task not found</p>"

    title, description, due_date, completed = row
    html = f"""
        <div class="fullscreen-task">
            <div class="task-detail">
                <h2>{title}</h2>
                <p>{description}</p>
                <p><strong>Due:</strong> {due_date}</p>
                <p><strong>Completed:</strong> {'Yes' if completed else 'No'}</p>
            </div>
        <button hx-get="http://127.0.0.1:8000/api/tasks" hx-target="#content" hx-swap="innerHTML">Close </button>
        <button hx-patch="http://127.0.0.1:8000/api/tasks/{task_id}/complete" hx-target="this" hx-swap="outerHTML" hx-trigger="click">Complete</button>
        </div>"""
    return html

def mark_task_complete(task_id):
    #TODO Have is set completion date as well
    status = sql_helper(method="update", cmd="UPDATE tasks SET completed = 1 WHERE id = ?", params=(task_id,))
    if status == None:
        print(f"Failed mark task {task_id} Complete")
        return "<p>Failed to mark complete</p>"