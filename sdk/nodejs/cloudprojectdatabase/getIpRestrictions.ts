// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use the list of IP restrictions associated with a public cloud project.
 *
 * ## Example Usage
 *
 * To get the list of IP restriction on a database cluster service:
 */
export function getIpRestrictions(args: GetIpRestrictionsArgs, opts?: pulumi.InvokeOptions): Promise<GetIpRestrictionsResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ovh:CloudProjectDatabase/getIpRestrictions:getIpRestrictions", {
        "clusterId": args.clusterId,
        "engine": args.engine,
        "serviceName": args.serviceName,
    }, opts);
}

/**
 * A collection of arguments for invoking getIpRestrictions.
 */
export interface GetIpRestrictionsArgs {
    /**
     * Cluster ID
     */
    clusterId: string;
    /**
     * The engine of the database cluster you want to list IP restrictions. To get a full list of available engine visit:
     * [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
     */
    engine: string;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName: string;
}

/**
 * A collection of values returned by getIpRestrictions.
 */
export interface GetIpRestrictionsResult {
    /**
     * See Argument Reference above.
     */
    readonly clusterId: string;
    /**
     * See Argument Reference above.
     */
    readonly engine: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The list of IP restriction of the database associated with the project.
     */
    readonly ips: string[];
    /**
     * See Argument Reference above.
     */
    readonly serviceName: string;
}
/**
 * Use the list of IP restrictions associated with a public cloud project.
 *
 * ## Example Usage
 *
 * To get the list of IP restriction on a database cluster service:
 */
export function getIpRestrictionsOutput(args: GetIpRestrictionsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetIpRestrictionsResult> {
    return pulumi.output(args).apply((a: any) => getIpRestrictions(a, opts))
}

/**
 * A collection of arguments for invoking getIpRestrictions.
 */
export interface GetIpRestrictionsOutputArgs {
    /**
     * Cluster ID
     */
    clusterId: pulumi.Input<string>;
    /**
     * The engine of the database cluster you want to list IP restrictions. To get a full list of available engine visit:
     * [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
     */
    engine: pulumi.Input<string>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName: pulumi.Input<string>;
}
