from config.config import Config
from db.db_helper import sql_helper

def getTasks():
    rows = sql_helper(method="fetchall", cmd="SELECT id, title, description, due_date FROM tasks WHERE completed = 0")
    
    if rows == None or rows == []:
        return "</p> All tasks Complete </p>"

    html = "<ul>"
    for row in rows:
        id, title, description, due_date = row
        
        html += f"""
            <li hx-get="http://{Config.LISTEN_ADDR}:{Config.LISTEN_PORT}/api/tasks/{id}" hx-target="#content" hx-swap="innerHTML">
                <h3>{title}</h3>
                <p>{description}</p>
                <i>Due: {due_date}</i>
                </li>"""
                
    html += """</ul><button hx-get="http://127.0.0.1:8000/api/tasks/create_task_menu" hx-target="#content" hx-swap="innerHTML" hx-trigger="click">Add Task</button>"""
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
        <button hx-get="http://{Config.LISTEN_ADDR}:{Config.LISTEN_PORT}/api/tasks" hx-target="#content" hx-swap="innerHTML">Close </button>
        <button hx-patch="http://{Config.LISTEN_ADDR}:{Config.LISTEN_PORT}/api/tasks/{task_id}/complete" hx-target="this" hx-swap="outerHTML" hx-trigger="click">Complete</button>
        </div>"""
    return html


def mark_task_complete(task_id):
    #TODO Have is set completion date as well
    status = sql_helper(method="update", cmd="UPDATE tasks SET completed = 1 WHERE id = ?", params=(task_id,))
    if status == None:
        print(f"Failed mark task {task_id} Complete")
        return "<p>Failed to mark complete</p>"
    
def create_task_menu():
    return f"""
        <form hx-post="http://{Config.LISTEN_ADDR}:{Config.LISTEN_PORT}/api/tasks/create_task" hx-target="#response" hx-swap="innerHTML">
            <label>Title:
                <input type="text" name="title" required>
            </label><br>

            <label>Description:
                <textarea name="description"></textarea>
            </label><br>

            <label>Due Date:
                <input type="date" name="due_date">
            </label><br>

            <button type="submit">Create Task</button>
        </form>
        <button hx-get="http://{Config.LISTEN_ADDR}:{Config.LISTEN_PORT}/api/tasks" hx-target="#content" hx-swap="innerHTML">Cancel</button>"""
    
#TODO Add a task

#TODO Add a reoccuring task (default should not display a task right away)
      #TODO Add ability to display task immedaitly after creation

#TODO Add utility to audit task templates table and auto populate a new task if one is due

#TODO Add ability to delete task

#TODO If reoccuring task add ability to delete task template (all reoccurances from happening)

#TODO Add ability to view all completed tasks (default should disply last 7 days)
      #TODO should have an option to view all completed tasks in the DB

#TODO Add utility to purge completed tasks after 90 days