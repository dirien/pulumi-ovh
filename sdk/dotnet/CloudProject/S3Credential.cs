// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Ovh.CloudProject
{
    /// <summary>
    /// Creates an S3 Credential for a user in a public cloud project.
    /// 
    /// ## Example Usage
    /// 
    /// ## Import
    /// 
    /// OVHcloud User S3 Credentials can be imported using the `service_name`, `user_id` and `access_key_id` of the credential, separated by "/" E.g., bash &lt;break&gt;&lt;break&gt;```sh&lt;break&gt; $ pulumi import ovh:CloudProject/s3Credential:S3Credential s3_credential service_name/user_id/access_key_id &lt;break&gt;```&lt;break&gt;&lt;break&gt;
    /// </summary>
    [OvhResourceType("ovh:CloudProject/s3Credential:S3Credential")]
    public partial class S3Credential : global::Pulumi.CustomResource
    {
        /// <summary>
        /// the Access Key ID
        /// </summary>
        [Output("accessKeyId")]
        public Output<string> AccessKeyId { get; private set; } = null!;

        [Output("internalUserId")]
        public Output<string> InternalUserId { get; private set; } = null!;

        /// <summary>
        /// (Sensitive) the Secret Access Key
        /// </summary>
        [Output("secretAccessKey")]
        public Output<string> SecretAccessKey { get; private set; } = null!;

        /// <summary>
        /// The ID of the public cloud project. If omitted,
        /// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        /// </summary>
        [Output("serviceName")]
        public Output<string> ServiceName { get; private set; } = null!;

        /// <summary>
        /// The ID of a public cloud project's user.
        /// </summary>
        [Output("userId")]
        public Output<string> UserId { get; private set; } = null!;


        /// <summary>
        /// Create a S3Credential resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public S3Credential(string name, S3CredentialArgs args, CustomResourceOptions? options = null)
            : base("ovh:CloudProject/s3Credential:S3Credential", name, args ?? new S3CredentialArgs(), MakeResourceOptions(options, ""))
        {
        }

        private S3Credential(string name, Input<string> id, S3CredentialState? state = null, CustomResourceOptions? options = null)
            : base("ovh:CloudProject/s3Credential:S3Credential", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/dirien/pulumi-ovh",
                AdditionalSecretOutputs =
                {
                    "secretAccessKey",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing S3Credential resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static S3Credential Get(string name, Input<string> id, S3CredentialState? state = null, CustomResourceOptions? options = null)
        {
            return new S3Credential(name, id, state, options);
        }
    }

    public sealed class S3CredentialArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the public cloud project. If omitted,
        /// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        /// <summary>
        /// The ID of a public cloud project's user.
        /// </summary>
        [Input("userId", required: true)]
        public Input<string> UserId { get; set; } = null!;

        public S3CredentialArgs()
        {
        }
        public static new S3CredentialArgs Empty => new S3CredentialArgs();
    }

    public sealed class S3CredentialState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// the Access Key ID
        /// </summary>
        [Input("accessKeyId")]
        public Input<string>? AccessKeyId { get; set; }

        [Input("internalUserId")]
        public Input<string>? InternalUserId { get; set; }

        [Input("secretAccessKey")]
        private Input<string>? _secretAccessKey;

        /// <summary>
        /// (Sensitive) the Secret Access Key
        /// </summary>
        public Input<string>? SecretAccessKey
        {
            get => _secretAccessKey;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _secretAccessKey = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The ID of the public cloud project. If omitted,
        /// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        /// </summary>
        [Input("serviceName")]
        public Input<string>? ServiceName { get; set; }

        /// <summary>
        /// The ID of a public cloud project's user.
        /// </summary>
        [Input("userId")]
        public Input<string>? UserId { get; set; }

        public S3CredentialState()
        {
        }
        public static new S3CredentialState Empty => new S3CredentialState();
    }
}
