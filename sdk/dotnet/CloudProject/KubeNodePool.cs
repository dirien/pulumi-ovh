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
    /// Creates a nodepool in a OVHcloud Managed Kubernetes Service cluster.
    /// 
    /// ## Example Usage
    /// 
    /// Create a simple node pool in your Kubernetes cluster:
    /// 
    /// Create an advanced node pool in your Kubernetes cluster:
    /// 
    /// ## Import
    /// 
    /// OVHcloud Managed Kubernetes Service cluster node pool can be imported using the `service_name`, the `id` of the cluster, and the `id` of the nodepool separated by "/" E.g., bash &lt;break&gt;&lt;break&gt;```sh&lt;break&gt; $ pulumi import ovh:CloudProject/kubeNodePool:KubeNodePool pool service_name/kube_id/poolid &lt;break&gt;```&lt;break&gt;&lt;break&gt;
    /// </summary>
    [OvhResourceType("ovh:CloudProject/kubeNodePool:KubeNodePool")]
    public partial class KubeNodePool : global::Pulumi.CustomResource
    {
        /// <summary>
        /// should the pool use the anti-affinity feature. Default to `false`. **Changing this value recreates the resource.**
        /// </summary>
        [Output("antiAffinity")]
        public Output<bool> AntiAffinity { get; private set; } = null!;

        /// <summary>
        /// Enable auto-scaling for the pool. Default to `false`.
        /// * `template ` - (Optional) Managed Kubernetes nodepool template, which is a complex object constituted by two main nested objects:
        /// </summary>
        [Output("autoscale")]
        public Output<bool> Autoscale { get; private set; } = null!;

        /// <summary>
        /// Number of nodes which are actually ready in the pool
        /// </summary>
        [Output("availableNodes")]
        public Output<int> AvailableNodes { get; private set; } = null!;

        /// <summary>
        /// Creation date
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// Number of nodes present in the pool
        /// </summary>
        [Output("currentNodes")]
        public Output<int> CurrentNodes { get; private set; } = null!;

        /// <summary>
        /// number of nodes to start.
        /// </summary>
        [Output("desiredNodes")]
        public Output<int> DesiredNodes { get; private set; } = null!;

        /// <summary>
        /// Flavor name
        /// </summary>
        [Output("flavor")]
        public Output<string> Flavor { get; private set; } = null!;

        /// <summary>
        /// a valid OVHcloud public cloud flavor ID in which the nodes will be started. Ex: "b2-7". You can find the list of flavor IDs: https://www.ovhcloud.com/fr/public-cloud/prices/.
        /// **Changing this value recreates the resource.**
        /// </summary>
        [Output("flavorName")]
        public Output<string> FlavorName { get; private set; } = null!;

        /// <summary>
        /// The id of the managed kubernetes cluster. **Changing this value recreates the resource.**
        /// </summary>
        [Output("kubeId")]
        public Output<string> KubeId { get; private set; } = null!;

        /// <summary>
        /// maximum number of nodes allowed in the pool. Setting `desired_nodes` over this value will raise an error.
        /// </summary>
        [Output("maxNodes")]
        public Output<int> MaxNodes { get; private set; } = null!;

        /// <summary>
        /// minimum number of nodes allowed in the pool. Setting `desired_nodes` under this value will raise an error.
        /// </summary>
        [Output("minNodes")]
        public Output<int> MinNodes { get; private set; } = null!;

        /// <summary>
        /// should the nodes be billed on a monthly basis. Default to `false`. **Changing this value recreates the resource.**
        /// </summary>
        [Output("monthlyBilled")]
        public Output<bool> MonthlyBilled { get; private set; } = null!;

        /// <summary>
        /// The name of the nodepool. Warning: `_` char is not allowed! **Changing this value recreates the resource.**
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Project id
        /// </summary>
        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

        /// <summary>
        /// The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        /// </summary>
        [Output("serviceName")]
        public Output<string> ServiceName { get; private set; } = null!;

        /// <summary>
        /// Status describing the state between number of nodes wanted and available ones
        /// </summary>
        [Output("sizeStatus")]
        public Output<string> SizeStatus { get; private set; } = null!;

        /// <summary>
        /// Current status
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// Node pool template
        /// </summary>
        [Output("template")]
        public Output<Outputs.KubeNodePoolTemplate?> Template { get; private set; } = null!;

        /// <summary>
        /// Number of nodes with the latest version installed in the pool
        /// </summary>
        [Output("upToDateNodes")]
        public Output<int> UpToDateNodes { get; private set; } = null!;

        /// <summary>
        /// Last update date
        /// </summary>
        [Output("updatedAt")]
        public Output<string> UpdatedAt { get; private set; } = null!;


        /// <summary>
        /// Create a KubeNodePool resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public KubeNodePool(string name, KubeNodePoolArgs args, CustomResourceOptions? options = null)
            : base("ovh:CloudProject/kubeNodePool:KubeNodePool", name, args ?? new KubeNodePoolArgs(), MakeResourceOptions(options, ""))
        {
        }

        private KubeNodePool(string name, Input<string> id, KubeNodePoolState? state = null, CustomResourceOptions? options = null)
            : base("ovh:CloudProject/kubeNodePool:KubeNodePool", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing KubeNodePool resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static KubeNodePool Get(string name, Input<string> id, KubeNodePoolState? state = null, CustomResourceOptions? options = null)
        {
            return new KubeNodePool(name, id, state, options);
        }
    }

    public sealed class KubeNodePoolArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// should the pool use the anti-affinity feature. Default to `false`. **Changing this value recreates the resource.**
        /// </summary>
        [Input("antiAffinity")]
        public Input<bool>? AntiAffinity { get; set; }

        /// <summary>
        /// Enable auto-scaling for the pool. Default to `false`.
        /// * `template ` - (Optional) Managed Kubernetes nodepool template, which is a complex object constituted by two main nested objects:
        /// </summary>
        [Input("autoscale")]
        public Input<bool>? Autoscale { get; set; }

        /// <summary>
        /// number of nodes to start.
        /// </summary>
        [Input("desiredNodes")]
        public Input<int>? DesiredNodes { get; set; }

        /// <summary>
        /// a valid OVHcloud public cloud flavor ID in which the nodes will be started. Ex: "b2-7". You can find the list of flavor IDs: https://www.ovhcloud.com/fr/public-cloud/prices/.
        /// **Changing this value recreates the resource.**
        /// </summary>
        [Input("flavorName", required: true)]
        public Input<string> FlavorName { get; set; } = null!;

        /// <summary>
        /// The id of the managed kubernetes cluster. **Changing this value recreates the resource.**
        /// </summary>
        [Input("kubeId", required: true)]
        public Input<string> KubeId { get; set; } = null!;

        /// <summary>
        /// maximum number of nodes allowed in the pool. Setting `desired_nodes` over this value will raise an error.
        /// </summary>
        [Input("maxNodes")]
        public Input<int>? MaxNodes { get; set; }

        /// <summary>
        /// minimum number of nodes allowed in the pool. Setting `desired_nodes` under this value will raise an error.
        /// </summary>
        [Input("minNodes")]
        public Input<int>? MinNodes { get; set; }

        /// <summary>
        /// should the nodes be billed on a monthly basis. Default to `false`. **Changing this value recreates the resource.**
        /// </summary>
        [Input("monthlyBilled")]
        public Input<bool>? MonthlyBilled { get; set; }

        /// <summary>
        /// The name of the nodepool. Warning: `_` char is not allowed! **Changing this value recreates the resource.**
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        /// <summary>
        /// Node pool template
        /// </summary>
        [Input("template")]
        public Input<Inputs.KubeNodePoolTemplateArgs>? Template { get; set; }

        public KubeNodePoolArgs()
        {
        }
        public static new KubeNodePoolArgs Empty => new KubeNodePoolArgs();
    }

    public sealed class KubeNodePoolState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// should the pool use the anti-affinity feature. Default to `false`. **Changing this value recreates the resource.**
        /// </summary>
        [Input("antiAffinity")]
        public Input<bool>? AntiAffinity { get; set; }

        /// <summary>
        /// Enable auto-scaling for the pool. Default to `false`.
        /// * `template ` - (Optional) Managed Kubernetes nodepool template, which is a complex object constituted by two main nested objects:
        /// </summary>
        [Input("autoscale")]
        public Input<bool>? Autoscale { get; set; }

        /// <summary>
        /// Number of nodes which are actually ready in the pool
        /// </summary>
        [Input("availableNodes")]
        public Input<int>? AvailableNodes { get; set; }

        /// <summary>
        /// Creation date
        /// </summary>
        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        /// <summary>
        /// Number of nodes present in the pool
        /// </summary>
        [Input("currentNodes")]
        public Input<int>? CurrentNodes { get; set; }

        /// <summary>
        /// number of nodes to start.
        /// </summary>
        [Input("desiredNodes")]
        public Input<int>? DesiredNodes { get; set; }

        /// <summary>
        /// Flavor name
        /// </summary>
        [Input("flavor")]
        public Input<string>? Flavor { get; set; }

        /// <summary>
        /// a valid OVHcloud public cloud flavor ID in which the nodes will be started. Ex: "b2-7". You can find the list of flavor IDs: https://www.ovhcloud.com/fr/public-cloud/prices/.
        /// **Changing this value recreates the resource.**
        /// </summary>
        [Input("flavorName")]
        public Input<string>? FlavorName { get; set; }

        /// <summary>
        /// The id of the managed kubernetes cluster. **Changing this value recreates the resource.**
        /// </summary>
        [Input("kubeId")]
        public Input<string>? KubeId { get; set; }

        /// <summary>
        /// maximum number of nodes allowed in the pool. Setting `desired_nodes` over this value will raise an error.
        /// </summary>
        [Input("maxNodes")]
        public Input<int>? MaxNodes { get; set; }

        /// <summary>
        /// minimum number of nodes allowed in the pool. Setting `desired_nodes` under this value will raise an error.
        /// </summary>
        [Input("minNodes")]
        public Input<int>? MinNodes { get; set; }

        /// <summary>
        /// should the nodes be billed on a monthly basis. Default to `false`. **Changing this value recreates the resource.**
        /// </summary>
        [Input("monthlyBilled")]
        public Input<bool>? MonthlyBilled { get; set; }

        /// <summary>
        /// The name of the nodepool. Warning: `_` char is not allowed! **Changing this value recreates the resource.**
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Project id
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        /// <summary>
        /// The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        /// </summary>
        [Input("serviceName")]
        public Input<string>? ServiceName { get; set; }

        /// <summary>
        /// Status describing the state between number of nodes wanted and available ones
        /// </summary>
        [Input("sizeStatus")]
        public Input<string>? SizeStatus { get; set; }

        /// <summary>
        /// Current status
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        /// <summary>
        /// Node pool template
        /// </summary>
        [Input("template")]
        public Input<Inputs.KubeNodePoolTemplateGetArgs>? Template { get; set; }

        /// <summary>
        /// Number of nodes with the latest version installed in the pool
        /// </summary>
        [Input("upToDateNodes")]
        public Input<int>? UpToDateNodes { get; set; }

        /// <summary>
        /// Last update date
        /// </summary>
        [Input("updatedAt")]
        public Input<string>? UpdatedAt { get; set; }

        public KubeNodePoolState()
        {
        }
        public static new KubeNodePoolState Empty => new KubeNodePoolState();
    }
}
