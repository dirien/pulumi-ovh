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
    public sealed class GetVolumesVolumeResult
    {
        /// <summary>
        /// The id of the volume
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The name of the volume
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The size of the volume
        /// </summary>
        public readonly double Size;

        [OutputConstructor]
        private GetVolumesVolumeResult(
            string id,

            string name,

            double size)
        {
            Id = id;
            Name = name;
            Size = size;
        }
    }
}
