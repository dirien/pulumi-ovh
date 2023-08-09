// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to retrieve the list of the account's identity groups
 *
 * ## Example Usage
 */
export function getIdentityGroups(opts?: pulumi.InvokeOptions): Promise<GetIdentityGroupsResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ovh:Me/getIdentityGroups:getIdentityGroups", {
    }, opts);
}

/**
 * A collection of values returned by getIdentityGroups.
 */
export interface GetIdentityGroupsResult {
    /**
     * The list of the group names of all the identity groups.
     */
    readonly groups: string[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
