// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to get the list of VPS associated with your OVH Account.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const servers = ovh.Vps.getVpss({});
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getVpss(opts?: pulumi.InvokeOptions): Promise<GetVpssResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ovh:Vps/getVpss:getVpss", {
    }, opts);
}

/**
 * A collection of values returned by getVpss.
 */
export interface GetVpssResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The list of VPS IDs associated with your OVH Account.
     */
    readonly results: string[];
}
/**
 * Use this data source to get the list of VPS associated with your OVH Account.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const servers = ovh.Vps.getVpss({});
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getVpssOutput(opts?: pulumi.InvokeOptions): pulumi.Output<GetVpssResult> {
    return pulumi.output(getVpss(opts))
}
