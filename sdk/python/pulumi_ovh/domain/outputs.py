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
    'ZoneOrder',
    'ZoneOrderDetail',
    'ZonePlan',
    'ZonePlanConfiguration',
    'ZonePlanOption',
    'ZonePlanOptionConfiguration',
]

@pulumi.output_type
class ZoneOrder(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "expirationDate":
            suggest = "expiration_date"
        elif key == "orderId":
            suggest = "order_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ZoneOrder. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ZoneOrder.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ZoneOrder.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 date: Optional[str] = None,
                 details: Optional[Sequence['outputs.ZoneOrderDetail']] = None,
                 expiration_date: Optional[str] = None,
                 order_id: Optional[int] = None):
        """
        :param str date: date
        :param Sequence['ZoneOrderDetailArgs'] details: Information about a Bill entry
        :param str expiration_date: expiration date
        :param int order_id: order id
        """
        if date is not None:
            pulumi.set(__self__, "date", date)
        if details is not None:
            pulumi.set(__self__, "details", details)
        if expiration_date is not None:
            pulumi.set(__self__, "expiration_date", expiration_date)
        if order_id is not None:
            pulumi.set(__self__, "order_id", order_id)

    @property
    @pulumi.getter
    def date(self) -> Optional[str]:
        """
        date
        """
        return pulumi.get(self, "date")

    @property
    @pulumi.getter
    def details(self) -> Optional[Sequence['outputs.ZoneOrderDetail']]:
        """
        Information about a Bill entry
        """
        return pulumi.get(self, "details")

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[str]:
        """
        expiration date
        """
        return pulumi.get(self, "expiration_date")

    @property
    @pulumi.getter(name="orderId")
    def order_id(self) -> Optional[int]:
        """
        order id
        """
        return pulumi.get(self, "order_id")


@pulumi.output_type
class ZoneOrderDetail(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "orderDetailId":
            suggest = "order_detail_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ZoneOrderDetail. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ZoneOrderDetail.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ZoneOrderDetail.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 description: Optional[str] = None,
                 domain: Optional[str] = None,
                 order_detail_id: Optional[int] = None,
                 quantity: Optional[str] = None):
        """
        :param str description: description
        :param str domain: expiration date
        :param int order_detail_id: order detail id
        :param str quantity: quantity
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if order_detail_id is not None:
            pulumi.set(__self__, "order_detail_id", order_detail_id)
        if quantity is not None:
            pulumi.set(__self__, "quantity", quantity)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def domain(self) -> Optional[str]:
        """
        expiration date
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="orderDetailId")
    def order_detail_id(self) -> Optional[int]:
        """
        order detail id
        """
        return pulumi.get(self, "order_detail_id")

    @property
    @pulumi.getter
    def quantity(self) -> Optional[str]:
        """
        quantity
        """
        return pulumi.get(self, "quantity")


