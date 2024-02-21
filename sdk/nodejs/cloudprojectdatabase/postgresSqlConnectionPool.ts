// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * ## Import
 *
 * OVHcloud Managed PostgreSQL clusters connection pools can be imported using the `service_name`, `cluster_id` and `id` of the connection pool, separated by "/" E.g.,
 *
 *  bash
 *
 * ```sh
 * $ pulumi import ovh:CloudProjectDatabase/postgresSqlConnectionPool:PostgresSqlConnectionPool my_connection_pool service_name/cluster_id/id
 * ```
 */
export class PostgresSqlConnectionPool extends pulumi.CustomResource {
    /**
     * Get an existing PostgresSqlConnectionPool resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PostgresSqlConnectionPoolState, opts?: pulumi.CustomResourceOptions): PostgresSqlConnectionPool {
        return new PostgresSqlConnectionPool(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:CloudProjectDatabase/postgresSqlConnectionPool:PostgresSqlConnectionPool';

    /**
     * Returns true if the given object is an instance of PostgresSqlConnectionPool.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PostgresSqlConnectionPool {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PostgresSqlConnectionPool.__pulumiType;
    }

    /**
     * Cluster ID.
     */
    public readonly clusterId!: pulumi.Output<string>;
    /**
     * Database ID for a database that belongs to the Database cluster given above.
     */
    public readonly databaseId!: pulumi.Output<string>;
    /**
     * Connection mode to the connection pool
     * Available modes:
     */
    public readonly mode!: pulumi.Output<string>;
    /**
     * Name of the connection pool.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Port of the connection pool.
     */
    public /*out*/ readonly port!: pulumi.Output<number>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    public readonly serviceName!: pulumi.Output<string>;
    /**
     * Size of the connection pool.
     */
    public readonly size!: pulumi.Output<number>;
    /**
     * Ssl connection mode for the pool.
     */
    public /*out*/ readonly sslMode!: pulumi.Output<string>;
    /**
     * Connection URI to the pool.
     */
    public /*out*/ readonly uri!: pulumi.Output<string>;
    /**
     * Database user authorized to connect to the pool, if none all the users are allowed.
     */
    public readonly userId!: pulumi.Output<string | undefined>;

    /**
     * Create a PostgresSqlConnectionPool resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PostgresSqlConnectionPoolArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PostgresSqlConnectionPoolArgs | PostgresSqlConnectionPoolState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as PostgresSqlConnectionPoolState | undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["databaseId"] = state ? state.databaseId : undefined;
            resourceInputs["mode"] = state ? state.mode : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["port"] = state ? state.port : undefined;
            resourceInputs["serviceName"] = state ? state.serviceName : undefined;
            resourceInputs["size"] = state ? state.size : undefined;
            resourceInputs["sslMode"] = state ? state.sslMode : undefined;
            resourceInputs["uri"] = state ? state.uri : undefined;
            resourceInputs["userId"] = state ? state.userId : undefined;
        } else {
            const args = argsOrState as PostgresSqlConnectionPoolArgs | undefined;
            if ((!args || args.clusterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterId'");
            }
            if ((!args || args.databaseId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'databaseId'");
            }
            if ((!args || args.mode === undefined) && !opts.urn) {
                throw new Error("Missing required property 'mode'");
            }
            if ((!args || args.serviceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceName'");
            }
            if ((!args || args.size === undefined) && !opts.urn) {
                throw new Error("Missing required property 'size'");
            }
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["databaseId"] = args ? args.databaseId : undefined;
            resourceInputs["mode"] = args ? args.mode : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["serviceName"] = args ? args.serviceName : undefined;
            resourceInputs["size"] = args ? args.size : undefined;
            resourceInputs["userId"] = args ? args.userId : undefined;
            resourceInputs["port"] = undefined /*out*/;
            resourceInputs["sslMode"] = undefined /*out*/;
            resourceInputs["uri"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(PostgresSqlConnectionPool.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PostgresSqlConnectionPool resources.
 */
export interface PostgresSqlConnectionPoolState {
    /**
     * Cluster ID.
     */
    clusterId?: pulumi.Input<string>;
    /**
     * Database ID for a database that belongs to the Database cluster given above.
     */
    databaseId?: pulumi.Input<string>;
    /**
     * Connection mode to the connection pool
     * Available modes:
     */
    mode?: pulumi.Input<string>;
    /**
     * Name of the connection pool.
     */
    name?: pulumi.Input<string>;
    /**
     * Port of the connection pool.
     */
    port?: pulumi.Input<number>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName?: pulumi.Input<string>;
    /**
     * Size of the connection pool.
     */
    size?: pulumi.Input<number>;
    /**
     * Ssl connection mode for the pool.
     */
    sslMode?: pulumi.Input<string>;
    /**
     * Connection URI to the pool.
     */
    uri?: pulumi.Input<string>;
    /**
     * Database user authorized to connect to the pool, if none all the users are allowed.
     */
    userId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a PostgresSqlConnectionPool resource.
 */
export interface PostgresSqlConnectionPoolArgs {
    /**
     * Cluster ID.
     */
    clusterId: pulumi.Input<string>;
    /**
     * Database ID for a database that belongs to the Database cluster given above.
     */
    databaseId: pulumi.Input<string>;
    /**
     * Connection mode to the connection pool
     * Available modes:
     */
    mode: pulumi.Input<string>;
    /**
     * Name of the connection pool.
     */
    name?: pulumi.Input<string>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName: pulumi.Input<string>;
    /**
     * Size of the connection pool.
     */
    size: pulumi.Input<number>;
    /**
     * Database user authorized to connect to the pool, if none all the users are allowed.
     */
    userId?: pulumi.Input<string>;
}
