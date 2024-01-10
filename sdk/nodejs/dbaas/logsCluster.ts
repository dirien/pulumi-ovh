// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@ovh-devrelteam/pulumi-ovh";
 *
 * const ldp = new ovh.dbaas.LogsCluster("ldp", {
 *     archiveAllowedNetworks: ["10.0.0.0/16"],
 *     clusterId: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
 *     directInputAllowedNetworks: ["10.0.0.0/16"],
 *     queryAllowedNetworks: ["10.0.0.0/16"],
 *     serviceName: "ldp-xx-xxxxx",
 * });
 * ```
 *
 * ## Import
 *
 * OVHcloud DBaaS Log Data Platform clusters can be imported using the `service_name` and `cluster_id` of the cluster, separated by "/" E.g., bash
 *
 * ```sh
 *  $ pulumi import ovh:Dbaas/logsCluster:LogsCluster ldp service_name/cluster_id
 * ```
 */
export class LogsCluster extends pulumi.CustomResource {
    /**
     * Get an existing LogsCluster resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LogsClusterState, opts?: pulumi.CustomResourceOptions): LogsCluster {
        return new LogsCluster(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:Dbaas/logsCluster:LogsCluster';

    /**
     * Returns true if the given object is an instance of LogsCluster.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LogsCluster {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LogsCluster.__pulumiType;
    }

    /**
     * List of IP blocks
     */
    public readonly archiveAllowedNetworks!: pulumi.Output<string[] | undefined>;
    /**
     * Cluster ID. If not provided, the default clusterId is used
     */
    public readonly clusterId!: pulumi.Output<string | undefined>;
    /**
     * type of cluster (DEDICATED, PRO or TRIAL)
     */
    public /*out*/ readonly clusterType!: pulumi.Output<string>;
    /**
     * PEM for dedicated inputs
     */
    public /*out*/ readonly dedicatedInputPem!: pulumi.Output<string>;
    /**
     * List of IP blocks
     */
    public readonly directInputAllowedNetworks!: pulumi.Output<string[] | undefined>;
    /**
     * PEM for direct inputs
     */
    public /*out*/ readonly directInputPem!: pulumi.Output<string>;
    /**
     * cluster hostname hosting tenant
     */
    public /*out*/ readonly hostname!: pulumi.Output<string>;
    /**
     * Initial allowed networks for ARCHIVE flow type
     */
    public /*out*/ readonly initialArchiveAllowedNetworks!: pulumi.Output<string[]>;
    /**
     * Initial allowed networks for DIRECT_INPUT flow type
     */
    public /*out*/ readonly initialDirectInputAllowedNetworks!: pulumi.Output<string[]>;
    /**
     * Initial allowed networks for QUERY flow type
     */
    public /*out*/ readonly initialQueryAllowedNetworks!: pulumi.Output<string[]>;
    /**
     * true if all content generated by given service will be placed on this cluster
     */
    public /*out*/ readonly isDefault!: pulumi.Output<boolean>;
    /**
     * true if given service can perform advanced operations on cluster
     */
    public /*out*/ readonly isUnlocked!: pulumi.Output<boolean>;
    /**
     * List of IP blocks
     */
    public readonly queryAllowedNetworks!: pulumi.Output<string[] | undefined>;
    /**
     * datacenter localization
     */
    public /*out*/ readonly region!: pulumi.Output<string>;
    /**
     * The service name
     */
    public readonly serviceName!: pulumi.Output<string>;

    /**
     * Create a LogsCluster resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LogsClusterArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: LogsClusterArgs | LogsClusterState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as LogsClusterState | undefined;
            resourceInputs["archiveAllowedNetworks"] = state ? state.archiveAllowedNetworks : undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["clusterType"] = state ? state.clusterType : undefined;
            resourceInputs["dedicatedInputPem"] = state ? state.dedicatedInputPem : undefined;
            resourceInputs["directInputAllowedNetworks"] = state ? state.directInputAllowedNetworks : undefined;
            resourceInputs["directInputPem"] = state ? state.directInputPem : undefined;
            resourceInputs["hostname"] = state ? state.hostname : undefined;
            resourceInputs["initialArchiveAllowedNetworks"] = state ? state.initialArchiveAllowedNetworks : undefined;
            resourceInputs["initialDirectInputAllowedNetworks"] = state ? state.initialDirectInputAllowedNetworks : undefined;
            resourceInputs["initialQueryAllowedNetworks"] = state ? state.initialQueryAllowedNetworks : undefined;
            resourceInputs["isDefault"] = state ? state.isDefault : undefined;
            resourceInputs["isUnlocked"] = state ? state.isUnlocked : undefined;
            resourceInputs["queryAllowedNetworks"] = state ? state.queryAllowedNetworks : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["serviceName"] = state ? state.serviceName : undefined;
        } else {
            const args = argsOrState as LogsClusterArgs | undefined;
            if ((!args || args.serviceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceName'");
            }
            resourceInputs["archiveAllowedNetworks"] = args ? args.archiveAllowedNetworks : undefined;
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["directInputAllowedNetworks"] = args ? args.directInputAllowedNetworks : undefined;
            resourceInputs["queryAllowedNetworks"] = args ? args.queryAllowedNetworks : undefined;
            resourceInputs["serviceName"] = args ? args.serviceName : undefined;
            resourceInputs["clusterType"] = undefined /*out*/;
            resourceInputs["dedicatedInputPem"] = undefined /*out*/;
            resourceInputs["directInputPem"] = undefined /*out*/;
            resourceInputs["hostname"] = undefined /*out*/;
            resourceInputs["initialArchiveAllowedNetworks"] = undefined /*out*/;
            resourceInputs["initialDirectInputAllowedNetworks"] = undefined /*out*/;
            resourceInputs["initialQueryAllowedNetworks"] = undefined /*out*/;
            resourceInputs["isDefault"] = undefined /*out*/;
            resourceInputs["isUnlocked"] = undefined /*out*/;
            resourceInputs["region"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["dedicatedInputPem", "directInputPem", "initialArchiveAllowedNetworks", "initialDirectInputAllowedNetworks", "initialQueryAllowedNetworks"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(LogsCluster.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering LogsCluster resources.
 */
export interface LogsClusterState {
    /**
     * List of IP blocks
     */
    archiveAllowedNetworks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Cluster ID. If not provided, the default clusterId is used
     */
    clusterId?: pulumi.Input<string>;
    /**
     * type of cluster (DEDICATED, PRO or TRIAL)
     */
    clusterType?: pulumi.Input<string>;
    /**
     * PEM for dedicated inputs
     */
    dedicatedInputPem?: pulumi.Input<string>;
    /**
     * List of IP blocks
     */
    directInputAllowedNetworks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * PEM for direct inputs
     */
    directInputPem?: pulumi.Input<string>;
    /**
     * cluster hostname hosting tenant
     */
    hostname?: pulumi.Input<string>;
    /**
     * Initial allowed networks for ARCHIVE flow type
     */
    initialArchiveAllowedNetworks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Initial allowed networks for DIRECT_INPUT flow type
     */
    initialDirectInputAllowedNetworks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Initial allowed networks for QUERY flow type
     */
    initialQueryAllowedNetworks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * true if all content generated by given service will be placed on this cluster
     */
    isDefault?: pulumi.Input<boolean>;
    /**
     * true if given service can perform advanced operations on cluster
     */
    isUnlocked?: pulumi.Input<boolean>;
    /**
     * List of IP blocks
     */
    queryAllowedNetworks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * datacenter localization
     */
    region?: pulumi.Input<string>;
    /**
     * The service name
     */
    serviceName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a LogsCluster resource.
 */
export interface LogsClusterArgs {
    /**
     * List of IP blocks
     */
    archiveAllowedNetworks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Cluster ID. If not provided, the default clusterId is used
     */
    clusterId?: pulumi.Input<string>;
    /**
     * List of IP blocks
     */
    directInputAllowedNetworks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * List of IP blocks
     */
    queryAllowedNetworks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The service name
     */
    serviceName: pulumi.Input<string>;
}
