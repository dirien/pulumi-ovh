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

__all__ = [
    'GetReferenceActionsResult',
    'AwaitableGetReferenceActionsResult',
    'get_reference_actions',
    'get_reference_actions_output',
]

@pulumi.output_type
class GetReferenceActionsResult:
    """
    A collection of values returned by getReferenceActions.
    """
    def __init__(__self__, actions=None, id=None, type=None):
        if actions and not isinstance(actions, list):
            raise TypeError("Expected argument 'actions' to be a list")
        pulumi.set(__self__, "actions", actions)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def actions(self) -> Sequence['outputs.GetReferenceActionsActionResult']:
        """
        List of actions
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


class AwaitableGetReferenceActionsResult(GetReferenceActionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReferenceActionsResult(
            actions=self.actions,
            id=self.id,
            type=self.type)


def get_reference_actions(type: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReferenceActionsResult:
    """
    Use this data source to list the IAM action associated with a resource type.


    :param str type: Kind of resource we want the actions for
    """
    __args__ = dict()
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ovh:Iam/getReferenceActions:getReferenceActions', __args__, opts=opts, typ=GetReferenceActionsResult).value

    return AwaitableGetReferenceActionsResult(
        actions=pulumi.get(__ret__, 'actions'),
        id=pulumi.get(__ret__, 'id'),
        type=pulumi.get(__ret__, 'type'))
def get_reference_actions_output(type: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReferenceActionsResult]:
    """
    Use this data source to list the IAM action associated with a resource type.


    :param str type: Kind of resource we want the actions for
    """
    __args__ = dict()
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ovh:Iam/getReferenceActions:getReferenceActions', __args__, opts=opts, typ=GetReferenceActionsResult)
    return __ret__.apply(lambda __response__: GetReferenceActionsResult(
        actions=pulumi.get(__response__, 'actions'),
        id=pulumi.get(__response__, 'id'),
        type=pulumi.get(__response__, 'type')))
