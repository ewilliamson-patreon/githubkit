"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0390 import EnterpriseWebhooks
from .group_0391 import SimpleInstallation
from .group_0393 import RepositoryWebhooks
from .group_0394 import SimpleUserWebhooks
from .group_0392 import OrganizationSimpleWebhooks


class WebhookProjectColumnDeleted(GitHubModel):
    """project_column deleted event"""

    action: Literal["deleted"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    project_column: WebhookProjectColumnDeletedPropProjectColumn = Field(
        title="Project Column"
    )
    repository: Missing[Union[None, RepositoryWebhooks]] = Field(default=UNSET)
    sender: Missing[SimpleUserWebhooks] = Field(
        default=UNSET,
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookProjectColumnDeletedPropProjectColumn(GitHubModel):
    """Project Column"""

    after_id: Missing[Union[int, None]] = Field(default=UNSET)
    cards_url: str = Field()
    created_at: datetime = Field()
    id: int = Field(description="The unique identifier of the project column")
    name: str = Field(description="Name of the project column")
    node_id: str = Field()
    project_url: str = Field()
    updated_at: datetime = Field()
    url: str = Field()


model_rebuild(WebhookProjectColumnDeleted)
model_rebuild(WebhookProjectColumnDeletedPropProjectColumn)

__all__ = (
    "WebhookProjectColumnDeleted",
    "WebhookProjectColumnDeletedPropProjectColumn",
)