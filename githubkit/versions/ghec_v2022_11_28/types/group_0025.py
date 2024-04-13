"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired


class ServerStatisticsItemsType(TypedDict):
    """ServerStatisticsItems"""

    server_id: NotRequired[str]
    collection_date: NotRequired[str]
    schema_version: NotRequired[str]
    ghes_version: NotRequired[str]
    host_name: NotRequired[str]
    github_connect: NotRequired[ServerStatisticsItemsPropGithubConnectType]
    ghe_stats: NotRequired[ServerStatisticsItemsPropGheStatsType]
    dormant_users: NotRequired[ServerStatisticsItemsPropDormantUsersType]
    actions_stats: NotRequired[ServerStatisticsActionsType]
    packages_stats: NotRequired[ServerStatisticsPackagesType]


class ServerStatisticsActionsType(TypedDict):
    """ServerStatisticsActions

    Actions metrics that are included in the Server Statistics payload/export from
    GHES
    """

    number_of_repos_using_actions: NotRequired[int]
    percentage_of_repos_using_actions: NotRequired[str]


class ServerStatisticsItemsPropGithubConnectType(TypedDict):
    """ServerStatisticsItemsPropGithubConnect"""

    features_enabled: NotRequired[List[str]]


class ServerStatisticsItemsPropDormantUsersType(TypedDict):
    """ServerStatisticsItemsPropDormantUsers"""

    total_dormant_users: NotRequired[int]
    dormancy_threshold: NotRequired[str]


class ServerStatisticsPackagesType(TypedDict):
    """ServerStatisticsPackages

    Packages metrics that are included in the Server Statistics payload/export from
    GHES
    """

    registry_enabled: NotRequired[bool]
    registry_v2_enabled: NotRequired[bool]
    ecosystems: NotRequired[List[ServerStatisticsPackagesPropEcosystemsItemsType]]


class ServerStatisticsPackagesPropEcosystemsItemsType(TypedDict):
    """ServerStatisticsPackagesPropEcosystemsItems"""

    name: NotRequired[
        Literal["npm", "maven", "docker", "nuget", "rubygems", "containers"]
    ]
    enabled: NotRequired[Literal["TRUE", "FALSE", "READONLY"]]
    published_packages_count: NotRequired[int]
    private_packages_count: NotRequired[int]
    public_packages_count: NotRequired[int]
    internal_packages_count: NotRequired[int]
    user_packages_count: NotRequired[int]
    organization_packages_count: NotRequired[int]
    daily_download_count: NotRequired[int]
    daily_update_count: NotRequired[int]
    daily_delete_count: NotRequired[int]
    daily_create_count: NotRequired[int]


class ServerStatisticsItemsPropGheStatsType(TypedDict):
    """ServerStatisticsItemsPropGheStats"""

    comments: NotRequired[ServerStatisticsItemsPropGheStatsPropCommentsType]
    gists: NotRequired[ServerStatisticsItemsPropGheStatsPropGistsType]
    hooks: NotRequired[ServerStatisticsItemsPropGheStatsPropHooksType]
    issues: NotRequired[ServerStatisticsItemsPropGheStatsPropIssuesType]
    milestones: NotRequired[ServerStatisticsItemsPropGheStatsPropMilestonesType]
    orgs: NotRequired[ServerStatisticsItemsPropGheStatsPropOrgsType]
    pages: NotRequired[ServerStatisticsItemsPropGheStatsPropPagesType]
    pulls: NotRequired[ServerStatisticsItemsPropGheStatsPropPullsType]
    repos: NotRequired[ServerStatisticsItemsPropGheStatsPropReposType]
    users: NotRequired[ServerStatisticsItemsPropGheStatsPropUsersType]


class ServerStatisticsItemsPropGheStatsPropCommentsType(TypedDict):
    """ServerStatisticsItemsPropGheStatsPropComments"""

    total_commit_comments: NotRequired[int]
    total_gist_comments: NotRequired[int]
    total_issue_comments: NotRequired[int]
    total_pull_request_comments: NotRequired[int]


