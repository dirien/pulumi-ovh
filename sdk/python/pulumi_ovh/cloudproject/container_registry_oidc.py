# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ContainerRegistryOIDCArgs', 'ContainerRegistryOIDC']

@pulumi.input_type
class ContainerRegistryOIDCArgs:
    def __init__(__self__, *,
                 oidc_client_id: pulumi.Input[str],
                 oidc_client_secret: pulumi.Input[str],
                 oidc_endpoint: pulumi.Input[str],
                 oidc_name: pulumi.Input[str],
                 oidc_scope: pulumi.Input[str],
                 registry_id: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 delete_users: Optional[pulumi.Input[bool]] = None,
                 oidc_admin_group: Optional[pulumi.Input[str]] = None,
                 oidc_auto_onboard: Optional[pulumi.Input[bool]] = None,
                 oidc_groups_claim: Optional[pulumi.Input[str]] = None,
                 oidc_user_claim: Optional[pulumi.Input[str]] = None,
                 oidc_verify_cert: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a ContainerRegistryOIDC resource.
        :param pulumi.Input[str] oidc_client_id: The client ID with which Harbor is registered as client application with the OIDC provider.
        :param pulumi.Input[str] oidc_client_secret: The secret for the Harbor client application.
        :param pulumi.Input[str] oidc_endpoint: The URL of an OIDC-compliant server.
        :param pulumi.Input[str] oidc_name: The name of the OIDC provider.
        :param pulumi.Input[str] oidc_scope: The scope sent to OIDC server during authentication. It's a comma-separated string that must contain 'openid' and usually also contains 'profile' and 'email'. To obtain refresh tokens it should also contain 'offline_access'.
        :param pulumi.Input[str] registry_id: The ID of the Managed Private Registry. **Changing this value recreates the resource.**
        :param pulumi.Input[str] service_name: The ID of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        :param pulumi.Input[bool] delete_users: Delete existing users from Harbor. OIDC can't be enabled if there is at least one user already created. This parameter is only used at OIDC configuration creation. **Changing this value recreates the resource.**
        :param pulumi.Input[str] oidc_admin_group: Specify an OIDC admin group name. All OIDC users in this group will have harbor admin privilege. Keep it blank if you do not want to.
        :param pulumi.Input[bool] oidc_auto_onboard: Skip the onboarding screen, so user cannot change its username. Username is provided from ID Token.
        :param pulumi.Input[str] oidc_groups_claim: The name of Claim in the ID token whose value is the list of group names.
        :param pulumi.Input[str] oidc_user_claim: The name of the claim in the ID Token where the username is retrieved from. If not specified, it will default to 'name' (only useful when automatic Onboarding is enabled).
        :param pulumi.Input[bool] oidc_verify_cert: Set it to `false` if your OIDC server is hosted via self-signed certificate.
        """
        pulumi.set(__self__, "oidc_client_id", oidc_client_id)
        pulumi.set(__self__, "oidc_client_secret", oidc_client_secret)
        pulumi.set(__self__, "oidc_endpoint", oidc_endpoint)
        pulumi.set(__self__, "oidc_name", oidc_name)
        pulumi.set(__self__, "oidc_scope", oidc_scope)
        pulumi.set(__self__, "registry_id", registry_id)
        pulumi.set(__self__, "service_name", service_name)
        if delete_users is not None:
            pulumi.set(__self__, "delete_users", delete_users)
        if oidc_admin_group is not None:
            pulumi.set(__self__, "oidc_admin_group", oidc_admin_group)
        if oidc_auto_onboard is not None:
            pulumi.set(__self__, "oidc_auto_onboard", oidc_auto_onboard)
        if oidc_groups_claim is not None:
            pulumi.set(__self__, "oidc_groups_claim", oidc_groups_claim)
        if oidc_user_claim is not None:
            pulumi.set(__self__, "oidc_user_claim", oidc_user_claim)
        if oidc_verify_cert is not None:
            pulumi.set(__self__, "oidc_verify_cert", oidc_verify_cert)

    @property
    @pulumi.getter(name="oidcClientId")
    def oidc_client_id(self) -> pulumi.Input[str]:
        """
        The client ID with which Harbor is registered as client application with the OIDC provider.
        """
        return pulumi.get(self, "oidc_client_id")

    @oidc_client_id.setter
    def oidc_client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "oidc_client_id", value)

    @property
    @pulumi.getter(name="oidcClientSecret")
    def oidc_client_secret(self) -> pulumi.Input[str]:
        """
        The secret for the Harbor client application.
        """
        return pulumi.get(self, "oidc_client_secret")

    @oidc_client_secret.setter
    def oidc_client_secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "oidc_client_secret", value)

    @property
    @pulumi.getter(name="oidcEndpoint")
    def oidc_endpoint(self) -> pulumi.Input[str]:
        """
        The URL of an OIDC-compliant server.
        """
        return pulumi.get(self, "oidc_endpoint")

    @oidc_endpoint.setter
    def oidc_endpoint(self, value: pulumi.Input[str]):
        pulumi.set(self, "oidc_endpoint", value)

    @property
    @pulumi.getter(name="oidcName")
    def oidc_name(self) -> pulumi.Input[str]:
        """
        The name of the OIDC provider.
        """
        return pulumi.get(self, "oidc_name")

    @oidc_name.setter
    def oidc_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "oidc_name", value)

    @property
    @pulumi.getter(name="oidcScope")
    def oidc_scope(self) -> pulumi.Input[str]:
        """
        The scope sent to OIDC server during authentication. It's a comma-separated string that must contain 'openid' and usually also contains 'profile' and 'email'. To obtain refresh tokens it should also contain 'offline_access'.
        """
        return pulumi.get(self, "oidc_scope")

    @oidc_scope.setter
    def oidc_scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "oidc_scope", value)

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> pulumi.Input[str]:
        """
        The ID of the Managed Private Registry. **Changing this value recreates the resource.**
        """
        return pulumi.get(self, "registry_id")

    @registry_id.setter
    def registry_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "registry_id", value)

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
    @pulumi.getter(name="deleteUsers")
    def delete_users(self) -> Optional[pulumi.Input[bool]]:
        """
        Delete existing users from Harbor. OIDC can't be enabled if there is at least one user already created. This parameter is only used at OIDC configuration creation. **Changing this value recreates the resource.**
        """
        return pulumi.get(self, "delete_users")

    @delete_users.setter
    def delete_users(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_users", value)

    @property
    @pulumi.getter(name="oidcAdminGroup")
    def oidc_admin_group(self) -> Optional[pulumi.Input[str]]:
        """
        Specify an OIDC admin group name. All OIDC users in this group will have harbor admin privilege. Keep it blank if you do not want to.
        """
        return pulumi.get(self, "oidc_admin_group")

    @oidc_admin_group.setter
    def oidc_admin_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_admin_group", value)

    @property
    @pulumi.getter(name="oidcAutoOnboard")
    def oidc_auto_onboard(self) -> Optional[pulumi.Input[bool]]:
        """
        Skip the onboarding screen, so user cannot change its username. Username is provided from ID Token.
        """
        return pulumi.get(self, "oidc_auto_onboard")

    @oidc_auto_onboard.setter
    def oidc_auto_onboard(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "oidc_auto_onboard", value)

    @property
    @pulumi.getter(name="oidcGroupsClaim")
    def oidc_groups_claim(self) -> Optional[pulumi.Input[str]]:
        """
        The name of Claim in the ID token whose value is the list of group names.
        """
        return pulumi.get(self, "oidc_groups_claim")

    @oidc_groups_claim.setter
    def oidc_groups_claim(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_groups_claim", value)

    @property
    @pulumi.getter(name="oidcUserClaim")
    def oidc_user_claim(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the claim in the ID Token where the username is retrieved from. If not specified, it will default to 'name' (only useful when automatic Onboarding is enabled).
        """
        return pulumi.get(self, "oidc_user_claim")

    @oidc_user_claim.setter
    def oidc_user_claim(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_user_claim", value)

    @property
    @pulumi.getter(name="oidcVerifyCert")
    def oidc_verify_cert(self) -> Optional[pulumi.Input[bool]]:
        """
        Set it to `false` if your OIDC server is hosted via self-signed certificate.
        """
        return pulumi.get(self, "oidc_verify_cert")

    @oidc_verify_cert.setter
    def oidc_verify_cert(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "oidc_verify_cert", value)


@pulumi.input_type
class _ContainerRegistryOIDCState:
    def __init__(__self__, *,
                 delete_users: Optional[pulumi.Input[bool]] = None,
                 oidc_admin_group: Optional[pulumi.Input[str]] = None,
                 oidc_auto_onboard: Optional[pulumi.Input[bool]] = None,
                 oidc_client_id: Optional[pulumi.Input[str]] = None,
                 oidc_client_secret: Optional[pulumi.Input[str]] = None,
                 oidc_endpoint: Optional[pulumi.Input[str]] = None,
                 oidc_groups_claim: Optional[pulumi.Input[str]] = None,
                 oidc_name: Optional[pulumi.Input[str]] = None,
                 oidc_scope: Optional[pulumi.Input[str]] = None,
                 oidc_user_claim: Optional[pulumi.Input[str]] = None,
                 oidc_verify_cert: Optional[pulumi.Input[bool]] = None,
                 registry_id: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ContainerRegistryOIDC resources.
        :param pulumi.Input[bool] delete_users: Delete existing users from Harbor. OIDC can't be enabled if there is at least one user already created. This parameter is only used at OIDC configuration creation. **Changing this value recreates the resource.**
        :param pulumi.Input[str] oidc_admin_group: Specify an OIDC admin group name. All OIDC users in this group will have harbor admin privilege. Keep it blank if you do not want to.
        :param pulumi.Input[bool] oidc_auto_onboard: Skip the onboarding screen, so user cannot change its username. Username is provided from ID Token.
        :param pulumi.Input[str] oidc_client_id: The client ID with which Harbor is registered as client application with the OIDC provider.
        :param pulumi.Input[str] oidc_client_secret: The secret for the Harbor client application.
        :param pulumi.Input[str] oidc_endpoint: The URL of an OIDC-compliant server.
        :param pulumi.Input[str] oidc_groups_claim: The name of Claim in the ID token whose value is the list of group names.
        :param pulumi.Input[str] oidc_name: The name of the OIDC provider.
        :param pulumi.Input[str] oidc_scope: The scope sent to OIDC server during authentication. It's a comma-separated string that must contain 'openid' and usually also contains 'profile' and 'email'. To obtain refresh tokens it should also contain 'offline_access'.
        :param pulumi.Input[str] oidc_user_claim: The name of the claim in the ID Token where the username is retrieved from. If not specified, it will default to 'name' (only useful when automatic Onboarding is enabled).
        :param pulumi.Input[bool] oidc_verify_cert: Set it to `false` if your OIDC server is hosted via self-signed certificate.
        :param pulumi.Input[str] registry_id: The ID of the Managed Private Registry. **Changing this value recreates the resource.**
        :param pulumi.Input[str] service_name: The ID of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        """
        if delete_users is not None:
            pulumi.set(__self__, "delete_users", delete_users)
        if oidc_admin_group is not None:
            pulumi.set(__self__, "oidc_admin_group", oidc_admin_group)
        if oidc_auto_onboard is not None:
            pulumi.set(__self__, "oidc_auto_onboard", oidc_auto_onboard)
        if oidc_client_id is not None:
            pulumi.set(__self__, "oidc_client_id", oidc_client_id)
        if oidc_client_secret is not None:
            pulumi.set(__self__, "oidc_client_secret", oidc_client_secret)
        if oidc_endpoint is not None:
            pulumi.set(__self__, "oidc_endpoint", oidc_endpoint)
        if oidc_groups_claim is not None:
            pulumi.set(__self__, "oidc_groups_claim", oidc_groups_claim)
        if oidc_name is not None:
            pulumi.set(__self__, "oidc_name", oidc_name)
        if oidc_scope is not None:
            pulumi.set(__self__, "oidc_scope", oidc_scope)
        if oidc_user_claim is not None:
            pulumi.set(__self__, "oidc_user_claim", oidc_user_claim)
        if oidc_verify_cert is not None:
            pulumi.set(__self__, "oidc_verify_cert", oidc_verify_cert)
        if registry_id is not None:
            pulumi.set(__self__, "registry_id", registry_id)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter(name="deleteUsers")
    def delete_users(self) -> Optional[pulumi.Input[bool]]:
        """
        Delete existing users from Harbor. OIDC can't be enabled if there is at least one user already created. This parameter is only used at OIDC configuration creation. **Changing this value recreates the resource.**
        """
        return pulumi.get(self, "delete_users")

    @delete_users.setter
    def delete_users(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_users", value)

    @property
    @pulumi.getter(name="oidcAdminGroup")
    def oidc_admin_group(self) -> Optional[pulumi.Input[str]]:
        """
        Specify an OIDC admin group name. All OIDC users in this group will have harbor admin privilege. Keep it blank if you do not want to.
        """
        return pulumi.get(self, "oidc_admin_group")

    @oidc_admin_group.setter
    def oidc_admin_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_admin_group", value)

    @property
    @pulumi.getter(name="oidcAutoOnboard")
    def oidc_auto_onboard(self) -> Optional[pulumi.Input[bool]]:
        """
        Skip the onboarding screen, so user cannot change its username. Username is provided from ID Token.
        """
        return pulumi.get(self, "oidc_auto_onboard")

    @oidc_auto_onboard.setter
    def oidc_auto_onboard(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "oidc_auto_onboard", value)

    @property
    @pulumi.getter(name="oidcClientId")
    def oidc_client_id(self) -> Optional[pulumi.Input[str]]:
        """
        The client ID with which Harbor is registered as client application with the OIDC provider.
        """
        return pulumi.get(self, "oidc_client_id")

    @oidc_client_id.setter
    def oidc_client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_client_id", value)

    @property
    @pulumi.getter(name="oidcClientSecret")
    def oidc_client_secret(self) -> Optional[pulumi.Input[str]]:
        """
        The secret for the Harbor client application.
        """
        return pulumi.get(self, "oidc_client_secret")

    @oidc_client_secret.setter
    def oidc_client_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_client_secret", value)

    @property
    @pulumi.getter(name="oidcEndpoint")
    def oidc_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of an OIDC-compliant server.
        """
        return pulumi.get(self, "oidc_endpoint")

    @oidc_endpoint.setter
    def oidc_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_endpoint", value)

    @property
    @pulumi.getter(name="oidcGroupsClaim")
    def oidc_groups_claim(self) -> Optional[pulumi.Input[str]]:
        """
        The name of Claim in the ID token whose value is the list of group names.
        """
        return pulumi.get(self, "oidc_groups_claim")

    @oidc_groups_claim.setter
    def oidc_groups_claim(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_groups_claim", value)

    @property
    @pulumi.getter(name="oidcName")
    def oidc_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the OIDC provider.
        """
        return pulumi.get(self, "oidc_name")

    @oidc_name.setter
    def oidc_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_name", value)

    @property
    @pulumi.getter(name="oidcScope")
    def oidc_scope(self) -> Optional[pulumi.Input[str]]:
        """
        The scope sent to OIDC server during authentication. It's a comma-separated string that must contain 'openid' and usually also contains 'profile' and 'email'. To obtain refresh tokens it should also contain 'offline_access'.
        """
        return pulumi.get(self, "oidc_scope")

    @oidc_scope.setter
    def oidc_scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_scope", value)

    @property
    @pulumi.getter(name="oidcUserClaim")
    def oidc_user_claim(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the claim in the ID Token where the username is retrieved from. If not specified, it will default to 'name' (only useful when automatic Onboarding is enabled).
        """
        return pulumi.get(self, "oidc_user_claim")

    @oidc_user_claim.setter
    def oidc_user_claim(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_user_claim", value)

    @property
    @pulumi.getter(name="oidcVerifyCert")
    def oidc_verify_cert(self) -> Optional[pulumi.Input[bool]]:
        """
        Set it to `false` if your OIDC server is hosted via self-signed certificate.
        """
        return pulumi.get(self, "oidc_verify_cert")

    @oidc_verify_cert.setter
    def oidc_verify_cert(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "oidc_verify_cert", value)

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Managed Private Registry. **Changing this value recreates the resource.**
        """
        return pulumi.get(self, "registry_id")

    @registry_id.setter
    def registry_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registry_id", value)

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


class ContainerRegistryOIDC(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delete_users: Optional[pulumi.Input[bool]] = None,
                 oidc_admin_group: Optional[pulumi.Input[str]] = None,
                 oidc_auto_onboard: Optional[pulumi.Input[bool]] = None,
                 oidc_client_id: Optional[pulumi.Input[str]] = None,
                 oidc_client_secret: Optional[pulumi.Input[str]] = None,
                 oidc_endpoint: Optional[pulumi.Input[str]] = None,
                 oidc_groups_claim: Optional[pulumi.Input[str]] = None,
                 oidc_name: Optional[pulumi.Input[str]] = None,
                 oidc_scope: Optional[pulumi.Input[str]] = None,
                 oidc_user_claim: Optional[pulumi.Input[str]] = None,
                 oidc_verify_cert: Optional[pulumi.Input[bool]] = None,
                 registry_id: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates an OIDC configuration in an OVHcloud Managed Private Registry.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        my_oidc = ovh.cloud_project.ContainerRegistryOIDC("my-oidc",
            service_name="XXXXXX",
            registry_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx",
            oidc_name="my-oidc-provider",
            oidc_endpoint="https://xxxx.yyy.com",
            oidc_client_id="xxx",
            oidc_client_secret="xxx",
            oidc_scope="openid,profile,email,offline_access",
            oidc_groups_claim="groups",
            oidc_admin_group="harbor-admin",
            oidc_verify_cert=True,
            oidc_auto_onboard=True,
            oidc_user_claim="preferred_username",
            delete_users=False)
        pulumi.export("oidcClientSecret", my_oidc.oidc_client_secret)
        ```

        ## Import

        OVHcloud Managed Private Registry OIDC can be imported using the tenant `service_name` and registry id `registry_id` separated by "/" E.g.,

         bash

        ```sh
        $ pulumi import ovh:CloudProject/containerRegistryOIDC:ContainerRegistryOIDC my-oidc service_name/registry_id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] delete_users: Delete existing users from Harbor. OIDC can't be enabled if there is at least one user already created. This parameter is only used at OIDC configuration creation. **Changing this value recreates the resource.**
        :param pulumi.Input[str] oidc_admin_group: Specify an OIDC admin group name. All OIDC users in this group will have harbor admin privilege. Keep it blank if you do not want to.
        :param pulumi.Input[bool] oidc_auto_onboard: Skip the onboarding screen, so user cannot change its username. Username is provided from ID Token.
        :param pulumi.Input[str] oidc_client_id: The client ID with which Harbor is registered as client application with the OIDC provider.
        :param pulumi.Input[str] oidc_client_secret: The secret for the Harbor client application.
        :param pulumi.Input[str] oidc_endpoint: The URL of an OIDC-compliant server.
        :param pulumi.Input[str] oidc_groups_claim: The name of Claim in the ID token whose value is the list of group names.
        :param pulumi.Input[str] oidc_name: The name of the OIDC provider.
        :param pulumi.Input[str] oidc_scope: The scope sent to OIDC server during authentication. It's a comma-separated string that must contain 'openid' and usually also contains 'profile' and 'email'. To obtain refresh tokens it should also contain 'offline_access'.
        :param pulumi.Input[str] oidc_user_claim: The name of the claim in the ID Token where the username is retrieved from. If not specified, it will default to 'name' (only useful when automatic Onboarding is enabled).
        :param pulumi.Input[bool] oidc_verify_cert: Set it to `false` if your OIDC server is hosted via self-signed certificate.
        :param pulumi.Input[str] registry_id: The ID of the Managed Private Registry. **Changing this value recreates the resource.**
        :param pulumi.Input[str] service_name: The ID of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ContainerRegistryOIDCArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an OIDC configuration in an OVHcloud Managed Private Registry.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        my_oidc = ovh.cloud_project.ContainerRegistryOIDC("my-oidc",
            service_name="XXXXXX",
            registry_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx",
            oidc_name="my-oidc-provider",
            oidc_endpoint="https://xxxx.yyy.com",
            oidc_client_id="xxx",
            oidc_client_secret="xxx",
            oidc_scope="openid,profile,email,offline_access",
            oidc_groups_claim="groups",
            oidc_admin_group="harbor-admin",
            oidc_verify_cert=True,
            oidc_auto_onboard=True,
            oidc_user_claim="preferred_username",
            delete_users=False)
        pulumi.export("oidcClientSecret", my_oidc.oidc_client_secret)
        ```

        ## Import

        OVHcloud Managed Private Registry OIDC can be imported using the tenant `service_name` and registry id `registry_id` separated by "/" E.g.,

         bash

        ```sh
        $ pulumi import ovh:CloudProject/containerRegistryOIDC:ContainerRegistryOIDC my-oidc service_name/registry_id
        ```

        :param str resource_name: The name of the resource.
        :param ContainerRegistryOIDCArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContainerRegistryOIDCArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delete_users: Optional[pulumi.Input[bool]] = None,
                 oidc_admin_group: Optional[pulumi.Input[str]] = None,
                 oidc_auto_onboard: Optional[pulumi.Input[bool]] = None,
                 oidc_client_id: Optional[pulumi.Input[str]] = None,
                 oidc_client_secret: Optional[pulumi.Input[str]] = None,
                 oidc_endpoint: Optional[pulumi.Input[str]] = None,
                 oidc_groups_claim: Optional[pulumi.Input[str]] = None,
                 oidc_name: Optional[pulumi.Input[str]] = None,
                 oidc_scope: Optional[pulumi.Input[str]] = None,
                 oidc_user_claim: Optional[pulumi.Input[str]] = None,
                 oidc_verify_cert: Optional[pulumi.Input[bool]] = None,
                 registry_id: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ContainerRegistryOIDCArgs.__new__(ContainerRegistryOIDCArgs)

            __props__.__dict__["delete_users"] = delete_users
            __props__.__dict__["oidc_admin_group"] = oidc_admin_group
            __props__.__dict__["oidc_auto_onboard"] = oidc_auto_onboard
            if oidc_client_id is None and not opts.urn:
                raise TypeError("Missing required property 'oidc_client_id'")
            __props__.__dict__["oidc_client_id"] = oidc_client_id
            if oidc_client_secret is None and not opts.urn:
                raise TypeError("Missing required property 'oidc_client_secret'")
            __props__.__dict__["oidc_client_secret"] = None if oidc_client_secret is None else pulumi.Output.secret(oidc_client_secret)
            if oidc_endpoint is None and not opts.urn:
                raise TypeError("Missing required property 'oidc_endpoint'")
            __props__.__dict__["oidc_endpoint"] = oidc_endpoint
            __props__.__dict__["oidc_groups_claim"] = oidc_groups_claim
            if oidc_name is None and not opts.urn:
                raise TypeError("Missing required property 'oidc_name'")
            __props__.__dict__["oidc_name"] = oidc_name
            if oidc_scope is None and not opts.urn:
                raise TypeError("Missing required property 'oidc_scope'")
            __props__.__dict__["oidc_scope"] = oidc_scope
            __props__.__dict__["oidc_user_claim"] = oidc_user_claim
            __props__.__dict__["oidc_verify_cert"] = oidc_verify_cert
            if registry_id is None and not opts.urn:
                raise TypeError("Missing required property 'registry_id'")
            __props__.__dict__["registry_id"] = registry_id
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["oidcClientSecret"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(ContainerRegistryOIDC, __self__).__init__(
            'ovh:CloudProject/containerRegistryOIDC:ContainerRegistryOIDC',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            delete_users: Optional[pulumi.Input[bool]] = None,
            oidc_admin_group: Optional[pulumi.Input[str]] = None,
            oidc_auto_onboard: Optional[pulumi.Input[bool]] = None,
            oidc_client_id: Optional[pulumi.Input[str]] = None,
            oidc_client_secret: Optional[pulumi.Input[str]] = None,
            oidc_endpoint: Optional[pulumi.Input[str]] = None,
            oidc_groups_claim: Optional[pulumi.Input[str]] = None,
            oidc_name: Optional[pulumi.Input[str]] = None,
            oidc_scope: Optional[pulumi.Input[str]] = None,
            oidc_user_claim: Optional[pulumi.Input[str]] = None,
            oidc_verify_cert: Optional[pulumi.Input[bool]] = None,
            registry_id: Optional[pulumi.Input[str]] = None,
            service_name: Optional[pulumi.Input[str]] = None) -> 'ContainerRegistryOIDC':
        """
        Get an existing ContainerRegistryOIDC resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] delete_users: Delete existing users from Harbor. OIDC can't be enabled if there is at least one user already created. This parameter is only used at OIDC configuration creation. **Changing this value recreates the resource.**
        :param pulumi.Input[str] oidc_admin_group: Specify an OIDC admin group name. All OIDC users in this group will have harbor admin privilege. Keep it blank if you do not want to.
        :param pulumi.Input[bool] oidc_auto_onboard: Skip the onboarding screen, so user cannot change its username. Username is provided from ID Token.
        :param pulumi.Input[str] oidc_client_id: The client ID with which Harbor is registered as client application with the OIDC provider.
        :param pulumi.Input[str] oidc_client_secret: The secret for the Harbor client application.
        :param pulumi.Input[str] oidc_endpoint: The URL of an OIDC-compliant server.
        :param pulumi.Input[str] oidc_groups_claim: The name of Claim in the ID token whose value is the list of group names.
        :param pulumi.Input[str] oidc_name: The name of the OIDC provider.
        :param pulumi.Input[str] oidc_scope: The scope sent to OIDC server during authentication. It's a comma-separated string that must contain 'openid' and usually also contains 'profile' and 'email'. To obtain refresh tokens it should also contain 'offline_access'.
        :param pulumi.Input[str] oidc_user_claim: The name of the claim in the ID Token where the username is retrieved from. If not specified, it will default to 'name' (only useful when automatic Onboarding is enabled).
        :param pulumi.Input[bool] oidc_verify_cert: Set it to `false` if your OIDC server is hosted via self-signed certificate.
        :param pulumi.Input[str] registry_id: The ID of the Managed Private Registry. **Changing this value recreates the resource.**
        :param pulumi.Input[str] service_name: The ID of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ContainerRegistryOIDCState.__new__(_ContainerRegistryOIDCState)

        __props__.__dict__["delete_users"] = delete_users
        __props__.__dict__["oidc_admin_group"] = oidc_admin_group
        __props__.__dict__["oidc_auto_onboard"] = oidc_auto_onboard
        __props__.__dict__["oidc_client_id"] = oidc_client_id
        __props__.__dict__["oidc_client_secret"] = oidc_client_secret
        __props__.__dict__["oidc_endpoint"] = oidc_endpoint
        __props__.__dict__["oidc_groups_claim"] = oidc_groups_claim
        __props__.__dict__["oidc_name"] = oidc_name
        __props__.__dict__["oidc_scope"] = oidc_scope
        __props__.__dict__["oidc_user_claim"] = oidc_user_claim
        __props__.__dict__["oidc_verify_cert"] = oidc_verify_cert
        __props__.__dict__["registry_id"] = registry_id
        __props__.__dict__["service_name"] = service_name
        return ContainerRegistryOIDC(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deleteUsers")
    def delete_users(self) -> pulumi.Output[Optional[bool]]:
        """
        Delete existing users from Harbor. OIDC can't be enabled if there is at least one user already created. This parameter is only used at OIDC configuration creation. **Changing this value recreates the resource.**
        """
        return pulumi.get(self, "delete_users")

    @property
    @pulumi.getter(name="oidcAdminGroup")
    def oidc_admin_group(self) -> pulumi.Output[Optional[str]]:
        """
        Specify an OIDC admin group name. All OIDC users in this group will have harbor admin privilege. Keep it blank if you do not want to.
        """
        return pulumi.get(self, "oidc_admin_group")

    @property
    @pulumi.getter(name="oidcAutoOnboard")
    def oidc_auto_onboard(self) -> pulumi.Output[Optional[bool]]:
        """
        Skip the onboarding screen, so user cannot change its username. Username is provided from ID Token.
        """
        return pulumi.get(self, "oidc_auto_onboard")

    @property
    @pulumi.getter(name="oidcClientId")
    def oidc_client_id(self) -> pulumi.Output[str]:
        """
        The client ID with which Harbor is registered as client application with the OIDC provider.
        """
        return pulumi.get(self, "oidc_client_id")

    @property
    @pulumi.getter(name="oidcClientSecret")
    def oidc_client_secret(self) -> pulumi.Output[str]:
        """
        The secret for the Harbor client application.
        """
        return pulumi.get(self, "oidc_client_secret")

    @property
    @pulumi.getter(name="oidcEndpoint")
    def oidc_endpoint(self) -> pulumi.Output[str]:
        """
        The URL of an OIDC-compliant server.
        """
        return pulumi.get(self, "oidc_endpoint")

    @property
    @pulumi.getter(name="oidcGroupsClaim")
    def oidc_groups_claim(self) -> pulumi.Output[Optional[str]]:
        """
        The name of Claim in the ID token whose value is the list of group names.
        """
        return pulumi.get(self, "oidc_groups_claim")

    @property
    @pulumi.getter(name="oidcName")
    def oidc_name(self) -> pulumi.Output[str]:
        """
        The name of the OIDC provider.
        """
        return pulumi.get(self, "oidc_name")

    @property
    @pulumi.getter(name="oidcScope")
    def oidc_scope(self) -> pulumi.Output[str]:
        """
        The scope sent to OIDC server during authentication. It's a comma-separated string that must contain 'openid' and usually also contains 'profile' and 'email'. To obtain refresh tokens it should also contain 'offline_access'.
        """
        return pulumi.get(self, "oidc_scope")

    @property
    @pulumi.getter(name="oidcUserClaim")
    def oidc_user_claim(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the claim in the ID Token where the username is retrieved from. If not specified, it will default to 'name' (only useful when automatic Onboarding is enabled).
        """
        return pulumi.get(self, "oidc_user_claim")

    @property
    @pulumi.getter(name="oidcVerifyCert")
    def oidc_verify_cert(self) -> pulumi.Output[Optional[bool]]:
        """
        Set it to `false` if your OIDC server is hosted via self-signed certificate.
        """
        return pulumi.get(self, "oidc_verify_cert")

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> pulumi.Output[str]:
        """
        The ID of the Managed Private Registry. **Changing this value recreates the resource.**
        """
        return pulumi.get(self, "registry_id")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        The ID of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        """
        return pulumi.get(self, "service_name")

