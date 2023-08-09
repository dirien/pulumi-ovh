// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Ovh.Domain.Inputs
{

    public sealed class ZoneOrderGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// date
        /// </summary>
        [Input("date")]
        public Input<string>? Date { get; set; }

        [Input("details")]
        private InputList<Inputs.ZoneOrderDetailGetArgs>? _details;

        /// <summary>
        /// Information about a Bill entry
        /// </summary>
        public InputList<Inputs.ZoneOrderDetailGetArgs> Details
        {
            get => _details ?? (_details = new InputList<Inputs.ZoneOrderDetailGetArgs>());
            set => _details = value;
        }

        /// <summary>
        /// expiration date
        /// </summary>
        [Input("expirationDate")]
        public Input<string>? ExpirationDate { get; set; }

        /// <summary>
        /// order id
        /// </summary>
        [Input("orderId")]
        public Input<int>? OrderId { get; set; }

        public ZoneOrderGetArgs()
        {
        }
        public static new ZoneOrderGetArgs Empty => new ZoneOrderGetArgs();
    }
}
