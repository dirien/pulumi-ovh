// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh.Domain
{
    /// <summary>
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ovh = Pulumi.Ovh;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var myaccount = Ovh.Me.GetMe.Invoke();
    /// 
    ///     var mycart = Ovh.Order.GetCart.Invoke(new()
    ///     {
    ///         OvhSubsidiary = myaccount.Apply(getMeResult =&gt; getMeResult.OvhSubsidiary),
    ///     });
    /// 
    ///     var zoneCartProductPlan = Ovh.Order.GetCartProductPlan.Invoke(new()
    ///     {
    ///         CartId = mycart.Apply(getCartResult =&gt; getCartResult.Id),
    ///         PriceCapacity = "renew",
    ///         Product = "dns",
    ///         PlanCode = "zone",
    ///     });
    /// 
    ///     var zoneZone = new Ovh.Domain.Zone("zoneZone", new()
    ///     {
    ///         OvhSubsidiary = mycart.Apply(getCartResult =&gt; getCartResult.OvhSubsidiary),
    ///         Plan = new Ovh.Domain.Inputs.ZonePlanArgs
    ///         {
    ///             Duration = zoneCartProductPlan.Apply(getCartProductPlanResult =&gt; getCartProductPlanResult.SelectedPrices[0]?.Duration),
    ///             PlanCode = zoneCartProductPlan.Apply(getCartProductPlanResult =&gt; getCartProductPlanResult.PlanCode),
    ///             PricingMode = zoneCartProductPlan.Apply(getCartProductPlanResult =&gt; getCartProductPlanResult.SelectedPrices[0]?.PricingMode),
    ///             Configurations = new[]
    ///             {
    ///                 new Ovh.Domain.Inputs.ZonePlanConfigurationArgs
    ///                 {
    ///                     Label = "zone",
    ///                     Value = "myzone.mydomain.com",
    ///                 },
    ///                 new Ovh.Domain.Inputs.ZonePlanConfigurationArgs
    ///                 {
    ///                     Label = "template",
    ///                     Value = "minimized",
    ///                 },
    ///             },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Zone can be imported using its `name`.
    /// 
    /// Using the following configuration:
    /// 
    /// hcl
    /// 
    /// import {
    /// 
    ///   to = ovh_domain_zone.zone
    /// 
    ///   id = "&lt;zone name&gt;"
    /// 
    /// }
    /// 
    /// You can then run:
    /// 
    /// bash
    /// 
    /// $ pulumi preview -generate-config-out=zone.tf
    /// 
    /// $ pulumi up
    /// 
    /// The file `zone.tf` will then contain the imported resource's configuration, that can be copied next to the `import` block above.
    /// 
    /// See https://developer.hashicorp.com/terraform/language/import/generating-configuration for more details.
    /// </summary>
    [OvhResourceType("ovh:Domain/zone:Zone")]
    public partial class Zone : global::Pulumi.CustomResource
    {
        [Output("ZoneURN")]
        public Output<string> ZoneURN { get; private set; } = null!;

        /// <summary>
        /// Is DNSSEC supported by this zone
        /// </summary>
        [Output("dnssecSupported")]
        public Output<bool> DnssecSupported { get; private set; } = null!;

        /// <summary>
        /// hasDnsAnycast flag of the DNS zone
        /// </summary>
        [Output("hasDnsAnycast")]
        public Output<bool> HasDnsAnycast { get; private set; } = null!;

        /// <summary>
        /// Last update date of the DNS zone
        /// </summary>
        [Output("lastUpdate")]
        public Output<string> LastUpdate { get; private set; } = null!;

        /// <summary>
        /// Zone name
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Name servers that host the DNS zone
        /// </summary>
        [Output("nameServers")]
        public Output<ImmutableArray<string>> NameServers { get; private set; } = null!;

        /// <summary>
        /// Details about an Order
        /// </summary>
        [Output("orders")]
        public Output<ImmutableArray<Outputs.ZoneOrder>> Orders { get; private set; } = null!;

        /// <summary>
        /// OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
        /// </summary>
        [Output("ovhSubsidiary")]
        public Output<string> OvhSubsidiary { get; private set; } = null!;

        /// <summary>
        /// Ovh payment mode
        /// </summary>
        [Output("paymentMean")]
        public Output<string?> PaymentMean { get; private set; } = null!;

        /// <summary>
        /// Product Plan to order
        /// </summary>
        [Output("plan")]
        public Output<Outputs.ZonePlan> Plan { get; private set; } = null!;

        /// <summary>
        /// Product Plan to order
        /// </summary>
        [Output("planOptions")]
        public Output<ImmutableArray<Outputs.ZonePlanOption>> PlanOptions { get; private set; } = null!;


        /// <summary>
        /// Create a Zone resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Zone(string name, ZoneArgs? args = null, CustomResourceOptions? options = null)
            : base("ovh:Domain/zone:Zone", name, args ?? new ZoneArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Zone(string name, Input<string> id, ZoneState? state = null, CustomResourceOptions? options = null)
            : base("ovh:Domain/zone:Zone", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/ovh/pulumi-ovh",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Zone resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Zone Get(string name, Input<string> id, ZoneState? state = null, CustomResourceOptions? options = null)
        {
            return new Zone(name, id, state, options);
        }
    }

    public sealed class ZoneArgs : global::Pulumi.ResourceArgs
    {
        [Input("orders")]
        private InputList<Inputs.ZoneOrderArgs>? _orders;

        /// <summary>
        /// Details about an Order
        /// </summary>
        public InputList<Inputs.ZoneOrderArgs> Orders
        {
            get => _orders ?? (_orders = new InputList<Inputs.ZoneOrderArgs>());
            set => _orders = value;
        }

        /// <summary>
        /// OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
        /// </summary>
        [Input("ovhSubsidiary")]
        public Input<string>? OvhSubsidiary { get; set; }

        /// <summary>
        /// Ovh payment mode
        /// </summary>
        [Input("paymentMean")]
        public Input<string>? PaymentMean { get; set; }

        /// <summary>
        /// Product Plan to order
        /// </summary>
        [Input("plan")]
        public Input<Inputs.ZonePlanArgs>? Plan { get; set; }

        [Input("planOptions")]
        private InputList<Inputs.ZonePlanOptionArgs>? _planOptions;

        /// <summary>
        /// Product Plan to order
        /// </summary>
        public InputList<Inputs.ZonePlanOptionArgs> PlanOptions
        {
            get => _planOptions ?? (_planOptions = new InputList<Inputs.ZonePlanOptionArgs>());
            set => _planOptions = value;
        }

        public ZoneArgs()
        {
        }
        public static new ZoneArgs Empty => new ZoneArgs();
    }

    public sealed class ZoneState : global::Pulumi.ResourceArgs
    {
        [Input("ZoneURN")]
        public Input<string>? ZoneURN { get; set; }

        /// <summary>
        /// Is DNSSEC supported by this zone
        /// </summary>
        [Input("dnssecSupported")]
        public Input<bool>? DnssecSupported { get; set; }

        /// <summary>
        /// hasDnsAnycast flag of the DNS zone
        /// </summary>
        [Input("hasDnsAnycast")]
        public Input<bool>? HasDnsAnycast { get; set; }

        /// <summary>
        /// Last update date of the DNS zone
        /// </summary>
        [Input("lastUpdate")]
        public Input<string>? LastUpdate { get; set; }

        /// <summary>
        /// Zone name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("nameServers")]
        private InputList<string>? _nameServers;

        /// <summary>
        /// Name servers that host the DNS zone
        /// </summary>
        public InputList<string> NameServers
        {
            get => _nameServers ?? (_nameServers = new InputList<string>());
            set => _nameServers = value;
        }

        [Input("orders")]
        private InputList<Inputs.ZoneOrderGetArgs>? _orders;

        /// <summary>
        /// Details about an Order
        /// </summary>
        public InputList<Inputs.ZoneOrderGetArgs> Orders
        {
            get => _orders ?? (_orders = new InputList<Inputs.ZoneOrderGetArgs>());
            set => _orders = value;
        }

        /// <summary>
        /// OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
        /// </summary>
        [Input("ovhSubsidiary")]
        public Input<string>? OvhSubsidiary { get; set; }

        /// <summary>
        /// Ovh payment mode
        /// </summary>
        [Input("paymentMean")]
        public Input<string>? PaymentMean { get; set; }

        /// <summary>
        /// Product Plan to order
        /// </summary>
        [Input("plan")]
        public Input<Inputs.ZonePlanGetArgs>? Plan { get; set; }

        [Input("planOptions")]
        private InputList<Inputs.ZonePlanOptionGetArgs>? _planOptions;

        /// <summary>
        /// Product Plan to order
        /// </summary>
        public InputList<Inputs.ZonePlanOptionGetArgs> PlanOptions
        {
            get => _planOptions ?? (_planOptions = new InputList<Inputs.ZonePlanOptionGetArgs>());
            set => _planOptions = value;
        }

        public ZoneState()
        {
        }
        public static new ZoneState Empty => new ZoneState();
    }
}
