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
    'GetKubeNodesResult',
    'AwaitableGetKubeNodesResult',
    'get_kube_nodes',
    'get_kube_nodes_output',
]

@pulumi.output_type
class GetKubeNodesResult:
    """
    A collection of values returned by getKubeNodes.
    """
    def __init__(__self__, id=None, kube_id=None, nodes=None, service_name=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kube_id and not isinstance(kube_id, str):
            raise TypeError("Expected argument 'kube_id' to be a str")
        pulumi.set(__self__, "kube_id", kube_id)
        if nodes and not isinstance(nodes, list):
            raise TypeError("Expected argument 'nodes' to be a list")
        pulumi.set(__self__, "nodes", nodes)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kubeId")
    def kube_id(self) -> str:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "kube_id")

    @property
    @pulumi.getter
    def nodes(self) -> Sequence['outputs.GetKubeNodesNodeResult']:
        """
        List of all nodes composing the kubernetes cluster
        """
        return pulumi.get(self, "nodes")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "service_name")


class AwaitableGetKubeNodesResult(GetKubeNodesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKubeNodesResult(
            id=self.id,
            kube_id=self.kube_id,
            nodes=self.nodes,
            service_name=self.service_name)


def get_kube_nodes(kube_id: Optional[str] = None,
                   service_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKubeNodesResult:
    """
    Use this data source to get a list of OVHcloud Managed Kubernetes nodes.

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ovh as ovh

    nodes_kube_nodes = ovh.CloudProject.get_kube_nodes(service_name="XXXXXX",
        kube_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxx")
    pulumi.export("nodes", nodes_kube_nodes)
    ```
    <!--End PulumiCodeChooser -->


    :param str kube_id: The ID of the managed kubernetes cluster.
    :param str service_name: The id of the public cloud project. If omitted,
           the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
    """
    __args__ = dict()
    __args__['kubeId'] = kube_id
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ovh:CloudProject/getKubeNodes:getKubeNodes', __args__, opts=opts, typ=GetKubeNodesResult).value

    return AwaitableGetKubeNodesResult(
        id=pulumi.get(__ret__, 'id'),
        kube_id=pulumi.get(__ret__, 'kube_id'),
        nodes=pulumi.get(__ret__, 'nodes'),
        service_name=pulumi.get(__ret__, 'service_name'))


@_utilities.lift_output_func(get_kube_nodes)
def get_kube_nodes_output(kube_id: Optional[pulumi.Input[str]] = None,
                          service_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKubeNodesResult]:
    """
    Use this data source to get a list of OVHcloud Managed Kubernetes nodes.

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ovh as ovh

    nodes_kube_nodes = ovh.CloudProject.get_kube_nodes(service_name="XXXXXX",
        kube_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxx")
    pulumi.export("nodes", nodes_kube_nodes)
    ```
    <!--End PulumiCodeChooser -->


    :param str kube_id: The ID of the managed kubernetes cluster.
    :param str service_name: The id of the public cloud project. If omitted,
           the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
    """
    ...
