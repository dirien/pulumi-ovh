// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Ovh.IpLoadBalancing.Inputs
{

    public sealed class TcpRouteActionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Farm ID for "farm" action type, empty for others.
        /// </summary>
        [Input("target")]
        public Input<string>? Target { get; set; }

        /// <summary>
        /// Action to trigger if all the rules of this route matches
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public TcpRouteActionArgs()
        {
        }
        public static new TcpRouteActionArgs Empty => new TcpRouteActionArgs();
    }
}
