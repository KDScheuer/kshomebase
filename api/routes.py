import json
from http.server import BaseHTTPRequestHandler
from api.tasks import getTasks, get_task_detail

class APIRouter(BaseHTTPRequestHandler):
    def _send_html(self, html, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "text/html")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(html.encode())

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, HX-Request, HX-Trigger, HX-Target, HX-Current-URL')
        self.end_headers()


    def do_GET(self):
        if self.path == "/api/tasks":
            return self._send_html(getTasks())
        elif self.path.startswith("/api/tasks/"):
            try:
                task_id = int(self.path.split("/")[-1])
                return self._send_html(get_task_detail(task_id))
            except ValueError:
                return self._send_html("<p>Invalid task ID</p>", status=400)
            
