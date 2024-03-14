// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * ## Example Usage
 *
 * Minimum settings for each engine (region choice is up to the user):
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@ovhcloud/pulumi-ovh";
 *
 * const cassandradb = new ovh.cloudproject.Database("cassandradb", {
 *     serviceName: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
 *     description: "my-first-cassandra",
 *     engine: "cassandra",
 *     version: "4.0",
 *     plan: "essential",
 *     nodes: [
 *         {
 *             region: "BHS",
 *         },
 *         {
 *             region: "BHS",
 *         },
 *         {
 *             region: "BHS",
 *         },
 *     ],
 *     flavor: "db1-4",
 * });
 * const kafkadb = new ovh.cloudproject.Database("kafkadb", {
 *     serviceName: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
 *     description: "my-first-kafka",
 *     engine: "kafka",
 *     version: "3.4",
 *     plan: "business",
 *     kafkaRestApi: true,
 *     nodes: [
 *         {
 *             region: "DE",
 *         },
 *         {
 *             region: "DE",
 *         },
 *         {
 *             region: "DE",
 *         },
 *     ],
 *     flavor: "db1-4",
 * });
 * const m3db = new ovh.cloudproject.Database("m3db", {
 *     serviceName: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
 *     description: "my-first-m3db",
 *     engine: "m3db",
 *     version: "1.2",
 *     plan: "essential",
 *     nodes: [{
 *         region: "BHS",
 *     }],
 *     flavor: "db1-7",
 * });
 * const mongodb = new ovh.cloudproject.Database("mongodb", {
 *     serviceName: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
 *     description: "my-first-mongodb",
 *     engine: "mongodb",
 *     version: "5.0",
 *     plan: "discovery",
 *     nodes: [{
 *         region: "GRA",
 *     }],
 *     flavor: "db1-2",
 * });
 * const mysqldb = new ovh.cloudproject.Database("mysqldb", {
 *     serviceName: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
 *     description: "my-first-mysql",
 *     engine: "mysql",
 *     version: "8",
 *     plan: "essential",
 *     nodes: [{
 *         region: "SBG",
 *     }],
 *     flavor: "db1-4",
 *     advancedConfiguration: {
 *         "mysql.sql_mode": "ANSI,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION,NO_ZERO_DATE,NO_ZERO_IN_DATE,STRICT_ALL_TABLES",
 *         "mysql.sql_require_primary_key": "true",
 *     },
 * });
 * const opensearchdb = new ovh.cloudproject.Database("opensearchdb", {
 *     serviceName: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
 *     description: "my-first-opensearch",
 *     engine: "opensearch",
 *     version: "1",
 *     plan: "essential",
 *     opensearchAclsEnabled: true,
 *     nodes: [{
 *         region: "UK",
 *     }],
 *     flavor: "db1-4",
 * });
 * const pgsqldb = new ovh.cloudproject.Database("pgsqldb", {
 *     serviceName: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
 *     description: "my-first-postgresql",
 *     engine: "postgresql",
 *     version: "14",
 *     plan: "essential",
 *     nodes: [{
 *         region: "WAW",
 *     }],
 *     flavor: "db1-4",
 * });
 * const redisdb = new ovh.cloudproject.Database("redisdb", {
 *     serviceName: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
 *     description: "my-first-redis",
 *     engine: "redis",
 *     version: "6.2",
 *     plan: "essential",
 *     nodes: [{
 *         region: "BHS",
 *     }],
 *     flavor: "db1-4",
 * });
 * const grafana = new ovh.cloudproject.Database("grafana", {
 *     serviceName: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
 *     description: "my-first-grafana",
 *     engine: "grafana",
 *     version: "9.1",
 *     plan: "essential",
 *     nodes: [{
 *         region: "GRA",
 *     }],
 *     flavor: "db1-4",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 *
 * To deploy a business PostgreSQL service with two nodes on public network:
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@ovhcloud/pulumi-ovh";
 *
 * const postgresql = new ovh.cloudproject.Database("postgresql", {
 *     description: "my-first-postgresql",
 *     engine: "postgresql",
 *     flavor: "db1-15",
 *     nodes: [
 *         {
 *             region: "GRA",
 *         },
 *         {
 *             region: "GRA",
 *         },
 *     ],
 *     plan: "business",
 *     serviceName: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
 *     version: "14",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 *
 * To deploy an enterprise MongoDB service with three nodes on private network:
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@ovhcloud/pulumi-ovh";
 *
 * const mongodb = new ovh.cloudproject.Database("mongodb", {
 *     description: "my-first-mongodb",
 *     engine: "mongodb",
 *     flavor: "db1-30",
 *     nodes: [
 *         {
 *             networkId: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
 *             region: "SBG",
 *             subnetId: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
 *         },
 *         {
 *             networkId: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
 *             region: "SBG",
 *             subnetId: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
 *         },
 *         {
 *             networkId: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
 *             region: "SBG",
 *             subnetId: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
 *         },
 *     ],
 *     plan: "production",
 *     serviceName: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
 *     version: "5.0",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 *
 * ## Import
 *
 * OVHcloud Managed database clusters can be imported using the `service_name`, `engine`, `id` of the cluster, separated by "/" E.g.,
 *
 * bash
 *
 * ```sh
 * $ pulumi import ovh:CloudProject/database:Database my_database_cluster service_name/engine/id
 * ```
 */
export class Database extends pulumi.CustomResource {
    /**
     * Get an existing Database resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseState, opts?: pulumi.CustomResourceOptions): Database {
        return new Database(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:CloudProject/database:Database';

    /**
     * Returns true if the given object is an instance of Database.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Database {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Database.__pulumiType;
    }

    /**
     * Advanced configuration key / value.
     */
    public readonly advancedConfiguration!: pulumi.Output<{[key: string]: string}>;
    /**
     * List of region where backups are pushed. Not more than 1 regions for MongoDB. Not more than 2 regions for the other engines with one being the same as the nodes[].region field
     */
    public readonly backupRegions!: pulumi.Output<string[]>;
    /**
     * Time on which backups start every day.
     */
    public readonly backupTime!: pulumi.Output<string>;
    /**
     * Date of the creation of the cluster.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * Small description of the database service.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The disk size (in GB) of the database service.
     */
    public readonly diskSize!: pulumi.Output<number>;
    /**
     * Defines the disk type of the database service.
     */
    public /*out*/ readonly diskType!: pulumi.Output<string>;
    /**
     * List of all endpoints objects of the service.
     */
    public /*out*/ readonly endpoints!: pulumi.Output<outputs.CloudProject.DatabaseEndpoint[]>;
    /**
     * The database engine you want to deploy. To get a full list of available engine visit.
     * [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
     */
    public readonly engine!: pulumi.Output<string>;
    /**
     * A valid OVHcloud public cloud database flavor name in which the nodes will be started.
     * Ex: "db1-7". Changing this value upgrade the nodes with the new flavor.
     * You can find the list of flavor names: https://www.ovhcloud.com/fr/public-cloud/prices/
     */
    public readonly flavor!: pulumi.Output<string>;
    /**
     * Defines whether the REST API is enabled on a kafka cluster
     */
    public readonly kafkaRestApi!: pulumi.Output<boolean | undefined>;
    /**
     * Time on which maintenances can start every day.
     */
    public /*out*/ readonly maintenanceTime!: pulumi.Output<string>;
    /**
     * Type of network of the cluster.
     */
    public /*out*/ readonly networkType!: pulumi.Output<string>;
    /**
     * List of nodes object.
     * Multi region cluster are not yet available, all node should be identical.
     */
    public readonly nodes!: pulumi.Output<outputs.CloudProject.DatabaseNode[]>;
    /**
     * Defines whether the ACLs are enabled on an OpenSearch cluster
     */
    public readonly opensearchAclsEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * Plan of the cluster.
     * * MongoDB: Enum: "discovery", "production", "advanced".
     * * Mysql, PosgreSQL, Cassandra, M3DB, : Enum: "essential", "business", "enterprise".
     * * M3 Aggregator: "business", "enterprise".
     * * Redis: "essential", "business"
     */
    public readonly plan!: pulumi.Output<string>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    public readonly serviceName!: pulumi.Output<string>;
    /**
     * Current status of the cluster.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * The version of the engine in which the service should be deployed
     */
    public readonly version!: pulumi.Output<string>;

    /**
     * Create a Database resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DatabaseArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DatabaseArgs | DatabaseState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DatabaseState | undefined;
            resourceInputs["advancedConfiguration"] = state ? state.advancedConfiguration : undefined;
            resourceInputs["backupRegions"] = state ? state.backupRegions : undefined;
            resourceInputs["backupTime"] = state ? state.backupTime : undefined;
            resourceInputs["createdAt"] = state ? state.createdAt : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["diskSize"] = state ? state.diskSize : undefined;
            resourceInputs["diskType"] = state ? state.diskType : undefined;
            resourceInputs["endpoints"] = state ? state.endpoints : undefined;
            resourceInputs["engine"] = state ? state.engine : undefined;
            resourceInputs["flavor"] = state ? state.flavor : undefined;
            resourceInputs["kafkaRestApi"] = state ? state.kafkaRestApi : undefined;
            resourceInputs["maintenanceTime"] = state ? state.maintenanceTime : undefined;
            resourceInputs["networkType"] = state ? state.networkType : undefined;
            resourceInputs["nodes"] = state ? state.nodes : undefined;
            resourceInputs["opensearchAclsEnabled"] = state ? state.opensearchAclsEnabled : undefined;
            resourceInputs["plan"] = state ? state.plan : undefined;
            resourceInputs["serviceName"] = state ? state.serviceName : undefined;
            resourceInputs["status"] = state ? state.status : undefined;
            resourceInputs["version"] = state ? state.version : undefined;
        } else {
            const args = argsOrState as DatabaseArgs | undefined;
            if ((!args || args.engine === undefined) && !opts.urn) {
                throw new Error("Missing required property 'engine'");
            }
            if ((!args || args.flavor === undefined) && !opts.urn) {
                throw new Error("Missing required property 'flavor'");
            }
            if ((!args || args.nodes === undefined) && !opts.urn) {
                throw new Error("Missing required property 'nodes'");
            }
            if ((!args || args.plan === undefined) && !opts.urn) {
                throw new Error("Missing required property 'plan'");
            }
            if ((!args || args.serviceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceName'");
            }
            if ((!args || args.version === undefined) && !opts.urn) {
                throw new Error("Missing required property 'version'");
            }
            resourceInputs["advancedConfiguration"] = args ? args.advancedConfiguration : undefined;
            resourceInputs["backupRegions"] = args ? args.backupRegions : undefined;
            resourceInputs["backupTime"] = args ? args.backupTime : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["diskSize"] = args ? args.diskSize : undefined;
            resourceInputs["engine"] = args ? args.engine : undefined;
            resourceInputs["flavor"] = args ? args.flavor : undefined;
            resourceInputs["kafkaRestApi"] = args ? args.kafkaRestApi : undefined;
            resourceInputs["nodes"] = args ? args.nodes : undefined;
            resourceInputs["opensearchAclsEnabled"] = args ? args.opensearchAclsEnabled : undefined;
            resourceInputs["plan"] = args ? args.plan : undefined;
            resourceInputs["serviceName"] = args ? args.serviceName : undefined;
            resourceInputs["version"] = args ? args.version : undefined;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["diskType"] = undefined /*out*/;
            resourceInputs["endpoints"] = undefined /*out*/;
            resourceInputs["maintenanceTime"] = undefined /*out*/;
            resourceInputs["networkType"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Database.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Database resources.
 */
export interface DatabaseState {
    /**
     * Advanced configuration key / value.
     */
    advancedConfiguration?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * List of region where backups are pushed. Not more than 1 regions for MongoDB. Not more than 2 regions for the other engines with one being the same as the nodes[].region field
     */
    backupRegions?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Time on which backups start every day.
     */
    backupTime?: pulumi.Input<string>;
    /**
     * Date of the creation of the cluster.
     */
    createdAt?: pulumi.Input<string>;
    /**
     * Small description of the database service.
     */
    description?: pulumi.Input<string>;
    /**
     * The disk size (in GB) of the database service.
     */
    diskSize?: pulumi.Input<number>;
    /**
     * Defines the disk type of the database service.
     */
    diskType?: pulumi.Input<string>;
    /**
     * List of all endpoints objects of the service.
     */
    endpoints?: pulumi.Input<pulumi.Input<inputs.CloudProject.DatabaseEndpoint>[]>;
    /**
     * The database engine you want to deploy. To get a full list of available engine visit.
     * [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
     */
    engine?: pulumi.Input<string>;
    /**
     * A valid OVHcloud public cloud database flavor name in which the nodes will be started.
     * Ex: "db1-7". Changing this value upgrade the nodes with the new flavor.
     * You can find the list of flavor names: https://www.ovhcloud.com/fr/public-cloud/prices/
     */
    flavor?: pulumi.Input<string>;
    /**
     * Defines whether the REST API is enabled on a kafka cluster
     */
    kafkaRestApi?: pulumi.Input<boolean>;
    /**
     * Time on which maintenances can start every day.
     */
    maintenanceTime?: pulumi.Input<string>;
    /**
     * Type of network of the cluster.
     */
    networkType?: pulumi.Input<string>;
    /**
     * List of nodes object.
     * Multi region cluster are not yet available, all node should be identical.
     */
    nodes?: pulumi.Input<pulumi.Input<inputs.CloudProject.DatabaseNode>[]>;
    /**
     * Defines whether the ACLs are enabled on an OpenSearch cluster
     */
    opensearchAclsEnabled?: pulumi.Input<boolean>;
    /**
     * Plan of the cluster.
     * * MongoDB: Enum: "discovery", "production", "advanced".
     * * Mysql, PosgreSQL, Cassandra, M3DB, : Enum: "essential", "business", "enterprise".
     * * M3 Aggregator: "business", "enterprise".
     * * Redis: "essential", "business"
     */
    plan?: pulumi.Input<string>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName?: pulumi.Input<string>;
    /**
     * Current status of the cluster.
     */
    status?: pulumi.Input<string>;
    /**
     * The version of the engine in which the service should be deployed
     */
    version?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Database resource.
 */
export interface DatabaseArgs {
    /**
     * Advanced configuration key / value.
     */
    advancedConfiguration?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * List of region where backups are pushed. Not more than 1 regions for MongoDB. Not more than 2 regions for the other engines with one being the same as the nodes[].region field
     */
    backupRegions?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Time on which backups start every day.
     */
    backupTime?: pulumi.Input<string>;
    /**
     * Small description of the database service.
     */
    description?: pulumi.Input<string>;
    /**
     * The disk size (in GB) of the database service.
     */
    diskSize?: pulumi.Input<number>;
    /**
     * The database engine you want to deploy. To get a full list of available engine visit.
     * [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
     */
    engine: pulumi.Input<string>;
    /**
     * A valid OVHcloud public cloud database flavor name in which the nodes will be started.
     * Ex: "db1-7". Changing this value upgrade the nodes with the new flavor.
     * You can find the list of flavor names: https://www.ovhcloud.com/fr/public-cloud/prices/
     */
    flavor: pulumi.Input<string>;
    /**
     * Defines whether the REST API is enabled on a kafka cluster
     */
    kafkaRestApi?: pulumi.Input<boolean>;
    /**
     * List of nodes object.
     * Multi region cluster are not yet available, all node should be identical.
     */
    nodes: pulumi.Input<pulumi.Input<inputs.CloudProject.DatabaseNode>[]>;
    /**
     * Defines whether the ACLs are enabled on an OpenSearch cluster
     */
    opensearchAclsEnabled?: pulumi.Input<boolean>;
    /**
     * Plan of the cluster.
     * * MongoDB: Enum: "discovery", "production", "advanced".
     * * Mysql, PosgreSQL, Cassandra, M3DB, : Enum: "essential", "business", "enterprise".
     * * M3 Aggregator: "business", "enterprise".
     * * Redis: "essential", "business"
     */
    plan: pulumi.Input<string>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName: pulumi.Input<string>;
    /**
     * The version of the engine in which the service should be deployed
     */
    version: pulumi.Input<string>;
}
