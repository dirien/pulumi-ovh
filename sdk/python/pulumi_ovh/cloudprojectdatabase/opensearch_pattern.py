# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['OpensearchPatternArgs', 'OpensearchPattern']

@pulumi.input_type
class OpensearchPatternArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 pattern: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 max_index_count: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a OpensearchPattern resource.
        :param pulumi.Input[str] cluster_id: Cluster ID.
        :param pulumi.Input[str] pattern: Pattern format.
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted,
               the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        :param pulumi.Input[int] max_index_count: Maximum number of index for this pattern.
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "pattern", pattern)
        pulumi.set(__self__, "service_name", service_name)
        if max_index_count is not None:
            pulumi.set(__self__, "max_index_count", max_index_count)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        Cluster ID.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def pattern(self) -> pulumi.Input[str]:
        """
        Pattern format.
        """
        return pulumi.get(self, "pattern")

    @pattern.setter
    def pattern(self, value: pulumi.Input[str]):
        pulumi.set(self, "pattern", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The id of the public cloud project. If omitted,
        the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="maxIndexCount")
    def max_index_count(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum number of index for this pattern.
        """
        return pulumi.get(self, "max_index_count")

    @max_index_count.setter
    def max_index_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_index_count", value)


@pulumi.input_type
class _OpensearchPatternState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 max_index_count: Optional[pulumi.Input[int]] = None,
                 pattern: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering OpensearchPattern resources.
        :param pulumi.Input[str] cluster_id: Cluster ID.
        :param pulumi.Input[int] max_index_count: Maximum number of index for this pattern.
        :param pulumi.Input[str] pattern: Pattern format.
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted,
               the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if max_index_count is not None:
            pulumi.set(__self__, "max_index_count", max_index_count)
        if pattern is not None:
            pulumi.set(__self__, "pattern", pattern)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        Cluster ID.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="maxIndexCount")
    def max_index_count(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum number of index for this pattern.
        """
        return pulumi.get(self, "max_index_count")

    @max_index_count.setter
    def max_index_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_index_count", value)

    @property
    @pulumi.getter
    def pattern(self) -> Optional[pulumi.Input[str]]:
        """
        Pattern format.
        """
        return pulumi.get(self, "pattern")

    @pattern.setter
    def pattern(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pattern", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the public cloud project. If omitted,
        the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)


class OpensearchPattern(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 max_index_count: Optional[pulumi.Input[int]] = None,
                 pattern: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a pattern for a opensearch cluster associated with a public cloud project.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumi_ovh as ovh

        opensearch = ovh.CloudProjectDatabase.get_database(service_name="XXX",
            engine="opensearch",
            id="ZZZ")
        pattern = ovh.cloud_project_database.OpensearchPattern("pattern",
            service_name=opensearch.service_name,
            cluster_id=opensearch.id,
            max_index_count=2,
            pattern="logs_*")
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        OVHcloud Managed opensearch clusters patterns can be imported using the `service_name`, `cluster_id` and `id` of the pattern, separated by "/" E.g.,

        bash

        ```sh
        $ pulumi import ovh:CloudProjectDatabase/opensearchPattern:OpensearchPattern my_pattern service_name/cluster_id/id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: Cluster ID.
        :param pulumi.Input[int] max_index_count: Maximum number of index for this pattern.
        :param pulumi.Input[str] pattern: Pattern format.
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted,
               the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OpensearchPatternArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a pattern for a opensearch cluster associated with a public cloud project.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumi_ovh as ovh

        opensearch = ovh.CloudProjectDatabase.get_database(service_name="XXX",
            engine="opensearch",
            id="ZZZ")
        pattern = ovh.cloud_project_database.OpensearchPattern("pattern",
            service_name=opensearch.service_name,
            cluster_id=opensearch.id,
            max_index_count=2,
            pattern="logs_*")
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        OVHcloud Managed opensearch clusters patterns can be imported using the `service_name`, `cluster_id` and `id` of the pattern, separated by "/" E.g.,

        bash

        ```sh
        $ pulumi import ovh:CloudProjectDatabase/opensearchPattern:OpensearchPattern my_pattern service_name/cluster_id/id
        ```

        :param str resource_name: The name of the resource.
        :param OpensearchPatternArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OpensearchPatternArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 max_index_count: Optional[pulumi.Input[int]] = None,
                 pattern: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OpensearchPatternArgs.__new__(OpensearchPatternArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["max_index_count"] = max_index_count
            if pattern is None and not opts.urn:
                raise TypeError("Missing required property 'pattern'")
            __props__.__dict__["pattern"] = pattern
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
        super(OpensearchPattern, __self__).__init__(
            'ovh:CloudProjectDatabase/opensearchPattern:OpensearchPattern',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            max_index_count: Optional[pulumi.Input[int]] = None,
            pattern: Optional[pulumi.Input[str]] = None,
            service_name: Optional[pulumi.Input[str]] = None) -> 'OpensearchPattern':
        """
        Get an existing OpensearchPattern resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: Cluster ID.
        :param pulumi.Input[int] max_index_count: Maximum number of index for this pattern.
        :param pulumi.Input[str] pattern: Pattern format.
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted,
               the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OpensearchPatternState.__new__(_OpensearchPatternState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["max_index_count"] = max_index_count
        __props__.__dict__["pattern"] = pattern
        __props__.__dict__["service_name"] = service_name
        return OpensearchPattern(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        Cluster ID.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="maxIndexCount")
    def max_index_count(self) -> pulumi.Output[Optional[int]]:
        """
        Maximum number of index for this pattern.
        """
        return pulumi.get(self, "max_index_count")

    @property
    @pulumi.getter
    def pattern(self) -> pulumi.Output[str]:
        """
        Pattern format.
        """
        return pulumi.get(self, "pattern")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        The id of the public cloud project. If omitted,
        the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        return pulumi.get(self, "service_name")

