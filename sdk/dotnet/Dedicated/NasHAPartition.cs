// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh.Dedicated
{
    /// <summary>
    /// Provides a resource for managing partitions on HA-NAS services
    /// 
    /// ## Example Usage
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
    ///     var my_partition = new Ovh.Dedicated.NasHAPartition("my-partition", new()
    ///     {
    ///         Protocol = "NFS",
    ///         ServiceName = "zpool-12345",
    ///         Size = 20,
    ///     });
    /// 
    /// });
    /// ```
    /// &lt;!--End PulumiCodeChooser --&gt;
    /// 
    /// ## Import
    /// 
    /// HA-NAS can be imported using the `{service_name}/{name}`, e.g.
    /// 
    /// ```sh
    /// $ pulumi import ovh:Dedicated/nasHAPartition:NasHAPartition my-partition zpool-12345/my-partition`
    /// ```
    /// </summary>
    [OvhResourceType("ovh:Dedicated/nasHAPartition:NasHAPartition")]
    public partial class NasHAPartition : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Percentage of partition space used in %!
        /// (MISSING)
        /// </summary>
        [Output("capacity")]
        public Output<int> Capacity { get; private set; } = null!;

        /// <summary>
        /// A brief description of the partition
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// name of the partition
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// one of "NFS", "CIFS" or "NFS_CIFS"
        /// </summary>
        [Output("protocol")]
        public Output<string> Protocol { get; private set; } = null!;

        /// <summary>
        /// The internal name of your HA-NAS (it has to be ordered via OVHcloud interface)
        /// </summary>
        [Output("serviceName")]
        public Output<string> ServiceName { get; private set; } = null!;

        /// <summary>
        /// size of the partition in GB
        /// </summary>
        [Output("size")]
        public Output<int> Size { get; private set; } = null!;

        /// <summary>
        /// Percentage of partition space used by snapshots in %!
        /// (MISSING)
        /// </summary>
        [Output("usedBySnapshots")]
        public Output<int> UsedBySnapshots { get; private set; } = null!;


        /// <summary>
        /// Create a NasHAPartition resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NasHAPartition(string name, NasHAPartitionArgs args, CustomResourceOptions? options = null)
            : base("ovh:Dedicated/nasHAPartition:NasHAPartition", name, args ?? new NasHAPartitionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private NasHAPartition(string name, Input<string> id, NasHAPartitionState? state = null, CustomResourceOptions? options = null)
            : base("ovh:Dedicated/nasHAPartition:NasHAPartition", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing NasHAPartition resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NasHAPartition Get(string name, Input<string> id, NasHAPartitionState? state = null, CustomResourceOptions? options = null)
        {
            return new NasHAPartition(name, id, state, options);
        }
    }

    public sealed class NasHAPartitionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A brief description of the partition
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// name of the partition
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// one of "NFS", "CIFS" or "NFS_CIFS"
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        /// <summary>
        /// The internal name of your HA-NAS (it has to be ordered via OVHcloud interface)
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        /// <summary>
        /// size of the partition in GB
        /// </summary>
        [Input("size", required: true)]
        public Input<int> Size { get; set; } = null!;

        public NasHAPartitionArgs()
        {
        }
        public static new NasHAPartitionArgs Empty => new NasHAPartitionArgs();
    }

    public sealed class NasHAPartitionState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Percentage of partition space used in %!
        /// (MISSING)
        /// </summary>
        [Input("capacity")]
        public Input<int>? Capacity { get; set; }

        /// <summary>
        /// A brief description of the partition
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// name of the partition
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// one of "NFS", "CIFS" or "NFS_CIFS"
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        /// <summary>
        /// The internal name of your HA-NAS (it has to be ordered via OVHcloud interface)
        /// </summary>
        [Input("serviceName")]
        public Input<string>? ServiceName { get; set; }

        /// <summary>
        /// size of the partition in GB
        /// </summary>
        [Input("size")]
        public Input<int>? Size { get; set; }

        /// <summary>
        /// Percentage of partition space used by snapshots in %!
        /// (MISSING)
        /// </summary>
        [Input("usedBySnapshots")]
        public Input<int>? UsedBySnapshots { get; set; }

        public NasHAPartitionState()
        {
        }
        public static new NasHAPartitionState Empty => new NasHAPartitionState();
    }
}
