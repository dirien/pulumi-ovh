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

__all__ = ['IpServiceArgs', 'IpService']

@pulumi.input_type
class IpServiceArgs:
    def __init__(__self__, *,
                 ovh_subsidiary: pulumi.Input[str],
                 plan: pulumi.Input['IpServicePlanArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 payment_mean: Optional[pulumi.Input[str]] = None,
                 plan_options: Optional[pulumi.Input[Sequence[pulumi.Input['IpServicePlanOptionArgs']]]] = None):
        """
        The set of arguments for constructing a IpService resource.
        :param pulumi.Input[str] ovh_subsidiary: OVHcloud Subsidiary
        :param pulumi.Input['IpServicePlanArgs'] plan: Product Plan to order
        :param pulumi.Input[str] description: Custom description on your ip.
        :param pulumi.Input[str] payment_mean: Ovh payment mode
        :param pulumi.Input[Sequence[pulumi.Input['IpServicePlanOptionArgs']]] plan_options: Product Plan to order
        """
        pulumi.set(__self__, "ovh_subsidiary", ovh_subsidiary)
        pulumi.set(__self__, "plan", plan)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if payment_mean is not None:
            warnings.warn("""This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""", DeprecationWarning)
            pulumi.log.warn("""payment_mean is deprecated: This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""")
        if payment_mean is not None:
            pulumi.set(__self__, "payment_mean", payment_mean)
        if plan_options is not None:
            pulumi.set(__self__, "plan_options", plan_options)

    @property
    @pulumi.getter(name="ovhSubsidiary")
    def ovh_subsidiary(self) -> pulumi.Input[str]:
        """
        OVHcloud Subsidiary
        """
        return pulumi.get(self, "ovh_subsidiary")

    @ovh_subsidiary.setter
    def ovh_subsidiary(self, value: pulumi.Input[str]):
        pulumi.set(self, "ovh_subsidiary", value)

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Input['IpServicePlanArgs']:
        """
        Product Plan to order
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: pulumi.Input['IpServicePlanArgs']):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Custom description on your ip.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="paymentMean")
    def payment_mean(self) -> Optional[pulumi.Input[str]]:
        """
        Ovh payment mode
        """
        warnings.warn("""This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""", DeprecationWarning)
        pulumi.log.warn("""payment_mean is deprecated: This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""")

        return pulumi.get(self, "payment_mean")

    @payment_mean.setter
    def payment_mean(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "payment_mean", value)

    @property
    @pulumi.getter(name="planOptions")
    def plan_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IpServicePlanOptionArgs']]]]:
        """
        Product Plan to order
        """
        return pulumi.get(self, "plan_options")

    @plan_options.setter
    def plan_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IpServicePlanOptionArgs']]]]):
        pulumi.set(self, "plan_options", value)


@pulumi.input_type
class _IpServiceState:
    def __init__(__self__, *,
                 can_be_terminated: Optional[pulumi.Input[bool]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ip: Optional[pulumi.Input[str]] = None,
                 orders: Optional[pulumi.Input[Sequence[pulumi.Input['IpServiceOrderArgs']]]] = None,
                 organisation_id: Optional[pulumi.Input[str]] = None,
                 ovh_subsidiary: Optional[pulumi.Input[str]] = None,
                 payment_mean: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input['IpServicePlanArgs']] = None,
                 plan_options: Optional[pulumi.Input[Sequence[pulumi.Input['IpServicePlanOptionArgs']]]] = None,
                 routed_tos: Optional[pulumi.Input[Sequence[pulumi.Input['IpServiceRoutedToArgs']]]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IpService resources.
        :param pulumi.Input[bool] can_be_terminated: can be terminated
        :param pulumi.Input[str] country: country
        :param pulumi.Input[str] description: Custom description on your ip.
        :param pulumi.Input[str] ip: ip block
        :param pulumi.Input[Sequence[pulumi.Input['IpServiceOrderArgs']]] orders: Details about an Order
        :param pulumi.Input[str] organisation_id: IP block organisation Id
        :param pulumi.Input[str] ovh_subsidiary: OVHcloud Subsidiary
        :param pulumi.Input[str] payment_mean: Ovh payment mode
        :param pulumi.Input['IpServicePlanArgs'] plan: Product Plan to order
        :param pulumi.Input[Sequence[pulumi.Input['IpServicePlanOptionArgs']]] plan_options: Product Plan to order
        :param pulumi.Input[Sequence[pulumi.Input['IpServiceRoutedToArgs']]] routed_tos: Routage information
        :param pulumi.Input[str] service_name: service name
        :param pulumi.Input[str] type: Possible values for ip type
        """
        if can_be_terminated is not None:
            pulumi.set(__self__, "can_be_terminated", can_be_terminated)
        if country is not None:
            pulumi.set(__self__, "country", country)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if ip is not None:
            pulumi.set(__self__, "ip", ip)
        if orders is not None:
            pulumi.set(__self__, "orders", orders)
        if organisation_id is not None:
            pulumi.set(__self__, "organisation_id", organisation_id)
        if ovh_subsidiary is not None:
            pulumi.set(__self__, "ovh_subsidiary", ovh_subsidiary)
        if payment_mean is not None:
            warnings.warn("""This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""", DeprecationWarning)
            pulumi.log.warn("""payment_mean is deprecated: This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""")
        if payment_mean is not None:
            pulumi.set(__self__, "payment_mean", payment_mean)
        if plan is not None:
            pulumi.set(__self__, "plan", plan)
        if plan_options is not None:
            pulumi.set(__self__, "plan_options", plan_options)
        if routed_tos is not None:
            pulumi.set(__self__, "routed_tos", routed_tos)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="canBeTerminated")
    def can_be_terminated(self) -> Optional[pulumi.Input[bool]]:
        """
        can be terminated
        """
        return pulumi.get(self, "can_be_terminated")

    @can_be_terminated.setter
    def can_be_terminated(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "can_be_terminated", value)

    @property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[str]]:
        """
        country
        """
        return pulumi.get(self, "country")

    @country.setter
    def country(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Custom description on your ip.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[str]]:
        """
        ip block
        """
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip", value)

    @property
    @pulumi.getter
    def orders(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IpServiceOrderArgs']]]]:
        """
        Details about an Order
        """
        return pulumi.get(self, "orders")

    @orders.setter
    def orders(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IpServiceOrderArgs']]]]):
        pulumi.set(self, "orders", value)

    @property
    @pulumi.getter(name="organisationId")
    def organisation_id(self) -> Optional[pulumi.Input[str]]:
        """
        IP block organisation Id
        """
        return pulumi.get(self, "organisation_id")

    @organisation_id.setter
    def organisation_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organisation_id", value)

    @property
    @pulumi.getter(name="ovhSubsidiary")
    def ovh_subsidiary(self) -> Optional[pulumi.Input[str]]:
        """
        OVHcloud Subsidiary
        """
        return pulumi.get(self, "ovh_subsidiary")

    @ovh_subsidiary.setter
    def ovh_subsidiary(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ovh_subsidiary", value)

    @property
    @pulumi.getter(name="paymentMean")
    def payment_mean(self) -> Optional[pulumi.Input[str]]:
        """
        Ovh payment mode
        """
        warnings.warn("""This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""", DeprecationWarning)
        pulumi.log.warn("""payment_mean is deprecated: This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""")

        return pulumi.get(self, "payment_mean")

    @payment_mean.setter
    def payment_mean(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "payment_mean", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input['IpServicePlanArgs']]:
        """
        Product Plan to order
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input['IpServicePlanArgs']]):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter(name="planOptions")
    def plan_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IpServicePlanOptionArgs']]]]:
        """
        Product Plan to order
        """
        return pulumi.get(self, "plan_options")

    @plan_options.setter
    def plan_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IpServicePlanOptionArgs']]]]):
        pulumi.set(self, "plan_options", value)

    @property
    @pulumi.getter(name="routedTos")
    def routed_tos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IpServiceRoutedToArgs']]]]:
        """
        Routage information
        """
        return pulumi.get(self, "routed_tos")

    @routed_tos.setter
    def routed_tos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IpServiceRoutedToArgs']]]]):
        pulumi.set(self, "routed_tos", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        service name
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Possible values for ip type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class IpService(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ovh_subsidiary: Optional[pulumi.Input[str]] = None,
                 payment_mean: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[pulumi.InputType['IpServicePlanArgs']]] = None,
                 plan_options: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpServicePlanOptionArgs']]]]] = None,
                 __props__=None):
        """
        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Custom description on your ip.
        :param pulumi.Input[str] ovh_subsidiary: OVHcloud Subsidiary
        :param pulumi.Input[str] payment_mean: Ovh payment mode
        :param pulumi.Input[pulumi.InputType['IpServicePlanArgs']] plan: Product Plan to order
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpServicePlanOptionArgs']]]] plan_options: Product Plan to order
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IpServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        :param str resource_name: The name of the resource.
        :param IpServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IpServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ovh_subsidiary: Optional[pulumi.Input[str]] = None,
                 payment_mean: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[pulumi.InputType['IpServicePlanArgs']]] = None,
                 plan_options: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpServicePlanOptionArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IpServiceArgs.__new__(IpServiceArgs)

            __props__.__dict__["description"] = description
            if ovh_subsidiary is None and not opts.urn:
                raise TypeError("Missing required property 'ovh_subsidiary'")
            __props__.__dict__["ovh_subsidiary"] = ovh_subsidiary
            if payment_mean is not None and not opts.urn:
                warnings.warn("""This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""", DeprecationWarning)
                pulumi.log.warn("""payment_mean is deprecated: This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""")
            __props__.__dict__["payment_mean"] = payment_mean
            if plan is None and not opts.urn:
                raise TypeError("Missing required property 'plan'")
            __props__.__dict__["plan"] = plan
            __props__.__dict__["plan_options"] = plan_options
            __props__.__dict__["can_be_terminated"] = None
            __props__.__dict__["country"] = None
            __props__.__dict__["ip"] = None
            __props__.__dict__["orders"] = None
            __props__.__dict__["organisation_id"] = None
            __props__.__dict__["routed_tos"] = None
            __props__.__dict__["service_name"] = None
            __props__.__dict__["type"] = None
        super(IpService, __self__).__init__(
            'ovh:Ip/ipService:IpService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            can_be_terminated: Optional[pulumi.Input[bool]] = None,
            country: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            ip: Optional[pulumi.Input[str]] = None,
            orders: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpServiceOrderArgs']]]]] = None,
            organisation_id: Optional[pulumi.Input[str]] = None,
            ovh_subsidiary: Optional[pulumi.Input[str]] = None,
            payment_mean: Optional[pulumi.Input[str]] = None,
            plan: Optional[pulumi.Input[pulumi.InputType['IpServicePlanArgs']]] = None,
            plan_options: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpServicePlanOptionArgs']]]]] = None,
            routed_tos: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpServiceRoutedToArgs']]]]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'IpService':
        """
        Get an existing IpService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] can_be_terminated: can be terminated
        :param pulumi.Input[str] country: country
        :param pulumi.Input[str] description: Custom description on your ip.
        :param pulumi.Input[str] ip: ip block
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpServiceOrderArgs']]]] orders: Details about an Order
        :param pulumi.Input[str] organisation_id: IP block organisation Id
        :param pulumi.Input[str] ovh_subsidiary: OVHcloud Subsidiary
        :param pulumi.Input[str] payment_mean: Ovh payment mode
        :param pulumi.Input[pulumi.InputType['IpServicePlanArgs']] plan: Product Plan to order
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpServicePlanOptionArgs']]]] plan_options: Product Plan to order
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpServiceRoutedToArgs']]]] routed_tos: Routage information
        :param pulumi.Input[str] service_name: service name
        :param pulumi.Input[str] type: Possible values for ip type
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IpServiceState.__new__(_IpServiceState)

        __props__.__dict__["can_be_terminated"] = can_be_terminated
        __props__.__dict__["country"] = country
        __props__.__dict__["description"] = description
        __props__.__dict__["ip"] = ip
        __props__.__dict__["orders"] = orders
        __props__.__dict__["organisation_id"] = organisation_id
        __props__.__dict__["ovh_subsidiary"] = ovh_subsidiary
        __props__.__dict__["payment_mean"] = payment_mean
        __props__.__dict__["plan"] = plan
        __props__.__dict__["plan_options"] = plan_options
        __props__.__dict__["routed_tos"] = routed_tos
        __props__.__dict__["service_name"] = service_name
        __props__.__dict__["type"] = type
        return IpService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="canBeTerminated")
    def can_be_terminated(self) -> pulumi.Output[bool]:
        """
        can be terminated
        """
        return pulumi.get(self, "can_be_terminated")

    @property
    @pulumi.getter
    def country(self) -> pulumi.Output[str]:
        """
        country
        """
        return pulumi.get(self, "country")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Custom description on your ip.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def ip(self) -> pulumi.Output[str]:
        """
        ip block
        """
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter
    def orders(self) -> pulumi.Output[Sequence['outputs.IpServiceOrder']]:
        """
        Details about an Order
        """
        return pulumi.get(self, "orders")

    @property
    @pulumi.getter(name="organisationId")
    def organisation_id(self) -> pulumi.Output[str]:
        """
        IP block organisation Id
        """
        return pulumi.get(self, "organisation_id")

    @property
    @pulumi.getter(name="ovhSubsidiary")
    def ovh_subsidiary(self) -> pulumi.Output[str]:
        """
        OVHcloud Subsidiary
        """
        return pulumi.get(self, "ovh_subsidiary")

    @property
    @pulumi.getter(name="paymentMean")
    def payment_mean(self) -> pulumi.Output[Optional[str]]:
        """
        Ovh payment mode
        """
        warnings.warn("""This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""", DeprecationWarning)
        pulumi.log.warn("""payment_mean is deprecated: This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""")

        return pulumi.get(self, "payment_mean")

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Output['outputs.IpServicePlan']:
        """
        Product Plan to order
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="planOptions")
    def plan_options(self) -> pulumi.Output[Optional[Sequence['outputs.IpServicePlanOption']]]:
        """
        Product Plan to order
        """
        return pulumi.get(self, "plan_options")

    @property
    @pulumi.getter(name="routedTos")
    def routed_tos(self) -> pulumi.Output[Sequence['outputs.IpServiceRoutedTo']]:
        """
        Routage information
        """
        return pulumi.get(self, "routed_tos")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        service name
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Possible values for ip type
        """
        return pulumi.get(self, "type")

