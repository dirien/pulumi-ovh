# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['IdentityUserArgs', 'IdentityUser']

@pulumi.input_type
class IdentityUserArgs:
    def __init__(__self__, *,
                 email: pulumi.Input[str],
                 login: pulumi.Input[str],
                 password: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 group: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IdentityUser resource.
        :param pulumi.Input[str] email: User's email.
        :param pulumi.Input[str] login: User's login suffix.
        :param pulumi.Input[str] password: User's password.
        :param pulumi.Input[str] description: User description.
        :param pulumi.Input[str] group: User's group.
        """
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "login", login)
        pulumi.set(__self__, "password", password)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if group is not None:
            pulumi.set(__self__, "group", group)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Input[str]:
        """
        User's email.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: pulumi.Input[str]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def login(self) -> pulumi.Input[str]:
        """
        User's login suffix.
        """
        return pulumi.get(self, "login")

    @login.setter
    def login(self, value: pulumi.Input[str]):
        pulumi.set(self, "login", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        User's password.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        User description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[str]]:
        """
        User's group.
        """
        return pulumi.get(self, "group")

    @group.setter
    def group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group", value)


@pulumi.input_type
class _IdentityUserState:
    def __init__(__self__, *,
                 creation: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 last_update: Optional[pulumi.Input[str]] = None,
                 login: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 password_last_update: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 urn: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IdentityUser resources.
        :param pulumi.Input[str] creation: Creation date of this user.
        :param pulumi.Input[str] description: User description.
        :param pulumi.Input[str] email: User's email.
        :param pulumi.Input[str] group: User's group.
        :param pulumi.Input[str] last_update: Last update of this user.
        :param pulumi.Input[str] login: User's login suffix.
        :param pulumi.Input[str] password: User's password.
        :param pulumi.Input[str] password_last_update: When the user changed his password for the last time.
        :param pulumi.Input[str] status: Current user's status.
        :param pulumi.Input[str] urn: URN of the user, used when writing IAM policies
        """
        if creation is not None:
            pulumi.set(__self__, "creation", creation)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if group is not None:
            pulumi.set(__self__, "group", group)
        if last_update is not None:
            pulumi.set(__self__, "last_update", last_update)
        if login is not None:
            pulumi.set(__self__, "login", login)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if password_last_update is not None:
            pulumi.set(__self__, "password_last_update", password_last_update)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if urn is not None:
            pulumi.set(__self__, "urn", urn)

    @property
    @pulumi.getter
    def creation(self) -> Optional[pulumi.Input[str]]:
        """
        Creation date of this user.
        """
        return pulumi.get(self, "creation")

    @creation.setter
    def creation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "creation", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        User description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        User's email.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[str]]:
        """
        User's group.
        """
        return pulumi.get(self, "group")

    @group.setter
    def group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group", value)

    @property
    @pulumi.getter(name="lastUpdate")
    def last_update(self) -> Optional[pulumi.Input[str]]:
        """
        Last update of this user.
        """
        return pulumi.get(self, "last_update")

    @last_update.setter
    def last_update(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_update", value)

    @property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input[str]]:
        """
        User's login suffix.
        """
        return pulumi.get(self, "login")

    @login.setter
    def login(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "login", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        User's password.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="passwordLastUpdate")
    def password_last_update(self) -> Optional[pulumi.Input[str]]:
        """
        When the user changed his password for the last time.
        """
        return pulumi.get(self, "password_last_update")

    @password_last_update.setter
    def password_last_update(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password_last_update", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Current user's status.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def urn(self) -> Optional[pulumi.Input[str]]:
        """
        URN of the user, used when writing IAM policies
        """
        return pulumi.get(self, "urn")

    @urn.setter
    def urn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "urn", value)


class IdentityUser(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 login: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates an identity user.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: User description.
        :param pulumi.Input[str] email: User's email.
        :param pulumi.Input[str] group: User's group.
        :param pulumi.Input[str] login: User's login suffix.
        :param pulumi.Input[str] password: User's password.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IdentityUserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an identity user.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param IdentityUserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IdentityUserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 login: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IdentityUserArgs.__new__(IdentityUserArgs)

            __props__.__dict__["description"] = description
            if email is None and not opts.urn:
                raise TypeError("Missing required property 'email'")
            __props__.__dict__["email"] = email
            __props__.__dict__["group"] = group
            if login is None and not opts.urn:
                raise TypeError("Missing required property 'login'")
            __props__.__dict__["login"] = login
            if password is None and not opts.urn:
                raise TypeError("Missing required property 'password'")
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            __props__.__dict__["creation"] = None
            __props__.__dict__["last_update"] = None
            __props__.__dict__["password_last_update"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["urn"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(IdentityUser, __self__).__init__(
            'ovh:Me/identityUser:IdentityUser',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            creation: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            email: Optional[pulumi.Input[str]] = None,
            group: Optional[pulumi.Input[str]] = None,
            last_update: Optional[pulumi.Input[str]] = None,
            login: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            password_last_update: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            urn: Optional[pulumi.Input[str]] = None) -> 'IdentityUser':
        """
        Get an existing IdentityUser resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] creation: Creation date of this user.
        :param pulumi.Input[str] description: User description.
        :param pulumi.Input[str] email: User's email.
        :param pulumi.Input[str] group: User's group.
        :param pulumi.Input[str] last_update: Last update of this user.
        :param pulumi.Input[str] login: User's login suffix.
        :param pulumi.Input[str] password: User's password.
        :param pulumi.Input[str] password_last_update: When the user changed his password for the last time.
        :param pulumi.Input[str] status: Current user's status.
        :param pulumi.Input[str] urn: URN of the user, used when writing IAM policies
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IdentityUserState.__new__(_IdentityUserState)

        __props__.__dict__["creation"] = creation
        __props__.__dict__["description"] = description
        __props__.__dict__["email"] = email
        __props__.__dict__["group"] = group
        __props__.__dict__["last_update"] = last_update
        __props__.__dict__["login"] = login
        __props__.__dict__["password"] = password
        __props__.__dict__["password_last_update"] = password_last_update
        __props__.__dict__["status"] = status
        __props__.__dict__["urn"] = urn
        return IdentityUser(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def creation(self) -> pulumi.Output[str]:
        """
        Creation date of this user.
        """
        return pulumi.get(self, "creation")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        User description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        User's email.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def group(self) -> pulumi.Output[Optional[str]]:
        """
        User's group.
        """
        return pulumi.get(self, "group")

    @property
    @pulumi.getter(name="lastUpdate")
    def last_update(self) -> pulumi.Output[str]:
        """
        Last update of this user.
        """
        return pulumi.get(self, "last_update")

    @property
    @pulumi.getter
    def login(self) -> pulumi.Output[str]:
        """
        User's login suffix.
        """
        return pulumi.get(self, "login")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        User's password.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="passwordLastUpdate")
    def password_last_update(self) -> pulumi.Output[str]:
        """
        When the user changed his password for the last time.
        """
        return pulumi.get(self, "password_last_update")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Current user's status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def urn(self) -> pulumi.Output[str]:
        """
        URN of the user, used when writing IAM policies
        """
        return pulumi.get(self, "urn")

