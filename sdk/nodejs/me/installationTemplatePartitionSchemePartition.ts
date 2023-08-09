// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this resource to create a partition in the partition scheme of a custom installation template available for dedicated servers.
 *
 * ## Example Usage
 *
 * ## Import
 *
 * The resource can be imported using the `template_name`, `scheme_name`, `mountpoint` of the cluster, separated by "/" E.g., bash <break><break>```sh<break> $ pulumi import ovh:Me/installationTemplatePartitionSchemePartition:InstallationTemplatePartitionSchemePartition root template_name/scheme_name/mountpoint <break>```<break><break>
 */
export class InstallationTemplatePartitionSchemePartition extends pulumi.CustomResource {
    /**
     * Get an existing InstallationTemplatePartitionSchemePartition resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstallationTemplatePartitionSchemePartitionState, opts?: pulumi.CustomResourceOptions): InstallationTemplatePartitionSchemePartition {
        return new InstallationTemplatePartitionSchemePartition(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:Me/installationTemplatePartitionSchemePartition:InstallationTemplatePartitionSchemePartition';

    /**
     * Returns true if the given object is an instance of InstallationTemplatePartitionSchemePartition.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is InstallationTemplatePartitionSchemePartition {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === InstallationTemplatePartitionSchemePartition.__pulumiType;
    }

    /**
     * Partition filesystem. Enum with possibles values:
     * - btrfs
     * - ext3
     * - ext4
     * - ntfs
     * - reiserfs
     * - swap
     * - ufs
     * - xfs
     * - zfs
     */
    public readonly filesystem!: pulumi.Output<string>;
    /**
     * partition mount point.
     */
    public readonly mountpoint!: pulumi.Output<string>;
    /**
     * step or order. specifies the creation order of the partition on the disk
     */
    public readonly order!: pulumi.Output<number>;
    /**
     * raid partition type. Enum with possible values: 
     * - raid0
     * - raid1
     * - raid10
     * - raid5
     * - raid6
     */
    public readonly raid!: pulumi.Output<string>;
    /**
     * The partition scheme name.
     */
    public readonly schemeName!: pulumi.Output<string>;
    /**
     * size of partition in MB, 0 => rest of the space.
     */
    public readonly size!: pulumi.Output<number>;
    /**
     * The template name of the partition scheme.
     */
    public readonly templateName!: pulumi.Output<string>;
    /**
     * partition type. Enum with possible values:
     * - lv
     * - primary
     * - logical
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * The volume name needed for proxmox distribution
     */
    public readonly volumeName!: pulumi.Output<string>;

    /**
     * Create a InstallationTemplatePartitionSchemePartition resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: InstallationTemplatePartitionSchemePartitionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: InstallationTemplatePartitionSchemePartitionArgs | InstallationTemplatePartitionSchemePartitionState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as InstallationTemplatePartitionSchemePartitionState | undefined;
            resourceInputs["filesystem"] = state ? state.filesystem : undefined;
            resourceInputs["mountpoint"] = state ? state.mountpoint : undefined;
            resourceInputs["order"] = state ? state.order : undefined;
            resourceInputs["raid"] = state ? state.raid : undefined;
            resourceInputs["schemeName"] = state ? state.schemeName : undefined;
            resourceInputs["size"] = state ? state.size : undefined;
            resourceInputs["templateName"] = state ? state.templateName : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
            resourceInputs["volumeName"] = state ? state.volumeName : undefined;
        } else {
            const args = argsOrState as InstallationTemplatePartitionSchemePartitionArgs | undefined;
            if ((!args || args.filesystem === undefined) && !opts.urn) {
                throw new Error("Missing required property 'filesystem'");
            }
            if ((!args || args.mountpoint === undefined) && !opts.urn) {
                throw new Error("Missing required property 'mountpoint'");
            }
            if ((!args || args.order === undefined) && !opts.urn) {
                throw new Error("Missing required property 'order'");
            }
            if ((!args || args.schemeName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'schemeName'");
            }
            if ((!args || args.size === undefined) && !opts.urn) {
                throw new Error("Missing required property 'size'");
            }
            if ((!args || args.templateName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'templateName'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["filesystem"] = args ? args.filesystem : undefined;
            resourceInputs["mountpoint"] = args ? args.mountpoint : undefined;
            resourceInputs["order"] = args ? args.order : undefined;
            resourceInputs["raid"] = args ? args.raid : undefined;
            resourceInputs["schemeName"] = args ? args.schemeName : undefined;
            resourceInputs["size"] = args ? args.size : undefined;
            resourceInputs["templateName"] = args ? args.templateName : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["volumeName"] = args ? args.volumeName : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(InstallationTemplatePartitionSchemePartition.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering InstallationTemplatePartitionSchemePartition resources.
 */
export interface InstallationTemplatePartitionSchemePartitionState {
    /**
     * Partition filesystem. Enum with possibles values:
     * - btrfs
     * - ext3
     * - ext4
     * - ntfs
     * - reiserfs
     * - swap
     * - ufs
     * - xfs
     * - zfs
     */
    filesystem?: pulumi.Input<string>;
    /**
     * partition mount point.
     */
    mountpoint?: pulumi.Input<string>;
    /**
     * step or order. specifies the creation order of the partition on the disk
     */
    order?: pulumi.Input<number>;
    /**
     * raid partition type. Enum with possible values: 
     * - raid0
     * - raid1
     * - raid10
     * - raid5
     * - raid6
     */
    raid?: pulumi.Input<string>;
    /**
     * The partition scheme name.
     */
    schemeName?: pulumi.Input<string>;
    /**
     * size of partition in MB, 0 => rest of the space.
     */
    size?: pulumi.Input<number>;
    /**
     * The template name of the partition scheme.
     */
    templateName?: pulumi.Input<string>;
    /**
     * partition type. Enum with possible values:
     * - lv
     * - primary
     * - logical
     */
    type?: pulumi.Input<string>;
    /**
     * The volume name needed for proxmox distribution
     */
    volumeName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a InstallationTemplatePartitionSchemePartition resource.
 */
export interface InstallationTemplatePartitionSchemePartitionArgs {
    /**
     * Partition filesystem. Enum with possibles values:
     * - btrfs
     * - ext3
     * - ext4
     * - ntfs
     * - reiserfs
     * - swap
     * - ufs
     * - xfs
     * - zfs
     */
    filesystem: pulumi.Input<string>;
    /**
     * partition mount point.
     */
    mountpoint: pulumi.Input<string>;
    /**
     * step or order. specifies the creation order of the partition on the disk
     */
    order: pulumi.Input<number>;
    /**
     * raid partition type. Enum with possible values: 
     * - raid0
     * - raid1
     * - raid10
     * - raid5
     * - raid6
     */
    raid?: pulumi.Input<string>;
    /**
     * The partition scheme name.
     */
    schemeName: pulumi.Input<string>;
    /**
     * size of partition in MB, 0 => rest of the space.
     */
    size: pulumi.Input<number>;
    /**
     * The template name of the partition scheme.
     */
    templateName: pulumi.Input<string>;
    /**
     * partition type. Enum with possible values:
     * - lv
     * - primary
     * - logical
     */
    type: pulumi.Input<string>;
    /**
     * The volume name needed for proxmox distribution
     */
    volumeName?: pulumi.Input<string>;
}
