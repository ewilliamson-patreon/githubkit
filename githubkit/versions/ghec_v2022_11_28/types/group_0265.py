"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired

from .group_0199 import VerificationType


class GitTagType(TypedDict):
    """Git Tag

    Metadata for a Git tag
    """

    node_id: str
    tag: str
    sha: str
    url: str
    message: str
    tagger: GitTagPropTaggerType
    object_: GitTagPropObjectType
    verification: NotRequired[VerificationType]


class GitTagPropTaggerType(TypedDict):
    """GitTagPropTagger"""

    date: str
    email: str
    name: str


class GitTagPropObjectType(TypedDict):
    """GitTagPropObject"""

    sha: str
    type: str
    url: str


__all__ = (
    "GitTagType",
    "GitTagPropTaggerType",
    "GitTagPropObjectType",
)