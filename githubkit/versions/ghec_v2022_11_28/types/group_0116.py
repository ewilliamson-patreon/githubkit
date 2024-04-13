"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0017 import RepositoryType
from .group_0016 import LicenseSimpleType
from .group_0075 import SecurityAndAnalysisType
from .group_0115 import CodeOfConductSimpleType


class FullRepositoryType(TypedDict):
    """Full Repository

    Full Repository
    """

    id: int
    node_id: str
    name: str
    full_name: str
    owner: SimpleUserType
    private: bool
    html_url: str
    description: Union[str, None]
    fork: bool
    url: str
    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    downloads_url: str
    events_url: str
    forks_url: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    notifications_url: str
    pulls_url: str
    releases_url: str
    ssh_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    clone_url: str
    mirror_url: Union[str, None]
    hooks_url: str
    svn_url: str
    homepage: Union[str, None]
    language: Union[str, None]
    forks_count: int
    stargazers_count: int
    watchers_count: int
    size: int
    default_branch: str
    open_issues_count: int
    is_template: NotRequired[bool]
    topics: NotRequired[List[str]]
    has_issues: bool
    has_projects: bool
    has_wiki: bool
    has_pages: bool
    has_downloads: NotRequired[bool]
    has_discussions: bool
    archived: bool
    disabled: bool
    visibility: NotRequired[str]
    pushed_at: datetime
    created_at: datetime
    updated_at: datetime
    permissions: NotRequired[FullRepositoryPropPermissionsType]
    allow_rebase_merge: NotRequired[bool]
    template_repository: NotRequired[Union[None, RepositoryType]]
    temp_clone_token: NotRequired[Union[str, None]]
    allow_squash_merge: NotRequired[bool]
    allow_auto_merge: NotRequired[bool]
    delete_branch_on_merge: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    use_squash_pr_title_as_default: NotRequired[bool]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    squash_merge_commit_message: NotRequired[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    allow_forking: NotRequired[bool]
    web_commit_signoff_required: NotRequired[bool]
    subscribers_count: int
    network_count: int
    license_: Union[None, LicenseSimpleType]
    organization: NotRequired[Union[None, SimpleUserType]]
    parent: NotRequired[RepositoryType]
    source: NotRequired[RepositoryType]
    forks: int
    master_branch: NotRequired[str]
    open_issues: int
    watchers: int
    anonymous_access_enabled: NotRequired[bool]
    code_of_conduct: NotRequired[CodeOfConductSimpleType]
    security_and_analysis: NotRequired[Union[SecurityAndAnalysisType, None]]
    custom_properties: NotRequired[FullRepositoryPropCustomPropertiesType]


class FullRepositoryPropPermissionsType(TypedDict):
    """FullRepositoryPropPermissions"""

    admin: bool
    maintain: NotRequired[bool]
    push: bool
    triage: NotRequired[bool]
    pull: bool


class FullRepositoryPropCustomPropertiesType(TypedDict):
    """FullRepositoryPropCustomProperties

    The custom properties that were defined for the repository. The keys are the
    custom property names, and the values are the corresponding custom property
    values.
    """


__all__ = (
    "FullRepositoryType",
    "FullRepositoryPropPermissionsType",
    "FullRepositoryPropCustomPropertiesType",
)