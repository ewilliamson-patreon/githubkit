"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict


class CustomDeploymentRuleAppType(TypedDict):
    """Custom deployment protection rule app

    A GitHub App that is providing a custom deployment protection rule.
    """

    id: int
    slug: str
    integration_url: str
    node_id: str


__all__ = ("CustomDeploymentRuleAppType",)