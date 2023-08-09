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

    public sealed class GetKubeCustomizationInputArgs : global::Pulumi.ResourceArgs
    {
        [Input("apiservers", required: true)]
        private InputList<Inputs.GetKubeCustomizationApiserverInputArgs>? _apiservers;

        /// <summary>
        /// Kubernetes API server customization
        /// </summary>
        [Obsolete(@"Use customization_apiserver instead")]
        public InputList<Inputs.GetKubeCustomizationApiserverInputArgs> Apiservers
        {
            get => _apiservers ?? (_apiservers = new InputList<Inputs.GetKubeCustomizationApiserverInputArgs>());
            set => _apiservers = value;
        }

        public GetKubeCustomizationInputArgs()
        {
        }
        public static new GetKubeCustomizationInputArgs Empty => new GetKubeCustomizationInputArgs();
    }
}
