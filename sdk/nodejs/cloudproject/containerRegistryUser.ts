// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Creates a user for a container registry associated with a public cloud project.
 *
 * ## Example Usage
 */
export class ContainerRegistryUser extends pulumi.CustomResource {
    /**
     * Get an existing ContainerRegistryUser resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ContainerRegistryUserState, opts?: pulumi.CustomResourceOptions): ContainerRegistryUser {
        return new ContainerRegistryUser(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:CloudProject/containerRegistryUser:ContainerRegistryUser';

    /**
     * Returns true if the given object is an instance of ContainerRegistryUser.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ContainerRegistryUser {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ContainerRegistryUser.__pulumiType;
    }

    /**
     * User email
     */
    public readonly email!: pulumi.Output<string>;
    /**
     * Registry name
     */
    public readonly login!: pulumi.Output<string>;
    /**
     * (Sensitive) User password
     */
    public /*out*/ readonly password!: pulumi.Output<string>;
    /**
     * Registry ID
     */
    public readonly registryId!: pulumi.Output<string>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    public readonly serviceName!: pulumi.Output<string>;
    /**
     * User name
     */
    public /*out*/ readonly user!: pulumi.Output<string>;

    /**
     * Create a ContainerRegistryUser resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ContainerRegistryUserArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ContainerRegistryUserArgs | ContainerRegistryUserState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ContainerRegistryUserState | undefined;
            resourceInputs["email"] = state ? state.email : undefined;
            resourceInputs["login"] = state ? state.login : undefined;
            resourceInputs["password"] = state ? state.password : undefined;
            resourceInputs["registryId"] = state ? state.registryId : undefined;
            resourceInputs["serviceName"] = state ? state.serviceName : undefined;
            resourceInputs["user"] = state ? state.user : undefined;
        } else {
            const args = argsOrState as ContainerRegistryUserArgs | undefined;
            if ((!args || args.email === undefined) && !opts.urn) {
                throw new Error("Missing required property 'email'");
            }
            if ((!args || args.login === undefined) && !opts.urn) {
                throw new Error("Missing required property 'login'");
            }
            if ((!args || args.registryId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'registryId'");
            }
            if ((!args || args.serviceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceName'");
            }
            resourceInputs["email"] = args ? args.email : undefined;
            resourceInputs["login"] = args ? args.login : undefined;
            resourceInputs["registryId"] = args ? args.registryId : undefined;
            resourceInputs["serviceName"] = args ? args.serviceName : undefined;
            resourceInputs["password"] = undefined /*out*/;
            resourceInputs["user"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["password"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(ContainerRegistryUser.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ContainerRegistryUser resources.
 */
export interface ContainerRegistryUserState {
    /**
     * User email
     */
    email?: pulumi.Input<string>;
    /**
     * Registry name
     */
    login?: pulumi.Input<string>;
    /**
     * (Sensitive) User password
     */
    password?: pulumi.Input<string>;
    /**
     * Registry ID
     */
    registryId?: pulumi.Input<string>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName?: pulumi.Input<string>;
    /**
     * User name
     */
    user?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ContainerRegistryUser resource.
 */
export interface ContainerRegistryUserArgs {
    /**
     * User email
     */
    email: pulumi.Input<string>;
    /**
     * Registry name
     */
    login: pulumi.Input<string>;
    /**
     * Registry ID
     */
    registryId: pulumi.Input<string>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName: pulumi.Input<string>;
}
