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
    'InstallationTemplateCustomizationArgs',
    'InstallationTemplateCustomizationArgsDict',
    'InstallationTemplateInputArgs',
    'InstallationTemplateInputArgsDict',
]

MYPY = False

if not MYPY:
    class InstallationTemplateCustomizationArgsDict(TypedDict):
        custom_hostname: NotRequired[pulumi.Input[str]]
        """
        Set up the server using the provided hostname instead of the default hostname.
        """
elif False:
    InstallationTemplateCustomizationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class InstallationTemplateCustomizationArgs:
    def __init__(__self__, *,
                 custom_hostname: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] custom_hostname: Set up the server using the provided hostname instead of the default hostname.
        """
        if custom_hostname is not None:
            pulumi.set(__self__, "custom_hostname", custom_hostname)

    @property
    @pulumi.getter(name="customHostname")
    def custom_hostname(self) -> Optional[pulumi.Input[str]]:
        """
        Set up the server using the provided hostname instead of the default hostname.
        """
        return pulumi.get(self, "custom_hostname")

    @custom_hostname.setter
    def custom_hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_hostname", value)


if not MYPY:
    class InstallationTemplateInputArgsDict(TypedDict):
        default: NotRequired[pulumi.Input[str]]
        description: NotRequired[pulumi.Input[str]]
        """
        information about this template.
        """
        enums: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        mandatory: NotRequired[pulumi.Input[bool]]
        name: NotRequired[pulumi.Input[str]]
        type: NotRequired[pulumi.Input[str]]
elif False:
    InstallationTemplateInputArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class InstallationTemplateInputArgs:
    def __init__(__self__, *,
                 default: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enums: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 mandatory: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] description: information about this template.
        """
        if default is not None:
            pulumi.set(__self__, "default", default)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enums is not None:
            pulumi.set(__self__, "enums", enums)
        if mandatory is not None:
            pulumi.set(__self__, "mandatory", mandatory)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def default(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default")

    @default.setter
    def default(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        information about this template.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enums(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "enums")

    @enums.setter
    def enums(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "enums", value)

    @property
    @pulumi.getter
    def mandatory(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "mandatory")

    @mandatory.setter
    def mandatory(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "mandatory", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


