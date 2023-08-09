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
from ._inputs import *

__all__ = ['TcpRouteArgs', 'TcpRoute']

@pulumi.input_type
class TcpRouteArgs:
    def __init__(__self__, *,
                 action: pulumi.Input['TcpRouteActionArgs'],
                 service_name: pulumi.Input[str],
                 display_name: Optional[pulumi.Input[str]] = None,
                 frontend_id: Optional[pulumi.Input[int]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a TcpRoute resource.
        :param pulumi.Input['TcpRouteActionArgs'] action: Action triggered when all rules match
        :param pulumi.Input[str] service_name: The internal name of your IP load balancing
        :param pulumi.Input[str] display_name: Human readable name for your route, this field is for you
        :param pulumi.Input[int] frontend_id: Route traffic for this frontend
        :param pulumi.Input[int] weight: Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "service_name", service_name)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if frontend_id is not None:
            pulumi.set(__self__, "frontend_id", frontend_id)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input['TcpRouteActionArgs']:
        """
        Action triggered when all rules match
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input['TcpRouteActionArgs']):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The internal name of your IP load balancing
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Human readable name for your route, this field is for you
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="frontendId")
    def frontend_id(self) -> Optional[pulumi.Input[int]]:
        """
        Route traffic for this frontend
        """
        return pulumi.get(self, "frontend_id")

    @frontend_id.setter
    def frontend_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "frontend_id", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        """
        Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


@pulumi.input_type
class _TcpRouteState:
    def __init__(__self__, *,
                 action: Optional[pulumi.Input['TcpRouteActionArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 frontend_id: Optional[pulumi.Input[int]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['TcpRouteRuleArgs']]]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering TcpRoute resources.
        :param pulumi.Input['TcpRouteActionArgs'] action: Action triggered when all rules match
        :param pulumi.Input[str] display_name: Human readable name for your route, this field is for you
        :param pulumi.Input[int] frontend_id: Route traffic for this frontend
        :param pulumi.Input[Sequence[pulumi.Input['TcpRouteRuleArgs']]] rules: List of rules to match to trigger action
        :param pulumi.Input[str] service_name: The internal name of your IP load balancing
        :param pulumi.Input[str] status: Route status. Routes in "ok" state are ready to operate
        :param pulumi.Input[int] weight: Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
        """
        if action is not None:
            pulumi.set(__self__, "action", action)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if frontend_id is not None:
            pulumi.set(__self__, "frontend_id", frontend_id)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input['TcpRouteActionArgs']]:
        """
        Action triggered when all rules match
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input['TcpRouteActionArgs']]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Human readable name for your route, this field is for you
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="frontendId")
    def frontend_id(self) -> Optional[pulumi.Input[int]]:
        """
        Route traffic for this frontend
        """
        return pulumi.get(self, "frontend_id")

    @frontend_id.setter
    def frontend_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "frontend_id", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TcpRouteRuleArgs']]]]:
        """
        List of rules to match to trigger action
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TcpRouteRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The internal name of your IP load balancing
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Route status. Routes in "ok" state are ready to operate
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        """
        Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


class TcpRoute(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[pulumi.InputType['TcpRouteActionArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 frontend_id: Optional[pulumi.Input[int]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Manage TCP route for a loadbalancer service

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['TcpRouteActionArgs']] action: Action triggered when all rules match
        :param pulumi.Input[str] display_name: Human readable name for your route, this field is for you
        :param pulumi.Input[int] frontend_id: Route traffic for this frontend
        :param pulumi.Input[str] service_name: The internal name of your IP load balancing
        :param pulumi.Input[int] weight: Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TcpRouteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manage TCP route for a loadbalancer service

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param TcpRouteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TcpRouteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[pulumi.InputType['TcpRouteActionArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 frontend_id: Optional[pulumi.Input[int]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TcpRouteArgs.__new__(TcpRouteArgs)

            if action is None and not opts.urn:
                raise TypeError("Missing required property 'action'")
            __props__.__dict__["action"] = action
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["frontend_id"] = frontend_id
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["weight"] = weight
            __props__.__dict__["rules"] = None
            __props__.__dict__["status"] = None
        super(TcpRoute, __self__).__init__(
            'ovh:IpLoadBalancing/tcpRoute:TcpRoute',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action: Optional[pulumi.Input[pulumi.InputType['TcpRouteActionArgs']]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            frontend_id: Optional[pulumi.Input[int]] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TcpRouteRuleArgs']]]]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            weight: Optional[pulumi.Input[int]] = None) -> 'TcpRoute':
        """
        Get an existing TcpRoute resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['TcpRouteActionArgs']] action: Action triggered when all rules match
        :param pulumi.Input[str] display_name: Human readable name for your route, this field is for you
        :param pulumi.Input[int] frontend_id: Route traffic for this frontend
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TcpRouteRuleArgs']]]] rules: List of rules to match to trigger action
        :param pulumi.Input[str] service_name: The internal name of your IP load balancing
        :param pulumi.Input[str] status: Route status. Routes in "ok" state are ready to operate
        :param pulumi.Input[int] weight: Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TcpRouteState.__new__(_TcpRouteState)

        __props__.__dict__["action"] = action
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["frontend_id"] = frontend_id
        __props__.__dict__["rules"] = rules
        __props__.__dict__["service_name"] = service_name
        __props__.__dict__["status"] = status
        __props__.__dict__["weight"] = weight
        return TcpRoute(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output['outputs.TcpRouteAction']:
        """
        Action triggered when all rules match
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Human readable name for your route, this field is for you
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="frontendId")
    def frontend_id(self) -> pulumi.Output[int]:
        """
        Route traffic for this frontend
        """
        return pulumi.get(self, "frontend_id")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.TcpRouteRule']]:
        """
        List of rules to match to trigger action
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        The internal name of your IP load balancing
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Route status. Routes in "ok" state are ready to operate
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Output[int]:
        """
        Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
        """
        return pulumi.get(self, "weight")

