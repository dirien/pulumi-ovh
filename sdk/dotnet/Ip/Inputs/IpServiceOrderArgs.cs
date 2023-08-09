// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Ovh.Ip.Inputs
{

    public sealed class IpServiceOrderArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// date
        /// </summary>
        [Input("date")]
        public Input<string>? Date { get; set; }

        [Input("details")]
        private InputList<Inputs.IpServiceOrderDetailArgs>? _details;

        /// <summary>
        /// Information about a Bill entry
        /// </summary>
        public InputList<Inputs.IpServiceOrderDetailArgs> Details
        {
            get => _details ?? (_details = new InputList<Inputs.IpServiceOrderDetailArgs>());
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

        public IpServiceOrderArgs()
        {
        }
        public static new IpServiceOrderArgs Empty => new IpServiceOrderArgs();
    }
}
