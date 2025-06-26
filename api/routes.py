import json
from http.server import BaseHTTPRequestHandler
from api.tasks import getTasks, get_task_detail, mark_task_complete

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
        self.send_header('Access-Control-Allow-Methods', 'GET, PATCH, POST, OPTIONS')
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

    def do_PATCH(self):
        if self.path.startswith("/api/tasks/"):
            parts = self.path.strip("/").split("/")
            # Expecting parts like ['api', 'tasks', '123', 'complete']
            print(parts)
            if len(parts) == 4:
                _, _, task_id_str, action = parts
                try:
                    task_id = int(task_id_str)
                except ValueError:
                    return self._send_html("<p>Invalid task ID</p>", status=400)

                if action.lower() == "complete":
                    return self._send_html(mark_task_complete(task_id))

        # If no match
        self._send_html("<p>Unsupported PATCH request</p>", status=404)