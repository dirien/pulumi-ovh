// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh.CloudProjectDatabase
{
    public static class GetDatabase
    {
        /// <summary>
        /// Use this data source to get the managed database of a public cloud project.
        /// 
        /// ## Example Usage
        /// 
        /// To get information of a database cluster service:
        /// 
        /// &lt;!--Start PulumiCodeChooser --&gt;
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ovh = Pulumi.Ovh;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var db = Ovh.CloudProjectDatabase.GetDatabase.Invoke(new()
        ///     {
        ///         ServiceName = "XXXXXX",
        ///         Engine = "YYYY",
        ///         Id = "ZZZZ",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["clusterId"] = db.Apply(getDatabaseResult =&gt; getDatabaseResult.Id),
        ///     };
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Task<GetDatabaseResult> InvokeAsync(GetDatabaseArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDatabaseResult>("ovh:CloudProjectDatabase/getDatabase:getDatabase", args ?? new GetDatabaseArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to get the managed database of a public cloud project.
        /// 
        /// ## Example Usage
        /// 
        /// To get information of a database cluster service:
        /// 
        /// &lt;!--Start PulumiCodeChooser --&gt;
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ovh = Pulumi.Ovh;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var db = Ovh.CloudProjectDatabase.GetDatabase.Invoke(new()
        ///     {
        ///         ServiceName = "XXXXXX",
        ///         Engine = "YYYY",
        ///         Id = "ZZZZ",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["clusterId"] = db.Apply(getDatabaseResult =&gt; getDatabaseResult.Id),
        ///     };
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Output<GetDatabaseResult> Invoke(GetDatabaseInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDatabaseResult>("ovh:CloudProjectDatabase/getDatabase:getDatabase", args ?? new GetDatabaseInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDatabaseArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The database engine you want to get information. To get a full list of available engine visit:
        /// [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
        /// </summary>
        [Input("engine", required: true)]
        public string Engine { get; set; } = null!;

        /// <summary>
        /// Cluster ID
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        /// <summary>
        /// The id of the public cloud project. If omitted,
        /// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        /// </summary>
        [Input("serviceName", required: true)]
        public string ServiceName { get; set; } = null!;

        public GetDatabaseArgs()
        {
        }
        public static new GetDatabaseArgs Empty => new GetDatabaseArgs();
    }

    public sealed class GetDatabaseInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The database engine you want to get information. To get a full list of available engine visit:
        /// [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
        /// </summary>
        [Input("engine", required: true)]
        public Input<string> Engine { get; set; } = null!;

        /// <summary>
        /// Cluster ID
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        /// <summary>
        /// The id of the public cloud project. If omitted,
        /// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        public GetDatabaseInvokeArgs()
        {
        }
        public static new GetDatabaseInvokeArgs Empty => new GetDatabaseInvokeArgs();
    }


    [OutputType]
    public sealed class GetDatabaseResult
    {
        /// <summary>
        /// Advanced configuration key / value.
        /// </summary>
        public readonly ImmutableDictionary<string, string> AdvancedConfiguration;
        /// <summary>
        /// List of region where backups are pushed.
        /// </summary>
        public readonly ImmutableArray<string> BackupRegions;
        /// <summary>
        /// Time on which backups start every day.
        /// </summary>
        public readonly string BackupTime;
        /// <summary>
        /// Date of the creation of the cluster.
        /// </summary>
        public readonly string CreatedAt;
        /// <summary>
        /// Description of the IP restriction
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The disk size (in GB) of the database service.
        /// </summary>
        public readonly int DiskSize;
        /// <summary>
        /// The disk type of the database service.
        /// </summary>
        public readonly string DiskType;
        /// <summary>
        /// List of all endpoints objects of the service.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetDatabaseEndpointResult> Endpoints;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string Engine;
        /// <summary>
        /// A valid OVHcloud public cloud database flavor name in which the nodes will be started.
        /// </summary>
        public readonly string Flavor;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// IP Blocks authorized to access to the cluster.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetDatabaseIpRestrictionResult> IpRestrictions;
        /// <summary>
        /// Defines whether the REST API is enabled on a kafka cluster.
        /// </summary>
        public readonly bool KafkaRestApi;
        /// <summary>
        /// Defines whether the schema registry is enabled on a Kafka cluster
        /// </summary>
        public readonly bool KafkaSchemaRegistry;
        /// <summary>
        /// Time on which maintenances can start every day.
        /// </summary>
        public readonly string MaintenanceTime;
        /// <summary>
        /// Type of network of the cluster.
        /// </summary>
        public readonly string NetworkType;
        /// <summary>
        /// List of nodes object.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetDatabaseNodeResult> Nodes;
        public readonly bool OpensearchAclsEnabled;
        /// <summary>
        /// Plan of the cluster.
        /// </summary>
        public readonly string Plan;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string ServiceName;
        /// <summary>
        /// Current status of the cluster.
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// The version of the engine in which the service should be deployed
        /// </summary>
        public readonly string Version;

        [OutputConstructor]
        private GetDatabaseResult(
            ImmutableDictionary<string, string> advancedConfiguration,

            ImmutableArray<string> backupRegions,

            string backupTime,

            string createdAt,

            string description,

            int diskSize,

            string diskType,

            ImmutableArray<Outputs.GetDatabaseEndpointResult> endpoints,

            string engine,

            string flavor,

            string id,

            ImmutableArray<Outputs.GetDatabaseIpRestrictionResult> ipRestrictions,

            bool kafkaRestApi,

            bool kafkaSchemaRegistry,

            string maintenanceTime,

            string networkType,

            ImmutableArray<Outputs.GetDatabaseNodeResult> nodes,

            bool opensearchAclsEnabled,

            string plan,

            string serviceName,

            string status,

            string version)
        {
            AdvancedConfiguration = advancedConfiguration;
            BackupRegions = backupRegions;
            BackupTime = backupTime;
            CreatedAt = createdAt;
            Description = description;
            DiskSize = diskSize;
            DiskType = diskType;
            Endpoints = endpoints;
            Engine = engine;
            Flavor = flavor;
            Id = id;
            IpRestrictions = ipRestrictions;
            KafkaRestApi = kafkaRestApi;
            KafkaSchemaRegistry = kafkaSchemaRegistry;
            MaintenanceTime = maintenanceTime;
            NetworkType = networkType;
            Nodes = nodes;
            OpensearchAclsEnabled = opensearchAclsEnabled;
            Plan = plan;
            ServiceName = serviceName;
            Status = status;
            Version = version;
        }
    }
}
