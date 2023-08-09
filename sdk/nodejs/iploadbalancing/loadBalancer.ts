// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * ## Example Usage
 */
export class LoadBalancer extends pulumi.CustomResource {
    /**
     * Get an existing LoadBalancer resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LoadBalancerState, opts?: pulumi.CustomResourceOptions): LoadBalancer {
        return new LoadBalancer(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:IpLoadBalancing/loadBalancer:LoadBalancer';

    /**
     * Returns true if the given object is an instance of LoadBalancer.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LoadBalancer {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LoadBalancer.__pulumiType;
    }

    /**
     * Set the name displayed in ManagerV6 for your iplb (max 50 chars)
     */
    public readonly displayName!: pulumi.Output<string>;
    /**
     * Your IP load balancing
     */
    public /*out*/ readonly ipLoadbalancing!: pulumi.Output<string>;
    /**
     * The IPV4 associated to your IP load balancing
     */
    public /*out*/ readonly ipv4!: pulumi.Output<string>;
    /**
     * The IPV6 associated to your IP load balancing. DEPRECATED.
     */
    public /*out*/ readonly ipv6!: pulumi.Output<string>;
    /**
     * The metrics token associated with your IP load balancing
     */
    public /*out*/ readonly metricsToken!: pulumi.Output<string>;
    /**
     * The offer of your IP load balancing
     */
    public /*out*/ readonly offer!: pulumi.Output<string>;
    /**
     * Available additional zone for your Load Balancer
     */
    public /*out*/ readonly orderableZones!: pulumi.Output<outputs.IpLoadBalancing.LoadBalancerOrderableZone[]>;
    /**
     * Details about an Order
     */
    public /*out*/ readonly orders!: pulumi.Output<outputs.IpLoadBalancing.LoadBalancerOrder[]>;
    /**
     * OVHcloud Subsidiary
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
    public readonly plan!: pulumi.Output<outputs.IpLoadBalancing.LoadBalancerPlan>;
    /**
     * Product Plan to order
     */
    public readonly planOptions!: pulumi.Output<outputs.IpLoadBalancing.LoadBalancerPlanOption[] | undefined>;
    /**
     * The internal name of your IP load balancing
     */
    public /*out*/ readonly serviceName!: pulumi.Output<string>;
    /**
     * Modern oldest compatible clients : Firefox 27, Chrome 30, IE 11 on Windows 7, Edge, Opera 17, Safari 9, Android 5.0, and Java 8. Intermediate oldest compatible clients : Firefox 1, Chrome 1, IE 7, Opera 5, Safari 1, Windows XP IE8, Android 2.3, Java 7. Intermediate if null. one of "intermediate", "modern".
     */
    public readonly sslConfiguration!: pulumi.Output<string>;
    /**
     * Current state of your IP
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * URN of the load balancer, used when writing IAM policies
     */
    public /*out*/ readonly urn!: pulumi.Output<string>;
    /**
     * Vrack eligibility
     */
    public /*out*/ readonly vrackEligibility!: pulumi.Output<boolean>;
    /**
     * Name of the vRack on which the current Load Balancer is attached to, as it is named on vRack product
     */
    public /*out*/ readonly vrackName!: pulumi.Output<string>;
    /**
     * Location where your service is
     */
    public /*out*/ readonly zones!: pulumi.Output<string[]>;

