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

__all__ = ['ContainerRegistryIPRestrictionsRegistryArgs', 'ContainerRegistryIPRestrictionsRegistry']

@pulumi.input_type
class ContainerRegistryIPRestrictionsRegistryArgs:
    def __init__(__self__, *,
                 ip_restrictions: pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]],
                 registry_id: pulumi.Input[str],
                 service_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a ContainerRegistryIPRestrictionsRegistry resource.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]] ip_restrictions: IP restrictions applied on artifact manager component.
        :param pulumi.Input[str] registry_id: The id of the Managed Private Registry.
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        pulumi.set(__self__, "ip_restrictions", ip_restrictions)
        pulumi.set(__self__, "registry_id", registry_id)
        pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter(name="ipRestrictions")
    def ip_restrictions(self) -> pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]:
        """
        IP restrictions applied on artifact manager component.
        """
        return pulumi.get(self, "ip_restrictions")

    @ip_restrictions.setter
    def ip_restrictions(self, value: pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]):
        pulumi.set(self, "ip_restrictions", value)

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> pulumi.Input[str]:
        """
        The id of the Managed Private Registry.
        """
        return pulumi.get(self, "registry_id")

    @registry_id.setter
    def registry_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "registry_id", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)


@pulumi.input_type
class _ContainerRegistryIPRestrictionsRegistryState:
    def __init__(__self__, *,
                 ip_restrictions: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None,
                 registry_id: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ContainerRegistryIPRestrictionsRegistry resources.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]] ip_restrictions: IP restrictions applied on artifact manager component.
        :param pulumi.Input[str] registry_id: The id of the Managed Private Registry.
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        if ip_restrictions is not None:
            pulumi.set(__self__, "ip_restrictions", ip_restrictions)
        if registry_id is not None:
            pulumi.set(__self__, "registry_id", registry_id)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter(name="ipRestrictions")
    def ip_restrictions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]]:
        """
        IP restrictions applied on artifact manager component.
        """
        return pulumi.get(self, "ip_restrictions")

    @ip_restrictions.setter
    def ip_restrictions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]]):
        pulumi.set(self, "ip_restrictions", value)

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the Managed Private Registry.
        """
        return pulumi.get(self, "registry_id")

    @registry_id.setter
    def registry_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registry_id", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)


class ContainerRegistryIPRestrictionsRegistry(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip_restrictions: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None,
                 registry_id: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Apply IP restrictions container registry associated with a public cloud project on artifact manager component.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        registry = ovh.CloudProject.get_container_registry(service_name="XXXXXX",
            registry_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx")
        my_registry_iprestrictions = ovh.cloud_project.ContainerRegistryIPRestrictionsRegistry("my-registry-iprestrictions",
            service_name=ovh_cloud_project_containerregistry["registry"]["service_name"],
            registry_id=ovh_cloud_project_containerregistry["registry"]["id"],
            ip_restrictions=[{
                "ip_block": "xxx.xxx.xxx.xxx/xx",
                "description": "xxxxxxx",
            }])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]] ip_restrictions: IP restrictions applied on artifact manager component.
        :param pulumi.Input[str] registry_id: The id of the Managed Private Registry.
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ContainerRegistryIPRestrictionsRegistryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Apply IP restrictions container registry associated with a public cloud project on artifact manager component.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        registry = ovh.CloudProject.get_container_registry(service_name="XXXXXX",
            registry_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx")
        my_registry_iprestrictions = ovh.cloud_project.ContainerRegistryIPRestrictionsRegistry("my-registry-iprestrictions",
            service_name=ovh_cloud_project_containerregistry["registry"]["service_name"],
            registry_id=ovh_cloud_project_containerregistry["registry"]["id"],
            ip_restrictions=[{
                "ip_block": "xxx.xxx.xxx.xxx/xx",
                "description": "xxxxxxx",
            }])
        ```

        :param str resource_name: The name of the resource.
        :param ContainerRegistryIPRestrictionsRegistryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContainerRegistryIPRestrictionsRegistryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip_restrictions: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None,
                 registry_id: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ContainerRegistryIPRestrictionsRegistryArgs.__new__(ContainerRegistryIPRestrictionsRegistryArgs)

            if ip_restrictions is None and not opts.urn:
                raise TypeError("Missing required property 'ip_restrictions'")
            __props__.__dict__["ip_restrictions"] = ip_restrictions
            if registry_id is None and not opts.urn:
                raise TypeError("Missing required property 'registry_id'")
            __props__.__dict__["registry_id"] = registry_id
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
        super(ContainerRegistryIPRestrictionsRegistry, __self__).__init__(
            'ovh:CloudProject/containerRegistryIPRestrictionsRegistry:ContainerRegistryIPRestrictionsRegistry',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            ip_restrictions: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None,
            registry_id: Optional[pulumi.Input[str]] = None,
            service_name: Optional[pulumi.Input[str]] = None) -> 'ContainerRegistryIPRestrictionsRegistry':
        """
        Get an existing ContainerRegistryIPRestrictionsRegistry resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]] ip_restrictions: IP restrictions applied on artifact manager component.
        :param pulumi.Input[str] registry_id: The id of the Managed Private Registry.
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ContainerRegistryIPRestrictionsRegistryState.__new__(_ContainerRegistryIPRestrictionsRegistryState)

        __props__.__dict__["ip_restrictions"] = ip_restrictions
        __props__.__dict__["registry_id"] = registry_id
        __props__.__dict__["service_name"] = service_name
        return ContainerRegistryIPRestrictionsRegistry(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ipRestrictions")
    def ip_restrictions(self) -> pulumi.Output[Sequence[Mapping[str, str]]]:
        """
        IP restrictions applied on artifact manager component.
        """
        return pulumi.get(self, "ip_restrictions")

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> pulumi.Output[str]:
        """
        The id of the Managed Private Registry.
        """
        return pulumi.get(self, "registry_id")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        return pulumi.get(self, "service_name")

