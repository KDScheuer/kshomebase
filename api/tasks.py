import sqlite3

def getTasks():
    
    sql = """SELECT id, title, description, due_date FROM tasks"""
    conn = sqlite3.connect("data/homebase.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()

    html = "<ul>"
    for row in rows:
        id, title, description, due_date = row
        html += f"""
<li hx-get="http://127.0.0.1:8000/api/tasks/{id}" hx-target="#task-details" hx-swap="innerHTML">
  <h3>{title}</h3>
  <p>{description}</p>
  <i>Due: {due_date}</i>
</li>"""
    html += "</ul>"

    return html


def get_task_detail(task_id):
    conn = sqlite3.connect("data/homebase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, description, due_date, completed FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return "<p>Task not found</p>"

    title, description, due_date, completed = row
    html = f"""
<div class="task-detail fullscreen">
  <button onclick="
  const modal = document.getElementById('task-details');
  modal.classList.remove('show');
  modal.innerHTML = '';
">Close</button>
  <h2>{title}</h2>
  <p>{description}</p>
  <p><strong>Due:</strong> {due_date}</p>
  <p><strong>Completed:</strong> {'Yes' if completed else 'No'}</p>
</div>
"""
    return html