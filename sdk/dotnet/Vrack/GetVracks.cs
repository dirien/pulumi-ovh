// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh.Vrack
{
    public static class GetVracks
    {
        /// <summary>
        /// Use this data source to get the list of Vrack IDs available for your OVHcloud account.
        /// 
        /// ## Example Usage
        /// 
        /// &lt;!--Start PulumiCodeChooser --&gt;
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ovh = Pulumi.Ovh;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var vracks = Ovh.Vrack.GetVracks.Invoke();
        /// 
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Task<GetVracksResult> InvokeAsync(InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVracksResult>("ovh:Vrack/getVracks:getVracks", InvokeArgs.Empty, options.WithDefaults());

        /// <summary>
        /// Use this data source to get the list of Vrack IDs available for your OVHcloud account.
        /// 
        /// ## Example Usage
        /// 
        /// &lt;!--Start PulumiCodeChooser --&gt;
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ovh = Pulumi.Ovh;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var vracks = Ovh.Vrack.GetVracks.Invoke();
        /// 
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Output<GetVracksResult> Invoke(InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVracksResult>("ovh:Vrack/getVracks:getVracks", InvokeArgs.Empty, options.WithDefaults());
    }


    [OutputType]
    public sealed class GetVracksResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The list of vrack service name available for your OVHcloud account.
        /// </summary>
        public readonly ImmutableArray<string> Results;

        [OutputConstructor]
        private GetVracksResult(
            string id,

            ImmutableArray<string> results)
        {
            Id = id;
            Results = results;
        }
    }
}
