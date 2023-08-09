// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Ovh.CloudProject.Inputs
{

    public sealed class GetKubeCustomizationKubeProxyIptablesInputArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Minimum period that IPVS rules are refreshed in [RFC3339](https://www.rfc-editor.org/rfc/rfc3339) duration.
        /// </summary>
        [Input("minSyncPeriod")]
        public Input<string>? MinSyncPeriod { get; set; }

        /// <summary>
        /// Minimum period that IPVS rules are refreshed, in [RFC3339](https://www.rfc-editor.org/rfc/rfc3339) duration format.
        /// </summary>
        [Input("syncPeriod")]
        public Input<string>? SyncPeriod { get; set; }

        public GetKubeCustomizationKubeProxyIptablesInputArgs()
        {
        }
        public static new GetKubeCustomizationKubeProxyIptablesInputArgs Empty => new GetKubeCustomizationKubeProxyIptablesInputArgs();
    }
}
