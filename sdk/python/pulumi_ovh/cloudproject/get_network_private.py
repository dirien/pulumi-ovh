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
    'GetNetworkPrivateResult',
    'AwaitableGetNetworkPrivateResult',
    'get_network_private',
    'get_network_private_output',
]

@pulumi.output_type
class GetNetworkPrivateResult:
    """
    A collection of values returned by getNetworkPrivate.
    """
    def __init__(__self__, id=None, name=None, network_id=None, regions=None, service_name=None, status=None, type=None, vlan_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_id and not isinstance(network_id, str):
            raise TypeError("Expected argument 'network_id' to be a str")
        pulumi.set(__self__, "network_id", network_id)
        if regions and not isinstance(regions, list):
            raise TypeError("Expected argument 'regions' to be a list")
        pulumi.set(__self__, "regions", regions)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vlan_id and not isinstance(vlan_id, float):
            raise TypeError("Expected argument 'vlan_id' to be a float")
        pulumi.set(__self__, "vlan_id", vlan_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the network
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> str:
        """
        ID of the network
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter
    def regions(self) -> Sequence['outputs.GetNetworkPrivateRegionResult']:
        """
        Information about the private network in the openstack region
        """
        return pulumi.get(self, "regions")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        """
        ID of the public cloud project
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the network
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the network
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> float:
        """
        VLAN ID of the network
        """
        return pulumi.get(self, "vlan_id")


class AwaitableGetNetworkPrivateResult(GetNetworkPrivateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkPrivateResult(
            id=self.id,
            name=self.name,
            network_id=self.network_id,
            regions=self.regions,
            service_name=self.service_name,
            status=self.status,
            type=self.type,
            vlan_id=self.vlan_id)


def get_network_private(network_id: Optional[str] = None,
                        service_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkPrivateResult:
    """
    Get the details of a public cloud project private network.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    private_network_private = ovh.CloudProject.get_network_private(service_name="XXXXXX",
        network_id="XXX")
    pulumi.export("private", private_network_private)
    ```


    :param str network_id: ID of the network
    :param str service_name: The ID of the public cloud project.
    """
    __args__ = dict()
    __args__['networkId'] = network_id
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ovh:CloudProject/getNetworkPrivate:getNetworkPrivate', __args__, opts=opts, typ=GetNetworkPrivateResult).value

    return AwaitableGetNetworkPrivateResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        network_id=pulumi.get(__ret__, 'network_id'),
        regions=pulumi.get(__ret__, 'regions'),
        service_name=pulumi.get(__ret__, 'service_name'),
        status=pulumi.get(__ret__, 'status'),
        type=pulumi.get(__ret__, 'type'),
        vlan_id=pulumi.get(__ret__, 'vlan_id'))
def get_network_private_output(network_id: Optional[pulumi.Input[str]] = None,
                               service_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkPrivateResult]:
    """
    Get the details of a public cloud project private network.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    private_network_private = ovh.CloudProject.get_network_private(service_name="XXXXXX",
        network_id="XXX")
    pulumi.export("private", private_network_private)
    ```


    :param str network_id: ID of the network
    :param str service_name: The ID of the public cloud project.
    """
    __args__ = dict()
    __args__['networkId'] = network_id
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ovh:CloudProject/getNetworkPrivate:getNetworkPrivate', __args__, opts=opts, typ=GetNetworkPrivateResult)
    return __ret__.apply(lambda __response__: GetNetworkPrivateResult(
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        network_id=pulumi.get(__response__, 'network_id'),
        regions=pulumi.get(__response__, 'regions'),
        service_name=pulumi.get(__response__, 'service_name'),
        status=pulumi.get(__response__, 'status'),
        type=pulumi.get(__response__, 'type'),
        vlan_id=pulumi.get(__response__, 'vlan_id')))
