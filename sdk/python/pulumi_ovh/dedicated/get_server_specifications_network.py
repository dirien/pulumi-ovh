# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetServerSpecificationsNetworkResult',
    'AwaitableGetServerSpecificationsNetworkResult',
    'get_server_specifications_network',
    'get_server_specifications_network_output',
]

@pulumi.output_type
class GetServerSpecificationsNetworkResult:
    """
    A collection of values returned by getServerSpecificationsNetwork.
    """
    def __init__(__self__, bandwidth=None, connection_val=None, id=None, ola=None, routing=None, service_name=None, switching=None, traffic=None, vmac=None, vrack=None):
        if bandwidth and not isinstance(bandwidth, dict):
            raise TypeError("Expected argument 'bandwidth' to be a dict")
        pulumi.set(__self__, "bandwidth", bandwidth)
        if connection_val and not isinstance(connection_val, dict):
            raise TypeError("Expected argument 'connection_val' to be a dict")
        pulumi.set(__self__, "connection_val", connection_val)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ola and not isinstance(ola, dict):
            raise TypeError("Expected argument 'ola' to be a dict")
        pulumi.set(__self__, "ola", ola)
        if routing and not isinstance(routing, dict):
            raise TypeError("Expected argument 'routing' to be a dict")
        pulumi.set(__self__, "routing", routing)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if switching and not isinstance(switching, dict):
            raise TypeError("Expected argument 'switching' to be a dict")
        pulumi.set(__self__, "switching", switching)
        if traffic and not isinstance(traffic, dict):
            raise TypeError("Expected argument 'traffic' to be a dict")
        pulumi.set(__self__, "traffic", traffic)
        if vmac and not isinstance(vmac, dict):
            raise TypeError("Expected argument 'vmac' to be a dict")
        pulumi.set(__self__, "vmac", vmac)
        if vrack and not isinstance(vrack, dict):
            raise TypeError("Expected argument 'vrack' to be a dict")
        pulumi.set(__self__, "vrack", vrack)

    @property
    @pulumi.getter
    def bandwidth(self) -> 'outputs.GetServerSpecificationsNetworkBandwidthResult':
        """
        vrack bandwidth limitation
        """
        return pulumi.get(self, "bandwidth")

    @property
    @pulumi.getter(name="connectionVal")
    def connection_val(self) -> 'outputs.GetServerSpecificationsNetworkConnectionValResult':
        """
        Network connection flow rate
        """
        return pulumi.get(self, "connection_val")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ola(self) -> 'outputs.GetServerSpecificationsNetworkOlaResult':
        """
        OLA details
        """
        return pulumi.get(self, "ola")

    @property
    @pulumi.getter
    def routing(self) -> 'outputs.GetServerSpecificationsNetworkRoutingResult':
        """
        Routing details
        """
        return pulumi.get(self, "routing")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def switching(self) -> 'outputs.GetServerSpecificationsNetworkSwitchingResult':
        """
        Switching details
        """
        return pulumi.get(self, "switching")

    @property
    @pulumi.getter
    def traffic(self) -> 'outputs.GetServerSpecificationsNetworkTrafficResult':
        """
        Traffic details
        """
        return pulumi.get(self, "traffic")

    @property
    @pulumi.getter
    def vmac(self) -> 'outputs.GetServerSpecificationsNetworkVmacResult':
        """
        VMAC information for this dedicated server
        """
        return pulumi.get(self, "vmac")

    @property
    @pulumi.getter
    def vrack(self) -> 'outputs.GetServerSpecificationsNetworkVrackResult':
        """
        vRack details
        """
        return pulumi.get(self, "vrack")


class AwaitableGetServerSpecificationsNetworkResult(GetServerSpecificationsNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerSpecificationsNetworkResult(
            bandwidth=self.bandwidth,
            connection_val=self.connection_val,
            id=self.id,
            ola=self.ola,
            routing=self.routing,
            service_name=self.service_name,
            switching=self.switching,
            traffic=self.traffic,
            vmac=self.vmac,
            vrack=self.vrack)


def get_server_specifications_network(service_name: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerSpecificationsNetworkResult:
    """
    Use this data source to get the network information about a dedicated server associated with your OVHcloud Account.

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ovh as ovh

    spec = ovh.Dedicated.get_server_specifications_network(service_name="myserver")
    ```
    <!--End PulumiCodeChooser -->


    :param str service_name: The internal name of your dedicated server.
    """
    __args__ = dict()
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ovh:Dedicated/getServerSpecificationsNetwork:getServerSpecificationsNetwork', __args__, opts=opts, typ=GetServerSpecificationsNetworkResult).value

    return AwaitableGetServerSpecificationsNetworkResult(
        bandwidth=pulumi.get(__ret__, 'bandwidth'),
        connection_val=pulumi.get(__ret__, 'connection_val'),
        id=pulumi.get(__ret__, 'id'),
        ola=pulumi.get(__ret__, 'ola'),
        routing=pulumi.get(__ret__, 'routing'),
        service_name=pulumi.get(__ret__, 'service_name'),
        switching=pulumi.get(__ret__, 'switching'),
        traffic=pulumi.get(__ret__, 'traffic'),
        vmac=pulumi.get(__ret__, 'vmac'),
        vrack=pulumi.get(__ret__, 'vrack'))


@_utilities.lift_output_func(get_server_specifications_network)
def get_server_specifications_network_output(service_name: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerSpecificationsNetworkResult]:
    """
    Use this data source to get the network information about a dedicated server associated with your OVHcloud Account.

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ovh as ovh

    spec = ovh.Dedicated.get_server_specifications_network(service_name="myserver")
    ```
    <!--End PulumiCodeChooser -->


    :param str service_name: The internal name of your dedicated server.
    """
    ...
