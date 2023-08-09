// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Ovh.Ip
{
    public static class GetService
    {
        /// <summary>
        /// Use this data source to retrieve information about an IP service.
        /// 
        /// ## Example Usage
        /// 
        /// ```hcl
        /// data "ovh_ip_service" "myip" {
        ///   service_name  = "XXXXXX"
        /// }
        /// ```
        /// </summary>
        public static Task<GetServiceResult> InvokeAsync(GetServiceArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetServiceResult>("ovh:Ip/getService:getService", args ?? new GetServiceArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to retrieve information about an IP service.
        /// 
        /// ## Example Usage
        /// 
        /// ```hcl
        /// data "ovh_ip_service" "myip" {
        ///   service_name  = "XXXXXX"
        /// }
        /// ```
        /// </summary>
        public static Output<GetServiceResult> Invoke(GetServiceInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetServiceResult>("ovh:Ip/getService:getService", args ?? new GetServiceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetServiceArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The service name
        /// </summary>
        [Input("serviceName", required: true)]
        public string ServiceName { get; set; } = null!;

        public GetServiceArgs()
        {
        }
        public static new GetServiceArgs Empty => new GetServiceArgs();
    }

    public sealed class GetServiceInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The service name
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        public GetServiceInvokeArgs()
        {
        }
        public static new GetServiceInvokeArgs Empty => new GetServiceInvokeArgs();
    }


    [OutputType]
    public sealed class GetServiceResult
    {
        /// <summary>
        /// can be terminated
        /// </summary>
        public readonly bool CanBeTerminated;
        /// <summary>
        /// country
        /// </summary>
        public readonly string Country;
        /// <summary>
        /// Custom description on your ip
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// ip block
        /// </summary>
        public readonly string Ip;
        /// <summary>
        /// IP block organisation Id
        /// </summary>
        public readonly string OrganisationId;
        /// <summary>
        /// Routage information
        /// </summary>
        public readonly ImmutableArray<Outputs.GetServiceRoutedToResult> RoutedTos;
        /// <summary>
        /// Service where ip is routed to
        /// </summary>
        public readonly string ServiceName;
        /// <summary>
        /// Possible values for ip type (    "cdn", "cloud", "dedicated", "failover", "hosted_ssl", "housing", "loadBalancing", "mail", "overthebox", "pcc", "pci", "private", "vpn", "vps", "vrack", "xdsl")
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private GetServiceResult(
            bool canBeTerminated,

            string country,

            string description,

            string id,

            string ip,

            string organisationId,

            ImmutableArray<Outputs.GetServiceRoutedToResult> routedTos,

            string serviceName,

            string type)
        {
            CanBeTerminated = canBeTerminated;
            Country = country;
            Description = description;
            Id = id;
            Ip = ip;
            OrganisationId = organisationId;
            RoutedTos = routedTos;
            ServiceName = serviceName;
            Type = type;
        }
    }
}
