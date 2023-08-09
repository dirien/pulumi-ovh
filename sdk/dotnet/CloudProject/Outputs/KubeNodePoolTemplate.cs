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
    public sealed class KubeNodePoolTemplate
    {
        /// <summary>
        /// Metadata of each node in the pool
        /// </summary>
        public readonly Outputs.KubeNodePoolTemplateMetadata? Metadata;
        /// <summary>
        /// Spec of each node in the pool
        /// </summary>
        public readonly Outputs.KubeNodePoolTemplateSpec? Spec;

        [OutputConstructor]
        private KubeNodePoolTemplate(
            Outputs.KubeNodePoolTemplateMetadata? metadata,

            Outputs.KubeNodePoolTemplateSpec? spec)
        {
            Metadata = metadata;
            Spec = spec;
        }
    }
}
