"""DO NOT EDIT THIS FILE!

This file is auto generated by github rest api discription.
See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, List, Union

from pydantic import Field

from githubkit.utils import UNSET, Unset, exclude_unset

from .models import (
    ScimUser,
    ScimError,
    BasicError,
    ScimUserList,
    ScimV2OrganizationsOrgUsersPostBody,
    ScimV2OrganizationsOrgUsersPostBodyPropName,
    ScimV2OrganizationsOrgUsersScimUserIdPutBody,
    ScimV2OrganizationsOrgUsersScimUserIdPatchBody,
    ScimV2OrganizationsOrgUsersPostBodyPropEmailsItems,
    ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropName,
    ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItems,
    ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItems,
)

if TYPE_CHECKING:
    from githubkit.core import GitHubCore
    from githubkit.response import Response


class ScimClient:
    def __init__(self, github: "GitHubCore"):
        self._github = github

    def list_provisioned_identities(
        self,
        org: str,
        start_index: Union[Unset, int] = UNSET,
        count: Union[Unset, int] = UNSET,
        filter_: Union[Unset, str] = UNSET,
    ) -> "Response[ScimUserList]":
        url = f"/scim/v2/organizations/{org}/Users"

        params = {
            "startIndex": start_index,
            "count": count,
            "filter": filter_,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=ScimUserList,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "400": ScimError,
                "429": ScimError,
            },
        )

    async def async_list_provisioned_identities(
        self,
        org: str,
        start_index: Union[Unset, int] = UNSET,
        count: Union[Unset, int] = UNSET,
        filter_: Union[Unset, str] = UNSET,
    ) -> "Response[ScimUserList]":
        url = f"/scim/v2/organizations/{org}/Users"

        params = {
            "startIndex": start_index,
            "count": count,
            "filter": filter_,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=ScimUserList,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "400": ScimError,
                "429": ScimError,
            },
        )

    def provision_and_invite_user(
        self,
        org: str,
        *,
        user_name: str,
        display_name: Union[Unset, str] = UNSET,
        name: ScimV2OrganizationsOrgUsersPostBodyPropName,
        emails: List[ScimV2OrganizationsOrgUsersPostBodyPropEmailsItems],
        schemas: Union[Unset, List[str]] = UNSET,
        external_id: Union[Unset, str] = UNSET,
        groups: Union[Unset, List[str]] = UNSET,
        active: Union[Unset, bool] = UNSET,
    ) -> "Response[ScimUser]":
        url = f"/scim/v2/organizations/{org}/Users"

        json = ScimV2OrganizationsOrgUsersPostBody(
            **{
                "userName": user_name,
                "displayName": display_name,
                "name": name,
                "emails": emails,
                "schemas": schemas,
                "externalId": external_id,
                "groups": groups,
                "active": active,
            }
        ).dict(by_alias=True)

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "500": ScimError,
                "409": ScimError,
                "400": ScimError,
            },
        )

    async def async_provision_and_invite_user(
        self,
        org: str,
        *,
        user_name: str,
        display_name: Union[Unset, str] = UNSET,
        name: ScimV2OrganizationsOrgUsersPostBodyPropName,
        emails: List[ScimV2OrganizationsOrgUsersPostBodyPropEmailsItems],
        schemas: Union[Unset, List[str]] = UNSET,
        external_id: Union[Unset, str] = UNSET,
        groups: Union[Unset, List[str]] = UNSET,
        active: Union[Unset, bool] = UNSET,
    ) -> "Response[ScimUser]":
        url = f"/scim/v2/organizations/{org}/Users"

        json = ScimV2OrganizationsOrgUsersPostBody(
            **{
                "userName": user_name,
                "displayName": display_name,
                "name": name,
                "emails": emails,
                "schemas": schemas,
                "externalId": external_id,
                "groups": groups,
                "active": active,
            }
        ).dict(by_alias=True)

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "500": ScimError,
                "409": ScimError,
                "400": ScimError,
            },
        )

    def get_provisioning_information_for_user(
        self,
        org: str,
        scim_user_id: str,
    ) -> "Response[ScimUser]":
        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        return self._github.request(
            "GET",
            url,
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    async def async_get_provisioning_information_for_user(
        self,
        org: str,
        scim_user_id: str,
    ) -> "Response[ScimUser]":
        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        return await self._github.arequest(
            "GET",
            url,
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    def set_information_for_provisioned_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        schemas: Union[Unset, List[str]] = UNSET,
        display_name: Union[Unset, str] = UNSET,
        external_id: Union[Unset, str] = UNSET,
        groups: Union[Unset, List[str]] = UNSET,
        active: Union[Unset, bool] = UNSET,
        user_name: str,
        name: ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropName,
        emails: List[ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItems],
    ) -> "Response[ScimUser]":
        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        json = ScimV2OrganizationsOrgUsersScimUserIdPutBody(
            **{
                "schemas": schemas,
                "displayName": display_name,
                "externalId": external_id,
                "groups": groups,
                "active": active,
                "userName": user_name,
                "name": name,
                "emails": emails,
            }
        ).dict(by_alias=True)

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    async def async_set_information_for_provisioned_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        schemas: Union[Unset, List[str]] = UNSET,
        display_name: Union[Unset, str] = UNSET,
        external_id: Union[Unset, str] = UNSET,
        groups: Union[Unset, List[str]] = UNSET,
        active: Union[Unset, bool] = UNSET,
        user_name: str,
        name: ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropName,
        emails: List[ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItems],
    ) -> "Response[ScimUser]":
        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        json = ScimV2OrganizationsOrgUsersScimUserIdPutBody(
            **{
                "schemas": schemas,
                "displayName": display_name,
                "externalId": external_id,
                "groups": groups,
                "active": active,
                "userName": user_name,
                "name": name,
                "emails": emails,
            }
        ).dict(by_alias=True)

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    def delete_user_from_org(
        self,
        org: str,
        scim_user_id: str,
    ) -> "Response":
        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        return self._github.request(
            "DELETE",
            url,
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    async def async_delete_user_from_org(
        self,
        org: str,
        scim_user_id: str,
    ) -> "Response":
        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        return await self._github.arequest(
            "DELETE",
            url,
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    def update_attribute_for_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        schemas: Union[Unset, List[str]] = UNSET,
        operations: List[
            ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItems
        ],
    ) -> "Response[ScimUser]":
        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        json = ScimV2OrganizationsOrgUsersScimUserIdPatchBody(
            **{
                "schemas": schemas,
                "Operations": operations,
            }
        ).dict(by_alias=True)

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "400": ScimError,
                "429": BasicError,
            },
        )

    async def async_update_attribute_for_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        schemas: Union[Unset, List[str]] = UNSET,
        operations: List[
            ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItems
        ],
    ) -> "Response[ScimUser]":
        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        json = ScimV2OrganizationsOrgUsersScimUserIdPatchBody(
            **{
                "schemas": schemas,
                "Operations": operations,
            }
        ).dict(by_alias=True)

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "400": ScimError,
                "429": BasicError,
            },
        )
