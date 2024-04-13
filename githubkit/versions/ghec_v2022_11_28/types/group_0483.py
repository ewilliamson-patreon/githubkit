"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0390 import EnterpriseWebhooksType
from .group_0391 import SimpleInstallationType
from .group_0393 import RepositoryWebhooksType
from .group_0394 import SimpleUserWebhooksType
from .group_0392 import OrganizationSimpleWebhooksType
from .group_0485 import WebhookIssueCommentCreatedPropIssueType
from .group_0484 import WebhookIssueCommentCreatedPropCommentType


class WebhookIssueCommentCreatedType(TypedDict):
    """issue_comment created event"""

    action: Literal["created"]
    comment: WebhookIssueCommentCreatedPropCommentType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    issue: WebhookIssueCommentCreatedPropIssueType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookIssueCommentCreatedType",)