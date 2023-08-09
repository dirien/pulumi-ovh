// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Creates a dbaas logs input.
 *
 * ## Example Usage
 */
export class LogsInput extends pulumi.CustomResource {
    /**
     * Get an existing LogsInput resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LogsInputState, opts?: pulumi.CustomResourceOptions): LogsInput {
        return new LogsInput(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:Dbaas/logsInput:LogsInput';

    /**
     * Returns true if the given object is an instance of LogsInput.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LogsInput {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LogsInput.__pulumiType;
    }

    /**
     * List of IP blocks
     */
    public readonly allowedNetworks!: pulumi.Output<string[]>;
    /**
     * Input configuration
     */
    public readonly configuration!: pulumi.Output<outputs.Dbaas.LogsInputConfiguration>;
    /**
     * Input creation
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * Input description
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * Input engine ID
     */
    public readonly engineId!: pulumi.Output<string>;
    /**
     * Port
     */
    public readonly exposedPort!: pulumi.Output<string>;
    /**
     * Hostname
     */
    public /*out*/ readonly hostname!: pulumi.Output<string>;
    /**
     * Input ID
     */
    public /*out*/ readonly inputId!: pulumi.Output<string>;
    /**
     * Indicate if input need to be restarted
     */
    public /*out*/ readonly isRestartRequired!: pulumi.Output<boolean>;
    /**
     * Number of instance running
     */
    public readonly nbInstance!: pulumi.Output<number>;
    /**
     * Input IP address
     */
    public /*out*/ readonly publicAddress!: pulumi.Output<string>;
    /**
     * service name
     */
    public readonly serviceName!: pulumi.Output<string>;
    /**
     * Input SSL certificate
     */
    public /*out*/ readonly sslCertificate!: pulumi.Output<string>;
    /**
     * init: configuration required, pending: ready to start, running: available
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * Associated Graylog stream
     */
    public readonly streamId!: pulumi.Output<string>;
    /**
     * Input title
     */
    public readonly title!: pulumi.Output<string>;
    /**
     * Input last update
     */
    public /*out*/ readonly updatedAt!: pulumi.Output<string>;

    /**
     * Create a LogsInput resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LogsInputArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: LogsInputArgs | LogsInputState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as LogsInputState | undefined;
            resourceInputs["allowedNetworks"] = state ? state.allowedNetworks : undefined;
            resourceInputs["configuration"] = state ? state.configuration : undefined;
            resourceInputs["createdAt"] = state ? state.createdAt : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["engineId"] = state ? state.engineId : undefined;
            resourceInputs["exposedPort"] = state ? state.exposedPort : undefined;
            resourceInputs["hostname"] = state ? state.hostname : undefined;
            resourceInputs["inputId"] = state ? state.inputId : undefined;
            resourceInputs["isRestartRequired"] = state ? state.isRestartRequired : undefined;
            resourceInputs["nbInstance"] = state ? state.nbInstance : undefined;
            resourceInputs["publicAddress"] = state ? state.publicAddress : undefined;
            resourceInputs["serviceName"] = state ? state.serviceName : undefined;
            resourceInputs["sslCertificate"] = state ? state.sslCertificate : undefined;
            resourceInputs["status"] = state ? state.status : undefined;
            resourceInputs["streamId"] = state ? state.streamId : undefined;
            resourceInputs["title"] = state ? state.title : undefined;
            resourceInputs["updatedAt"] = state ? state.updatedAt : undefined;
        } else {
            const args = argsOrState as LogsInputArgs | undefined;
            if ((!args || args.configuration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'configuration'");
            }
            if ((!args || args.description === undefined) && !opts.urn) {
                throw new Error("Missing required property 'description'");
            }
            if ((!args || args.engineId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'engineId'");
            }
            if ((!args || args.serviceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceName'");
            }
            if ((!args || args.streamId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'streamId'");
            }
            if ((!args || args.title === undefined) && !opts.urn) {
                throw new Error("Missing required property 'title'");
            }
            resourceInputs["allowedNetworks"] = args ? args.allowedNetworks : undefined;
            resourceInputs["configuration"] = args ? args.configuration : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["engineId"] = args ? args.engineId : undefined;
            resourceInputs["exposedPort"] = args ? args.exposedPort : undefined;
            resourceInputs["nbInstance"] = args ? args.nbInstance : undefined;
            resourceInputs["serviceName"] = args ? args.serviceName : undefined;
            resourceInputs["streamId"] = args ? args.streamId : undefined;
            resourceInputs["title"] = args ? args.title : undefined;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["hostname"] = undefined /*out*/;
            resourceInputs["inputId"] = undefined /*out*/;
            resourceInputs["isRestartRequired"] = undefined /*out*/;
            resourceInputs["publicAddress"] = undefined /*out*/;
            resourceInputs["sslCertificate"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["updatedAt"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["sslCertificate"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(LogsInput.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering LogsInput resources.
 */
export interface LogsInputState {
    /**
     * List of IP blocks
     */
    allowedNetworks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Input configuration
     */
    configuration?: pulumi.Input<inputs.Dbaas.LogsInputConfiguration>;
    /**
     * Input creation
     */
    createdAt?: pulumi.Input<string>;
    /**
     * Input description
     */
    description?: pulumi.Input<string>;
    /**
     * Input engine ID
     */
    engineId?: pulumi.Input<string>;
    /**
     * Port
     */
    exposedPort?: pulumi.Input<string>;
    /**
     * Hostname
     */
    hostname?: pulumi.Input<string>;
    /**
     * Input ID
     */
    inputId?: pulumi.Input<string>;
    /**
     * Indicate if input need to be restarted
     */
    isRestartRequired?: pulumi.Input<boolean>;
    /**
     * Number of instance running
     */
    nbInstance?: pulumi.Input<number>;
    /**
     * Input IP address
     */
    publicAddress?: pulumi.Input<string>;
    /**
     * service name
     */
    serviceName?: pulumi.Input<string>;
    /**
     * Input SSL certificate
     */
    sslCertificate?: pulumi.Input<string>;
    /**
     * init: configuration required, pending: ready to start, running: available
     */
    status?: pulumi.Input<string>;
    /**
     * Associated Graylog stream
     */
    streamId?: pulumi.Input<string>;
    /**
     * Input title
     */
    title?: pulumi.Input<string>;
    /**
     * Input last update
     */
    updatedAt?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a LogsInput resource.
 */
export interface LogsInputArgs {
    /**
     * List of IP blocks
     */
    allowedNetworks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Input configuration
     */
    configuration: pulumi.Input<inputs.Dbaas.LogsInputConfiguration>;
    /**
     * Input description
     */
    description: pulumi.Input<string>;
    /**
     * Input engine ID
     */
    engineId: pulumi.Input<string>;
    /**
     * Port
     */
    exposedPort?: pulumi.Input<string>;
    /**
     * Number of instance running
     */
    nbInstance?: pulumi.Input<number>;
    /**
     * service name
     */
    serviceName: pulumi.Input<string>;
    /**
     * Associated Graylog stream
     */
    streamId: pulumi.Input<string>;
    /**
     * Input title
     */
    title: pulumi.Input<string>;
}
