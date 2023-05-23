"""API class for OwlML."""
import os
from typing import Any

import requests


def _get_required_env_var(env_var: str) -> str:
    """Get an environment variable or raise an error if it doesn't exist."""
    value = os.getenv(env_var)
    if value is None:
        raise ValueError(f"Missing required environment variable: {env_var}")
    return value    


class OwlMLAPI:
    """API class for OwlML."""

    base_url: str = _get_required_env_var("OWLML_API")

    @classmethod
    def get(cls, route: str) -> dict[str, Any]:
        """Make a GET request to the OwlML API."""
        response = requests.get(os.path.join(cls.base_url, route))
        response.raise_for_status()
        return response.json()

    @classmethod
    def post(cls, route: str, payload: dict[str, Any]) -> dict[str, Any]:
        """Make a POST request to the OwlML API."""
        response = requests.post(os.path.join(cls.base_url, route), json=payload)
        response.raise_for_status()
        return response.json()
