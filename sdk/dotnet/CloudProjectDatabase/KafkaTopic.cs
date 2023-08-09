// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Ovh.CloudProjectDatabase
{
    /// <summary>
    /// Creates a topic for a kafka cluster associated with a public cloud project.
    /// 
    /// ## Example Usage
    /// 
    /// ## Import
    /// 
    /// OVHcloud Managed kafka clusters topics can be imported using the `service_name`, `cluster_id` and `id` of the topic, separated by "/" E.g., bash &lt;break&gt;&lt;break&gt;```sh&lt;break&gt; $ pulumi import ovh:CloudProjectDatabase/kafkaTopic:KafkaTopic my_topic service_name/cluster_id/id &lt;break&gt;```&lt;break&gt;&lt;break&gt;
    /// </summary>
    [OvhResourceType("ovh:CloudProjectDatabase/kafkaTopic:KafkaTopic")]
    public partial class KafkaTopic : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Cluster ID.
        /// </summary>
        [Output("clusterId")]
        public Output<string> ClusterId { get; private set; } = null!;

        /// <summary>
        /// Minimum insync replica accepted for this topic. Should be superior to 0
        /// </summary>
        [Output("minInsyncReplicas")]
        public Output<int> MinInsyncReplicas { get; private set; } = null!;

        /// <summary>
        /// Name of the topic. No spaces allowed.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Number of partitions for this topic. Should be superior to 0
        /// </summary>
        [Output("partitions")]
        public Output<int> Partitions { get; private set; } = null!;

        /// <summary>
        /// Number of replication for this topic. Should be superior to 1
        /// </summary>
        [Output("replication")]
        public Output<int> Replication { get; private set; } = null!;

        /// <summary>
        /// Number of bytes for the retention of the data for this topic. Inferior to 0 means unlimited
        /// </summary>
        [Output("retentionBytes")]
        public Output<int> RetentionBytes { get; private set; } = null!;

        /// <summary>
        /// Number of hours for the retention of the data for this topic. Should be superior to -2. Inferior to 0 means unlimited
        /// </summary>
        [Output("retentionHours")]
        public Output<int> RetentionHours { get; private set; } = null!;

        /// <summary>
        /// The id of the public cloud project. If omitted,
        /// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        /// </summary>
        [Output("serviceName")]
        public Output<string> ServiceName { get; private set; } = null!;


        /// <summary>
        /// Create a KafkaTopic resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public KafkaTopic(string name, KafkaTopicArgs args, CustomResourceOptions? options = null)
            : base("ovh:CloudProjectDatabase/kafkaTopic:KafkaTopic", name, args ?? new KafkaTopicArgs(), MakeResourceOptions(options, ""))
        {
        }

        private KafkaTopic(string name, Input<string> id, KafkaTopicState? state = null, CustomResourceOptions? options = null)
            : base("ovh:CloudProjectDatabase/kafkaTopic:KafkaTopic", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing KafkaTopic resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static KafkaTopic Get(string name, Input<string> id, KafkaTopicState? state = null, CustomResourceOptions? options = null)
        {
            return new KafkaTopic(name, id, state, options);
        }
    }

    public sealed class KafkaTopicArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Cluster ID.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// Minimum insync replica accepted for this topic. Should be superior to 0
        /// </summary>
        [Input("minInsyncReplicas")]
        public Input<int>? MinInsyncReplicas { get; set; }

        /// <summary>
        /// Name of the topic. No spaces allowed.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Number of partitions for this topic. Should be superior to 0
        /// </summary>
        [Input("partitions")]
        public Input<int>? Partitions { get; set; }

        /// <summary>
        /// Number of replication for this topic. Should be superior to 1
        /// </summary>
        [Input("replication")]
        public Input<int>? Replication { get; set; }

        /// <summary>
        /// Number of bytes for the retention of the data for this topic. Inferior to 0 means unlimited
        /// </summary>
        [Input("retentionBytes")]
        public Input<int>? RetentionBytes { get; set; }

        /// <summary>
        /// Number of hours for the retention of the data for this topic. Should be superior to -2. Inferior to 0 means unlimited
        /// </summary>
        [Input("retentionHours")]
        public Input<int>? RetentionHours { get; set; }

        /// <summary>
        /// The id of the public cloud project. If omitted,
        /// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        public KafkaTopicArgs()
        {
        }
        public static new KafkaTopicArgs Empty => new KafkaTopicArgs();
    }

    public sealed class KafkaTopicState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Cluster ID.
        /// </summary>
        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        /// <summary>
        /// Minimum insync replica accepted for this topic. Should be superior to 0
        /// </summary>
        [Input("minInsyncReplicas")]
        public Input<int>? MinInsyncReplicas { get; set; }

        /// <summary>
        /// Name of the topic. No spaces allowed.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Number of partitions for this topic. Should be superior to 0
        /// </summary>
        [Input("partitions")]
        public Input<int>? Partitions { get; set; }

        /// <summary>
        /// Number of replication for this topic. Should be superior to 1
        /// </summary>
        [Input("replication")]
        public Input<int>? Replication { get; set; }

        /// <summary>
        /// Number of bytes for the retention of the data for this topic. Inferior to 0 means unlimited
        /// </summary>
        [Input("retentionBytes")]
        public Input<int>? RetentionBytes { get; set; }

        /// <summary>
        /// Number of hours for the retention of the data for this topic. Should be superior to -2. Inferior to 0 means unlimited
        /// </summary>
        [Input("retentionHours")]
        public Input<int>? RetentionHours { get; set; }

        /// <summary>
        /// The id of the public cloud project. If omitted,
        /// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        /// </summary>
        [Input("serviceName")]
        public Input<string>? ServiceName { get; set; }

        public KafkaTopicState()
        {
        }
        public static new KafkaTopicState Empty => new KafkaTopicState();
    }
}
