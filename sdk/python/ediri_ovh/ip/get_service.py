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
    'GetServiceResult',
    'AwaitableGetServiceResult',
    'get_service',
    'get_service_output',
]

@pulumi.output_type
class GetServiceResult:
    """
    A collection of values returned by getService.
    """
    def __init__(__self__, can_be_terminated=None, country=None, description=None, id=None, ip=None, organisation_id=None, routed_tos=None, service_name=None, type=None):
        if can_be_terminated and not isinstance(can_be_terminated, bool):
            raise TypeError("Expected argument 'can_be_terminated' to be a bool")
        pulumi.set(__self__, "can_be_terminated", can_be_terminated)
        if country and not isinstance(country, str):
            raise TypeError("Expected argument 'country' to be a str")
        pulumi.set(__self__, "country", country)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip and not isinstance(ip, str):
            raise TypeError("Expected argument 'ip' to be a str")
        pulumi.set(__self__, "ip", ip)
        if organisation_id and not isinstance(organisation_id, str):
            raise TypeError("Expected argument 'organisation_id' to be a str")
        pulumi.set(__self__, "organisation_id", organisation_id)
        if routed_tos and not isinstance(routed_tos, list):
            raise TypeError("Expected argument 'routed_tos' to be a list")
        pulumi.set(__self__, "routed_tos", routed_tos)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="canBeTerminated")
    def can_be_terminated(self) -> bool:
        """
        can be terminated
        """
        return pulumi.get(self, "can_be_terminated")

    @property
    @pulumi.getter
    def country(self) -> str:
        """
        country
        """
        return pulumi.get(self, "country")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Custom description on your ip
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ip(self) -> str:
        """
        ip block
        """
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter(name="organisationId")
    def organisation_id(self) -> str:
        """
        IP block organisation Id
        """
        return pulumi.get(self, "organisation_id")

    @property
    @pulumi.getter(name="routedTos")
    def routed_tos(self) -> Sequence['outputs.GetServiceRoutedToResult']:
        """
        Routage information
        """
        return pulumi.get(self, "routed_tos")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        """
        Service where ip is routed to
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Possible values for ip type (    "cdn", "cloud", "dedicated", "failover", "hosted_ssl", "housing", "loadBalancing", "mail", "overthebox", "pcc", "pci", "private", "vpn", "vps", "vrack", "xdsl")
        """
        return pulumi.get(self, "type")


class AwaitableGetServiceResult(GetServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceResult(
            can_be_terminated=self.can_be_terminated,
            country=self.country,
            description=self.description,
            id=self.id,
            ip=self.ip,
            organisation_id=self.organisation_id,
            routed_tos=self.routed_tos,
            service_name=self.service_name,
            type=self.type)


def get_service(service_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceResult:
    """
    Use this data source to retrieve information about an IP service.

    ## Example Usage


    :param str service_name: The service name
    """
    __args__ = dict()
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ovh:Ip/getService:getService', __args__, opts=opts, typ=GetServiceResult).value

    return AwaitableGetServiceResult(
        can_be_terminated=pulumi.get(__ret__, 'can_be_terminated'),
        country=pulumi.get(__ret__, 'country'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        ip=pulumi.get(__ret__, 'ip'),
        organisation_id=pulumi.get(__ret__, 'organisation_id'),
        routed_tos=pulumi.get(__ret__, 'routed_tos'),
        service_name=pulumi.get(__ret__, 'service_name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_service)
def get_service_output(service_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceResult]:
    """
    Use this data source to retrieve information about an IP service.

    ## Example Usage


    :param str service_name: The service name
    """
    ...
