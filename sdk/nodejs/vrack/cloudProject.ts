// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Attach a Public Cloud Project to a VRack.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@ovhcloud/pulumi-ovh";
 *
 * const vcp = new ovh.vrack.CloudProject("vcp", {
 *     projectId: "67890",
 *     serviceName: "12345",
 * });
 * ```
 *
 * ## Import
 *
 * Attachment of a public cloud project and a VRack can be imported using the `project_id`, the `service_name` (vRackID) and the `attach_id`, separated by "/" E.g.,
 *
 *  bash
 *
 * ```sh
 * $ pulumi import ovh:Vrack/cloudProject:CloudProject myattach ookie9mee8Shaeghaeleeju7Xeghohv6e/pn-12345678/vrack_pn-12345678-cloudproject_ookie9mee8Shaeghaeleeju7Xeghohv6e-attach
 * ```
 */
export class CloudProject extends pulumi.CustomResource {
    /**
     * Get an existing CloudProject resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CloudProjectState, opts?: pulumi.CustomResourceOptions): CloudProject {
        return new CloudProject(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:Vrack/cloudProject:CloudProject';

    /**
     * Returns true if the given object is an instance of CloudProject.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CloudProject {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CloudProject.__pulumiType;
    }

    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * The service name of the vrack. If omitted,
     * the `OVH_VRACK_SERVICE` environment variable is used.
     */
    public readonly serviceName!: pulumi.Output<string>;

    /**
     * Create a CloudProject resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CloudProjectArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CloudProjectArgs | CloudProjectState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CloudProjectState | undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["serviceName"] = state ? state.serviceName : undefined;
        } else {
            const args = argsOrState as CloudProjectArgs | undefined;
            if ((!args || args.projectId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'projectId'");
            }
            if ((!args || args.serviceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceName'");
            }
            resourceInputs["projectId"] = args ? args.projectId : undefined;
            resourceInputs["serviceName"] = args ? args.serviceName : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(CloudProject.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CloudProject resources.
 */
export interface CloudProjectState {
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    projectId?: pulumi.Input<string>;
    /**
     * The service name of the vrack. If omitted,
     * the `OVH_VRACK_SERVICE` environment variable is used.
     */
    serviceName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a CloudProject resource.
 */
export interface CloudProjectArgs {
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    projectId: pulumi.Input<string>;
    /**
     * The service name of the vrack. If omitted,
     * the `OVH_VRACK_SERVICE` environment variable is used.
     */
    serviceName: pulumi.Input<string>;
}
