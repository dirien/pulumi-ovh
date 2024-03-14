// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh.CloudProjectDatabase
{
    public static class GetKafkaSchemaRegistryAcls
    {
        /// <summary>
        /// Use this data source to get the list of ACLs of a kafka cluster associated with a public cloud project.
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
        ///     var schemaRegistryAcls = Ovh.CloudProjectDatabase.GetKafkaSchemaRegistryAcls.Invoke(new()
        ///     {
        ///         ServiceName = "XXX",
        ///         ClusterId = "YYY",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["aclIds"] = schemaRegistryAcls.Apply(getKafkaSchemaRegistryAclsResult =&gt; getKafkaSchemaRegistryAclsResult.AclIds),
        ///     };
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Task<GetKafkaSchemaRegistryAclsResult> InvokeAsync(GetKafkaSchemaRegistryAclsArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetKafkaSchemaRegistryAclsResult>("ovh:CloudProjectDatabase/getKafkaSchemaRegistryAcls:getKafkaSchemaRegistryAcls", args ?? new GetKafkaSchemaRegistryAclsArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to get the list of ACLs of a kafka cluster associated with a public cloud project.
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
        ///     var schemaRegistryAcls = Ovh.CloudProjectDatabase.GetKafkaSchemaRegistryAcls.Invoke(new()
        ///     {
        ///         ServiceName = "XXX",
        ///         ClusterId = "YYY",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["aclIds"] = schemaRegistryAcls.Apply(getKafkaSchemaRegistryAclsResult =&gt; getKafkaSchemaRegistryAclsResult.AclIds),
        ///     };
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Output<GetKafkaSchemaRegistryAclsResult> Invoke(GetKafkaSchemaRegistryAclsInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetKafkaSchemaRegistryAclsResult>("ovh:CloudProjectDatabase/getKafkaSchemaRegistryAcls:getKafkaSchemaRegistryAcls", args ?? new GetKafkaSchemaRegistryAclsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetKafkaSchemaRegistryAclsArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Cluster ID
        /// </summary>
        [Input("clusterId", required: true)]
        public string ClusterId { get; set; } = null!;

        /// <summary>
        /// The id of the public cloud project. If omitted,
        /// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        /// </summary>
        [Input("serviceName", required: true)]
        public string ServiceName { get; set; } = null!;

        public GetKafkaSchemaRegistryAclsArgs()
        {
        }
        public static new GetKafkaSchemaRegistryAclsArgs Empty => new GetKafkaSchemaRegistryAclsArgs();
    }

    public sealed class GetKafkaSchemaRegistryAclsInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Cluster ID
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// The id of the public cloud project. If omitted,
        /// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        public GetKafkaSchemaRegistryAclsInvokeArgs()
        {
        }
        public static new GetKafkaSchemaRegistryAclsInvokeArgs Empty => new GetKafkaSchemaRegistryAclsInvokeArgs();
    }


    [OutputType]
    public sealed class GetKafkaSchemaRegistryAclsResult
    {
        /// <summary>
        /// The list of schema refistry ACLs ids of the kafka cluster associated with the project.
        /// </summary>
        public readonly ImmutableArray<string> AclIds;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string ClusterId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string ServiceName;

        [OutputConstructor]
        private GetKafkaSchemaRegistryAclsResult(
            ImmutableArray<string> aclIds,

            string clusterId,

            string id,

            string serviceName)
        {
            AclIds = aclIds;
            ClusterId = clusterId;
            Id = id;
            ServiceName = serviceName;
        }
    }
}
