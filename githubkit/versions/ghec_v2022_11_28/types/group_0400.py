"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypedDict

from .group_0001 import SimpleUserType


class ProjectsV2Type(TypedDict):
    """Projects v2 Project

    A projects v2 project
    """

    id: float
    node_id: str
    owner: SimpleUserType
    creator: SimpleUserType
    title: str
    description: Union[str, None]
    public: bool
    closed_at: Union[datetime, None]
    created_at: datetime
    updated_at: datetime
    number: int
    short_description: Union[str, None]
    deleted_at: Union[datetime, None]
    deleted_by: Union[None, SimpleUserType]


__all__ = ("ProjectsV2Type",)