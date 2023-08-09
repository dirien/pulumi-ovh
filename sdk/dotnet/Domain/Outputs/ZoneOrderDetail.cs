// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Ovh.Domain.Outputs
{

    [OutputType]
    public sealed class ZoneOrderDetail
    {
        /// <summary>
        /// description
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// expiration date
        /// </summary>
        public readonly string? Domain;
        /// <summary>
        /// order detail id
        /// </summary>
        public readonly int? OrderDetailId;
        /// <summary>
        /// quantity
        /// </summary>
        public readonly string? Quantity;

        [OutputConstructor]
        private ZoneOrderDetail(
            string? description,

            string? domain,

            int? orderDetailId,

            string? quantity)
        {
            Description = description;
            Domain = domain;
            OrderDetailId = orderDetailId;
            Quantity = quantity;
        }
    }
}
