import os

class ReplicateAdapter:
    def __init__(self):
        self.api_token = os.getenv("REPLICATE_API_TOKEN")

    def estimate(self, prompt, **kwargs):
        if not self.api_token:
            raise ValueError("REPLICATE_API_TOKEN is missing")
        return {"provider": "replicate", "prompt": prompt, "status": "ready_for_estimate"}

    def generate_image(self, prompt, **kwargs):
        return {"provider": "replicate", "prompt": prompt, "status": "not_implemented"}

    def generate_video(self, prompt, **kwargs):
        return {"provider": "replicate", "prompt": prompt, "status": "not_implemented"}

    def poll(self, job_id):
        return {"job_id": job_id, "status": "unknown"}

