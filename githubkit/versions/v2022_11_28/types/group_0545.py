"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired


class WebhookIssuesUnlockedPropIssueAllof1Type(TypedDict):
    """WebhookIssuesUnlockedPropIssueAllof1"""

    active_lock_reason: None
    assignee: NotRequired[
        Union[WebhookIssuesUnlockedPropIssueAllof1PropAssigneeType, None]
    ]
    assignees: NotRequired[
        List[Union[WebhookIssuesUnlockedPropIssueAllof1PropAssigneesItemsType, None]]
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
        List[Union[WebhookIssuesUnlockedPropIssueAllof1PropLabelsItemsType, None]]
    ]
    labels_url: NotRequired[str]
    locked: Literal[False]
    milestone: NotRequired[
        Union[WebhookIssuesUnlockedPropIssueAllof1PropMilestoneType, None]
    ]
    node_id: NotRequired[str]
    number: NotRequired[int]
    performed_via_github_app: NotRequired[None]
    reactions: NotRequired[WebhookIssuesUnlockedPropIssueAllof1PropReactionsType]
    repository_url: NotRequired[str]
    state: NotRequired[str]
    timeline_url: NotRequired[str]
    title: NotRequired[str]
    updated_at: NotRequired[str]
    url: NotRequired[str]
    user: NotRequired[WebhookIssuesUnlockedPropIssueAllof1PropUserType]


class WebhookIssuesUnlockedPropIssueAllof1PropAssigneeType(TypedDict):
    """WebhookIssuesUnlockedPropIssueAllof1PropAssignee"""


class WebhookIssuesUnlockedPropIssueAllof1PropAssigneesItemsType(TypedDict):
    """WebhookIssuesUnlockedPropIssueAllof1PropAssigneesItems"""


class WebhookIssuesUnlockedPropIssueAllof1PropLabelsItemsType(TypedDict):
    """WebhookIssuesUnlockedPropIssueAllof1PropLabelsItems"""


class WebhookIssuesUnlockedPropIssueAllof1PropMilestoneType(TypedDict):
    """WebhookIssuesUnlockedPropIssueAllof1PropMilestone"""


class WebhookIssuesUnlockedPropIssueAllof1PropReactionsType(TypedDict):
    """WebhookIssuesUnlockedPropIssueAllof1PropReactions"""

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


class WebhookIssuesUnlockedPropIssueAllof1PropUserType(TypedDict):
    """WebhookIssuesUnlockedPropIssueAllof1PropUser"""

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
    "WebhookIssuesUnlockedPropIssueAllof1Type",
    "WebhookIssuesUnlockedPropIssueAllof1PropAssigneeType",
    "WebhookIssuesUnlockedPropIssueAllof1PropAssigneesItemsType",
    "WebhookIssuesUnlockedPropIssueAllof1PropLabelsItemsType",
    "WebhookIssuesUnlockedPropIssueAllof1PropMilestoneType",
    "WebhookIssuesUnlockedPropIssueAllof1PropReactionsType",
    "WebhookIssuesUnlockedPropIssueAllof1PropUserType",
)