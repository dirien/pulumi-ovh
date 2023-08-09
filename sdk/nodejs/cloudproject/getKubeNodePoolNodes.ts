// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to get a list of OVHcloud Managed Kubernetes nodes in a specific node pool.
 *
 * ## Example Usage
 */
export function getKubeNodePoolNodes(args: GetKubeNodePoolNodesArgs, opts?: pulumi.InvokeOptions): Promise<GetKubeNodePoolNodesResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ovh:CloudProject/getKubeNodePoolNodes:getKubeNodePoolNodes", {
        "kubeId": args.kubeId,
        "name": args.name,
        "serviceName": args.serviceName,
    }, opts);
}

/**
 * A collection of arguments for invoking getKubeNodePoolNodes.
 */
export interface GetKubeNodePoolNodesArgs {
    /**
     * The ID of the managed kubernetes cluster.
     */
    kubeId: string;
    /**
     * Name of the node pool from which we want the nodes.
     */
    name: string;
    /**
     * The ID of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName: string;
}

/**
 * A collection of values returned by getKubeNodePoolNodes.
 */
export interface GetKubeNodePoolNodesResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * See Argument Reference above.
     */
    readonly kubeId: string;
    /**
     * Name of the node.
     */
    readonly name: string;
    /**
     * List of all nodes composing the kubernetes cluster.
     */
    readonly nodes: outputs.CloudProject.GetKubeNodePoolNodesNode[];
    /**
     * See Argument Reference above.
     */
    readonly serviceName: string;
}
/**
 * Use this data source to get a list of OVHcloud Managed Kubernetes nodes in a specific node pool.
 *
 * ## Example Usage
 */
export function getKubeNodePoolNodesOutput(args: GetKubeNodePoolNodesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetKubeNodePoolNodesResult> {
    return pulumi.output(args).apply((a: any) => getKubeNodePoolNodes(a, opts))
}

/**
 * A collection of arguments for invoking getKubeNodePoolNodes.
 */
export interface GetKubeNodePoolNodesOutputArgs {
    /**
     * The ID of the managed kubernetes cluster.
     */
    kubeId: pulumi.Input<string>;
    /**
     * Name of the node pool from which we want the nodes.
     */
    name: pulumi.Input<string>;
    /**
     * The ID of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName: pulumi.Input<string>;
}
