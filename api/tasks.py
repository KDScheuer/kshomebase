import urllib.parse
from datetime import datetime



from config.config import Config
from db.db_helper import sql_helper

def getTasks():
    rows = sql_helper(method="fetchall", cmd="SELECT id, title, due_date FROM tasks WHERE completed = 0")
    
    if rows == None or rows == []:
        return """
            </p> All tasks Complete </p>
            <button hx-get="http://127.0.0.1:8000/api/tasks/create_task_menu" hx-target="#content" hx-swap="innerHTML" hx-trigger="click">Add Task</button>"""

    html = "<ul>"
    for row in rows:
        id, title, due_date = row
        
        html += f"""
            <li hx-get="http://{Config.LISTEN_ADDR}:{Config.LISTEN_PORT}/api/tasks/{id}" hx-target="#content" hx-swap="innerHTML">
                <h3>{title}</h3>
                <i>Due: {due_date}</i>
                </li>"""
                
    html += """</ul><button hx-get="http://127.0.0.1:8000/api/tasks/create_task_menu" hx-target="#content" hx-swap="innerHTML" hx-trigger="click">Add Task</button>"""
    return html


def get_task_detail(task_id):
    row = sql_helper(method="fetchone", cmd="SELECT title, description, created_at, due_date, completed, completed_on FROM tasks WHERE id = ?", params= (task_id,))
    if not row:
        print(task_id)
        return "<p>Task not found</p>"

    title, description, created_on, due_date, completed, completed_on = row
    html = f"""
        <div class="fullscreen-task">
            <div class="task-detail">
                <h2>{title}</h2>
                <p>{description}</p>
                <p><strong>Created:</strong> {created_on}</p>
                <p><strong>Due:</strong> {due_date}</p>
                <p><strong>Completed:</strong> {'Yes' if completed else 'No'}</p>
                <p><strong>Completed On:</strong> {completed_on}</p>
                <i>Task ID: {task_id}</i>
            </div>
        <button hx-get="http://{Config.LISTEN_ADDR}:{Config.LISTEN_PORT}/api/tasks" hx-target="#content" hx-swap="innerHTML">Close </button>
        <button hx-patch="http://{Config.LISTEN_ADDR}:{Config.LISTEN_PORT}/api/tasks/{task_id}/complete" hx-target="this" hx-swap="outerHTML" hx-trigger="click">Complete</button>
        </div>"""
    return html


def mark_task_complete(task_id):
    #TODO Have is set completion date as well
    completed_on = datetime.now().date().isoformat()
    status = sql_helper(method="update", cmd="UPDATE tasks SET completed = 1, completed_on = ? WHERE id = ?", params=(completed_on, task_id))
    if status == None:
        print(f"Failed mark task {task_id} Complete")
        return "<p>Failed to mark complete</p>"
    
def create_task_menu():
    return f"""
        <form hx-post="http://{Config.LISTEN_ADDR}:{Config.LISTEN_PORT}/api/tasks/create_task" hx-target="#content" hx-swap="innerHTML">
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

def create_task(request):
     #TODO Something causes a page reload when sql is executed if it is not then status of success or failure is displayed but if sql executes then the message flashes

     # read the raw body
    content_length = int(request.headers.get('Content-Length', 0))
    body = request.rfile.read(content_length).decode()

    # parse form data
    form_data = urllib.parse.parse_qs(body)

    # extract form values
    title = form_data.get("title", ["NONE"])[0]
    description = form_data.get("description", ["NONE"])[0]
    due_date = form_data.get("due_date", ["None"])[0]
        
    created_at = datetime.now().date().isoformat()

    print(f"Received task: {title=}, {description=}, {due_date=}")

    sql = "INSERT INTO tasks (title, description, due_date, created_at) VALUES (?, ?, ?, ?)"
    params = (title, description, due_date, created_at)
    status = sql_helper(method="insert", cmd=sql, params=params)

    if status is None: 
        html ="<h2>Error creating task</h2>"
    else:
        html = "<h2>Task added successfully</h2>"
    
    return html

#TODO Add a task

#TODO Add a reoccuring task (default should not display a task right away)
      #TODO Add ability to display task immedaitly after creation

#TODO Add utility to audit task templates table and auto populate a new task if one is due

#TODO Add ability to delete task

#TODO If reoccuring task add ability to delete task template (all reoccurances from happening)

#TODO Add ability to view all completed tasks (default should disply last 7 days)
      #TODO should have an option to view all completed tasks in the DB

#TODO Add utility to purge completed tasks after 90 days