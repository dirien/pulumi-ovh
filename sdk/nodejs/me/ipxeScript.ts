// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Creates an IPXE Script.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as fs from "fs";
 * import * as ovh from "@ovh-devrelteam/pulumi-ovh";
 *
 * const script = new ovh.me.IpxeScript("script", {script: fs.readFileSync(`${path.module}/boot.ipxe`, "utf8")});
 * ```
 */
export class IpxeScript extends pulumi.CustomResource {
    /**
     * Get an existing IpxeScript resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IpxeScriptState, opts?: pulumi.CustomResourceOptions): IpxeScript {
        return new IpxeScript(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:Me/ipxeScript:IpxeScript';

    /**
     * Returns true if the given object is an instance of IpxeScript.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is IpxeScript {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === IpxeScript.__pulumiType;
    }

    /**
     * For documentation purpose only. This attribute is not passed to the OVHcloud API as it cannot be retrieved back. Instead a fake description ('$name auto description') is passed at creation time.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * The name of the IPXE Script.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The content of the script.
     */
    public readonly script!: pulumi.Output<string>;

    /**
     * Create a IpxeScript resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IpxeScriptArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: IpxeScriptArgs | IpxeScriptState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as IpxeScriptState | undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["script"] = state ? state.script : undefined;
        } else {
            const args = argsOrState as IpxeScriptArgs | undefined;
            if ((!args || args.script === undefined) && !opts.urn) {
                throw new Error("Missing required property 'script'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["script"] = args ? args.script : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(IpxeScript.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering IpxeScript resources.
 */
export interface IpxeScriptState {
    /**
     * For documentation purpose only. This attribute is not passed to the OVHcloud API as it cannot be retrieved back. Instead a fake description ('$name auto description') is passed at creation time.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the IPXE Script.
     */
    name?: pulumi.Input<string>;
    /**
     * The content of the script.
     */
    script?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a IpxeScript resource.
 */
export interface IpxeScriptArgs {
    /**
     * For documentation purpose only. This attribute is not passed to the OVHcloud API as it cannot be retrieved back. Instead a fake description ('$name auto description') is passed at creation time.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the IPXE Script.
     */
    name?: pulumi.Input<string>;
    /**
     * The content of the script.
     */
    script: pulumi.Input<string>;
}
