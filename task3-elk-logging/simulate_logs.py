import json
import datetime

log_entry = {
    "@timestamp": datetime.datetime.utcnow().isoformat(),
    "level": "INFO",
    "service": "auth-service",
    "message": "User authentication successful for user_id=krish_agg",
    "status_code": 200
}

print("Generated Centralized Log Payload:")
print(json.dumps(log_entry, indent=2))
with open("centralized_log_output.json", "w") as f:
    json.dump(log_entry, f, indent=2)
