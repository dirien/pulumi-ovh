// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to retrieve information about an hosting privatedatabase user grant.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const userGrant = ovh.Hosting.getPrivateDatabaseUserGrant({
 *     databaseName: "XXXXXX",
 *     serviceName: "XXXXXX",
 *     userName: "XXXXXX",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getPrivateDatabaseUserGrant(args: GetPrivateDatabaseUserGrantArgs, opts?: pulumi.InvokeOptions): Promise<GetPrivateDatabaseUserGrantResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ovh:Hosting/getPrivateDatabaseUserGrant:getPrivateDatabaseUserGrant", {
        "databaseName": args.databaseName,
        "serviceName": args.serviceName,
        "userName": args.userName,
    }, opts);
}

/**
 * A collection of arguments for invoking getPrivateDatabaseUserGrant.
 */
export interface GetPrivateDatabaseUserGrantArgs {
    /**
     * The database name on which grant the user
     */
    databaseName: string;
    /**
     * The internal name of your private database
     */
    serviceName: string;
    /**
     * The user name
     */
    userName: string;
}

/**
 * A collection of values returned by getPrivateDatabaseUserGrant.
 */
export interface GetPrivateDatabaseUserGrantResult {
    /**
     * Creation date of the database
     */
    readonly creationDate: string;
    readonly databaseName: string;
    /**
     * Grant name
     */
    readonly grant: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly serviceName: string;
    readonly userName: string;
}
/**
 * Use this data source to retrieve information about an hosting privatedatabase user grant.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const userGrant = ovh.Hosting.getPrivateDatabaseUserGrant({
 *     databaseName: "XXXXXX",
 *     serviceName: "XXXXXX",
 *     userName: "XXXXXX",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getPrivateDatabaseUserGrantOutput(args: GetPrivateDatabaseUserGrantOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPrivateDatabaseUserGrantResult> {
    return pulumi.output(args).apply((a: any) => getPrivateDatabaseUserGrant(a, opts))
}

/**
 * A collection of arguments for invoking getPrivateDatabaseUserGrant.
 */
export interface GetPrivateDatabaseUserGrantOutputArgs {
    /**
     * The database name on which grant the user
     */
    databaseName: pulumi.Input<string>;
    /**
     * The internal name of your private database
     */
    serviceName: pulumi.Input<string>;
    /**
     * The user name
     */
    userName: pulumi.Input<string>;
}
