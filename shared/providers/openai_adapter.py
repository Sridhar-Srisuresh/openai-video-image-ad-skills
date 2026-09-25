import os
import json
import requests

class OpenAIAdapter:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.base_url = "https://api.openai.com/v1"

    def estimate(self, prompt, model="gpt-4o-mini", **kwargs):
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is missing")

        payload = {
            "model": model,
            "input": prompt,
            "max_output_tokens": kwargs.get("max_output_tokens", 512),
        }
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        response = requests.post(f"{self.base_url}/responses", headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()

    def generate_image(self, prompt, model="gpt-4o-mini", **kwargs):
        return self.estimate(prompt, model=model, **kwargs)

    def generate_video(self, prompt, model="sora", **kwargs):
        return {"provider": "openai", "model": model, "prompt": prompt, "status": "not_implemented"}

    def poll(self, job_id):
        return {"job_id": job_id, "status": "unknown"}

