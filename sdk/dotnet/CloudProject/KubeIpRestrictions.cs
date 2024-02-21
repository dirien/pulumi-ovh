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
    /// Apply IP restrictions to an OVHcloud Managed Kubernetes cluster.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ovh = Pulumi.Ovh;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var vrackOnly = new Ovh.CloudProject.KubeIpRestrictions("vrackOnly", new()
    ///     {
    ///         Ips = new[]
    ///         {
    ///             "10.42.0.0/16",
    ///         },
    ///         KubeId = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx",
    ///         ServiceName = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// OVHcloud Managed Kubernetes Service cluster IP restrictions can be imported using the `service_name` and the `id` of the cluster, separated by "/" E.g.,
    /// 
    ///  bash
    /// 
    /// ```sh
    /// $ pulumi import ovh:CloudProject/kubeIpRestrictions:KubeIpRestrictions iprestrictions service_name/kube_id
    /// ```
    /// </summary>
    [OvhResourceType("ovh:CloudProject/kubeIpRestrictions:KubeIpRestrictions")]
    public partial class KubeIpRestrictions : global::Pulumi.CustomResource
    {
        /// <summary>
        /// List of CIDR authorized to interact with the managed Kubernetes cluster.
        /// </summary>
        [Output("ips")]
        public Output<ImmutableArray<string>> Ips { get; private set; } = null!;

        /// <summary>
        /// The id of the managed Kubernetes cluster. **Changing this value recreates the resource.**
        /// </summary>
        [Output("kubeId")]
        public Output<string> KubeId { get; private set; } = null!;

        /// <summary>
        /// The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        /// </summary>
        [Output("serviceName")]
        public Output<string> ServiceName { get; private set; } = null!;


        /// <summary>
        /// Create a KubeIpRestrictions resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public KubeIpRestrictions(string name, KubeIpRestrictionsArgs args, CustomResourceOptions? options = null)
            : base("ovh:CloudProject/kubeIpRestrictions:KubeIpRestrictions", name, args ?? new KubeIpRestrictionsArgs(), MakeResourceOptions(options, ""))
        {
        }

        private KubeIpRestrictions(string name, Input<string> id, KubeIpRestrictionsState? state = null, CustomResourceOptions? options = null)
            : base("ovh:CloudProject/kubeIpRestrictions:KubeIpRestrictions", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing KubeIpRestrictions resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static KubeIpRestrictions Get(string name, Input<string> id, KubeIpRestrictionsState? state = null, CustomResourceOptions? options = null)
        {
            return new KubeIpRestrictions(name, id, state, options);
        }
    }

    public sealed class KubeIpRestrictionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("ips", required: true)]
        private InputList<string>? _ips;

        /// <summary>
        /// List of CIDR authorized to interact with the managed Kubernetes cluster.
        /// </summary>
        public InputList<string> Ips
        {
            get => _ips ?? (_ips = new InputList<string>());
            set => _ips = value;
        }

        /// <summary>
        /// The id of the managed Kubernetes cluster. **Changing this value recreates the resource.**
        /// </summary>
        [Input("kubeId", required: true)]
        public Input<string> KubeId { get; set; } = null!;

        /// <summary>
        /// The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        public KubeIpRestrictionsArgs()
        {
        }
        public static new KubeIpRestrictionsArgs Empty => new KubeIpRestrictionsArgs();
    }

    public sealed class KubeIpRestrictionsState : global::Pulumi.ResourceArgs
    {
        [Input("ips")]
        private InputList<string>? _ips;

        /// <summary>
        /// List of CIDR authorized to interact with the managed Kubernetes cluster.
        /// </summary>
        public InputList<string> Ips
        {
            get => _ips ?? (_ips = new InputList<string>());
            set => _ips = value;
        }

        /// <summary>
        /// The id of the managed Kubernetes cluster. **Changing this value recreates the resource.**
        /// </summary>
        [Input("kubeId")]
        public Input<string>? KubeId { get; set; }

        /// <summary>
        /// The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
        /// </summary>
        [Input("serviceName")]
        public Input<string>? ServiceName { get; set; }

        public KubeIpRestrictionsState()
        {
        }
        public static new KubeIpRestrictionsState Empty => new KubeIpRestrictionsState();
    }
}
