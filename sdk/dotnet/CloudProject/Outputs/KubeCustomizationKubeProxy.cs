// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Ovh.CloudProject.Outputs
{

    [OutputType]
    public sealed class KubeCustomizationKubeProxy
    {
        /// <summary>
        /// Kubernetes cluster kube-proxy customization of iptables specific config (durations format is RFC3339 duration, e.g. `PT60S`)
        /// </summary>
        public readonly Outputs.KubeCustomizationKubeProxyIptables? Iptables;
        /// <summary>
        /// Kubernetes cluster kube-proxy customization of IPVS specific config (durations format is [RFC3339](https://www.rfc-editor.org/rfc/rfc3339) duration, e.g. `PT60S`)
        /// </summary>
        public readonly Outputs.KubeCustomizationKubeProxyIpvs? Ipvs;

        [OutputConstructor]
        private KubeCustomizationKubeProxy(
            Outputs.KubeCustomizationKubeProxyIptables? iptables,

            Outputs.KubeCustomizationKubeProxyIpvs? ipvs)
        {
            Iptables = iptables;
            Ipvs = ipvs;
        }
    }
}