@pulumi.output_type
class ZonePlan(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "planCode":
            suggest = "plan_code"
        elif key == "pricingMode":
            suggest = "pricing_mode"
        elif key == "catalogName":
            suggest = "catalog_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ZonePlan. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ZonePlan.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ZonePlan.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 duration: str,
                 plan_code: str,
                 pricing_mode: str,
                 catalog_name: Optional[str] = None,
                 configurations: Optional[Sequence['outputs.ZonePlanConfiguration']] = None):
        """
        :param str duration: duration
        :param str plan_code: Plan code
        :param str pricing_mode: Pricing model identifier
        :param str catalog_name: Catalog name
        :param Sequence['ZonePlanConfigurationArgs'] configurations: Representation of a configuration item for personalizing product. 2 configurations are required : one for `zone` and one for `template`
        """
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "plan_code", plan_code)
        pulumi.set(__self__, "pricing_mode", pricing_mode)
        if catalog_name is not None:
            pulumi.set(__self__, "catalog_name", catalog_name)
        if configurations is not None:
            pulumi.set(__self__, "configurations", configurations)

    @property
    @pulumi.getter
    def duration(self) -> str:
        """
        duration
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter(name="planCode")
    def plan_code(self) -> str:
        """
        Plan code
        """
        return pulumi.get(self, "plan_code")

    @property
    @pulumi.getter(name="pricingMode")
    def pricing_mode(self) -> str:
        """
        Pricing model identifier
        """
        return pulumi.get(self, "pricing_mode")

    @property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> Optional[str]:
        """
        Catalog name
        """
        return pulumi.get(self, "catalog_name")

    @property
    @pulumi.getter
    def configurations(self) -> Optional[Sequence['outputs.ZonePlanConfiguration']]:
        """
        Representation of a configuration item for personalizing product. 2 configurations are required : one for `zone` and one for `template`
        """
        return pulumi.get(self, "configurations")


@pulumi.output_type
class ZonePlanConfiguration(dict):
    def __init__(__self__, *,
                 label: str,
                 value: str):
        """
        :param str label: Identifier of the resource : `zone` or `template`
        :param str value: For `zone`, the value is the zone name `myzone.example.com`. For `template`, the value can be `basic`, `minimized` or  `redirect` which is the same as `minimized` with additional entries for a redirect configuration.
        """
        pulumi.set(__self__, "label", label)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def label(self) -> str:
        """
        Identifier of the resource : `zone` or `template`
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        For `zone`, the value is the zone name `myzone.example.com`. For `template`, the value can be `basic`, `minimized` or  `redirect` which is the same as `minimized` with additional entries for a redirect configuration.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class ZonePlanOption(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "planCode":
            suggest = "plan_code"
        elif key == "pricingMode":
            suggest = "pricing_mode"
        elif key == "catalogName":
            suggest = "catalog_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ZonePlanOption. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ZonePlanOption.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ZonePlanOption.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 duration: str,
                 plan_code: str,
                 pricing_mode: str,
                 catalog_name: Optional[str] = None,
                 configurations: Optional[Sequence['outputs.ZonePlanOptionConfiguration']] = None):
        """
        :param str duration: duration
        :param str plan_code: Plan code
        :param str pricing_mode: Pricing model identifier
        :param str catalog_name: Catalog name
        :param Sequence['ZonePlanOptionConfigurationArgs'] configurations: Representation of a configuration item for personalizing product
        """
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "plan_code", plan_code)
        pulumi.set(__self__, "pricing_mode", pricing_mode)
        if catalog_name is not None:
            pulumi.set(__self__, "catalog_name", catalog_name)
        if configurations is not None:
            pulumi.set(__self__, "configurations", configurations)

    @property
    @pulumi.getter
    def duration(self) -> str:
        """
        duration
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter(name="planCode")
    def plan_code(self) -> str:
        """
        Plan code
        """
        return pulumi.get(self, "plan_code")

    @property
    @pulumi.getter(name="pricingMode")
    def pricing_mode(self) -> str:
        """
        Pricing model identifier
        """
        return pulumi.get(self, "pricing_mode")

    @property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> Optional[str]:
        """
        Catalog name
        """
        return pulumi.get(self, "catalog_name")

    @property
    @pulumi.getter
    def configurations(self) -> Optional[Sequence['outputs.ZonePlanOptionConfiguration']]:
        """
        Representation of a configuration item for personalizing product
        """
        return pulumi.get(self, "configurations")


@pulumi.output_type
class ZonePlanOptionConfiguration(dict):
    def __init__(__self__, *,
                 label: str,
                 value: str):
        """
        :param str label: Identifier of the resource
        :param str value: Path to the resource in API.OVH.COM
        """
        pulumi.set(__self__, "label", label)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def label(self) -> str:
        """
        Identifier of the resource
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Path to the resource in API.OVH.COM
        """
        return pulumi.get(self, "value")


