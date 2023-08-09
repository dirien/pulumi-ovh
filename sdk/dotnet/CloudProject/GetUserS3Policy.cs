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
    public static class GetUserS3Policy
    {
        /// <summary>
        /// Get the S3 Policy of a public cloud project user. The policy can be set by using the `ovh.CloudProject.S3Policy` resource.
        /// 
        /// ## Example Usage
        /// 
        /// ```hcl
        /// data "ovh_cloud_project_users" "project_users" {
        ///   service_name = "XXX"
        /// }
        /// 
        /// locals {
        ///   # Get the user ID of a previously created user with the description "S3-User"
        ///   users      = [for user in data.ovh_cloud_project_users.project_users.users : user.user_id if user.description == "S3-User"]
        ///   s3_user_id = local.users[0]
        /// }
        /// 
        /// data "ovh_cloud_project_user_s3_policy" "policy" {
        ///   service_name = data.ovh_cloud_project_users.project_users.service_name
        ///   user_id      = local.s3_user_id
        /// }
        /// ```
        /// </summary>
        public static Task<GetUserS3PolicyResult> InvokeAsync(GetUserS3PolicyArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetUserS3PolicyResult>("ovh:CloudProject/getUserS3Policy:getUserS3Policy", args ?? new GetUserS3PolicyArgs(), options.WithDefaults());

        /// <summary>
        /// Get the S3 Policy of a public cloud project user. The policy can be set by using the `ovh.CloudProject.S3Policy` resource.
        /// 
        /// ## Example Usage
        /// 
        /// ```hcl
        /// data "ovh_cloud_project_users" "project_users" {
        ///   service_name = "XXX"
        /// }
        /// 
        /// locals {
        ///   # Get the user ID of a previously created user with the description "S3-User"
        ///   users      = [for user in data.ovh_cloud_project_users.project_users.users : user.user_id if user.description == "S3-User"]
        ///   s3_user_id = local.users[0]
        /// }
        /// 
        /// data "ovh_cloud_project_user_s3_policy" "policy" {
        ///   service_name = data.ovh_cloud_project_users.project_users.service_name
        ///   user_id      = local.s3_user_id
        /// }
        /// ```
        /// </summary>
        public static Output<GetUserS3PolicyResult> Invoke(GetUserS3PolicyInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetUserS3PolicyResult>("ovh:CloudProject/getUserS3Policy:getUserS3Policy", args ?? new GetUserS3PolicyInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetUserS3PolicyArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the public cloud project. If omitted,
        /// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        /// </summary>
        [Input("serviceName", required: true)]
        public string ServiceName { get; set; } = null!;

        /// <summary>
        /// The ID of a public cloud project's user.
        /// </summary>
        [Input("userId", required: true)]
        public string UserId { get; set; } = null!;

        public GetUserS3PolicyArgs()
        {
        }
        public static new GetUserS3PolicyArgs Empty => new GetUserS3PolicyArgs();
    }

    public sealed class GetUserS3PolicyInvokeArgs : global::Pulumi.InvokeArgs
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

        public GetUserS3PolicyInvokeArgs()
        {
        }
        public static new GetUserS3PolicyInvokeArgs Empty => new GetUserS3PolicyInvokeArgs();
    }


    [OutputType]
    public sealed class GetUserS3PolicyResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// (Required) The policy document. This is a JSON formatted string.
        /// </summary>
        public readonly string Policy;
        public readonly string ServiceName;
        public readonly string UserId;

        [OutputConstructor]
        private GetUserS3PolicyResult(
            string id,

            string policy,

            string serviceName,

            string userId)
        {
            Id = id;
            Policy = policy;
            ServiceName = serviceName;
            UserId = userId;
        }
    }
}
