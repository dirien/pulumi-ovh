// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Ovh.Ip.Outputs
{

    [OutputType]
    public sealed class IpServiceOrder
    {
        /// <summary>
        /// date
        /// </summary>
        public readonly string? Date;
        /// <summary>
        /// Information about a Bill entry
        /// </summary>
        public readonly ImmutableArray<Outputs.IpServiceOrderDetail> Details;
        /// <summary>
        /// expiration date
        /// </summary>
        public readonly string? ExpirationDate;
        /// <summary>
        /// order id
        /// </summary>
        public readonly int? OrderId;

        [OutputConstructor]
        private IpServiceOrder(
            string? date,

            ImmutableArray<Outputs.IpServiceOrderDetail> details,

            string? expirationDate,

            int? orderId)
        {
            Date = date;
            Details = details;
            ExpirationDate = expirationDate;
            OrderId = orderId;
        }
    }
}
