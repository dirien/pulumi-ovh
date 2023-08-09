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
    public sealed class GetKubeCustomizationApiserverResult
    {
        /// <summary>
        /// Kubernetes API server admission plugins customization
        /// </summary>
        public readonly ImmutableArray<Outputs.GetKubeCustomizationApiserverAdmissionpluginResult> Admissionplugins;

        [OutputConstructor]
        private GetKubeCustomizationApiserverResult(ImmutableArray<Outputs.GetKubeCustomizationApiserverAdmissionpluginResult> admissionplugins)
        {
            Admissionplugins = admissionplugins;
        }
    }
}
