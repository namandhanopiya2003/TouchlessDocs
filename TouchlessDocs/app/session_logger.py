import json
from datetime import datetime

def log_interaction(event_type, details):
    timestamp = datetime.now().isoformat()
    entry = {"time": timestamp, "event": event_type, "details": details}
    with open("data/logs/session_log.json", "a") as f:
        f.write(json.dumps(entry) + "\n")