    /**
     * Create a LoadBalancer resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LoadBalancerArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: LoadBalancerArgs | LoadBalancerState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as LoadBalancerState | undefined;
            resourceInputs["displayName"] = state ? state.displayName : undefined;
            resourceInputs["ipLoadbalancing"] = state ? state.ipLoadbalancing : undefined;
            resourceInputs["ipv4"] = state ? state.ipv4 : undefined;
            resourceInputs["ipv6"] = state ? state.ipv6 : undefined;
            resourceInputs["metricsToken"] = state ? state.metricsToken : undefined;
            resourceInputs["offer"] = state ? state.offer : undefined;
            resourceInputs["orderableZones"] = state ? state.orderableZones : undefined;
            resourceInputs["orders"] = state ? state.orders : undefined;
            resourceInputs["ovhSubsidiary"] = state ? state.ovhSubsidiary : undefined;
            resourceInputs["paymentMean"] = state ? state.paymentMean : undefined;
            resourceInputs["plan"] = state ? state.plan : undefined;
            resourceInputs["planOptions"] = state ? state.planOptions : undefined;
            resourceInputs["serviceName"] = state ? state.serviceName : undefined;
            resourceInputs["sslConfiguration"] = state ? state.sslConfiguration : undefined;
            resourceInputs["state"] = state ? state.state : undefined;
            resourceInputs["urn"] = state ? state.urn : undefined;
            resourceInputs["vrackEligibility"] = state ? state.vrackEligibility : undefined;
            resourceInputs["vrackName"] = state ? state.vrackName : undefined;
            resourceInputs["zones"] = state ? state.zones : undefined;
        } else {
            const args = argsOrState as LoadBalancerArgs | undefined;
            if ((!args || args.ovhSubsidiary === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ovhSubsidiary'");
            }
            if ((!args || args.plan === undefined) && !opts.urn) {
                throw new Error("Missing required property 'plan'");
            }
            resourceInputs["displayName"] = args ? args.displayName : undefined;
            resourceInputs["ovhSubsidiary"] = args ? args.ovhSubsidiary : undefined;
            resourceInputs["paymentMean"] = args ? args.paymentMean : undefined;
            resourceInputs["plan"] = args ? args.plan : undefined;
            resourceInputs["planOptions"] = args ? args.planOptions : undefined;
            resourceInputs["sslConfiguration"] = args ? args.sslConfiguration : undefined;
            resourceInputs["ipLoadbalancing"] = undefined /*out*/;
            resourceInputs["ipv4"] = undefined /*out*/;
            resourceInputs["ipv6"] = undefined /*out*/;
            resourceInputs["metricsToken"] = undefined /*out*/;
            resourceInputs["offer"] = undefined /*out*/;
            resourceInputs["orderableZones"] = undefined /*out*/;
            resourceInputs["orders"] = undefined /*out*/;
            resourceInputs["serviceName"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["urn"] = undefined /*out*/;
            resourceInputs["vrackEligibility"] = undefined /*out*/;
            resourceInputs["vrackName"] = undefined /*out*/;
            resourceInputs["zones"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["metricsToken"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(LoadBalancer.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering LoadBalancer resources.
 */
export interface LoadBalancerState {
    /**
     * Set the name displayed in ManagerV6 for your iplb (max 50 chars)
     */
    displayName?: pulumi.Input<string>;
    /**
     * Your IP load balancing
     */
    ipLoadbalancing?: pulumi.Input<string>;
    /**
     * The IPV4 associated to your IP load balancing
     */
    ipv4?: pulumi.Input<string>;
    /**
     * The IPV6 associated to your IP load balancing. DEPRECATED.
     */
    ipv6?: pulumi.Input<string>;
    /**
     * The metrics token associated with your IP load balancing
     */
    metricsToken?: pulumi.Input<string>;
    /**
     * The offer of your IP load balancing
     */
    offer?: pulumi.Input<string>;
    /**
     * Available additional zone for your Load Balancer
     */
    orderableZones?: pulumi.Input<pulumi.Input<inputs.IpLoadBalancing.LoadBalancerOrderableZone>[]>;
    /**
     * Details about an Order
     */
    orders?: pulumi.Input<pulumi.Input<inputs.IpLoadBalancing.LoadBalancerOrder>[]>;
    /**
     * OVHcloud Subsidiary
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
    plan?: pulumi.Input<inputs.IpLoadBalancing.LoadBalancerPlan>;
    /**
     * Product Plan to order
     */
    planOptions?: pulumi.Input<pulumi.Input<inputs.IpLoadBalancing.LoadBalancerPlanOption>[]>;
    /**
     * The internal name of your IP load balancing
     */
    serviceName?: pulumi.Input<string>;
    /**
     * Modern oldest compatible clients : Firefox 27, Chrome 30, IE 11 on Windows 7, Edge, Opera 17, Safari 9, Android 5.0, and Java 8. Intermediate oldest compatible clients : Firefox 1, Chrome 1, IE 7, Opera 5, Safari 1, Windows XP IE8, Android 2.3, Java 7. Intermediate if null. one of "intermediate", "modern".
     */
    sslConfiguration?: pulumi.Input<string>;
    /**
     * Current state of your IP
     */
    state?: pulumi.Input<string>;
    /**
     * URN of the load balancer, used when writing IAM policies
     */
    urn?: pulumi.Input<string>;
    /**
     * Vrack eligibility
     */
    vrackEligibility?: pulumi.Input<boolean>;
    /**
     * Name of the vRack on which the current Load Balancer is attached to, as it is named on vRack product
     */
    vrackName?: pulumi.Input<string>;
    /**
     * Location where your service is
     */
    zones?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a LoadBalancer resource.
 */
export interface LoadBalancerArgs {
    /**
     * Set the name displayed in ManagerV6 for your iplb (max 50 chars)
     */
    displayName?: pulumi.Input<string>;
    /**
     * OVHcloud Subsidiary
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
    plan: pulumi.Input<inputs.IpLoadBalancing.LoadBalancerPlan>;
    /**
     * Product Plan to order
     */
    planOptions?: pulumi.Input<pulumi.Input<inputs.IpLoadBalancing.LoadBalancerPlanOption>[]>;
    /**
     * Modern oldest compatible clients : Firefox 27, Chrome 30, IE 11 on Windows 7, Edge, Opera 17, Safari 9, Android 5.0, and Java 8. Intermediate oldest compatible clients : Firefox 1, Chrome 1, IE 7, Opera 5, Safari 1, Windows XP IE8, Android 2.3, Java 7. Intermediate if null. one of "intermediate", "modern".
     */
    sslConfiguration?: pulumi.Input<string>;
}
