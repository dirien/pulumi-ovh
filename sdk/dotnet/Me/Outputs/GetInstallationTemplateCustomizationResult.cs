// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Ovh.Me.Outputs
{

    [OutputType]
    public sealed class GetInstallationTemplateCustomizationResult
    {
        /// <summary>
        /// (DEPRECATED) Template change log details.
        /// </summary>
        public readonly string ChangeLog;
        /// <summary>
        /// Set up the server using the provided hostname instead of the default hostname.
        /// </summary>
        public readonly string CustomHostname;
        /// <summary>
        /// Indicate the URL where your postinstall customisation script is located.
        /// </summary>
        public readonly string PostInstallationScriptLink;
        /// <summary>
        /// indicate the string returned by your postinstall customisation script on successful execution. Advice: your script should return a unique validation string in case of succes. A good example is 'loh1Xee7eo OK OK OK UGh8Ang1Gu'.
        /// </summary>
        public readonly string PostInstallationScriptReturn;
        /// <summary>
        /// (DEPRECATED) Rating.
        /// </summary>
        public readonly int Rating;
        /// <summary>
        /// Name of the ssh key that should be installed. Password login will be disabled.
        /// </summary>
        public readonly string SshKeyName;
        /// <summary>
        /// Use the distribution's native kernel instead of the recommended OVHcloud Kernel.
        /// </summary>
        public readonly bool UseDistributionKernel;

        [OutputConstructor]
        private GetInstallationTemplateCustomizationResult(
            string changeLog,

            string customHostname,

            string postInstallationScriptLink,

            string postInstallationScriptReturn,

            int rating,

            string sshKeyName,

            bool useDistributionKernel)
        {
            ChangeLog = changeLog;
            CustomHostname = customHostname;
            PostInstallationScriptLink = postInstallationScriptLink;
            PostInstallationScriptReturn = postInstallationScriptReturn;
            Rating = rating;
            SshKeyName = sshKeyName;
            UseDistributionKernel = useDistributionKernel;
        }
    }
}
