import json
from datetime import datetime

# Function to log user interactions
def log_interaction(event_type, details):
    # Gets current timestamp in ISO format
    timestamp = datetime.now().isoformat()
    # Prepares a log entry in the form of a dictionary
    entry = {"time": timestamp, "event": event_type, "details": details}
    # Appends the log entry to the session log file
    with open("data/logs/session_log.json", "a") as f:
        f.write(json.dumps(entry) + "\n")
