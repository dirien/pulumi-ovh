// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Create a new database on your private cloud database service.
 *
 * ## Example Usage
 *
 * ## Import
 *
 * OVHcloud Webhosting database can be imported using the `service_name` and the `database_name`, separated by "/" E.g., <break><break>```sh<break> $ pulumi import ovh:Hosting/privateDatabaseDb:PrivateDatabaseDb database service_name/database_name <break>```<break><break>
 */
export class PrivateDatabaseDb extends pulumi.CustomResource {
    /**
     * Get an existing PrivateDatabaseDb resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PrivateDatabaseDbState, opts?: pulumi.CustomResourceOptions): PrivateDatabaseDb {
        return new PrivateDatabaseDb(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:Hosting/privateDatabaseDb:PrivateDatabaseDb';

    /**
     * Returns true if the given object is an instance of PrivateDatabaseDb.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PrivateDatabaseDb {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PrivateDatabaseDb.__pulumiType;
    }

    /**
     * Name of your new database
     */
    public readonly databaseName!: pulumi.Output<string>;
    /**
     * The internal name of your private database.
     */
    public readonly serviceName!: pulumi.Output<string>;

    /**
     * Create a PrivateDatabaseDb resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PrivateDatabaseDbArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PrivateDatabaseDbArgs | PrivateDatabaseDbState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as PrivateDatabaseDbState | undefined;
            resourceInputs["databaseName"] = state ? state.databaseName : undefined;
            resourceInputs["serviceName"] = state ? state.serviceName : undefined;
        } else {
            const args = argsOrState as PrivateDatabaseDbArgs | undefined;
            if ((!args || args.databaseName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'databaseName'");
            }
            if ((!args || args.serviceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceName'");
            }
            resourceInputs["databaseName"] = args ? args.databaseName : undefined;
            resourceInputs["serviceName"] = args ? args.serviceName : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(PrivateDatabaseDb.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PrivateDatabaseDb resources.
 */
export interface PrivateDatabaseDbState {
    /**
     * Name of your new database
     */
    databaseName?: pulumi.Input<string>;
    /**
     * The internal name of your private database.
     */
    serviceName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a PrivateDatabaseDb resource.
 */
export interface PrivateDatabaseDbArgs {
    /**
     * Name of your new database
     */
    databaseName: pulumi.Input<string>;
    /**
     * The internal name of your private database.
     */
    serviceName: pulumi.Input<string>;
}
