// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Creates an IAM policy.
 *
 * ## Important
 *
 * > Using this resource requires that the account is enrolled in the OVHcloud [IAM beta](https://labs.ovhcloud.com/en/iam/)
 *
 * ## Example Usage
 */
export class Policy extends pulumi.CustomResource {
    /**
     * Get an existing Policy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyState, opts?: pulumi.CustomResourceOptions): Policy {
        return new Policy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:Iam/policy:Policy';

    /**
     * Returns true if the given object is an instance of Policy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Policy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Policy.__pulumiType;
    }

    /**
     * List of actions allowed on resources by identities
     */
    public readonly allows!: pulumi.Output<string[] | undefined>;
    /**
     * Creation date of this group.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * Description of the policy
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * List of overrides of action that must not be allowed even if they are caught by allow. Only makes sens if allow contains wildcards.
     */
    public readonly excepts!: pulumi.Output<string[] | undefined>;
    /**
     * List of identities affected by the policy
     */
    public readonly identities!: pulumi.Output<string[]>;
    /**
     * Name of the policy, must be unique
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Owner of the policy.
     */
    public /*out*/ readonly owner!: pulumi.Output<string>;
    /**
     * Indicates that the policy is a default one.
     */
    public /*out*/ readonly readOnly!: pulumi.Output<boolean>;
    /**
     * List of resources affected by the policy
     */
    public readonly resources!: pulumi.Output<string[]>;
    /**
     * Date of the last update of this group.
     */
    public /*out*/ readonly updatedAt!: pulumi.Output<string>;

    /**
     * Create a Policy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PolicyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PolicyArgs | PolicyState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as PolicyState | undefined;
            resourceInputs["allows"] = state ? state.allows : undefined;
            resourceInputs["createdAt"] = state ? state.createdAt : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["excepts"] = state ? state.excepts : undefined;
            resourceInputs["identities"] = state ? state.identities : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["owner"] = state ? state.owner : undefined;
            resourceInputs["readOnly"] = state ? state.readOnly : undefined;
            resourceInputs["resources"] = state ? state.resources : undefined;
            resourceInputs["updatedAt"] = state ? state.updatedAt : undefined;
        } else {
            const args = argsOrState as PolicyArgs | undefined;
            if ((!args || args.identities === undefined) && !opts.urn) {
                throw new Error("Missing required property 'identities'");
            }
            if ((!args || args.resources === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resources'");
            }
            resourceInputs["allows"] = args ? args.allows : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["excepts"] = args ? args.excepts : undefined;
            resourceInputs["identities"] = args ? args.identities : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["resources"] = args ? args.resources : undefined;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["owner"] = undefined /*out*/;
            resourceInputs["readOnly"] = undefined /*out*/;
            resourceInputs["updatedAt"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Policy.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Policy resources.
 */
export interface PolicyState {
    /**
     * List of actions allowed on resources by identities
     */
    allows?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Creation date of this group.
     */
    createdAt?: pulumi.Input<string>;
    /**
     * Description of the policy
     */
    description?: pulumi.Input<string>;
    /**
     * List of overrides of action that must not be allowed even if they are caught by allow. Only makes sens if allow contains wildcards.
     */
    excepts?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * List of identities affected by the policy
     */
    identities?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Name of the policy, must be unique
     */
    name?: pulumi.Input<string>;
    /**
     * Owner of the policy.
     */
    owner?: pulumi.Input<string>;
    /**
     * Indicates that the policy is a default one.
     */
    readOnly?: pulumi.Input<boolean>;
    /**
     * List of resources affected by the policy
     */
    resources?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Date of the last update of this group.
     */
    updatedAt?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Policy resource.
 */
export interface PolicyArgs {
    /**
     * List of actions allowed on resources by identities
     */
    allows?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Description of the policy
     */
    description?: pulumi.Input<string>;
    /**
     * List of overrides of action that must not be allowed even if they are caught by allow. Only makes sens if allow contains wildcards.
     */
    excepts?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * List of identities affected by the policy
     */
    identities: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Name of the policy, must be unique
     */
    name?: pulumi.Input<string>;
    /**
     * List of resources affected by the policy
     */
    resources: pulumi.Input<pulumi.Input<string>[]>;
}
