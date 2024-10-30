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
from . import outputs
from ._inputs import *

__all__ = ['OpensearchUserArgs', 'OpensearchUser']

@pulumi.input_type
class OpensearchUserArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 acls: Optional[pulumi.Input[Sequence[pulumi.Input['OpensearchUserAclArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password_reset: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OpensearchUser resource.
        :param pulumi.Input[str] cluster_id: Cluster ID.
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted,
               the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        :param pulumi.Input[Sequence[pulumi.Input['OpensearchUserAclArgs']]] acls: Acls of the user.
        :param pulumi.Input[str] name: Username affected by this acl. A user named "avnadmin" is mapped with already created admin user and reset his password instead of creating a new user.
        :param pulumi.Input[str] password_reset: Arbitrary string to change to trigger a password update
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "service_name", service_name)
        if acls is not None:
            pulumi.set(__self__, "acls", acls)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if password_reset is not None:
            pulumi.set(__self__, "password_reset", password_reset)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        Cluster ID.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The id of the public cloud project. If omitted,
        the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def acls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OpensearchUserAclArgs']]]]:
        """
        Acls of the user.
        """
        return pulumi.get(self, "acls")

    @acls.setter
    def acls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OpensearchUserAclArgs']]]]):
        pulumi.set(self, "acls", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Username affected by this acl. A user named "avnadmin" is mapped with already created admin user and reset his password instead of creating a new user.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="passwordReset")
    def password_reset(self) -> Optional[pulumi.Input[str]]:
        """
        Arbitrary string to change to trigger a password update
        """
        return pulumi.get(self, "password_reset")

    @password_reset.setter
    def password_reset(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password_reset", value)


@pulumi.input_type
class _OpensearchUserState:
    def __init__(__self__, *,
                 acls: Optional[pulumi.Input[Sequence[pulumi.Input['OpensearchUserAclArgs']]]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 password_reset: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering OpensearchUser resources.
        :param pulumi.Input[Sequence[pulumi.Input['OpensearchUserAclArgs']]] acls: Acls of the user.
        :param pulumi.Input[str] cluster_id: Cluster ID.
        :param pulumi.Input[str] created_at: Date of the creation of the user.
        :param pulumi.Input[str] name: Username affected by this acl. A user named "avnadmin" is mapped with already created admin user and reset his password instead of creating a new user.
        :param pulumi.Input[str] password: (Sensitive) Password of the user.
        :param pulumi.Input[str] password_reset: Arbitrary string to change to trigger a password update
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted,
               the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        :param pulumi.Input[str] status: Current status of the user.
        """
        if acls is not None:
            pulumi.set(__self__, "acls", acls)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if password_reset is not None:
            pulumi.set(__self__, "password_reset", password_reset)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def acls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OpensearchUserAclArgs']]]]:
        """
        Acls of the user.
        """
        return pulumi.get(self, "acls")

    @acls.setter
    def acls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OpensearchUserAclArgs']]]]):
        pulumi.set(self, "acls", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        Cluster ID.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Date of the creation of the user.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Username affected by this acl. A user named "avnadmin" is mapped with already created admin user and reset his password instead of creating a new user.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        (Sensitive) Password of the user.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="passwordReset")
    def password_reset(self) -> Optional[pulumi.Input[str]]:
        """
        Arbitrary string to change to trigger a password update
        """
        return pulumi.get(self, "password_reset")

    @password_reset.setter
    def password_reset(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password_reset", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the public cloud project. If omitted,
        the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Current status of the user.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class OpensearchUser(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acls: Optional[pulumi.Input[Sequence[pulumi.Input[Union['OpensearchUserAclArgs', 'OpensearchUserAclArgsDict']]]]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password_reset: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Import

        OVHcloud Managed OpenSearch clusters users can be imported using the `service_name`, `cluster_id` and `id` of the user, separated by "/" E.g.,

        bash

        ```sh
        $ pulumi import ovh:CloudProjectDatabase/opensearchUser:OpensearchUser my_user service_name/cluster_id/id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['OpensearchUserAclArgs', 'OpensearchUserAclArgsDict']]]] acls: Acls of the user.
        :param pulumi.Input[str] cluster_id: Cluster ID.
        :param pulumi.Input[str] name: Username affected by this acl. A user named "avnadmin" is mapped with already created admin user and reset his password instead of creating a new user.
        :param pulumi.Input[str] password_reset: Arbitrary string to change to trigger a password update
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted,
               the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OpensearchUserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        OVHcloud Managed OpenSearch clusters users can be imported using the `service_name`, `cluster_id` and `id` of the user, separated by "/" E.g.,

        bash

        ```sh
        $ pulumi import ovh:CloudProjectDatabase/opensearchUser:OpensearchUser my_user service_name/cluster_id/id
        ```

        :param str resource_name: The name of the resource.
        :param OpensearchUserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OpensearchUserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acls: Optional[pulumi.Input[Sequence[pulumi.Input[Union['OpensearchUserAclArgs', 'OpensearchUserAclArgsDict']]]]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password_reset: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OpensearchUserArgs.__new__(OpensearchUserArgs)

            __props__.__dict__["acls"] = acls
            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["name"] = name
            __props__.__dict__["password_reset"] = password_reset
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["created_at"] = None
            __props__.__dict__["password"] = None
            __props__.__dict__["status"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(OpensearchUser, __self__).__init__(
            'ovh:CloudProjectDatabase/opensearchUser:OpensearchUser',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            acls: Optional[pulumi.Input[Sequence[pulumi.Input[Union['OpensearchUserAclArgs', 'OpensearchUserAclArgsDict']]]]] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            password_reset: Optional[pulumi.Input[str]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'OpensearchUser':
        """
        Get an existing OpensearchUser resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['OpensearchUserAclArgs', 'OpensearchUserAclArgsDict']]]] acls: Acls of the user.
        :param pulumi.Input[str] cluster_id: Cluster ID.
        :param pulumi.Input[str] created_at: Date of the creation of the user.
        :param pulumi.Input[str] name: Username affected by this acl. A user named "avnadmin" is mapped with already created admin user and reset his password instead of creating a new user.
        :param pulumi.Input[str] password: (Sensitive) Password of the user.
        :param pulumi.Input[str] password_reset: Arbitrary string to change to trigger a password update
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted,
               the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        :param pulumi.Input[str] status: Current status of the user.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OpensearchUserState.__new__(_OpensearchUserState)

        __props__.__dict__["acls"] = acls
        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["name"] = name
        __props__.__dict__["password"] = password
        __props__.__dict__["password_reset"] = password_reset
        __props__.__dict__["service_name"] = service_name
        __props__.__dict__["status"] = status
        return OpensearchUser(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def acls(self) -> pulumi.Output[Optional[Sequence['outputs.OpensearchUserAcl']]]:
        """
        Acls of the user.
        """
        return pulumi.get(self, "acls")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        Cluster ID.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Date of the creation of the user.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Username affected by this acl. A user named "avnadmin" is mapped with already created admin user and reset his password instead of creating a new user.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        (Sensitive) Password of the user.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="passwordReset")
    def password_reset(self) -> pulumi.Output[Optional[str]]:
        """
        Arbitrary string to change to trigger a password update
        """
        return pulumi.get(self, "password_reset")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        The id of the public cloud project. If omitted,
        the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Current status of the user.
        """
        return pulumi.get(self, "status")

