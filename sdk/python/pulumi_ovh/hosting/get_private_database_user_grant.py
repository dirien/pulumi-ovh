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
    'GetPrivateDatabaseUserGrantResult',
    'AwaitableGetPrivateDatabaseUserGrantResult',
    'get_private_database_user_grant',
    'get_private_database_user_grant_output',
]

@pulumi.output_type
class GetPrivateDatabaseUserGrantResult:
    """
    A collection of values returned by getPrivateDatabaseUserGrant.
    """
    def __init__(__self__, creation_date=None, database_name=None, grant=None, id=None, service_name=None, user_name=None):
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if database_name and not isinstance(database_name, str):
            raise TypeError("Expected argument 'database_name' to be a str")
        pulumi.set(__self__, "database_name", database_name)
        if grant and not isinstance(grant, str):
            raise TypeError("Expected argument 'grant' to be a str")
        pulumi.set(__self__, "grant", grant)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> str:
        """
        Creation date of the database
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> str:
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter
    def grant(self) -> str:
        """
        Grant name
        """
        return pulumi.get(self, "grant")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> str:
        return pulumi.get(self, "user_name")


class AwaitableGetPrivateDatabaseUserGrantResult(GetPrivateDatabaseUserGrantResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateDatabaseUserGrantResult(
            creation_date=self.creation_date,
            database_name=self.database_name,
            grant=self.grant,
            id=self.id,
            service_name=self.service_name,
            user_name=self.user_name)


def get_private_database_user_grant(database_name: Optional[str] = None,
                                    service_name: Optional[str] = None,
                                    user_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateDatabaseUserGrantResult:
    """
    Use this data source to retrieve information about an hosting privatedatabase user grant.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    user_grant = ovh.Hosting.get_private_database_user_grant(database_name="XXXXXX",
        service_name="XXXXXX",
        user_name="XXXXXX")
    ```


    :param str database_name: The database name on which grant the user
    :param str service_name: The internal name of your private database
    :param str user_name: The user name
    """
    __args__ = dict()
    __args__['databaseName'] = database_name
    __args__['serviceName'] = service_name
    __args__['userName'] = user_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ovh:Hosting/getPrivateDatabaseUserGrant:getPrivateDatabaseUserGrant', __args__, opts=opts, typ=GetPrivateDatabaseUserGrantResult).value

    return AwaitableGetPrivateDatabaseUserGrantResult(
        creation_date=pulumi.get(__ret__, 'creation_date'),
        database_name=pulumi.get(__ret__, 'database_name'),
        grant=pulumi.get(__ret__, 'grant'),
        id=pulumi.get(__ret__, 'id'),
        service_name=pulumi.get(__ret__, 'service_name'),
        user_name=pulumi.get(__ret__, 'user_name'))
def get_private_database_user_grant_output(database_name: Optional[pulumi.Input[str]] = None,
                                           service_name: Optional[pulumi.Input[str]] = None,
                                           user_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPrivateDatabaseUserGrantResult]:
    """
    Use this data source to retrieve information about an hosting privatedatabase user grant.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    user_grant = ovh.Hosting.get_private_database_user_grant(database_name="XXXXXX",
        service_name="XXXXXX",
        user_name="XXXXXX")
    ```


    :param str database_name: The database name on which grant the user
    :param str service_name: The internal name of your private database
    :param str user_name: The user name
    """
    __args__ = dict()
    __args__['databaseName'] = database_name
    __args__['serviceName'] = service_name
    __args__['userName'] = user_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ovh:Hosting/getPrivateDatabaseUserGrant:getPrivateDatabaseUserGrant', __args__, opts=opts, typ=GetPrivateDatabaseUserGrantResult)
    return __ret__.apply(lambda __response__: GetPrivateDatabaseUserGrantResult(
        creation_date=pulumi.get(__response__, 'creation_date'),
        database_name=pulumi.get(__response__, 'database_name'),
        grant=pulumi.get(__response__, 'grant'),
        id=pulumi.get(__response__, 'id'),
        service_name=pulumi.get(__response__, 'service_name'),
        user_name=pulumi.get(__response__, 'user_name')))
