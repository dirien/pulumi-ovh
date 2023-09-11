// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to get the list of Vrack IDs available for your OVHcloud account.
 *
 * ## Example Usage
 */
export function getVracks(opts?: pulumi.InvokeOptions): Promise<GetVracksResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ovh:Vrack/getVracks:getVracks", {
    }, opts);
}

/**
 * A collection of values returned by getVracks.
 */
export interface GetVracksResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The list of vrack service name available for your OVHcloud account.
     */
    readonly results: string[];
}
/**
 * Use this data source to get the list of Vrack IDs available for your OVHcloud account.
 *
 * ## Example Usage
 */
export function getVracksOutput(opts?: pulumi.InvokeOptions): pulumi.Output<GetVracksResult> {
    return pulumi.output(getVracks(opts))
}
