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

    public sealed class GetKubeNodePoolTemplateSpecInputArgs : global::Pulumi.ResourceArgs
    {
        [Input("taints")]
        private InputList<ImmutableDictionary<string, object>>? _taints;
        public InputList<ImmutableDictionary<string, object>> Taints
        {
            get => _taints ?? (_taints = new InputList<ImmutableDictionary<string, object>>());
            set => _taints = value;
        }

        [Input("unschedulable")]
        public Input<bool>? Unschedulable { get; set; }

        public GetKubeNodePoolTemplateSpecInputArgs()
        {
        }
        public static new GetKubeNodePoolTemplateSpecInputArgs Empty => new GetKubeNodePoolTemplateSpecInputArgs();
    }
}
