// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to retrieve information about a DBaas logs output opensearch index.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const index = ovh.Dbaas.getLogsOutputOpenSearchIndex({
 *     name: "index-name",
 *     serviceName: "ldp-xx-xxxxx",
 * });
 * ```
 */
export function getLogsOutputOpenSearchIndex(args: GetLogsOutputOpenSearchIndexArgs, opts?: pulumi.InvokeOptions): Promise<GetLogsOutputOpenSearchIndexResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ovh:Dbaas/getLogsOutputOpenSearchIndex:getLogsOutputOpenSearchIndex", {
        "name": args.name,
        "nbShard": args.nbShard,
        "serviceName": args.serviceName,
    }, opts);
}

/**
 * A collection of arguments for invoking getLogsOutputOpenSearchIndex.
 */
export interface GetLogsOutputOpenSearchIndexArgs {
    /**
     * Index name
     */
    name: string;
    /**
     * Number of shard
     */
    nbShard?: number;
    /**
     * The service name. It's the ID of your Logs Data Platform instance.
     */
    serviceName: string;
}

/**
 * A collection of values returned by getLogsOutputOpenSearchIndex.
 */
export interface GetLogsOutputOpenSearchIndexResult {
    /**
     * If set, notify when size is near 80, 90 or 100 % of its maximum capacity
     */
    readonly alertNotifyEnabled: boolean;
    /**
     * Index creation
     */
    readonly createdAt: string;
    /**
     * Current index size (in bytes)
     */
    readonly currentSize: number;
    /**
     * Index description
     */
    readonly description: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * Index ID
     */
    readonly indexId: string;
    /**
     * Indicates if you are allowed to edit entry
     */
    readonly isEditable: boolean;
    /**
     * Maximum index size (in bytes)
     */
    readonly maxSize: number;
    /**
     * Index name
     */
    readonly name: string;
    /**
     * Number of shard
     */
    readonly nbShard: number;
    readonly serviceName: string;
    /**
     * Index last update
     */
    readonly updatedAt: string;
}
/**
 * Use this data source to retrieve information about a DBaas logs output opensearch index.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const index = ovh.Dbaas.getLogsOutputOpenSearchIndex({
 *     name: "index-name",
 *     serviceName: "ldp-xx-xxxxx",
 * });
 * ```
 */
export function getLogsOutputOpenSearchIndexOutput(args: GetLogsOutputOpenSearchIndexOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetLogsOutputOpenSearchIndexResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ovh:Dbaas/getLogsOutputOpenSearchIndex:getLogsOutputOpenSearchIndex", {
        "name": args.name,
        "nbShard": args.nbShard,
        "serviceName": args.serviceName,
    }, opts);
}

/**
 * A collection of arguments for invoking getLogsOutputOpenSearchIndex.
 */
export interface GetLogsOutputOpenSearchIndexOutputArgs {
    /**
     * Index name
     */
    name: pulumi.Input<string>;
    /**
     * Number of shard
     */
    nbShard?: pulumi.Input<number>;
    /**
     * The service name. It's the ID of your Logs Data Platform instance.
     */
    serviceName: pulumi.Input<string>;
}
