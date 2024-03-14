// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh.CloudProject
{
    public static class GetOpenSearchPattern
    {
        /// <summary>
        /// Use this data source to get information about a pattern of a opensearch cluster associated with a public cloud project.
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
        ///     var pattern = Ovh.CloudProject.GetOpenSearchPattern.Invoke(new()
        ///     {
        ///         ServiceName = "XXX",
        ///         ClusterId = "YYY",
        ///         Id = "ZZZ",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["patternPattern"] = pattern.Apply(getOpenSearchPatternResult =&gt; getOpenSearchPatternResult.Pattern),
        ///     };
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Task<GetOpenSearchPatternResult> InvokeAsync(GetOpenSearchPatternArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetOpenSearchPatternResult>("ovh:CloudProject/getOpenSearchPattern:getOpenSearchPattern", args ?? new GetOpenSearchPatternArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to get information about a pattern of a opensearch cluster associated with a public cloud project.
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
        ///     var pattern = Ovh.CloudProject.GetOpenSearchPattern.Invoke(new()
        ///     {
        ///         ServiceName = "XXX",
        ///         ClusterId = "YYY",
        ///         Id = "ZZZ",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["patternPattern"] = pattern.Apply(getOpenSearchPatternResult =&gt; getOpenSearchPatternResult.Pattern),
        ///     };
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Output<GetOpenSearchPatternResult> Invoke(GetOpenSearchPatternInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetOpenSearchPatternResult>("ovh:CloudProject/getOpenSearchPattern:getOpenSearchPattern", args ?? new GetOpenSearchPatternInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetOpenSearchPatternArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Cluster ID
        /// </summary>
        [Input("clusterId", required: true)]
        public string ClusterId { get; set; } = null!;

        /// <summary>
        /// Pattern ID.
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        /// <summary>
        /// The id of the public cloud project. If omitted,
        /// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        /// </summary>
        [Input("serviceName", required: true)]
        public string ServiceName { get; set; } = null!;

        public GetOpenSearchPatternArgs()
        {
        }
        public static new GetOpenSearchPatternArgs Empty => new GetOpenSearchPatternArgs();
    }

    public sealed class GetOpenSearchPatternInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Cluster ID
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// Pattern ID.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        /// <summary>
        /// The id of the public cloud project. If omitted,
        /// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        public GetOpenSearchPatternInvokeArgs()
        {
        }
        public static new GetOpenSearchPatternInvokeArgs Empty => new GetOpenSearchPatternInvokeArgs();
    }


    [OutputType]
    public sealed class GetOpenSearchPatternResult
    {
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string ClusterId;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Maximum number of index for this pattern.
        /// </summary>
        public readonly int MaxIndexCount;
        /// <summary>
        /// Pattern format.
        /// </summary>
        public readonly string Pattern;
        /// <summary>
        /// Current status of the pattern.
        /// </summary>
        public readonly string ServiceName;

        [OutputConstructor]
        private GetOpenSearchPatternResult(
            string clusterId,

            string id,

            int maxIndexCount,

            string pattern,

            string serviceName)
        {
            ClusterId = clusterId;
            Id = id;
            MaxIndexCount = maxIndexCount;
            Pattern = pattern;
            ServiceName = serviceName;
        }
    }
}
