// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh.Iam
{
    public static class GetPolicy
    {
        /// <summary>
        /// Use this data source to retrieve am IAM policy.
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
        ///     var myPolicy = Ovh.Iam.GetPolicy.Invoke(new()
        ///     {
        ///         Id = "my_policy_id",
        ///     });
        /// 
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Task<GetPolicyResult> InvokeAsync(GetPolicyArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPolicyResult>("ovh:Iam/getPolicy:getPolicy", args ?? new GetPolicyArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to retrieve am IAM policy.
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
        ///     var myPolicy = Ovh.Iam.GetPolicy.Invoke(new()
        ///     {
        ///         Id = "my_policy_id",
        ///     });
        /// 
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Output<GetPolicyResult> Invoke(GetPolicyInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPolicyResult>("ovh:Iam/getPolicy:getPolicy", args ?? new GetPolicyInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPolicyArgs : global::Pulumi.InvokeArgs
    {
        [Input("allows")]
        private List<string>? _allows;

        /// <summary>
        /// Set of actions allowed by the policy.
        /// </summary>
        public List<string> Allows
        {
            get => _allows ?? (_allows = new List<string>());
            set => _allows = value;
        }

        [Input("denies")]
        private List<string>? _denies;

        /// <summary>
        /// Set of actions that will be denied no matter what policy exists.
        /// </summary>
        public List<string> Denies
        {
            get => _denies ?? (_denies = new List<string>());
            set => _denies = value;
        }

        /// <summary>
        /// Group description.
        /// </summary>
        [Input("description")]
        public string? Description { get; set; }

        [Input("excepts")]
        private List<string>? _excepts;

        /// <summary>
        /// Set of actions that will be subtracted from the `allow` list.
        /// </summary>
        public List<string> Excepts
        {
            get => _excepts ?? (_excepts = new List<string>());
            set => _excepts = value;
        }

        /// <summary>
        /// UUID of the policy.
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        [Input("permissionsGroups")]
        private List<string>? _permissionsGroups;

        /// <summary>
        /// Set of permissions groups that apply to the policy.
        /// </summary>
        public List<string> PermissionsGroups
        {
            get => _permissionsGroups ?? (_permissionsGroups = new List<string>());
            set => _permissionsGroups = value;
        }

        public GetPolicyArgs()
        {
        }
        public static new GetPolicyArgs Empty => new GetPolicyArgs();
    }

    public sealed class GetPolicyInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("allows")]
        private InputList<string>? _allows;

        /// <summary>
        /// Set of actions allowed by the policy.
        /// </summary>
        public InputList<string> Allows
        {
            get => _allows ?? (_allows = new InputList<string>());
            set => _allows = value;
        }

        [Input("denies")]
        private InputList<string>? _denies;

        /// <summary>
        /// Set of actions that will be denied no matter what policy exists.
        /// </summary>
        public InputList<string> Denies
        {
            get => _denies ?? (_denies = new InputList<string>());
            set => _denies = value;
        }

        /// <summary>
        /// Group description.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("excepts")]
        private InputList<string>? _excepts;

        /// <summary>
        /// Set of actions that will be subtracted from the `allow` list.
        /// </summary>
        public InputList<string> Excepts
        {
            get => _excepts ?? (_excepts = new InputList<string>());
            set => _excepts = value;
        }

        /// <summary>
        /// UUID of the policy.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        [Input("permissionsGroups")]
        private InputList<string>? _permissionsGroups;

        /// <summary>
        /// Set of permissions groups that apply to the policy.
        /// </summary>
        public InputList<string> PermissionsGroups
        {
            get => _permissionsGroups ?? (_permissionsGroups = new InputList<string>());
            set => _permissionsGroups = value;
        }

        public GetPolicyInvokeArgs()
        {
        }
        public static new GetPolicyInvokeArgs Empty => new GetPolicyInvokeArgs();
    }


    [OutputType]
    public sealed class GetPolicyResult
    {
        /// <summary>
        /// Set of actions allowed by the policy.
        /// </summary>
        public readonly ImmutableArray<string> Allows;
        /// <summary>
        /// Creation date of this group.
        /// </summary>
        public readonly string CreatedAt;
        /// <summary>
        /// Set of actions that will be denied no matter what policy exists.
        /// </summary>
        public readonly ImmutableArray<string> Denies;
        /// <summary>
        /// Group description.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// Set of actions that will be subtracted from the `allow` list.
        /// </summary>
        public readonly ImmutableArray<string> Excepts;
        public readonly string Id;
        /// <summary>
        /// Set of identities affected by the policy.
        /// </summary>
        public readonly ImmutableArray<string> Identities;
        /// <summary>
        /// Name of the policy.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Owner of the policy.
        /// </summary>
        public readonly string Owner;
        /// <summary>
        /// Set of permissions groups that apply to the policy.
        /// </summary>
        public readonly ImmutableArray<string> PermissionsGroups;
        /// <summary>
        /// Indicates that the policy is a default one.
        /// </summary>
        public readonly bool ReadOnly;
        /// <summary>
        /// Set of resources affected by the policy.
        /// </summary>
        public readonly ImmutableArray<string> Resources;
        /// <summary>
        /// Date of the last update of this group.
        /// </summary>
        public readonly string UpdatedAt;

        [OutputConstructor]
        private GetPolicyResult(
            ImmutableArray<string> allows,

            string createdAt,

            ImmutableArray<string> denies,

            string? description,

            ImmutableArray<string> excepts,

            string id,

            ImmutableArray<string> identities,

            string name,

            string owner,

            ImmutableArray<string> permissionsGroups,

            bool readOnly,

            ImmutableArray<string> resources,

            string updatedAt)
        {
            Allows = allows;
            CreatedAt = createdAt;
            Denies = denies;
            Description = description;
            Excepts = excepts;
            Id = id;
            Identities = identities;
            Name = name;
            Owner = owner;
            PermissionsGroups = permissionsGroups;
            ReadOnly = readOnly;
            Resources = resources;
            UpdatedAt = updatedAt;
        }
    }
}
