// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@ovhcloud/pulumi-ovh";
 * import * as ovh from "@pulumi/ovh";
 *
 * const myaccount = ovh.Me.getMe({});
 * const mycart = myaccount.then(myaccount => ovh.Order.getCart({
 *     ovhSubsidiary: myaccount.ovhSubsidiary,
 * }));
 * const zoneCartProductPlan = mycart.then(mycart => ovh.Order.getCartProductPlan({
 *     cartId: mycart.id,
 *     priceCapacity: "renew",
 *     product: "dns",
 *     planCode: "zone",
 * }));
 * const zoneZone = new ovh.domain.Zone("zoneZone", {
 *     ovhSubsidiary: mycart.then(mycart => mycart.ovhSubsidiary),
 *     plan: {
 *         duration: zoneCartProductPlan.then(zoneCartProductPlan => zoneCartProductPlan.selectedPrices?.[0]?.duration),
 *         planCode: zoneCartProductPlan.then(zoneCartProductPlan => zoneCartProductPlan.planCode),
 *         pricingMode: zoneCartProductPlan.then(zoneCartProductPlan => zoneCartProductPlan.selectedPrices?.[0]?.pricingMode),
 *         configurations: [
 *             {
 *                 label: "zone",
 *                 value: "myzone.mydomain.com",
 *             },
 *             {
 *                 label: "template",
 *                 value: "minimized",
 *             },
 *         ],
 *     },
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 *
 * ## Import
 *
 * Zone can be imported using the `order_id` that can be retrieved in the [order page](https://www.ovh.com/manager/#/dedicated/billing/orders/orders) at the creation time of the zone.
 *
 * bash
 *
 * ```sh
 * $ pulumi import ovh:Domain/zone:Zone zone order_id
 * ```
 */
export class Zone extends pulumi.CustomResource {
    /**
     * Get an existing Zone resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ZoneState, opts?: pulumi.CustomResourceOptions): Zone {
        return new Zone(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:Domain/zone:Zone';

    /**
     * Returns true if the given object is an instance of Zone.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Zone {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Zone.__pulumiType;
    }

    public /*out*/ readonly ZoneURN!: pulumi.Output<string>;
    /**
     * Is DNSSEC supported by this zone
     */
    public /*out*/ readonly dnssecSupported!: pulumi.Output<boolean>;
    /**
     * hasDnsAnycast flag of the DNS zone
     */
    public /*out*/ readonly hasDnsAnycast!: pulumi.Output<boolean>;
    /**
     * Last update date of the DNS zone
     */
    public /*out*/ readonly lastUpdate!: pulumi.Output<string>;
    /**
     * Zone name
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * Name servers that host the DNS zone
     */
    public /*out*/ readonly nameServers!: pulumi.Output<string[]>;
    /**
     * Details about an Order
     */
    public /*out*/ readonly orders!: pulumi.Output<outputs.Domain.ZoneOrder[]>;
    /**
     * OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
     */
    public readonly ovhSubsidiary!: pulumi.Output<string>;
    /**
     * Ovh payment mode
     *
     * @deprecated This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
     */
    public readonly paymentMean!: pulumi.Output<string | undefined>;
    /**
     * Product Plan to order
     */
    public readonly plan!: pulumi.Output<outputs.Domain.ZonePlan>;
    /**
     * Product Plan to order
     */
    public readonly planOptions!: pulumi.Output<outputs.Domain.ZonePlanOption[] | undefined>;

    /**
     * Create a Zone resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ZoneArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ZoneArgs | ZoneState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ZoneState | undefined;
            resourceInputs["ZoneURN"] = state ? state.ZoneURN : undefined;
            resourceInputs["dnssecSupported"] = state ? state.dnssecSupported : undefined;
            resourceInputs["hasDnsAnycast"] = state ? state.hasDnsAnycast : undefined;
            resourceInputs["lastUpdate"] = state ? state.lastUpdate : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["nameServers"] = state ? state.nameServers : undefined;
            resourceInputs["orders"] = state ? state.orders : undefined;
            resourceInputs["ovhSubsidiary"] = state ? state.ovhSubsidiary : undefined;
            resourceInputs["paymentMean"] = state ? state.paymentMean : undefined;
            resourceInputs["plan"] = state ? state.plan : undefined;
            resourceInputs["planOptions"] = state ? state.planOptions : undefined;
        } else {
            const args = argsOrState as ZoneArgs | undefined;
            if ((!args || args.ovhSubsidiary === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ovhSubsidiary'");
            }
            if ((!args || args.plan === undefined) && !opts.urn) {
                throw new Error("Missing required property 'plan'");
            }
            resourceInputs["ovhSubsidiary"] = args ? args.ovhSubsidiary : undefined;
            resourceInputs["paymentMean"] = args ? args.paymentMean : undefined;
            resourceInputs["plan"] = args ? args.plan : undefined;
            resourceInputs["planOptions"] = args ? args.planOptions : undefined;
            resourceInputs["ZoneURN"] = undefined /*out*/;
            resourceInputs["dnssecSupported"] = undefined /*out*/;
            resourceInputs["hasDnsAnycast"] = undefined /*out*/;
            resourceInputs["lastUpdate"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["nameServers"] = undefined /*out*/;
            resourceInputs["orders"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Zone.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Zone resources.
 */
export interface ZoneState {
    ZoneURN?: pulumi.Input<string>;
    /**
     * Is DNSSEC supported by this zone
     */
    dnssecSupported?: pulumi.Input<boolean>;
    /**
     * hasDnsAnycast flag of the DNS zone
     */
    hasDnsAnycast?: pulumi.Input<boolean>;
    /**
     * Last update date of the DNS zone
     */
    lastUpdate?: pulumi.Input<string>;
    /**
     * Zone name
     */
    name?: pulumi.Input<string>;
    /**
     * Name servers that host the DNS zone
     */
    nameServers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Details about an Order
     */
    orders?: pulumi.Input<pulumi.Input<inputs.Domain.ZoneOrder>[]>;
    /**
     * OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
     */
    ovhSubsidiary?: pulumi.Input<string>;
    /**
     * Ovh payment mode
     *
     * @deprecated This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
     */
    paymentMean?: pulumi.Input<string>;
    /**
     * Product Plan to order
     */
    plan?: pulumi.Input<inputs.Domain.ZonePlan>;
    /**
     * Product Plan to order
     */
    planOptions?: pulumi.Input<pulumi.Input<inputs.Domain.ZonePlanOption>[]>;
}

/**
 * The set of arguments for constructing a Zone resource.
 */
export interface ZoneArgs {
    /**
     * OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
     */
    ovhSubsidiary: pulumi.Input<string>;
    /**
     * Ovh payment mode
     *
     * @deprecated This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
     */
    paymentMean?: pulumi.Input<string>;
    /**
     * Product Plan to order
     */
    plan: pulumi.Input<inputs.Domain.ZonePlan>;
    /**
     * Product Plan to order
     */
    planOptions?: pulumi.Input<pulumi.Input<inputs.Domain.ZonePlanOption>[]>;
}
