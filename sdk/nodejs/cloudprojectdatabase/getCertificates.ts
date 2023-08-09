// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to get information about certificates of a cluster associated with a public cloud project.
 *
 * ## Example Usage
 */
export function getCertificates(args: GetCertificatesArgs, opts?: pulumi.InvokeOptions): Promise<GetCertificatesResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ovh:CloudProjectDatabase/getCertificates:getCertificates", {
        "clusterId": args.clusterId,
        "engine": args.engine,
        "serviceName": args.serviceName,
    }, opts);
}

/**
 * A collection of arguments for invoking getCertificates.
 */
export interface GetCertificatesArgs {
    /**
     * Cluster ID
     */
    clusterId: string;
    /**
     * The engine of the database cluster you want database information. To get a full list of available engine visit:
     * [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
     * Available engines:
     */
    engine: string;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName: string;
}

/**
 * A collection of values returned by getCertificates.
 */
export interface GetCertificatesResult {
    /**
     * CA certificate used for the service.
     */
    readonly ca: string;
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
     * See Argument Reference above.
     */
    readonly serviceName: string;
}
/**
 * Use this data source to get information about certificates of a cluster associated with a public cloud project.
 *
 * ## Example Usage
 */
export function getCertificatesOutput(args: GetCertificatesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetCertificatesResult> {
    return pulumi.output(args).apply((a: any) => getCertificates(a, opts))
}

/**
 * A collection of arguments for invoking getCertificates.
 */
export interface GetCertificatesOutputArgs {
    /**
     * Cluster ID
     */
    clusterId: pulumi.Input<string>;
    /**
     * The engine of the database cluster you want database information. To get a full list of available engine visit:
     * [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
     * Available engines:
     */
    engine: pulumi.Input<string>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName: pulumi.Input<string>;
}
