"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0560 import WebhookIssuesMilestonedPropIssueAllof1PropMilestoneType


class WebhookIssuesMilestonedPropIssueAllof1Type(TypedDict):
    """WebhookIssuesMilestonedPropIssueAllof1"""

    active_lock_reason: NotRequired[Union[str, None]]
    assignee: NotRequired[
        Union[WebhookIssuesMilestonedPropIssueAllof1PropAssigneeType, None]
    ]
    assignees: NotRequired[
        List[Union[WebhookIssuesMilestonedPropIssueAllof1PropAssigneesItemsType, None]]
    ]
    author_association: NotRequired[str]
    body: NotRequired[Union[str, None]]
    closed_at: NotRequired[Union[str, None]]
    comments: NotRequired[int]
    comments_url: NotRequired[str]
    created_at: NotRequired[str]
    events_url: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    labels: NotRequired[
        List[Union[WebhookIssuesMilestonedPropIssueAllof1PropLabelsItemsType, None]]
    ]
    labels_url: NotRequired[str]
    locked: NotRequired[bool]
    milestone: WebhookIssuesMilestonedPropIssueAllof1PropMilestoneType
    node_id: NotRequired[str]
    number: NotRequired[int]
    performed_via_github_app: NotRequired[
        Union[WebhookIssuesMilestonedPropIssueAllof1PropPerformedViaGithubAppType, None]
    ]
    reactions: NotRequired[WebhookIssuesMilestonedPropIssueAllof1PropReactionsType]
    repository_url: NotRequired[str]
    state: NotRequired[str]
    timeline_url: NotRequired[str]
    title: NotRequired[str]
    updated_at: NotRequired[str]
    url: NotRequired[str]
    user: NotRequired[WebhookIssuesMilestonedPropIssueAllof1PropUserType]


class WebhookIssuesMilestonedPropIssueAllof1PropAssigneeType(TypedDict):
    """WebhookIssuesMilestonedPropIssueAllof1PropAssignee"""


class WebhookIssuesMilestonedPropIssueAllof1PropAssigneesItemsType(TypedDict):
    """WebhookIssuesMilestonedPropIssueAllof1PropAssigneesItems"""


class WebhookIssuesMilestonedPropIssueAllof1PropLabelsItemsType(TypedDict):
    """WebhookIssuesMilestonedPropIssueAllof1PropLabelsItems"""


class WebhookIssuesMilestonedPropIssueAllof1PropPerformedViaGithubAppType(TypedDict):
    """WebhookIssuesMilestonedPropIssueAllof1PropPerformedViaGithubApp"""


class WebhookIssuesMilestonedPropIssueAllof1PropReactionsType(TypedDict):
    """WebhookIssuesMilestonedPropIssueAllof1PropReactions"""

    plus_one: NotRequired[int]
    minus_one: NotRequired[int]
    confused: NotRequired[int]
    eyes: NotRequired[int]
    heart: NotRequired[int]
    hooray: NotRequired[int]
    laugh: NotRequired[int]
    rocket: NotRequired[int]
    total_count: NotRequired[int]
    url: NotRequired[str]


class WebhookIssuesMilestonedPropIssueAllof1PropUserType(TypedDict):
    """WebhookIssuesMilestonedPropIssueAllof1PropUser"""

    avatar_url: NotRequired[str]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    login: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]


__all__ = (
    "WebhookIssuesMilestonedPropIssueAllof1Type",
    "WebhookIssuesMilestonedPropIssueAllof1PropAssigneeType",
    "WebhookIssuesMilestonedPropIssueAllof1PropAssigneesItemsType",
    "WebhookIssuesMilestonedPropIssueAllof1PropLabelsItemsType",
    "WebhookIssuesMilestonedPropIssueAllof1PropPerformedViaGithubAppType",
    "WebhookIssuesMilestonedPropIssueAllof1PropReactionsType",
    "WebhookIssuesMilestonedPropIssueAllof1PropUserType",
)