"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0090 import TeamType
from .group_0001 import SimpleUserType


class EnvironmentPropProtectionRulesItemsAnyof1PropReviewersItemsType(TypedDict):
    """EnvironmentPropProtectionRulesItemsAnyof1PropReviewersItems"""

    type: NotRequired[Literal["User", "Team"]]
    reviewer: NotRequired[Union[SimpleUserType, TeamType]]


__all__ = ("EnvironmentPropProtectionRulesItemsAnyof1PropReviewersItemsType",)