import json
import os
from datetime import datetime


class GenerationLogger:
    """Log generation calls to jsonl format."""

    def __init__(self, log_path="logs/generation-calls.jsonl"):
        self.log_path = log_path
        os.makedirs(os.path.dirname(log_path) or ".", exist_ok=True)

    def log_call(
        self,
        provider,
        endpoint,
        model,
        job_id,
        request_data,
        response_data,
    ):
        """Log a single API call."""
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "provider": provider,
            "endpoint": endpoint,
            "model": model,
            "jobId": job_id,
            "request": request_data,
            "response": response_data,
        }
        with open(self.log_path, "a") as f:
            f.write(json.dumps(entry) + "\n")

    def update_call(self, job_id, status, timing_sec=None, final_cost=None):
        """Update a call with final status."""
        lines = []
        found = False
        with open(self.log_path, "r") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            entry = json.loads(line)
            if entry.get("jobId") == job_id:
                entry["response"]["status"] = status
                if timing_sec is not None:
                    entry["response"]["generationTimeSec"] = timing_sec
                if final_cost is not None:
                    entry["response"]["cost"] = final_cost
                lines[i] = json.dumps(entry) + "\n"
                found = True
                break

        if found:
            with open(self.log_path, "w") as f:
                f.writelines(lines)
