"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import Dict, Type, Union
from typing_extensions import Annotated, TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import (
    WebhookSponsorshipEdited,
    WebhookSponsorshipCreated,
    WebhookSponsorshipCancelled,
    WebhookSponsorshipTierChanged,
    WebhookSponsorshipPendingTierChange,
    WebhookSponsorshipPendingCancellation,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookSponsorshipCancelled,
        WebhookSponsorshipCreated,
        WebhookSponsorshipEdited,
        WebhookSponsorshipPendingCancellation,
        WebhookSponsorshipPendingTierChange,
        WebhookSponsorshipTierChanged,
    ],
    Field(discriminator="action"),
]

SponsorshipEvent: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "cancelled": WebhookSponsorshipCancelled,
    "created": WebhookSponsorshipCreated,
    "edited": WebhookSponsorshipEdited,
    "pending_cancellation": WebhookSponsorshipPendingCancellation,
    "pending_tier_change": WebhookSponsorshipPendingTierChange,
    "tier_changed": WebhookSponsorshipTierChanged,
}

sponsorship_action_types = action_types

__all__ = ("Event", "SponsorshipEvent", "action_types", "sponsorship_action_types")