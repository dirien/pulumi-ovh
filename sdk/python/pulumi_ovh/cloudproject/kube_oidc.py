# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['KubeOidcArgs', 'KubeOidc']

@pulumi.input_type
class KubeOidcArgs:
    def __init__(__self__, *,
                 client_id: pulumi.Input[str],
                 issuer_url: pulumi.Input[str],
                 kube_id: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 oidc_ca_content: Optional[pulumi.Input[str]] = None,
                 oidc_groups_claims: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 oidc_groups_prefix: Optional[pulumi.Input[str]] = None,
                 oidc_required_claims: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 oidc_signing_algs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 oidc_username_claim: Optional[pulumi.Input[str]] = None,
                 oidc_username_prefix: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a KubeOidc resource.
        :param pulumi.Input[str] client_id: The OIDC client ID.
        :param pulumi.Input[str] issuer_url: The OIDC issuer url.
        :param pulumi.Input[str] kube_id: The ID of the managed kubernetes cluster. **Changing this value recreates the resource.**
        :param pulumi.Input[str] service_name: The ID of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "issuer_url", issuer_url)
        pulumi.set(__self__, "kube_id", kube_id)
        pulumi.set(__self__, "service_name", service_name)
        if oidc_ca_content is not None:
            pulumi.set(__self__, "oidc_ca_content", oidc_ca_content)
        if oidc_groups_claims is not None:
            pulumi.set(__self__, "oidc_groups_claims", oidc_groups_claims)
        if oidc_groups_prefix is not None:
            pulumi.set(__self__, "oidc_groups_prefix", oidc_groups_prefix)
        if oidc_required_claims is not None:
            pulumi.set(__self__, "oidc_required_claims", oidc_required_claims)
        if oidc_signing_algs is not None:
            pulumi.set(__self__, "oidc_signing_algs", oidc_signing_algs)
        if oidc_username_claim is not None:
            pulumi.set(__self__, "oidc_username_claim", oidc_username_claim)
        if oidc_username_prefix is not None:
            pulumi.set(__self__, "oidc_username_prefix", oidc_username_prefix)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[str]:
        """
        The OIDC client ID.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="issuerUrl")
    def issuer_url(self) -> pulumi.Input[str]:
        """
        The OIDC issuer url.
        """
        return pulumi.get(self, "issuer_url")

    @issuer_url.setter
    def issuer_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "issuer_url", value)

    @property
    @pulumi.getter(name="kubeId")
    def kube_id(self) -> pulumi.Input[str]:
        """
        The ID of the managed kubernetes cluster. **Changing this value recreates the resource.**
        """
        return pulumi.get(self, "kube_id")

    @kube_id.setter
    def kube_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "kube_id", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The ID of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="oidcCaContent")
    def oidc_ca_content(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "oidc_ca_content")

    @oidc_ca_content.setter
    def oidc_ca_content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_ca_content", value)

    @property
    @pulumi.getter(name="oidcGroupsClaims")
    def oidc_groups_claims(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "oidc_groups_claims")

    @oidc_groups_claims.setter
    def oidc_groups_claims(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "oidc_groups_claims", value)

    @property
    @pulumi.getter(name="oidcGroupsPrefix")
    def oidc_groups_prefix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "oidc_groups_prefix")

    @oidc_groups_prefix.setter
    def oidc_groups_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_groups_prefix", value)

    @property
    @pulumi.getter(name="oidcRequiredClaims")
    def oidc_required_claims(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "oidc_required_claims")

    @oidc_required_claims.setter
    def oidc_required_claims(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "oidc_required_claims", value)

    @property
    @pulumi.getter(name="oidcSigningAlgs")
    def oidc_signing_algs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "oidc_signing_algs")

    @oidc_signing_algs.setter
    def oidc_signing_algs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "oidc_signing_algs", value)

    @property
    @pulumi.getter(name="oidcUsernameClaim")
    def oidc_username_claim(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "oidc_username_claim")

    @oidc_username_claim.setter
    def oidc_username_claim(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_username_claim", value)

    @property
    @pulumi.getter(name="oidcUsernamePrefix")
    def oidc_username_prefix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "oidc_username_prefix")

    @oidc_username_prefix.setter
    def oidc_username_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_username_prefix", value)


@pulumi.input_type
class _KubeOidcState:
    def __init__(__self__, *,
                 client_id: Optional[pulumi.Input[str]] = None,
                 issuer_url: Optional[pulumi.Input[str]] = None,
                 kube_id: Optional[pulumi.Input[str]] = None,
                 oidc_ca_content: Optional[pulumi.Input[str]] = None,
                 oidc_groups_claims: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 oidc_groups_prefix: Optional[pulumi.Input[str]] = None,
                 oidc_required_claims: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 oidc_signing_algs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 oidc_username_claim: Optional[pulumi.Input[str]] = None,
                 oidc_username_prefix: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering KubeOidc resources.
        :param pulumi.Input[str] client_id: The OIDC client ID.
        :param pulumi.Input[str] issuer_url: The OIDC issuer url.
        :param pulumi.Input[str] kube_id: The ID of the managed kubernetes cluster. **Changing this value recreates the resource.**
        :param pulumi.Input[str] service_name: The ID of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        """
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if issuer_url is not None:
            pulumi.set(__self__, "issuer_url", issuer_url)
        if kube_id is not None:
            pulumi.set(__self__, "kube_id", kube_id)
        if oidc_ca_content is not None:
            pulumi.set(__self__, "oidc_ca_content", oidc_ca_content)
        if oidc_groups_claims is not None:
            pulumi.set(__self__, "oidc_groups_claims", oidc_groups_claims)
        if oidc_groups_prefix is not None:
            pulumi.set(__self__, "oidc_groups_prefix", oidc_groups_prefix)
        if oidc_required_claims is not None:
            pulumi.set(__self__, "oidc_required_claims", oidc_required_claims)
        if oidc_signing_algs is not None:
            pulumi.set(__self__, "oidc_signing_algs", oidc_signing_algs)
        if oidc_username_claim is not None:
            pulumi.set(__self__, "oidc_username_claim", oidc_username_claim)
        if oidc_username_prefix is not None:
            pulumi.set(__self__, "oidc_username_prefix", oidc_username_prefix)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OIDC client ID.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="issuerUrl")
    def issuer_url(self) -> Optional[pulumi.Input[str]]:
        """
        The OIDC issuer url.
        """
        return pulumi.get(self, "issuer_url")

    @issuer_url.setter
    def issuer_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "issuer_url", value)

    @property
    @pulumi.getter(name="kubeId")
    def kube_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the managed kubernetes cluster. **Changing this value recreates the resource.**
        """
        return pulumi.get(self, "kube_id")

    @kube_id.setter
    def kube_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kube_id", value)

    @property
    @pulumi.getter(name="oidcCaContent")
    def oidc_ca_content(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "oidc_ca_content")

    @oidc_ca_content.setter
    def oidc_ca_content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_ca_content", value)

    @property
    @pulumi.getter(name="oidcGroupsClaims")
    def oidc_groups_claims(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "oidc_groups_claims")

    @oidc_groups_claims.setter
    def oidc_groups_claims(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "oidc_groups_claims", value)

    @property
    @pulumi.getter(name="oidcGroupsPrefix")
    def oidc_groups_prefix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "oidc_groups_prefix")

    @oidc_groups_prefix.setter
    def oidc_groups_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_groups_prefix", value)

    @property
    @pulumi.getter(name="oidcRequiredClaims")
    def oidc_required_claims(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "oidc_required_claims")

    @oidc_required_claims.setter
    def oidc_required_claims(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "oidc_required_claims", value)

    @property
    @pulumi.getter(name="oidcSigningAlgs")
    def oidc_signing_algs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "oidc_signing_algs")

    @oidc_signing_algs.setter
    def oidc_signing_algs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "oidc_signing_algs", value)

    @property
    @pulumi.getter(name="oidcUsernameClaim")
    def oidc_username_claim(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "oidc_username_claim")

    @oidc_username_claim.setter
    def oidc_username_claim(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_username_claim", value)

    @property
    @pulumi.getter(name="oidcUsernamePrefix")
    def oidc_username_prefix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "oidc_username_prefix")

    @oidc_username_prefix.setter
    def oidc_username_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_username_prefix", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)


class KubeOidc(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 issuer_url: Optional[pulumi.Input[str]] = None,
                 kube_id: Optional[pulumi.Input[str]] = None,
                 oidc_ca_content: Optional[pulumi.Input[str]] = None,
                 oidc_groups_claims: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 oidc_groups_prefix: Optional[pulumi.Input[str]] = None,
                 oidc_required_claims: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 oidc_signing_algs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 oidc_username_claim: Optional[pulumi.Input[str]] = None,
                 oidc_username_prefix: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates an OIDC configuration in an OVHcloud Managed Kubernetes cluster.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumi_ovh as ovh

        my_oidc = ovh.cloud_project.KubeOidc("my-oidc",
            service_name=var["projectid"],
            kube_id=ovh_cloud_project_kube["mykube"]["id"],
            client_id="xxx",
            issuer_url="https://ovh.com",
            oidc_username_claim="an-email",
            oidc_username_prefix="ovh:",
            oidc_groups_claims=["groups"],
            oidc_groups_prefix="ovh:",
            oidc_required_claims=["claim1=val1"],
            oidc_signing_algs=["RS512"],
            oidc_ca_content="LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUZhekNDQTFPZ0F3SUJBZ0lVYm9YRkZrL1hCQmdQUUI4UHlqbkttUGVWekNjd0RRWUpLb1pJaHZjTkFRRUwKQlFBd1JURUxNQWtHQTFVRUJoTUNRVlV4RXpBUkJnTlZCQWdNQ2xOdmJXVXRVM1JoZEdVeElUQWZCZ05WQkFvTQpHRWx1ZEdWeWJtVjBJRmRwWkdkcGRITWdVSFI1SUV4MFpEQWVGdzB5TWpFd01UUXdOalE0TlROYUZ3MHlNekV3Ck1UUXdOalE0TlROYU1FVXhDekFKQmdOVkJBWVRBa0ZWTVJNd0VRWURWUVFJREFwVGIyMWxMVk4wWVhSbE1TRXcKSHdZRFZRUUtEQmhKYm5SbGNtNWxkQ0JYYVdSbmFYUnpJRkIwZVNCTWRHUXdnZ0lpTUEwR0NTcUdTSWIzRFFFQgpBUVVBQTRJQ0R3QXdnZ0lLQW9JQ0FRQytPMk53bGx2QTQyT05SUHMyZWlqTUp2UHhpN21RblVSS3FrOHJEV1VkCkwzZU0yM1JXeVhtS1AydDQ5Zi9LVGsweEZNVStOSTUzTEhwWmh6N3NpK3dEUFUvWWZWSS9rQmZsRm8zeVZCMSsKZWdCSnpyNGIrQ3FoaWlCUkh0Vm5LblFKUmdvOVJjVkxhRm82UEY0N1V0UWJ2bWVuNGdERnExVkYwVHhUdnFMdwpIMzRZL0U2QUJsSlZnWFBzaWQzNm54eTErNnlKV05vRXNVekFiekpWMHhzTGhxc2hOazA0TWx4YnBhcG1XcEUxCmFFMHRIZGpjUlI3Y1dTRUUwMnRSQzNYL2tSNjBKb3MxR0N0Y0ZQTTVIN3NjOFBXNFRUem1EWWhOeDRiVjV4T28KU0xYRnI5ajBzZEgxbm1wSlI1dWxJT2dPTWV3MHA2d3JOYVV2MGpxc1hzdVdqMVpxdTRLRi81aEQ3azVhRlhKNQpjYWNTUi9mRWxreW1uZis0eHZFOG8wdkRWNFR5NHo3K3lSS1U0clZvZFNBZWZIN3lqeitLV1RRck96L0lHU2NwCmV1YTdqV0hRMDdMYWxyTjV2b0tFaU1JM3MrWjhzeUdVUGVyYXQwdzJMWlc3NnhxVGl4R002clZxUldxVlQ4L1oKQTJMMEc4WGRvNTZvV2lFYVF5RkJtRDFnMXU2UEsvTmFGVDI1L2tTNWJ1dnF5L1dLVGt0UVNhNHNZc1ZLbUlQTQp0Zys0NUZ2aFErNkRuQzd0TmVnaTZDTkdTb0w0R1dPOEE5UDZRNjE5RkJJZ1VjcGpFMTgvUHpQOEJmcTAxajhnCjZmdm1jNkVPMkxHVHhDcW1DbVp0TnI3OCtQaUxkMHZIY3pqY3E3NzhiNW5WRXRpUVNRQkUyb0ozTVlIZUFIUUkKYVFJREFRQUJvMU13VVRBZEJnTlZIUTRFRmdRVUpaMUhlVmx1U3pjY0U2NEZQYWtuNkRBWnhmSXdId1lEVlIwagpCQmd3Rm9BVUpaMUhlVmx1U3pjY0U2NEZQYWtuNkRBWnhmSXdEd1lEVlIwVEFRSC9CQVV3QXdFQi96QU5CZ2txCmhraUc5dzBCQVFzRkFBT0NBZ0VBQlhNSlU2MjJZVFZVNnZ1K2svNnkwMGNaWlRmVnZtdVJMOXhTcWxVM0I1QmQKVWdyVWx1TmdjN2dhUUlrYzkvWmh2MnhNd0xxUldMWEhiTWx1NkNvdkNiVTVpeWt0NHVWMnl5UzlZYWhmVVRNVQo3TVE0WFRta2hoS0dGbWZBQ2QzTUVwRE55T3hmWXh0UVBwM1NZT2IxRGFKMmUwY01Gc081bytORGQ5aFVBVzFoCjFLMjMwQnZzYldYYVo4MStIdTU4U1BsYTM5R3FMTG85MzR6dEs4WkRWNFRGTVJxMnNVQ1cxcWFidDh5ejd2RzAKSGV3dXdxelRwR1lTSFI1U0ZvMm45R0xKVUN4SnhxcDlOWVJjMlhUdXRUdkJESzVPMXFZZEJaQzd6cmcxSnczawp2SjI4UGx2TzBQRE42ZVlUdElJdC9yU05ZbW56eVVNRTRYREt0di9KRitLZWZNSWxDTkpzZDRHYXVTdlo5M1NOClhINmcrNEZvRkp4UzNxRmZ0WEc4czNRNnppNzNLRzh5UHZVNHU0WmZNRGd2aG92L0V5YkNLWUpFdVVZSlJWNGEKbmc3cWh3NDBabXQ0eWNCRzU5a2tFSGhNYWtxTWpPaUNkV2x4MEVjZXIxcEFGT1pqN3o1NktURXIxa0ZwUHVaRApjVER5SnNwTjh6dm9CQ0l1ancvQjR6S3kyWStOQitRR1p3dXhyTk9mRGR6ek9yQUE1Ym9OS2gwUUh4c0RxNTExClFaU3hCR21EcGJzN2QzMUQvQll3WEhIUWdwb3FoVUU5dFBGSThpN0pkM2FyeXZCdHlnTWlxSmt1VlRFVk1Ta0UKNTZ0VnFsMjlXenFhRXNrbDN3VUlmczVKKzN3RzRPcWNxRDdXaGQxWUtnc0VUMjdFTWlqVXZIYzQ4TXE0bU1rPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==")
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        OVHcloud Managed Kubernetes Service cluster OIDC can be imported using the tenant `service_name` and cluster id `kube_id` separated by "/" E.g.,

        bash

        ```sh
        $ pulumi import ovh:CloudProject/kubeOidc:KubeOidc my-oidc service_name/kube_id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_id: The OIDC client ID.
        :param pulumi.Input[str] issuer_url: The OIDC issuer url.
        :param pulumi.Input[str] kube_id: The ID of the managed kubernetes cluster. **Changing this value recreates the resource.**
        :param pulumi.Input[str] service_name: The ID of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KubeOidcArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an OIDC configuration in an OVHcloud Managed Kubernetes cluster.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumi_ovh as ovh

        my_oidc = ovh.cloud_project.KubeOidc("my-oidc",
            service_name=var["projectid"],
            kube_id=ovh_cloud_project_kube["mykube"]["id"],
            client_id="xxx",
            issuer_url="https://ovh.com",
            oidc_username_claim="an-email",
            oidc_username_prefix="ovh:",
            oidc_groups_claims=["groups"],
            oidc_groups_prefix="ovh:",
            oidc_required_claims=["claim1=val1"],
            oidc_signing_algs=["RS512"],
            oidc_ca_content="LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUZhekNDQTFPZ0F3SUJBZ0lVYm9YRkZrL1hCQmdQUUI4UHlqbkttUGVWekNjd0RRWUpLb1pJaHZjTkFRRUwKQlFBd1JURUxNQWtHQTFVRUJoTUNRVlV4RXpBUkJnTlZCQWdNQ2xOdmJXVXRVM1JoZEdVeElUQWZCZ05WQkFvTQpHRWx1ZEdWeWJtVjBJRmRwWkdkcGRITWdVSFI1SUV4MFpEQWVGdzB5TWpFd01UUXdOalE0TlROYUZ3MHlNekV3Ck1UUXdOalE0TlROYU1FVXhDekFKQmdOVkJBWVRBa0ZWTVJNd0VRWURWUVFJREFwVGIyMWxMVk4wWVhSbE1TRXcKSHdZRFZRUUtEQmhKYm5SbGNtNWxkQ0JYYVdSbmFYUnpJRkIwZVNCTWRHUXdnZ0lpTUEwR0NTcUdTSWIzRFFFQgpBUVVBQTRJQ0R3QXdnZ0lLQW9JQ0FRQytPMk53bGx2QTQyT05SUHMyZWlqTUp2UHhpN21RblVSS3FrOHJEV1VkCkwzZU0yM1JXeVhtS1AydDQ5Zi9LVGsweEZNVStOSTUzTEhwWmh6N3NpK3dEUFUvWWZWSS9rQmZsRm8zeVZCMSsKZWdCSnpyNGIrQ3FoaWlCUkh0Vm5LblFKUmdvOVJjVkxhRm82UEY0N1V0UWJ2bWVuNGdERnExVkYwVHhUdnFMdwpIMzRZL0U2QUJsSlZnWFBzaWQzNm54eTErNnlKV05vRXNVekFiekpWMHhzTGhxc2hOazA0TWx4YnBhcG1XcEUxCmFFMHRIZGpjUlI3Y1dTRUUwMnRSQzNYL2tSNjBKb3MxR0N0Y0ZQTTVIN3NjOFBXNFRUem1EWWhOeDRiVjV4T28KU0xYRnI5ajBzZEgxbm1wSlI1dWxJT2dPTWV3MHA2d3JOYVV2MGpxc1hzdVdqMVpxdTRLRi81aEQ3azVhRlhKNQpjYWNTUi9mRWxreW1uZis0eHZFOG8wdkRWNFR5NHo3K3lSS1U0clZvZFNBZWZIN3lqeitLV1RRck96L0lHU2NwCmV1YTdqV0hRMDdMYWxyTjV2b0tFaU1JM3MrWjhzeUdVUGVyYXQwdzJMWlc3NnhxVGl4R002clZxUldxVlQ4L1oKQTJMMEc4WGRvNTZvV2lFYVF5RkJtRDFnMXU2UEsvTmFGVDI1L2tTNWJ1dnF5L1dLVGt0UVNhNHNZc1ZLbUlQTQp0Zys0NUZ2aFErNkRuQzd0TmVnaTZDTkdTb0w0R1dPOEE5UDZRNjE5RkJJZ1VjcGpFMTgvUHpQOEJmcTAxajhnCjZmdm1jNkVPMkxHVHhDcW1DbVp0TnI3OCtQaUxkMHZIY3pqY3E3NzhiNW5WRXRpUVNRQkUyb0ozTVlIZUFIUUkKYVFJREFRQUJvMU13VVRBZEJnTlZIUTRFRmdRVUpaMUhlVmx1U3pjY0U2NEZQYWtuNkRBWnhmSXdId1lEVlIwagpCQmd3Rm9BVUpaMUhlVmx1U3pjY0U2NEZQYWtuNkRBWnhmSXdEd1lEVlIwVEFRSC9CQVV3QXdFQi96QU5CZ2txCmhraUc5dzBCQVFzRkFBT0NBZ0VBQlhNSlU2MjJZVFZVNnZ1K2svNnkwMGNaWlRmVnZtdVJMOXhTcWxVM0I1QmQKVWdyVWx1TmdjN2dhUUlrYzkvWmh2MnhNd0xxUldMWEhiTWx1NkNvdkNiVTVpeWt0NHVWMnl5UzlZYWhmVVRNVQo3TVE0WFRta2hoS0dGbWZBQ2QzTUVwRE55T3hmWXh0UVBwM1NZT2IxRGFKMmUwY01Gc081bytORGQ5aFVBVzFoCjFLMjMwQnZzYldYYVo4MStIdTU4U1BsYTM5R3FMTG85MzR6dEs4WkRWNFRGTVJxMnNVQ1cxcWFidDh5ejd2RzAKSGV3dXdxelRwR1lTSFI1U0ZvMm45R0xKVUN4SnhxcDlOWVJjMlhUdXRUdkJESzVPMXFZZEJaQzd6cmcxSnczawp2SjI4UGx2TzBQRE42ZVlUdElJdC9yU05ZbW56eVVNRTRYREt0di9KRitLZWZNSWxDTkpzZDRHYXVTdlo5M1NOClhINmcrNEZvRkp4UzNxRmZ0WEc4czNRNnppNzNLRzh5UHZVNHU0WmZNRGd2aG92L0V5YkNLWUpFdVVZSlJWNGEKbmc3cWh3NDBabXQ0eWNCRzU5a2tFSGhNYWtxTWpPaUNkV2x4MEVjZXIxcEFGT1pqN3o1NktURXIxa0ZwUHVaRApjVER5SnNwTjh6dm9CQ0l1ancvQjR6S3kyWStOQitRR1p3dXhyTk9mRGR6ek9yQUE1Ym9OS2gwUUh4c0RxNTExClFaU3hCR21EcGJzN2QzMUQvQll3WEhIUWdwb3FoVUU5dFBGSThpN0pkM2FyeXZCdHlnTWlxSmt1VlRFVk1Ta0UKNTZ0VnFsMjlXenFhRXNrbDN3VUlmczVKKzN3RzRPcWNxRDdXaGQxWUtnc0VUMjdFTWlqVXZIYzQ4TXE0bU1rPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==")
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        OVHcloud Managed Kubernetes Service cluster OIDC can be imported using the tenant `service_name` and cluster id `kube_id` separated by "/" E.g.,

        bash

        ```sh
        $ pulumi import ovh:CloudProject/kubeOidc:KubeOidc my-oidc service_name/kube_id
        ```

        :param str resource_name: The name of the resource.
        :param KubeOidcArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KubeOidcArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 issuer_url: Optional[pulumi.Input[str]] = None,
                 kube_id: Optional[pulumi.Input[str]] = None,
                 oidc_ca_content: Optional[pulumi.Input[str]] = None,
                 oidc_groups_claims: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 oidc_groups_prefix: Optional[pulumi.Input[str]] = None,
                 oidc_required_claims: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 oidc_signing_algs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 oidc_username_claim: Optional[pulumi.Input[str]] = None,
                 oidc_username_prefix: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KubeOidcArgs.__new__(KubeOidcArgs)

            if client_id is None and not opts.urn:
                raise TypeError("Missing required property 'client_id'")
            __props__.__dict__["client_id"] = client_id
            if issuer_url is None and not opts.urn:
                raise TypeError("Missing required property 'issuer_url'")
            __props__.__dict__["issuer_url"] = issuer_url
            if kube_id is None and not opts.urn:
                raise TypeError("Missing required property 'kube_id'")
            __props__.__dict__["kube_id"] = kube_id
            __props__.__dict__["oidc_ca_content"] = oidc_ca_content
            __props__.__dict__["oidc_groups_claims"] = oidc_groups_claims
            __props__.__dict__["oidc_groups_prefix"] = oidc_groups_prefix
            __props__.__dict__["oidc_required_claims"] = oidc_required_claims
            __props__.__dict__["oidc_signing_algs"] = oidc_signing_algs
            __props__.__dict__["oidc_username_claim"] = oidc_username_claim
            __props__.__dict__["oidc_username_prefix"] = oidc_username_prefix
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
        super(KubeOidc, __self__).__init__(
            'ovh:CloudProject/kubeOidc:KubeOidc',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            client_id: Optional[pulumi.Input[str]] = None,
            issuer_url: Optional[pulumi.Input[str]] = None,
            kube_id: Optional[pulumi.Input[str]] = None,
            oidc_ca_content: Optional[pulumi.Input[str]] = None,
            oidc_groups_claims: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            oidc_groups_prefix: Optional[pulumi.Input[str]] = None,
            oidc_required_claims: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            oidc_signing_algs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            oidc_username_claim: Optional[pulumi.Input[str]] = None,
            oidc_username_prefix: Optional[pulumi.Input[str]] = None,
            service_name: Optional[pulumi.Input[str]] = None) -> 'KubeOidc':
        """
        Get an existing KubeOidc resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_id: The OIDC client ID.
        :param pulumi.Input[str] issuer_url: The OIDC issuer url.
        :param pulumi.Input[str] kube_id: The ID of the managed kubernetes cluster. **Changing this value recreates the resource.**
        :param pulumi.Input[str] service_name: The ID of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KubeOidcState.__new__(_KubeOidcState)

        __props__.__dict__["client_id"] = client_id
        __props__.__dict__["issuer_url"] = issuer_url
        __props__.__dict__["kube_id"] = kube_id
        __props__.__dict__["oidc_ca_content"] = oidc_ca_content
        __props__.__dict__["oidc_groups_claims"] = oidc_groups_claims
        __props__.__dict__["oidc_groups_prefix"] = oidc_groups_prefix
        __props__.__dict__["oidc_required_claims"] = oidc_required_claims
        __props__.__dict__["oidc_signing_algs"] = oidc_signing_algs
        __props__.__dict__["oidc_username_claim"] = oidc_username_claim
        __props__.__dict__["oidc_username_prefix"] = oidc_username_prefix
        __props__.__dict__["service_name"] = service_name
        return KubeOidc(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[str]:
        """
        The OIDC client ID.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="issuerUrl")
    def issuer_url(self) -> pulumi.Output[str]:
        """
        The OIDC issuer url.
        """
        return pulumi.get(self, "issuer_url")

    @property
    @pulumi.getter(name="kubeId")
    def kube_id(self) -> pulumi.Output[str]:
        """
        The ID of the managed kubernetes cluster. **Changing this value recreates the resource.**
        """
        return pulumi.get(self, "kube_id")

    @property
    @pulumi.getter(name="oidcCaContent")
    def oidc_ca_content(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "oidc_ca_content")

    @property
    @pulumi.getter(name="oidcGroupsClaims")
    def oidc_groups_claims(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "oidc_groups_claims")

    @property
    @pulumi.getter(name="oidcGroupsPrefix")
    def oidc_groups_prefix(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "oidc_groups_prefix")

    @property
    @pulumi.getter(name="oidcRequiredClaims")
    def oidc_required_claims(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "oidc_required_claims")

    @property
    @pulumi.getter(name="oidcSigningAlgs")
    def oidc_signing_algs(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "oidc_signing_algs")

    @property
    @pulumi.getter(name="oidcUsernameClaim")
    def oidc_username_claim(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "oidc_username_claim")

    @property
    @pulumi.getter(name="oidcUsernamePrefix")
    def oidc_username_prefix(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "oidc_username_prefix")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        The ID of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        """
        return pulumi.get(self, "service_name")

