# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities

__all__ = [
    'GetPermissionsGroupResult',
    'AwaitableGetPermissionsGroupResult',
    'get_permissions_group',
    'get_permissions_group_output',
]

@pulumi.output_type
class GetPermissionsGroupResult:
    """
    A collection of values returned by getPermissionsGroup.
    """
    def __init__(__self__, allows=None, created_at=None, denies=None, description=None, excepts=None, id=None, name=None, owner=None, updated_at=None, urn=None):
        if allows and not isinstance(allows, list):
            raise TypeError("Expected argument 'allows' to be a list")
        pulumi.set(__self__, "allows", allows)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if denies and not isinstance(denies, list):
            raise TypeError("Expected argument 'denies' to be a list")
        pulumi.set(__self__, "denies", denies)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if excepts and not isinstance(excepts, list):
            raise TypeError("Expected argument 'excepts' to be a list")
        pulumi.set(__self__, "excepts", excepts)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if owner and not isinstance(owner, str):
            raise TypeError("Expected argument 'owner' to be a str")
        pulumi.set(__self__, "owner", owner)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if urn and not isinstance(urn, str):
            raise TypeError("Expected argument 'urn' to be a str")
        pulumi.set(__self__, "urn", urn)

    @property
    @pulumi.getter
    def allows(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "allows")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def denies(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "denies")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def excepts(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "excepts")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> str:
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter
    def urn(self) -> str:
        return pulumi.get(self, "urn")


class AwaitableGetPermissionsGroupResult(GetPermissionsGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPermissionsGroupResult(
            allows=self.allows,
            created_at=self.created_at,
            denies=self.denies,
            description=self.description,
            excepts=self.excepts,
            id=self.id,
            name=self.name,
            owner=self.owner,
            updated_at=self.updated_at,
            urn=self.urn)


def get_permissions_group(allows: Optional[Sequence[str]] = None,
                          denies: Optional[Sequence[str]] = None,
                          description: Optional[str] = None,
                          excepts: Optional[Sequence[str]] = None,
                          updated_at: Optional[str] = None,
                          urn: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPermissionsGroupResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['allows'] = allows
    __args__['denies'] = denies
    __args__['description'] = description
    __args__['excepts'] = excepts
    __args__['updatedAt'] = updated_at
    __args__['urn'] = urn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ovh:Iam/getPermissionsGroup:getPermissionsGroup', __args__, opts=opts, typ=GetPermissionsGroupResult).value

    return AwaitableGetPermissionsGroupResult(
        allows=pulumi.get(__ret__, 'allows'),
        created_at=pulumi.get(__ret__, 'created_at'),
        denies=pulumi.get(__ret__, 'denies'),
        description=pulumi.get(__ret__, 'description'),
        excepts=pulumi.get(__ret__, 'excepts'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        owner=pulumi.get(__ret__, 'owner'),
        updated_at=pulumi.get(__ret__, 'updated_at'),
        urn=pulumi.get(__ret__, 'urn'))
def get_permissions_group_output(allows: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                 denies: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                 description: Optional[pulumi.Input[Optional[str]]] = None,
                                 excepts: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                 updated_at: Optional[pulumi.Input[Optional[str]]] = None,
                                 urn: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPermissionsGroupResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['allows'] = allows
    __args__['denies'] = denies
    __args__['description'] = description
    __args__['excepts'] = excepts
    __args__['updatedAt'] = updated_at
    __args__['urn'] = urn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ovh:Iam/getPermissionsGroup:getPermissionsGroup', __args__, opts=opts, typ=GetPermissionsGroupResult)
    return __ret__.apply(lambda __response__: GetPermissionsGroupResult(
        allows=pulumi.get(__response__, 'allows'),
        created_at=pulumi.get(__response__, 'created_at'),
        denies=pulumi.get(__response__, 'denies'),
        description=pulumi.get(__response__, 'description'),
        excepts=pulumi.get(__response__, 'excepts'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        owner=pulumi.get(__response__, 'owner'),
        updated_at=pulumi.get(__response__, 'updated_at'),
        urn=pulumi.get(__response__, 'urn')))
