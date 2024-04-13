"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0228 import Link


class PullRequestPropLinks(GitHubModel):
    """PullRequestPropLinks"""

    comments: Link = Field(title="Link", description="Hypermedia Link")
    commits: Link = Field(title="Link", description="Hypermedia Link")
    statuses: Link = Field(title="Link", description="Hypermedia Link")
    html: Link = Field(title="Link", description="Hypermedia Link")
    issue: Link = Field(title="Link", description="Hypermedia Link")
    review_comments: Link = Field(title="Link", description="Hypermedia Link")
    review_comment: Link = Field(title="Link", description="Hypermedia Link")
    self_: Link = Field(alias="self", title="Link", description="Hypermedia Link")


model_rebuild(PullRequestPropLinks)

__all__ = ("PullRequestPropLinks",)