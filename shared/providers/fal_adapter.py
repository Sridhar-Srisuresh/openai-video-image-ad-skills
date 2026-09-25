import os

class FalAdapter:
    def __init__(self):
        self.api_key = os.getenv("FAL_KEY")

    def estimate(self, prompt, **kwargs):
        if not self.api_key:
            raise ValueError("FAL_KEY is missing")
        return {"provider": "fal", "prompt": prompt, "status": "ready_for_estimate"}

    def generate_image(self, prompt, **kwargs):
        return {"provider": "fal", "prompt": prompt, "status": "not_implemented"}

    def generate_video(self, prompt, **kwargs):
        return {"provider": "fal", "prompt": prompt, "status": "not_implemented"}

    def poll(self, job_id):
        return {"job_id": job_id, "status": "unknown"}

