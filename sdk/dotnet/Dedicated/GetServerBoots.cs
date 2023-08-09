// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Ovh.Dedicated
{
    public static class GetServerBoots
    {
        /// <summary>
        /// Use this data source to get the list of compatible netboots for a dedicated server associated with your OVHcloud Account.
        /// 
        /// ## Example Usage
        /// 
        /// ```hcl
        /// data "ovh_dedicated_server_boots" "netboots" {
        ///   service_name = "myserver"
        ///   boot_type    = "harddisk"
        /// }
        /// ```
        /// </summary>
        public static Task<GetServerBootsResult> InvokeAsync(GetServerBootsArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetServerBootsResult>("ovh:Dedicated/getServerBoots:getServerBoots", args ?? new GetServerBootsArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to get the list of compatible netboots for a dedicated server associated with your OVHcloud Account.
        /// 
        /// ## Example Usage
        /// 
        /// ```hcl
        /// data "ovh_dedicated_server_boots" "netboots" {
        ///   service_name = "myserver"
        ///   boot_type    = "harddisk"
        /// }
        /// ```
        /// </summary>
        public static Output<GetServerBootsResult> Invoke(GetServerBootsInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetServerBootsResult>("ovh:Dedicated/getServerBoots:getServerBoots", args ?? new GetServerBootsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetServerBootsArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Filter the value of bootType property (harddisk, rescue, ipxeCustomerScript, internal, network)
        /// </summary>
        [Input("bootType")]
        public string? BootType { get; set; }

        [Input("kernel")]
        public string? Kernel { get; set; }

        /// <summary>
        /// The internal name of your dedicated server.
        /// </summary>
        [Input("serviceName", required: true)]
        public string ServiceName { get; set; } = null!;

        public GetServerBootsArgs()
        {
        }
        public static new GetServerBootsArgs Empty => new GetServerBootsArgs();
    }

    public sealed class GetServerBootsInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Filter the value of bootType property (harddisk, rescue, ipxeCustomerScript, internal, network)
        /// </summary>
        [Input("bootType")]
        public Input<string>? BootType { get; set; }

        [Input("kernel")]
        public Input<string>? Kernel { get; set; }

        /// <summary>
        /// The internal name of your dedicated server.
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        public GetServerBootsInvokeArgs()
        {
        }
        public static new GetServerBootsInvokeArgs Empty => new GetServerBootsInvokeArgs();
    }


    [OutputType]
    public sealed class GetServerBootsResult
    {
        public readonly string? BootType;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string? Kernel;
        /// <summary>
        /// The list of dedicated server netboots.
        /// </summary>
        public readonly ImmutableArray<int> Results;
        public readonly string ServiceName;

        [OutputConstructor]
        private GetServerBootsResult(
            string? bootType,

            string id,

            string? kernel,

            ImmutableArray<int> results,

            string serviceName)
        {
            BootType = bootType;
            Id = id;
            Kernel = kernel;
            Results = results;
            ServiceName = serviceName;
        }
    }
}
