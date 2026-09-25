from shared.providers.openai_adapter import OpenAIAdapter
from shared.providers.google_adapter import GoogleAdapter
from shared.providers.runway_adapter import RunwayAdapter
from shared.providers.replicate_adapter import ReplicateAdapter
from shared.providers.fal_adapter import FalAdapter
from shared.providers.kling_adapter import KlingAdapter
import os

PROVIDER_MAP = {
    "openai": OpenAIAdapter,
    "google": GoogleAdapter,
    "runway": RunwayAdapter,
    "replicate": ReplicateAdapter,
    "fal": FalAdapter,
    "kling": KlingAdapter,
}


def get_adapter(provider_name: str):
    provider = provider_name.strip().lower()
    if provider not in PROVIDER_MAP:
        raise ValueError(f"Unsupported provider: {provider}")
    return PROVIDER_MAP[provider]()


def get_image_provider():
    return os.getenv("IMAGE_PROVIDER", "openai")


def get_video_provider():
    return os.getenv("VIDEO_PROVIDER", "openai")

