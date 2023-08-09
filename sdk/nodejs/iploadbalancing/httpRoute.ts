// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manage HTTP route for a loadbalancer service
 *
 * ## Example Usage
 *
 * Route which redirect all url to https.
 */
export class HttpRoute extends pulumi.CustomResource {
    /**
     * Get an existing HttpRoute resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HttpRouteState, opts?: pulumi.CustomResourceOptions): HttpRoute {
        return new HttpRoute(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:IpLoadBalancing/httpRoute:HttpRoute';

    /**
     * Returns true if the given object is an instance of HttpRoute.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is HttpRoute {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === HttpRoute.__pulumiType;
    }

    /**
     * Action triggered when all rules match
     */
    public readonly action!: pulumi.Output<outputs.IpLoadBalancing.HttpRouteAction>;
    /**
     * Human readable name for your route, this field is for you
     */
    public readonly displayName!: pulumi.Output<string | undefined>;
    /**
     * Route traffic for this frontend
     */
    public readonly frontendId!: pulumi.Output<number>;
    /**
     * List of rules to match to trigger action
     */
    public /*out*/ readonly rules!: pulumi.Output<outputs.IpLoadBalancing.HttpRouteRule[]>;
    /**
     * The internal name of your IP load balancing
     */
    public readonly serviceName!: pulumi.Output<string>;
    /**
     * HTTP status code for "redirect" and "reject" actions
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
     */
    public readonly weight!: pulumi.Output<number>;

    /**
     * Create a HttpRoute resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: HttpRouteArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: HttpRouteArgs | HttpRouteState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as HttpRouteState | undefined;
            resourceInputs["action"] = state ? state.action : undefined;
            resourceInputs["displayName"] = state ? state.displayName : undefined;
            resourceInputs["frontendId"] = state ? state.frontendId : undefined;
            resourceInputs["rules"] = state ? state.rules : undefined;
            resourceInputs["serviceName"] = state ? state.serviceName : undefined;
            resourceInputs["status"] = state ? state.status : undefined;
            resourceInputs["weight"] = state ? state.weight : undefined;
        } else {
            const args = argsOrState as HttpRouteArgs | undefined;
            if ((!args || args.action === undefined) && !opts.urn) {
                throw new Error("Missing required property 'action'");
            }
            if ((!args || args.serviceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceName'");
            }
            resourceInputs["action"] = args ? args.action : undefined;
            resourceInputs["displayName"] = args ? args.displayName : undefined;
            resourceInputs["frontendId"] = args ? args.frontendId : undefined;
            resourceInputs["serviceName"] = args ? args.serviceName : undefined;
            resourceInputs["weight"] = args ? args.weight : undefined;
            resourceInputs["rules"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(HttpRoute.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering HttpRoute resources.
 */
export interface HttpRouteState {
    /**
     * Action triggered when all rules match
     */
    action?: pulumi.Input<inputs.IpLoadBalancing.HttpRouteAction>;
    /**
     * Human readable name for your route, this field is for you
     */
    displayName?: pulumi.Input<string>;
    /**
     * Route traffic for this frontend
     */
    frontendId?: pulumi.Input<number>;
    /**
     * List of rules to match to trigger action
     */
    rules?: pulumi.Input<pulumi.Input<inputs.IpLoadBalancing.HttpRouteRule>[]>;
    /**
     * The internal name of your IP load balancing
     */
    serviceName?: pulumi.Input<string>;
    /**
     * HTTP status code for "redirect" and "reject" actions
     */
    status?: pulumi.Input<string>;
    /**
     * Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
     */
    weight?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a HttpRoute resource.
 */
export interface HttpRouteArgs {
    /**
     * Action triggered when all rules match
     */
    action: pulumi.Input<inputs.IpLoadBalancing.HttpRouteAction>;
    /**
     * Human readable name for your route, this field is for you
     */
    displayName?: pulumi.Input<string>;
    /**
     * Route traffic for this frontend
     */
    frontendId?: pulumi.Input<number>;
    /**
     * The internal name of your IP load balancing
     */
    serviceName: pulumi.Input<string>;
    /**
     * Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
     */
    weight?: pulumi.Input<number>;
}
