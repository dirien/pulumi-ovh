// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Ovh.CloudProject
{
    /// <summary>
    /// ## Example Usage
    /// 
    /// Minimum settings for each engine (region choice is up to the user):
    /// 
    /// To deploy a business PostgreSQL service with two nodes on public network:
    /// 
    /// To deploy an enterprise MongoDB service with three nodes on private network:
    /// 
    /// ## Import
    /// 
    /// OVHcloud Managed database clusters can be imported using the `service_name`, `engine`, `id` of the cluster, separated by "/" E.g., bash &lt;break&gt;&lt;break&gt;```sh&lt;break&gt; $ pulumi import ovh:CloudProject/database:Database my_database_cluster service_name/engine/id &lt;break&gt;```&lt;break&gt;&lt;break&gt;
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
        /// Time on which backups start every day.
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
        /// Defines whether the REST API is enabled on a kafka cluster
        /// </summary>
        [Output("kafkaRestApi")]
        public Output<bool?> KafkaRestApi { get; private set; } = null!;

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
        /// Enum: "essential", "business", "enterprise".
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
                PluginDownloadURL = "github://api.github.com/dirien/pulumi-ovh",
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

        /// <summary>
        /// Defines whether the REST API is enabled on a kafka cluster
        /// </summary>
        [Input("kafkaRestApi")]
        public Input<bool>? KafkaRestApi { get; set; }

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
        /// Enum: "essential", "business", "enterprise".
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

        /// <summary>
        /// Time on which backups start every day.
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

        /// <summary>
        /// Defines whether the REST API is enabled on a kafka cluster
        /// </summary>
        [Input("kafkaRestApi")]
        public Input<bool>? KafkaRestApi { get; set; }

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
        /// Enum: "essential", "business", "enterprise".
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
