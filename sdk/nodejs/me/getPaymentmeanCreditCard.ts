// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to retrieve information about a credit card
 * payment mean associated with an OVHcloud account.
 *
 * ## Example Usage
 */
export function getPaymentmeanCreditCard(args?: GetPaymentmeanCreditCardArgs, opts?: pulumi.InvokeOptions): Promise<GetPaymentmeanCreditCardResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ovh:Me/getPaymentmeanCreditCard:getPaymentmeanCreditCard", {
        "descriptionRegexp": args.descriptionRegexp,
        "states": args.states,
        "useDefault": args.useDefault,
        "useLastToExpire": args.useLastToExpire,
    }, opts);
}

/**
 * A collection of arguments for invoking getPaymentmeanCreditCard.
 */
export interface GetPaymentmeanCreditCardArgs {
    /**
     * a regexp used to filter credit cards 
     * on their `description` attributes.
     */
    descriptionRegexp?: string;
    /**
     * Filter credit cards on their `state` attribute.
     * Can be "expired", "valid", "tooManyFailures"
     */
    states?: string[];
    /**
     * Retrieve credit card marked as default payment mean.
     */
    useDefault?: boolean;
    /**
     * Retrieve the credit card that will be the last
     * to expire according to its expiration date.
     */
    useLastToExpire?: boolean;
}

/**
 * A collection of values returned by getPaymentmeanCreditCard.
 */
export interface GetPaymentmeanCreditCardResult {
    /**
     * a boolean which tells if the retrieved credit card
     * is marked as the default payment mean
     */
    readonly default: boolean;
    /**
     * the description attribute of the credit card
     */
    readonly description: string;
    readonly descriptionRegexp?: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * the state attribute of the credit card
     */
    readonly state: string;
    readonly states?: string[];
    readonly useDefault?: boolean;
    readonly useLastToExpire?: boolean;
}
/**
 * Use this data source to retrieve information about a credit card
 * payment mean associated with an OVHcloud account.
 *
 * ## Example Usage
 */
export function getPaymentmeanCreditCardOutput(args?: GetPaymentmeanCreditCardOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPaymentmeanCreditCardResult> {
    return pulumi.output(args).apply((a: any) => getPaymentmeanCreditCard(a, opts))
}

/**
 * A collection of arguments for invoking getPaymentmeanCreditCard.
 */
export interface GetPaymentmeanCreditCardOutputArgs {
    /**
     * a regexp used to filter credit cards 
     * on their `description` attributes.
     */
    descriptionRegexp?: pulumi.Input<string>;
    /**
     * Filter credit cards on their `state` attribute.
     * Can be "expired", "valid", "tooManyFailures"
     */
    states?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Retrieve credit card marked as default payment mean.
     */
    useDefault?: pulumi.Input<boolean>;
    /**
     * Retrieve the credit card that will be the last
     * to expire according to its expiration date.
     */
    useLastToExpire?: pulumi.Input<boolean>;
}
