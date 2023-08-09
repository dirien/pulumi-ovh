// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Ovh.Hosting
{
    public static class GetPrivateDatabaseUser
    {
        /// <summary>
        /// Use this data source to retrieve information about an hosting privatedatabase user.
        /// 
        /// ## Example Usage
        /// 
        /// ```hcl
        /// data "ovh_hosting_privatedatabase_user" "user" {
        ///   service_name  = "XXXXXX"
        ///   user_name     = "XXXXXX"
        /// }
        /// ```
        /// </summary>
        public static Task<GetPrivateDatabaseUserResult> InvokeAsync(GetPrivateDatabaseUserArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPrivateDatabaseUserResult>("ovh:Hosting/getPrivateDatabaseUser:getPrivateDatabaseUser", args ?? new GetPrivateDatabaseUserArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to retrieve information about an hosting privatedatabase user.
        /// 
        /// ## Example Usage
        /// 
        /// ```hcl
        /// data "ovh_hosting_privatedatabase_user" "user" {
        ///   service_name  = "XXXXXX"
        ///   user_name     = "XXXXXX"
        /// }
        /// ```
        /// </summary>
        public static Output<GetPrivateDatabaseUserResult> Invoke(GetPrivateDatabaseUserInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPrivateDatabaseUserResult>("ovh:Hosting/getPrivateDatabaseUser:getPrivateDatabaseUser", args ?? new GetPrivateDatabaseUserInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPrivateDatabaseUserArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The internal name of your private database
        /// </summary>
        [Input("serviceName", required: true)]
        public string ServiceName { get; set; } = null!;

        /// <summary>
        /// User name
        /// </summary>
        [Input("userName", required: true)]
        public string UserName { get; set; } = null!;

        public GetPrivateDatabaseUserArgs()
        {
        }
        public static new GetPrivateDatabaseUserArgs Empty => new GetPrivateDatabaseUserArgs();
    }

    public sealed class GetPrivateDatabaseUserInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The internal name of your private database
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        /// <summary>
        /// User name
        /// </summary>
        [Input("userName", required: true)]
        public Input<string> UserName { get; set; } = null!;

        public GetPrivateDatabaseUserInvokeArgs()
        {
        }
        public static new GetPrivateDatabaseUserInvokeArgs Empty => new GetPrivateDatabaseUserInvokeArgs();
    }


    [OutputType]
    public sealed class GetPrivateDatabaseUserResult
    {
        /// <summary>
        /// Creation date of the database
        /// </summary>
        public readonly string CreationDate;
        /// <summary>
        /// Users granted to this database
        /// </summary>
        public readonly ImmutableArray<Outputs.GetPrivateDatabaseUserDatabaseResult> Databases;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string ServiceName;
        public readonly string UserName;

        [OutputConstructor]
        private GetPrivateDatabaseUserResult(
            string creationDate,

            ImmutableArray<Outputs.GetPrivateDatabaseUserDatabaseResult> databases,

            string id,

            string serviceName,

            string userName)
        {
            CreationDate = creationDate;
            Databases = databases;
            Id = id;
            ServiceName = serviceName;
            UserName = userName;
        }
    }
}
