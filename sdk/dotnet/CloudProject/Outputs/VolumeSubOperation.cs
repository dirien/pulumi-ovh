// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh.CloudProject.Outputs
{

    [OutputType]
    public sealed class VolumeSubOperation
    {
        /// <summary>
        /// Affected resource of the sub-operation
        /// </summary>
        public readonly string? ResourceId;
        /// <summary>
        /// The started date of the sub-operation
        /// </summary>
        public readonly string? ResourceType;

        [OutputConstructor]
        private VolumeSubOperation(
            string? resourceId,

            string? resourceType)
        {
            ResourceId = resourceId;
            ResourceType = resourceType;
        }
    }
}
