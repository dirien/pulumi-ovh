# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetServerBootsResult',
    'AwaitableGetServerBootsResult',
    'get_server_boots',
    'get_server_boots_output',
]

@pulumi.output_type
class GetServerBootsResult:
    """
    A collection of values returned by getServerBoots.
    """
    def __init__(__self__, boot_type=None, id=None, kernel=None, results=None, service_name=None):
        if boot_type and not isinstance(boot_type, str):
            raise TypeError("Expected argument 'boot_type' to be a str")
        pulumi.set(__self__, "boot_type", boot_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kernel and not isinstance(kernel, str):
            raise TypeError("Expected argument 'kernel' to be a str")
        pulumi.set(__self__, "kernel", kernel)
        if results and not isinstance(results, list):
            raise TypeError("Expected argument 'results' to be a list")
        pulumi.set(__self__, "results", results)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter(name="bootType")
    def boot_type(self) -> Optional[str]:
        return pulumi.get(self, "boot_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kernel(self) -> Optional[str]:
        return pulumi.get(self, "kernel")

    @property
    @pulumi.getter
    def results(self) -> Sequence[int]:
        """
        The list of dedicated server netboots.
        """
        return pulumi.get(self, "results")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        return pulumi.get(self, "service_name")


class AwaitableGetServerBootsResult(GetServerBootsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerBootsResult(
            boot_type=self.boot_type,
            id=self.id,
            kernel=self.kernel,
            results=self.results,
            service_name=self.service_name)


def get_server_boots(boot_type: Optional[str] = None,
                     kernel: Optional[str] = None,
                     service_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerBootsResult:
    """
    Use this data source to get the list of compatible netboots for a dedicated server associated with your OVHcloud Account.

    ## Example Usage


    :param str boot_type: Filter the value of bootType property (harddisk, rescue, ipxeCustomerScript, internal, network)
    :param str service_name: The internal name of your dedicated server.
    """
    __args__ = dict()
    __args__['bootType'] = boot_type
    __args__['kernel'] = kernel
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ovh:Dedicated/getServerBoots:getServerBoots', __args__, opts=opts, typ=GetServerBootsResult).value

    return AwaitableGetServerBootsResult(
        boot_type=pulumi.get(__ret__, 'boot_type'),
        id=pulumi.get(__ret__, 'id'),
        kernel=pulumi.get(__ret__, 'kernel'),
        results=pulumi.get(__ret__, 'results'),
        service_name=pulumi.get(__ret__, 'service_name'))


@_utilities.lift_output_func(get_server_boots)
def get_server_boots_output(boot_type: Optional[pulumi.Input[Optional[str]]] = None,
                            kernel: Optional[pulumi.Input[Optional[str]]] = None,
                            service_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerBootsResult]:
    """
    Use this data source to get the list of compatible netboots for a dedicated server associated with your OVHcloud Account.

    ## Example Usage


    :param str boot_type: Filter the value of bootType property (harddisk, rescue, ipxeCustomerScript, internal, network)
    :param str service_name: The internal name of your dedicated server.
    """
    ...
