"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0016 import LicenseSimpleType
from .group_0368 import SearchResultTextMatchesItemsType


class RepoSearchResultItemType(TypedDict):
    """Repo Search Result Item

    Repo Search Result Item
    """

    id: int
    node_id: str
    name: str
    full_name: str
    owner: Union[None, SimpleUserType]
    private: bool
    html_url: str
    description: Union[str, None]
    fork: bool
    url: str
    created_at: datetime
    updated_at: datetime
    pushed_at: datetime
    homepage: Union[str, None]
    size: int
    stargazers_count: int
    watchers_count: int
    language: Union[str, None]
    forks_count: int
    open_issues_count: int
    master_branch: NotRequired[str]
    default_branch: str
    score: float
    forks_url: str
    keys_url: str
    collaborators_url: str
    teams_url: str
    hooks_url: str
    issue_events_url: str
    events_url: str
    assignees_url: str
    branches_url: str
    tags_url: str
    blobs_url: str
    git_tags_url: str
    git_refs_url: str
    trees_url: str
    statuses_url: str
    languages_url: str
    stargazers_url: str
    contributors_url: str
    subscribers_url: str
    subscription_url: str
    commits_url: str
    git_commits_url: str
    comments_url: str
    issue_comment_url: str
    contents_url: str
    compare_url: str
    merges_url: str
    archive_url: str
    downloads_url: str
    issues_url: str
    pulls_url: str
    milestones_url: str
    notifications_url: str
    labels_url: str
    releases_url: str
    deployments_url: str
    git_url: str
    ssh_url: str
    clone_url: str
    svn_url: str
    forks: int
    open_issues: int
    watchers: int
    topics: NotRequired[List[str]]
    mirror_url: Union[str, None]
    has_issues: bool
    has_projects: bool
    has_pages: bool
    has_wiki: bool
    has_downloads: bool
    has_discussions: NotRequired[bool]
    archived: bool
    disabled: bool
    visibility: NotRequired[str]
    license_: Union[None, LicenseSimpleType]
    permissions: NotRequired[RepoSearchResultItemPropPermissionsType]
    text_matches: NotRequired[List[SearchResultTextMatchesItemsType]]
    temp_clone_token: NotRequired[Union[str, None]]
    allow_merge_commit: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_auto_merge: NotRequired[bool]
    delete_branch_on_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    is_template: NotRequired[bool]
    web_commit_signoff_required: NotRequired[bool]


class RepoSearchResultItemPropPermissionsType(TypedDict):
    """RepoSearchResultItemPropPermissions"""

    admin: bool
    maintain: NotRequired[bool]
    push: bool
    triage: NotRequired[bool]
    pull: bool


class SearchRepositoriesGetResponse200Type(TypedDict):
    """SearchRepositoriesGetResponse200"""

    total_count: int
    incomplete_results: bool
    items: List[RepoSearchResultItemType]


__all__ = (
    "RepoSearchResultItemType",
    "RepoSearchResultItemPropPermissionsType",
    "SearchRepositoriesGetResponse200Type",
)