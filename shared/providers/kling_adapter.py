import os

class KlingAdapter:
    def __init__(self):
        self.api_key = os.getenv("KLING_API_KEY")

    def estimate(self, prompt, **kwargs):
        if not self.api_key:
            raise ValueError("KLING_API_KEY is missing")
        return {"provider": "kling", "prompt": prompt, "status": "ready_for_estimate"}

    def generate_image(self, prompt, **kwargs):
        return {"provider": "kling", "prompt": prompt, "status": "not_implemented"}

    def generate_video(self, prompt, **kwargs):
        return {"provider": "kling", "prompt": prompt, "status": "not_implemented"}

    def poll(self, job_id):
        return {"job_id": job_id, "status": "unknown"}