class ServerStatisticsItemsPropGheStatsPropGistsType(TypedDict):
    """ServerStatisticsItemsPropGheStatsPropGists"""

    total_gists: NotRequired[int]
    private_gists: NotRequired[int]
    public_gists: NotRequired[int]


class ServerStatisticsItemsPropGheStatsPropHooksType(TypedDict):
    """ServerStatisticsItemsPropGheStatsPropHooks"""

    total_hooks: NotRequired[int]
    active_hooks: NotRequired[int]
    inactive_hooks: NotRequired[int]


class ServerStatisticsItemsPropGheStatsPropIssuesType(TypedDict):
    """ServerStatisticsItemsPropGheStatsPropIssues"""

    total_issues: NotRequired[int]
    open_issues: NotRequired[int]
    closed_issues: NotRequired[int]


class ServerStatisticsItemsPropGheStatsPropMilestonesType(TypedDict):
    """ServerStatisticsItemsPropGheStatsPropMilestones"""

    total_milestones: NotRequired[int]
    open_milestones: NotRequired[int]
    closed_milestones: NotRequired[int]


class ServerStatisticsItemsPropGheStatsPropOrgsType(TypedDict):
    """ServerStatisticsItemsPropGheStatsPropOrgs"""

    total_orgs: NotRequired[int]
    disabled_orgs: NotRequired[int]
    total_teams: NotRequired[int]
    total_team_members: NotRequired[int]


class ServerStatisticsItemsPropGheStatsPropPagesType(TypedDict):
    """ServerStatisticsItemsPropGheStatsPropPages"""

    total_pages: NotRequired[int]


class ServerStatisticsItemsPropGheStatsPropPullsType(TypedDict):
    """ServerStatisticsItemsPropGheStatsPropPulls"""

    total_pulls: NotRequired[int]
    merged_pulls: NotRequired[int]
    mergeable_pulls: NotRequired[int]
    unmergeable_pulls: NotRequired[int]


class ServerStatisticsItemsPropGheStatsPropReposType(TypedDict):
    """ServerStatisticsItemsPropGheStatsPropRepos"""

    total_repos: NotRequired[int]
    root_repos: NotRequired[int]
    fork_repos: NotRequired[int]
    org_repos: NotRequired[int]
    total_pushes: NotRequired[int]
    total_wikis: NotRequired[int]


class ServerStatisticsItemsPropGheStatsPropUsersType(TypedDict):
    """ServerStatisticsItemsPropGheStatsPropUsers"""

    total_users: NotRequired[int]
    admin_users: NotRequired[int]
    suspended_users: NotRequired[int]


__all__ = (
    "ServerStatisticsItemsType",
    "ServerStatisticsActionsType",
    "ServerStatisticsItemsPropGithubConnectType",
    "ServerStatisticsItemsPropDormantUsersType",
    "ServerStatisticsPackagesType",
    "ServerStatisticsPackagesPropEcosystemsItemsType",
    "ServerStatisticsItemsPropGheStatsType",
    "ServerStatisticsItemsPropGheStatsPropCommentsType",
    "ServerStatisticsItemsPropGheStatsPropGistsType",
    "ServerStatisticsItemsPropGheStatsPropHooksType",
    "ServerStatisticsItemsPropGheStatsPropIssuesType",
    "ServerStatisticsItemsPropGheStatsPropMilestonesType",
    "ServerStatisticsItemsPropGheStatsPropOrgsType",
    "ServerStatisticsItemsPropGheStatsPropPagesType",
    "ServerStatisticsItemsPropGheStatsPropPullsType",
    "ServerStatisticsItemsPropGheStatsPropReposType",
    "ServerStatisticsItemsPropGheStatsPropUsersType",
)