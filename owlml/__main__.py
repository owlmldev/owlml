"""Main entry point for OwlML CLI."""
import fire

from .auth import create_user, create_org, invite_user


def main() -> None:
    """Expose CLI commands."""
    fire.Fire({
        "create-org": create_org,
        "create-user": create_user,
        "invite-user": invite_user,
    })
