// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Attach an IP block to a VRack.
 *
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
 * const vrackCartProductPlan = mycart.then(mycart => ovh.Order.getCartProductPlan({
 *     cartId: mycart.id,
 *     priceCapacity: "renew",
 *     product: "vrack",
 *     planCode: "vrack",
 * }));
 * const vrackVrack = new ovh.vrack.Vrack("vrackVrack", {
 *     description: mycart.then(mycart => mycart.description),
 *     ovhSubsidiary: mycart.then(mycart => mycart.ovhSubsidiary),
 *     plan: {
 *         duration: vrackCartProductPlan.then(vrackCartProductPlan => vrackCartProductPlan.selectedPrices?.[0]?.duration),
 *         planCode: vrackCartProductPlan.then(vrackCartProductPlan => vrackCartProductPlan.planCode),
 *         pricingMode: vrackCartProductPlan.then(vrackCartProductPlan => vrackCartProductPlan.selectedPrices?.[0]?.pricingMode),
 *     },
 * });
 * const ipblockCartProductPlan = mycart.then(mycart => ovh.Order.getCartProductPlan({
 *     cartId: mycart.id,
 *     priceCapacity: "renew",
 *     product: "ip",
 *     planCode: "ip-v4-s30-ripe",
 * }));
 * const ipblockIpService = new ovh.ip.IpService("ipblockIpService", {
 *     ovhSubsidiary: mycart.then(mycart => mycart.ovhSubsidiary),
 *     description: mycart.then(mycart => mycart.description),
 *     plan: {
 *         duration: ipblockCartProductPlan.then(ipblockCartProductPlan => ipblockCartProductPlan.selectedPrices?.[0]?.duration),
 *         planCode: ipblockCartProductPlan.then(ipblockCartProductPlan => ipblockCartProductPlan.planCode),
 *         pricingMode: ipblockCartProductPlan.then(ipblockCartProductPlan => ipblockCartProductPlan.selectedPrices?.[0]?.pricingMode),
 *         configurations: [{
 *             label: "country",
 *             value: "FR",
 *         }],
 *     },
 * });
 * const vrackblock = new ovh.vrack.IpAddress("vrackblock", {
 *     serviceName: vrackVrack.serviceName,
 *     block: ipblockIpService.ip,
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export class IpAddress extends pulumi.CustomResource {
    /**
     * Get an existing IpAddress resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IpAddressState, opts?: pulumi.CustomResourceOptions): IpAddress {
        return new IpAddress(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:Vrack/ipAddress:IpAddress';

    /**
     * Returns true if the given object is an instance of IpAddress.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is IpAddress {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === IpAddress.__pulumiType;
    }

    /**
     * Your IP block.
     */
    public readonly block!: pulumi.Output<string>;
    /**
     * Your gateway
     */
    public /*out*/ readonly gateway!: pulumi.Output<string>;
    /**
     * Your IP block
     */
    public /*out*/ readonly ip!: pulumi.Output<string>;
    /**
     * The internal name of your vrack
     */
    public readonly serviceName!: pulumi.Output<string>;
    /**
     * Where you want your block announced on the network
     */
    public /*out*/ readonly zone!: pulumi.Output<string>;

    /**
     * Create a IpAddress resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IpAddressArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: IpAddressArgs | IpAddressState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as IpAddressState | undefined;
            resourceInputs["block"] = state ? state.block : undefined;
            resourceInputs["gateway"] = state ? state.gateway : undefined;
            resourceInputs["ip"] = state ? state.ip : undefined;
            resourceInputs["serviceName"] = state ? state.serviceName : undefined;
            resourceInputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as IpAddressArgs | undefined;
            if ((!args || args.block === undefined) && !opts.urn) {
                throw new Error("Missing required property 'block'");
            }
            if ((!args || args.serviceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceName'");
            }
            resourceInputs["block"] = args ? args.block : undefined;
            resourceInputs["serviceName"] = args ? args.serviceName : undefined;
            resourceInputs["gateway"] = undefined /*out*/;
            resourceInputs["ip"] = undefined /*out*/;
            resourceInputs["zone"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(IpAddress.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering IpAddress resources.
 */
export interface IpAddressState {
    /**
     * Your IP block.
     */
    block?: pulumi.Input<string>;
    /**
     * Your gateway
     */
    gateway?: pulumi.Input<string>;
    /**
     * Your IP block
     */
    ip?: pulumi.Input<string>;
    /**
     * The internal name of your vrack
     */
    serviceName?: pulumi.Input<string>;
    /**
     * Where you want your block announced on the network
     */
    zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a IpAddress resource.
 */
export interface IpAddressArgs {
    /**
     * Your IP block.
     */
    block: pulumi.Input<string>;
    /**
     * The internal name of your vrack
     */
    serviceName: pulumi.Input<string>;
}
