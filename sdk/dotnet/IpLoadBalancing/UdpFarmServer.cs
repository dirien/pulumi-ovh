// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh.IpLoadBalancing
{
    /// <summary>
    /// Creates a backend server entry linked to loadbalancing group (farm)
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
    ///     var lb = Ovh.IpLoadBalancing.GetIpLoadBalancing.Invoke(new()
    ///     {
    ///         ServiceName = "ip-1.2.3.4",
    ///         State = "ok",
    ///     });
    /// 
    ///     var farmname = new Ovh.IpLoadBalancing.UdpFarm("farmname", new()
    ///     {
    ///         DisplayName = "ingress-8080-gra",
    ///         Port = 80,
    ///         ServiceName = lb.Apply(getIpLoadBalancingResult =&gt; getIpLoadBalancingResult.ServiceName),
    ///         Zone = "gra",
    ///     });
    /// 
    ///     var backend = new Ovh.IpLoadBalancing.UdpFarmServer("backend", new()
    ///     {
    ///         Address = "4.5.6.7",
    ///         DisplayName = "mybackend",
    ///         FarmId = farmname.FarmId,
    ///         Port = 80,
    ///         ServiceName = lb.Apply(getIpLoadBalancingResult =&gt; getIpLoadBalancingResult.ServiceName),
    ///         Status = "active",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// UDP farm server can be imported using the following format `service_name`, the `id` of the farm and the `id` of the server separated by "/" e.g.
    /// </summary>
    [OvhResourceType("ovh:IpLoadBalancing/udpFarmServer:UdpFarmServer")]
    public partial class UdpFarmServer : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Address of the backend server (IP from either internal or OVHcloud network)
        /// </summary>
        [Output("address")]
        public Output<string> Address { get; private set; } = null!;

        /// <summary>
        /// Synonym for `farm_id`.
        /// </summary>
        [Output("backendId")]
        public Output<double> BackendId { get; private set; } = null!;

        /// <summary>
        /// Label for the server
        /// </summary>
        [Output("displayName")]
        public Output<string?> DisplayName { get; private set; } = null!;

        /// <summary>
        /// ID of the farm this server is attached to
        /// </summary>
        [Output("farmId")]
        public Output<double> FarmId { get; private set; } = null!;

        /// <summary>
        /// Port that backend will respond on
        /// </summary>
        [Output("port")]
        public Output<double?> Port { get; private set; } = null!;

        /// <summary>
        /// Id of your server.
        /// </summary>
        [Output("serverId")]
        public Output<double> ServerId { get; private set; } = null!;

        /// <summary>
        /// The internal name of your IP load balancing
        /// </summary>
        [Output("serviceName")]
        public Output<string> ServiceName { get; private set; } = null!;

        /// <summary>
        /// backend status - `active` or `inactive`
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;


        /// <summary>
        /// Create a UdpFarmServer resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public UdpFarmServer(string name, UdpFarmServerArgs args, CustomResourceOptions? options = null)
            : base("ovh:IpLoadBalancing/udpFarmServer:UdpFarmServer", name, args ?? new UdpFarmServerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private UdpFarmServer(string name, Input<string> id, UdpFarmServerState? state = null, CustomResourceOptions? options = null)
            : base("ovh:IpLoadBalancing/udpFarmServer:UdpFarmServer", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing UdpFarmServer resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static UdpFarmServer Get(string name, Input<string> id, UdpFarmServerState? state = null, CustomResourceOptions? options = null)
        {
            return new UdpFarmServer(name, id, state, options);
        }
    }

    public sealed class UdpFarmServerArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Address of the backend server (IP from either internal or OVHcloud network)
        /// </summary>
        [Input("address", required: true)]
        public Input<string> Address { get; set; } = null!;

        /// <summary>
        /// Label for the server
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// ID of the farm this server is attached to
        /// </summary>
        [Input("farmId", required: true)]
        public Input<double> FarmId { get; set; } = null!;

        /// <summary>
        /// Port that backend will respond on
        /// </summary>
        [Input("port")]
        public Input<double>? Port { get; set; }

        /// <summary>
        /// The internal name of your IP load balancing
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        /// <summary>
        /// backend status - `active` or `inactive`
        /// </summary>
        [Input("status", required: true)]
        public Input<string> Status { get; set; } = null!;

        public UdpFarmServerArgs()
        {
        }
        public static new UdpFarmServerArgs Empty => new UdpFarmServerArgs();
    }

    public sealed class UdpFarmServerState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Address of the backend server (IP from either internal or OVHcloud network)
        /// </summary>
        [Input("address")]
        public Input<string>? Address { get; set; }

        /// <summary>
        /// Synonym for `farm_id`.
        /// </summary>
        [Input("backendId")]
        public Input<double>? BackendId { get; set; }

        /// <summary>
        /// Label for the server
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// ID of the farm this server is attached to
        /// </summary>
        [Input("farmId")]
        public Input<double>? FarmId { get; set; }

        /// <summary>
        /// Port that backend will respond on
        /// </summary>
        [Input("port")]
        public Input<double>? Port { get; set; }

        /// <summary>
        /// Id of your server.
        /// </summary>
        [Input("serverId")]
        public Input<double>? ServerId { get; set; }

        /// <summary>
        /// The internal name of your IP load balancing
        /// </summary>
        [Input("serviceName")]
        public Input<string>? ServiceName { get; set; }

        /// <summary>
        /// backend status - `active` or `inactive`
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        public UdpFarmServerState()
        {
        }
        public static new UdpFarmServerState Empty => new UdpFarmServerState();
    }
}
