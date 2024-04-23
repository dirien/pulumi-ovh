// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to get a custom installation template available for dedicated servers.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const mytemplate = ovh.Me.getInstallationTemplate({
 *     templateName: "mytemplate",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getInstallationTemplate(args: GetInstallationTemplateArgs, opts?: pulumi.InvokeOptions): Promise<GetInstallationTemplateResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ovh:Me/getInstallationTemplate:getInstallationTemplate", {
        "templateName": args.templateName,
    }, opts);
}

/**
 * A collection of arguments for invoking getInstallationTemplate.
 */
export interface GetInstallationTemplateArgs {
    /**
     * This template name
     */
    templateName: string;
}

/**
 * A collection of values returned by getInstallationTemplate.
 */
export interface GetInstallationTemplateResult {
    /**
     * List of all language available for this template. Deprecated, will be removed in next release.
     */
    readonly availableLanguages: string[];
    /**
     * This template bit format (32 or 64).
     */
    readonly bitFormat: number;
    /**
     * Category of this template (informative only). (basic, customer, hosting, other, readyToUse, virtualisation).
     */
    readonly category: string;
    readonly customizations: outputs.Me.GetInstallationTemplateCustomization[];
    /**
     * The default language of this template. Deprecated, will be removed in next release.
     *
     * @deprecated This field will be removed from the API, please use `userMetadata` instead.
     */
    readonly defaultLanguage: string;
    /**
     * information about this template.
     */
    readonly description: string;
    /**
     * the distribution this template is based on.
     */
    readonly distribution: string;
    /**
     * this template family type (bsd,linux,solaris,windows).
     */
    readonly family: string;
    /**
     * Filesystems available (btrfs,ext3,ext4,ntfs,reiserfs,swap,ufs,xfs,zfs).
     */
    readonly filesystems: string[];
    /**
     * This distribution supports hardware raid configuration through the OVHcloud API.
     */
    readonly hardRaidConfiguration: boolean;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly lvmReady: boolean;
    readonly partitionSchemes: outputs.Me.GetInstallationTemplatePartitionScheme[];
    readonly templateName: string;
}
/**
 * Use this data source to get a custom installation template available for dedicated servers.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const mytemplate = ovh.Me.getInstallationTemplate({
 *     templateName: "mytemplate",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getInstallationTemplateOutput(args: GetInstallationTemplateOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetInstallationTemplateResult> {
    return pulumi.output(args).apply((a: any) => getInstallationTemplate(a, opts))
}

/**
 * A collection of arguments for invoking getInstallationTemplate.
 */
export interface GetInstallationTemplateOutputArgs {
    /**
     * This template name
     */
    templateName: pulumi.Input<string>;
}
