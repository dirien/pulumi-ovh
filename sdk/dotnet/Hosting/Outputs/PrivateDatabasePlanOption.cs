// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Ovh.Hosting.Outputs
{

    [OutputType]
    public sealed class PrivateDatabasePlanOption
    {
        /// <summary>
        /// Catalog name
        /// </summary>
        public readonly string? CatalogName;
        /// <summary>
        /// Representation of a configuration item for personalizing product
        /// </summary>
        public readonly ImmutableArray<Outputs.PrivateDatabasePlanOptionConfiguration> Configurations;
        /// <summary>
        /// duration.
        /// </summary>
        public readonly string Duration;
        /// <summary>
        /// Plan code.
        /// </summary>
        public readonly string PlanCode;
        /// <summary>
        /// Pricing model identifier
        /// </summary>
        public readonly string PricingMode;

        [OutputConstructor]
        private PrivateDatabasePlanOption(
            string? catalogName,

            ImmutableArray<Outputs.PrivateDatabasePlanOptionConfiguration> configurations,

            string duration,

            string planCode,

            string pricingMode)
        {
            CatalogName = catalogName;
            Configurations = configurations;
            Duration = duration;
            PlanCode = planCode;
            PricingMode = pricingMode;
        }
    }
}
