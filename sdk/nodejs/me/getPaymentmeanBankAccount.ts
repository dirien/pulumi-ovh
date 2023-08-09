// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to retrieve information about a bank account
 * payment mean associated with an OVHcloud account.
 *
 * ## Example Usage
 */
export function getPaymentmeanBankAccount(args?: GetPaymentmeanBankAccountArgs, opts?: pulumi.InvokeOptions): Promise<GetPaymentmeanBankAccountResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ovh:Me/getPaymentmeanBankAccount:getPaymentmeanBankAccount", {
        "descriptionRegexp": args.descriptionRegexp,
        "state": args.state,
        "useDefault": args.useDefault,
        "useOldest": args.useOldest,
    }, opts);
}

/**
 * A collection of arguments for invoking getPaymentmeanBankAccount.
 */
export interface GetPaymentmeanBankAccountArgs {
    /**
     * a regexp used to filter bank accounts 
     * on their `description` attributes.
     */
    descriptionRegexp?: string;
    /**
     * Filter bank accounts on their `state` attribute.
     * Can be "blockedForIncidents", "valid", "pendingValidation"
     */
    state?: string;
    /**
     * Retrieve bank account marked as default payment mean.
     */
    useDefault?: boolean;
    /**
     * Retrieve oldest bank account.
     * project.
     */
    useOldest?: boolean;
}

/**
 * A collection of values returned by getPaymentmeanBankAccount.
 */
export interface GetPaymentmeanBankAccountResult {
    /**
     * a boolean which tells if the retrieved bank account
     * is marked as the default payment mean
     */
    readonly default: boolean;
    /**
     * the description attribute of the bank account
     */
    readonly description: string;
    readonly descriptionRegexp?: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly state: string;
    readonly useDefault?: boolean;
    readonly useOldest?: boolean;
}
/**
 * Use this data source to retrieve information about a bank account
 * payment mean associated with an OVHcloud account.
 *
 * ## Example Usage
 */
export function getPaymentmeanBankAccountOutput(args?: GetPaymentmeanBankAccountOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPaymentmeanBankAccountResult> {
    return pulumi.output(args).apply((a: any) => getPaymentmeanBankAccount(a, opts))
}

/**
 * A collection of arguments for invoking getPaymentmeanBankAccount.
 */
export interface GetPaymentmeanBankAccountOutputArgs {
    /**
     * a regexp used to filter bank accounts 
     * on their `description` attributes.
     */
    descriptionRegexp?: pulumi.Input<string>;
    /**
     * Filter bank accounts on their `state` attribute.
     * Can be "blockedForIncidents", "valid", "pendingValidation"
     */
    state?: pulumi.Input<string>;
    /**
     * Retrieve bank account marked as default payment mean.
     */
    useDefault?: pulumi.Input<boolean>;
    /**
     * Retrieve oldest bank account.
     * project.
     */
    useOldest?: pulumi.Input<boolean>;
}
