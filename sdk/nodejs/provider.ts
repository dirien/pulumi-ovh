// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The provider type for the ovh package. By default, resources use package-wide configuration
 * settings, however an explicit `Provider` instance may be created and passed during resource
 * construction to achieve fine-grained programmatic control over provider settings. See the
 * [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
 */
export class Provider extends pulumi.ProviderResource {
    /** @internal */
    public static readonly __pulumiType = 'ovh';

    /**
     * Returns true if the given object is an instance of Provider.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Provider {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === "pulumi:providers:" + Provider.__pulumiType;
    }

    /**
     * The OVH API Application Key.
     */
    public readonly applicationKey!: pulumi.Output<string | undefined>;
    /**
     * The OVH API Application Secret.
     */
    public readonly applicationSecret!: pulumi.Output<string | undefined>;
    /**
     * The OVH API Consumer key.
     */
    public readonly consumerKey!: pulumi.Output<string | undefined>;
    /**
     * The OVH API endpoint to target (ex: "ovh-eu").
     */
    public readonly endpoint!: pulumi.Output<string>;

    /**
     * Create a Provider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProviderArgs, opts?: pulumi.ResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        {
            if ((!args || args.endpoint === undefined) && !opts.urn) {
                throw new Error("Missing required property 'endpoint'");
            }
            resourceInputs["applicationKey"] = args ? args.applicationKey : undefined;
            resourceInputs["applicationSecret"] = args ? args.applicationSecret : undefined;
            resourceInputs["consumerKey"] = args ? args.consumerKey : undefined;
            resourceInputs["endpoint"] = args ? args.endpoint : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Provider.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Provider resource.
 */
export interface ProviderArgs {
    /**
     * The OVH API Application Key.
     */
    applicationKey?: pulumi.Input<string>;
    /**
     * The OVH API Application Secret.
     */
    applicationSecret?: pulumi.Input<string>;
    /**
     * The OVH API Consumer key.
     */
    consumerKey?: pulumi.Input<string>;
    /**
     * The OVH API endpoint to target (ex: "ovh-eu").
     */
    endpoint: pulumi.Input<string>;
}
