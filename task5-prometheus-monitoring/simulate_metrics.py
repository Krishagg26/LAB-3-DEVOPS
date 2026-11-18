import json
import datetime

metrics_payload = {
    "@timestamp": datetime.datetime.utcnow().isoformat(),
    "system": "Lab-3-Monitoring-System",
    "prometheus_target": "localhost:9090",
    "grafana_target": "localhost:3000",
    "status": "METRICS_SCRAPING_ACTIVE",
    "active_targets": 2,
    "metric_sample": "http_requests_total{method=\"GET\",handler=\"/health\"} 1425"
}

print("Generated Prometheus Metrics Simulation Payload:")
print(json.dumps(metrics_payload, indent=2))
with open("prometheus_metrics_output.json", "w") as f:
    json.dump(metrics_payload, f, indent=2)
