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

from .group_0001 import SimpleUser
from .group_0076 import MinimalRepository


class Package(GitHubModel):
    """Package

    A software package
    """

    id: int = Field(description="Unique identifier of the package.")
    name: str = Field(description="The name of the package.")
    package_type: Literal[
        "npm", "maven", "rubygems", "docker", "nuget", "container"
    ] = Field()
    url: str = Field()
    html_url: str = Field()
    version_count: int = Field(description="The number of versions of the package.")
    visibility: Literal["private", "public"] = Field()
    owner: Missing[Union[None, SimpleUser]] = Field(default=UNSET)
    repository: Missing[Union[None, MinimalRepository]] = Field(default=UNSET)
    created_at: datetime = Field()
    updated_at: datetime = Field()


model_rebuild(Package)

__all__ = ("Package",)