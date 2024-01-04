"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import Annotated

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser
from .group_0028 import SimpleRepository
from .group_0067 import CodeScanningAnalysisTool
from .group_0068 import CodeScanningAlertInstance
from .group_0066 import CodeScanningAlertRuleSummary


class CodeScanningOrganizationAlertItems(GitHubModel):
    """CodeScanningOrganizationAlertItems"""

    number: int = Field(description="The security alert number.")
    created_at: datetime = Field(
        description="The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )
    updated_at: Missing[datetime] = Field(
        default=UNSET,
        description="The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    url: str = Field(description="The REST API URL of the alert resource.")
    html_url: str = Field(description="The GitHub URL of the alert resource.")
    instances_url: str = Field(
        description="The REST API URL for fetching the list of instances for an alert."
    )
    state: Literal["open", "dismissed", "fixed"] = Field(
        description="State of a code scanning alert."
    )
    fixed_at: Missing[Union[datetime, None]] = Field(
        default=UNSET,
        description="The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    dismissed_by: Union[None, SimpleUser] = Field()
    dismissed_at: Union[datetime, None] = Field(
        description="The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )
    dismissed_reason: Union[
        None, Literal["false positive", "won't fix", "used in tests"]
    ] = Field(
        description="**Required when the state is dismissed.** The reason for dismissing or closing the alert."
    )
    dismissed_comment: Missing[
        Union[Annotated[str, Field(max_length=280)], None]
    ] = Field(
        default=UNSET,
        description="The dismissal comment associated with the dismissal of the alert.",
    )
    rule: CodeScanningAlertRuleSummary = Field()
    tool: CodeScanningAnalysisTool = Field()
    most_recent_instance: CodeScanningAlertInstance = Field()
    repository: SimpleRepository = Field(
        title="Simple Repository", description="A GitHub repository."
    )


model_rebuild(CodeScanningOrganizationAlertItems)

__all__ = ("CodeScanningOrganizationAlertItems",)