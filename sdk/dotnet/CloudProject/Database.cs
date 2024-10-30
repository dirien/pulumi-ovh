// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh.CloudProject
{
    /// <summary>
    /// ## Example Usage
    /// 
    /// Minimum settings for each engine (region choice is up to the user):
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ovh = Pulumi.Ovh;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var cassandradb = new Ovh.CloudProject.Database("cassandradb", new()
    ///     {
    ///         ServiceName = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    ///         Description = "my-first-cassandra",
    ///         Engine = "cassandra",
    ///         Version = "4.0",
    ///         Plan = "essential",
    ///         Nodes = new[]
    ///         {
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 Region = "BHS",
    ///             },
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 Region = "BHS",
    ///             },
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 Region = "BHS",
    ///             },
    ///         },
    ///         Flavor = "db1-4",
    ///     });
    /// 
    ///     var kafkadb = new Ovh.CloudProject.Database("kafkadb", new()
    ///     {
    ///         ServiceName = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    ///         Description = "my-first-kafka",
    ///         Engine = "kafka",
    ///         Version = "3.8",
    ///         Flavor = "db1-4",
    ///         Plan = "business",
    ///         KafkaRestApi = true,
    ///         KafkaSchemaRegistry = true,
    ///         Nodes = new[]
    ///         {
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 Region = "DE",
    ///             },
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 Region = "DE",
    ///             },
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 Region = "DE",
    ///             },
    ///         },
    ///     });
    /// 
    ///     var m3db = new Ovh.CloudProject.Database("m3db", new()
    ///     {
    ///         ServiceName = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    ///         Description = "my-first-m3db",
    ///         Engine = "m3db",
    ///         Version = "1.2",
    ///         Plan = "essential",
    ///         Nodes = new[]
    ///         {
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 Region = "BHS",
    ///             },
    ///         },
    ///         Flavor = "db1-7",
    ///     });
    /// 
    ///     var mongodb = new Ovh.CloudProject.Database("mongodb", new()
    ///     {
    ///         ServiceName = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    ///         Description = "my-first-mongodb",
    ///         Engine = "mongodb",
    ///         Version = "5.0",
    ///         Plan = "discovery",
    ///         Nodes = new[]
    ///         {
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 Region = "GRA",
    ///             },
    ///         },
    ///         Flavor = "db1-2",
    ///     });
    /// 
    ///     var mysqldb = new Ovh.CloudProject.Database("mysqldb", new()
    ///     {
    ///         ServiceName = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    ///         Description = "my-first-mysql",
    ///         Engine = "mysql",
    ///         Version = "8",
    ///         Plan = "essential",
    ///         Nodes = new[]
    ///         {
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 Region = "SBG",
    ///             },
    ///         },
    ///         Flavor = "db1-4",
    ///         AdvancedConfiguration = 
    ///         {
    ///             { "mysql.sql_mode", "ANSI,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION,NO_ZERO_DATE,NO_ZERO_IN_DATE,STRICT_ALL_TABLES" },
    ///             { "mysql.sql_require_primary_key", "true" },
    ///         },
    ///     });
    /// 
    ///     var opensearchdb = new Ovh.CloudProject.Database("opensearchdb", new()
    ///     {
    ///         ServiceName = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    ///         Description = "my-first-opensearch",
    ///         Engine = "opensearch",
    ///         Version = "1",
    ///         Plan = "essential",
    ///         OpensearchAclsEnabled = true,
    ///         Nodes = new[]
    ///         {
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 Region = "UK",
    ///             },
    ///         },
    ///         Flavor = "db1-4",
    ///     });
    /// 
    ///     var pgsqldb = new Ovh.CloudProject.Database("pgsqldb", new()
    ///     {
    ///         ServiceName = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    ///         Description = "my-first-postgresql",
    ///         Engine = "postgresql",
    ///         Version = "14",
    ///         Plan = "essential",
    ///         Nodes = new[]
    ///         {
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 Region = "WAW",
    ///             },
    ///         },
    ///         Flavor = "db1-4",
    ///         IpRestrictions = new[]
    ///         {
    ///             new Ovh.CloudProject.Inputs.DatabaseIpRestrictionArgs
    ///             {
    ///                 Description = "ip 1",
    ///                 Ip = "178.97.6.0/24",
    ///             },
    ///             new Ovh.CloudProject.Inputs.DatabaseIpRestrictionArgs
    ///             {
    ///                 Description = "ip 2",
    ///                 Ip = "178.97.7.0/24",
    ///             },
    ///         },
    ///     });
    /// 
    ///     var redisdb = new Ovh.CloudProject.Database("redisdb", new()
    ///     {
    ///         ServiceName = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    ///         Description = "my-first-redis",
    ///         Engine = "redis",
    ///         Version = "6.2",
    ///         Plan = "essential",
    ///         Nodes = new[]
    ///         {
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 Region = "BHS",
    ///             },
    ///         },
    ///         Flavor = "db1-4",
    ///     });
    /// 
    ///     var grafana = new Ovh.CloudProject.Database("grafana", new()
    ///     {
    ///         ServiceName = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    ///         Description = "my-first-grafana",
    ///         Engine = "grafana",
    ///         Version = "9.1",
    ///         Plan = "essential",
    ///         Nodes = new[]
    ///         {
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 Region = "GRA",
    ///             },
    ///         },
    ///         Flavor = "db1-4",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// To deploy a business PostgreSQL service with two nodes on public network:
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ovh = Pulumi.Ovh;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var postgresql = new Ovh.CloudProject.Database("postgresql", new()
    ///     {
    ///         Description = "my-first-postgresql",
    ///         Engine = "postgresql",
    ///         Flavor = "db1-15",
    ///         Nodes = new[]
    ///         {
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 Region = "GRA",
    ///             },
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 Region = "GRA",
    ///             },
    ///         },
    ///         Plan = "business",
    ///         ServiceName = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    ///         Version = "14",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// To deploy an enterprise MongoDB service with three nodes on private network:
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ovh = Pulumi.Ovh;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var mongodb = new Ovh.CloudProject.Database("mongodb", new()
    ///     {
    ///         Description = "my-first-mongodb",
    ///         Engine = "mongodb",
    ///         Flavor = "db1-30",
    ///         Nodes = new[]
    ///         {
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 NetworkId = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    ///                 Region = "SBG",
    ///                 SubnetId = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    ///             },
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 NetworkId = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    ///                 Region = "SBG",
    ///                 SubnetId = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    ///             },
    ///             new Ovh.CloudProject.Inputs.DatabaseNodeArgs
    ///             {
    ///                 NetworkId = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    ///                 Region = "SBG",
    ///                 SubnetId = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    ///             },
    ///         },
    ///         Plan = "production",
    ///         ServiceName = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    ///         Version = "5.0",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// OVHcloud Managed database clusters can be imported using the `service_name`, `engine`, `id` of the cluster, separated by "/" E.g.,
    /// 
    /// bash
    /// 
    /// ```sh
    /// $ pulumi import ovh:CloudProject/database:Database my_database_cluster service_name/engine/id
    /// ```
    /// </summary>
    [OvhResourceType("ovh:CloudProject/database:Database")]
    public partial class Database : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Advanced configuration key / value.
        /// </summary>
        [Output("advancedConfiguration")]
        public Output<ImmutableDictionary<string, string>> AdvancedConfiguration { get; private set; } = null!;

        /// <summary>
        /// List of region where backups are pushed. Not more than 1 regions for MongoDB. Not more than 2 regions for the other engines with one being the same as the nodes[].region field
        /// </summary>
        [Output("backupRegions")]
        public Output<ImmutableArray<string>> BackupRegions { get; private set; } = null!;

        /// <summary>
        /// Time on which backups start every day (this parameter is not usable on the following engines: "m3db", "grafana", "kafka", "kafkaconnect", "kafkamirrormaker", "opensearch", "m3aggregator").
        /// </summary>
        [Output("backupTime")]
        public Output<string> BackupTime { get; private set; } = null!;

        /// <summary>
        /// Date of the creation of the cluster.
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// Small description of the database service.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The disk size (in GB) of the database service.
        /// </summary>
        [Output("diskSize")]
        public Output<int> DiskSize { get; private set; } = null!;

        /// <summary>
        /// Defines the disk type of the database service.
        /// </summary>
        [Output("diskType")]
        public Output<string> DiskType { get; private set; } = null!;

        /// <summary>
        /// List of all endpoints objects of the service.
        /// </summary>
        [Output("endpoints")]
        public Output<ImmutableArray<Outputs.DatabaseEndpoint>> Endpoints { get; private set; } = null!;

        /// <summary>
        /// The database engine you want to deploy. To get a full list of available engine visit.
        /// [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
        /// </summary>
        [Output("engine")]
        public Output<string> Engine { get; private set; } = null!;

        /// <summary>
        /// A valid OVHcloud public cloud database flavor name in which the nodes will be started.
        /// Ex: "db1-7". Changing this value upgrade the nodes with the new flavor.
        /// You can find the list of flavor names: https://www.ovhcloud.com/fr/public-cloud/prices/
        /// </summary>
        [Output("flavor")]
        public Output<string> Flavor { get; private set; } = null!;

        /// <summary>
        /// IP Blocks authorized to access to the cluster.
        /// </summary>
        [Output("ipRestrictions")]
        public Output<ImmutableArray<Outputs.DatabaseIpRestriction>> IpRestrictions { get; private set; } = null!;

        /// <summary>
        /// Defines whether the REST API is enabled on a kafka cluster
        /// </summary>
        [Output("kafkaRestApi")]
        public Output<bool?> KafkaRestApi { get; private set; } = null!;

        /// <summary>
        /// Defines whether the schema registry is enabled on a Kafka cluster
        /// </summary>
        [Output("kafkaSchemaRegistry")]
        public Output<bool?> KafkaSchemaRegistry { get; private set; } = null!;

        /// <summary>
        /// Time on which maintenances can start every day.
        /// </summary>
        [Output("maintenanceTime")]
        public Output<string> MaintenanceTime { get; private set; } = null!;

        /// <summary>
        /// Type of network of the cluster.
        /// </summary>
        [Output("networkType")]
        public Output<string> NetworkType { get; private set; } = null!;

        /// <summary>
        /// List of nodes object.
        /// Multi region cluster are not yet available, all node should be identical.
        /// </summary>
        [Output("nodes")]
        public Output<ImmutableArray<Outputs.DatabaseNode>> Nodes { get; private set; } = null!;

        /// <summary>
        /// Defines whether the ACLs are enabled on an OpenSearch cluster
        /// </summary>
        [Output("opensearchAclsEnabled")]
        public Output<bool?> OpensearchAclsEnabled { get; private set; } = null!;

        /// <summary>
        /// Plan of the cluster.
        /// * MongoDB: Enum: "discovery", "production", "advanced".
        /// * Mysql, PosgreSQL, Cassandra, M3DB, : Enum: "essential", "business", "enterprise".
        /// * M3 Aggregator: "business", "enterprise".
        /// * Redis: "essential", "business"
        /// </summary>
        [Output("plan")]
        public Output<string> Plan { get; private set; } = null!;

        /// <summary>
        /// The id of the public cloud project. If omitted,
        /// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        /// </summary>
        [Output("serviceName")]
        public Output<string> ServiceName { get; private set; } = null!;

        /// <summary>
        /// Current status of the cluster.
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// The version of the engine in which the service should be deployed
        /// </summary>
        [Output("version")]
        public Output<string> Version { get; private set; } = null!;


        /// <summary>
        /// Create a Database resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Database(string name, DatabaseArgs args, CustomResourceOptions? options = null)
            : base("ovh:CloudProject/database:Database", name, args ?? new DatabaseArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Database(string name, Input<string> id, DatabaseState? state = null, CustomResourceOptions? options = null)
            : base("ovh:CloudProject/database:Database", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/ovh/pulumi-ovh",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Database resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Database Get(string name, Input<string> id, DatabaseState? state = null, CustomResourceOptions? options = null)
        {
            return new Database(name, id, state, options);
        }
    }

    public sealed class DatabaseArgs : global::Pulumi.ResourceArgs
    {
        [Input("advancedConfiguration")]
        private InputMap<string>? _advancedConfiguration;

        /// <summary>
        /// Advanced configuration key / value.
        /// </summary>
        public InputMap<string> AdvancedConfiguration
        {
            get => _advancedConfiguration ?? (_advancedConfiguration = new InputMap<string>());
            set => _advancedConfiguration = value;
        }

        [Input("backupRegions")]
        private InputList<string>? _backupRegions;

        /// <summary>
        /// List of region where backups are pushed. Not more than 1 regions for MongoDB. Not more than 2 regions for the other engines with one being the same as the nodes[].region field
        /// </summary>
        public InputList<string> BackupRegions
        {
            get => _backupRegions ?? (_backupRegions = new InputList<string>());
            set => _backupRegions = value;
        }

        /// <summary>
        /// Time on which backups start every day (this parameter is not usable on the following engines: "m3db", "grafana", "kafka", "kafkaconnect", "kafkamirrormaker", "opensearch", "m3aggregator").
        /// </summary>
        [Input("backupTime")]
        public Input<string>? BackupTime { get; set; }

        /// <summary>
        /// Small description of the database service.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The disk size (in GB) of the database service.
        /// </summary>
        [Input("diskSize")]
        public Input<int>? DiskSize { get; set; }

        /// <summary>
        /// The database engine you want to deploy. To get a full list of available engine visit.
        /// [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
        /// </summary>
        [Input("engine", required: true)]
        public Input<string> Engine { get; set; } = null!;

        /// <summary>
        /// A valid OVHcloud public cloud database flavor name in which the nodes will be started.
        /// Ex: "db1-7". Changing this value upgrade the nodes with the new flavor.
        /// You can find the list of flavor names: https://www.ovhcloud.com/fr/public-cloud/prices/
        /// </summary>
        [Input("flavor", required: true)]
        public Input<string> Flavor { get; set; } = null!;

        [Input("ipRestrictions")]
        private InputList<Inputs.DatabaseIpRestrictionArgs>? _ipRestrictions;

        /// <summary>
        /// IP Blocks authorized to access to the cluster.
        /// </summary>
        public InputList<Inputs.DatabaseIpRestrictionArgs> IpRestrictions
        {
            get => _ipRestrictions ?? (_ipRestrictions = new InputList<Inputs.DatabaseIpRestrictionArgs>());
            set => _ipRestrictions = value;
        }

        /// <summary>
        /// Defines whether the REST API is enabled on a kafka cluster
        /// </summary>
        [Input("kafkaRestApi")]
        public Input<bool>? KafkaRestApi { get; set; }

        /// <summary>
        /// Defines whether the schema registry is enabled on a Kafka cluster
        /// </summary>
        [Input("kafkaSchemaRegistry")]
        public Input<bool>? KafkaSchemaRegistry { get; set; }

        /// <summary>
        /// Time on which maintenances can start every day.
        /// </summary>
        [Input("maintenanceTime")]
        public Input<string>? MaintenanceTime { get; set; }

        [Input("nodes", required: true)]
        private InputList<Inputs.DatabaseNodeArgs>? _nodes;

        /// <summary>
        /// List of nodes object.
        /// Multi region cluster are not yet available, all node should be identical.
        /// </summary>
        public InputList<Inputs.DatabaseNodeArgs> Nodes
        {
            get => _nodes ?? (_nodes = new InputList<Inputs.DatabaseNodeArgs>());
            set => _nodes = value;
        }

        /// <summary>
        /// Defines whether the ACLs are enabled on an OpenSearch cluster
        /// </summary>
        [Input("opensearchAclsEnabled")]
        public Input<bool>? OpensearchAclsEnabled { get; set; }

        /// <summary>
        /// Plan of the cluster.
        /// * MongoDB: Enum: "discovery", "production", "advanced".
        /// * Mysql, PosgreSQL, Cassandra, M3DB, : Enum: "essential", "business", "enterprise".
        /// * M3 Aggregator: "business", "enterprise".
        /// * Redis: "essential", "business"
        /// </summary>
        [Input("plan", required: true)]
        public Input<string> Plan { get; set; } = null!;

        /// <summary>
        /// The id of the public cloud project. If omitted,
        /// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        /// <summary>
        /// The version of the engine in which the service should be deployed
        /// </summary>
        [Input("version", required: true)]
        public Input<string> Version { get; set; } = null!;

        public DatabaseArgs()
        {
        }
        public static new DatabaseArgs Empty => new DatabaseArgs();
    }

    public sealed class DatabaseState : global::Pulumi.ResourceArgs
    {
        [Input("advancedConfiguration")]
        private InputMap<string>? _advancedConfiguration;

        /// <summary>
        /// Advanced configuration key / value.
        /// </summary>
        public InputMap<string> AdvancedConfiguration
        {
            get => _advancedConfiguration ?? (_advancedConfiguration = new InputMap<string>());
            set => _advancedConfiguration = value;
        }

        [Input("backupRegions")]
        private InputList<string>? _backupRegions;

        /// <summary>
        /// List of region where backups are pushed. Not more than 1 regions for MongoDB. Not more than 2 regions for the other engines with one being the same as the nodes[].region field
        /// </summary>
        public InputList<string> BackupRegions
        {
            get => _backupRegions ?? (_backupRegions = new InputList<string>());
            set => _backupRegions = value;
        }

        /// <summary>
        /// Time on which backups start every day (this parameter is not usable on the following engines: "m3db", "grafana", "kafka", "kafkaconnect", "kafkamirrormaker", "opensearch", "m3aggregator").
        /// </summary>
        [Input("backupTime")]
        public Input<string>? BackupTime { get; set; }

        /// <summary>
        /// Date of the creation of the cluster.
        /// </summary>
        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        /// <summary>
        /// Small description of the database service.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The disk size (in GB) of the database service.
        /// </summary>
        [Input("diskSize")]
        public Input<int>? DiskSize { get; set; }

        /// <summary>
        /// Defines the disk type of the database service.
        /// </summary>
        [Input("diskType")]
        public Input<string>? DiskType { get; set; }

        [Input("endpoints")]
        private InputList<Inputs.DatabaseEndpointGetArgs>? _endpoints;

        /// <summary>
        /// List of all endpoints objects of the service.
        /// </summary>
        public InputList<Inputs.DatabaseEndpointGetArgs> Endpoints
        {
            get => _endpoints ?? (_endpoints = new InputList<Inputs.DatabaseEndpointGetArgs>());
            set => _endpoints = value;
        }

        /// <summary>
        /// The database engine you want to deploy. To get a full list of available engine visit.
        /// [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
        /// </summary>
        [Input("engine")]
        public Input<string>? Engine { get; set; }

        /// <summary>
        /// A valid OVHcloud public cloud database flavor name in which the nodes will be started.
        /// Ex: "db1-7". Changing this value upgrade the nodes with the new flavor.
        /// You can find the list of flavor names: https://www.ovhcloud.com/fr/public-cloud/prices/
        /// </summary>
        [Input("flavor")]
        public Input<string>? Flavor { get; set; }

        [Input("ipRestrictions")]
        private InputList<Inputs.DatabaseIpRestrictionGetArgs>? _ipRestrictions;

        /// <summary>
        /// IP Blocks authorized to access to the cluster.
        /// </summary>
        public InputList<Inputs.DatabaseIpRestrictionGetArgs> IpRestrictions
        {
            get => _ipRestrictions ?? (_ipRestrictions = new InputList<Inputs.DatabaseIpRestrictionGetArgs>());
            set => _ipRestrictions = value;
        }

        /// <summary>
        /// Defines whether the REST API is enabled on a kafka cluster
        /// </summary>
        [Input("kafkaRestApi")]
        public Input<bool>? KafkaRestApi { get; set; }

        /// <summary>
        /// Defines whether the schema registry is enabled on a Kafka cluster
        /// </summary>
        [Input("kafkaSchemaRegistry")]
        public Input<bool>? KafkaSchemaRegistry { get; set; }

        /// <summary>
        /// Time on which maintenances can start every day.
        /// </summary>
        [Input("maintenanceTime")]
        public Input<string>? MaintenanceTime { get; set; }

        /// <summary>
        /// Type of network of the cluster.
        /// </summary>
        [Input("networkType")]
        public Input<string>? NetworkType { get; set; }

        [Input("nodes")]
        private InputList<Inputs.DatabaseNodeGetArgs>? _nodes;

        /// <summary>
        /// List of nodes object.
        /// Multi region cluster are not yet available, all node should be identical.
        /// </summary>
        public InputList<Inputs.DatabaseNodeGetArgs> Nodes
        {
            get => _nodes ?? (_nodes = new InputList<Inputs.DatabaseNodeGetArgs>());
            set => _nodes = value;
        }

        /// <summary>
        /// Defines whether the ACLs are enabled on an OpenSearch cluster
        /// </summary>
        [Input("opensearchAclsEnabled")]
        public Input<bool>? OpensearchAclsEnabled { get; set; }

        /// <summary>
        /// Plan of the cluster.
        /// * MongoDB: Enum: "discovery", "production", "advanced".
        /// * Mysql, PosgreSQL, Cassandra, M3DB, : Enum: "essential", "business", "enterprise".
        /// * M3 Aggregator: "business", "enterprise".
        /// * Redis: "essential", "business"
        /// </summary>
        [Input("plan")]
        public Input<string>? Plan { get; set; }

        /// <summary>
        /// The id of the public cloud project. If omitted,
        /// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        /// </summary>
        [Input("serviceName")]
        public Input<string>? ServiceName { get; set; }

        /// <summary>
        /// Current status of the cluster.
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        /// <summary>
        /// The version of the engine in which the service should be deployed
        /// </summary>
        [Input("version")]
        public Input<string>? Version { get; set; }

        public DatabaseState()
        {
        }
        public static new DatabaseState Empty => new DatabaseState();
    }
}
