// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Creates a subnet in a private network of a public cloud project.
 *
 * ## Example Usage
 *
 * ## Import
 *
 * Subnet in a private network of a public cloud project can be imported using the `service_name` , the `network_id` and the `subnet_id`, separated by "/" E.g., bash <break><break>```sh<break> $ pulumi import ovh:CloudProject/networkPrivateSubnet:NetworkPrivateSubnet mysubnet ookie9mee8Shaeghaeleeju7Xeghohv6e/pn-12345678/0f0b73a4-403b-45e4-86d0-b438f1291909 <break>```<break><break>
 */
export class NetworkPrivateSubnet extends pulumi.CustomResource {
    /**
     * Get an existing NetworkPrivateSubnet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkPrivateSubnetState, opts?: pulumi.CustomResourceOptions): NetworkPrivateSubnet {
        return new NetworkPrivateSubnet(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:CloudProject/networkPrivateSubnet:NetworkPrivateSubnet';

    /**
     * Returns true if the given object is an instance of NetworkPrivateSubnet.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is NetworkPrivateSubnet {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === NetworkPrivateSubnet.__pulumiType;
    }

    /**
     * Ip Block representing the subnet cidr.
     */
    public /*out*/ readonly cidr!: pulumi.Output<string>;
    /**
     * Enable DHCP.
     * Changing this forces a new resource to be created. Defaults to false.
     * _
     */
    public readonly dhcp!: pulumi.Output<boolean | undefined>;
    /**
     * Last ip for this region.
     * Changing this value recreates the subnet.
     */
    public readonly end!: pulumi.Output<string>;
    /**
     * The IP of the gateway
     */
    public /*out*/ readonly gatewayIp!: pulumi.Output<string>;
    /**
     * List of ip pools allocated in the subnet.
     * * `ip_pools/network` - Global network with cidr.
     * * `ip_pools/region` - Region where this subnet is created.
     * * `ip_pools/dhcp` - DHCP enabled.
     * * `ip_pools/end` - Last ip for this region.
     * * `ip_pools/start` - First ip for this region.
     */
    public /*out*/ readonly ipPools!: pulumi.Output<outputs.CloudProject.NetworkPrivateSubnetIpPool[]>;
    /**
     * Global network in CIDR format.
     * Changing this value recreates the subnet
     */
    public readonly network!: pulumi.Output<string>;
    /**
     * The id of the network.
     * Changing this forces a new resource to be created.
     */
    public readonly networkId!: pulumi.Output<string>;
    /**
     * Set to true if you don't want to set a default gateway IP.
     * Changing this value recreates the resource. Defaults to false.
     */
    public readonly noGateway!: pulumi.Output<boolean | undefined>;
    /**
     * The region in which the network subnet will be created.
     * Ex.: "GRA1". Changing this value recreates the resource.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    public readonly serviceName!: pulumi.Output<string>;
    /**
     * First ip for this region.
     * Changing this value recreates the subnet.
     */
    public readonly start!: pulumi.Output<string>;

    /**
     * Create a NetworkPrivateSubnet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NetworkPrivateSubnetArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NetworkPrivateSubnetArgs | NetworkPrivateSubnetState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as NetworkPrivateSubnetState | undefined;
            resourceInputs["cidr"] = state ? state.cidr : undefined;
            resourceInputs["dhcp"] = state ? state.dhcp : undefined;
            resourceInputs["end"] = state ? state.end : undefined;
            resourceInputs["gatewayIp"] = state ? state.gatewayIp : undefined;
            resourceInputs["ipPools"] = state ? state.ipPools : undefined;
            resourceInputs["network"] = state ? state.network : undefined;
            resourceInputs["networkId"] = state ? state.networkId : undefined;
            resourceInputs["noGateway"] = state ? state.noGateway : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["serviceName"] = state ? state.serviceName : undefined;
            resourceInputs["start"] = state ? state.start : undefined;
        } else {
            const args = argsOrState as NetworkPrivateSubnetArgs | undefined;
            if ((!args || args.end === undefined) && !opts.urn) {
                throw new Error("Missing required property 'end'");
            }
            if ((!args || args.network === undefined) && !opts.urn) {
                throw new Error("Missing required property 'network'");
            }
            if ((!args || args.networkId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'networkId'");
            }
            if ((!args || args.region === undefined) && !opts.urn) {
                throw new Error("Missing required property 'region'");
            }
            if ((!args || args.serviceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceName'");
            }
            if ((!args || args.start === undefined) && !opts.urn) {
                throw new Error("Missing required property 'start'");
            }
            resourceInputs["dhcp"] = args ? args.dhcp : undefined;
            resourceInputs["end"] = args ? args.end : undefined;
            resourceInputs["network"] = args ? args.network : undefined;
            resourceInputs["networkId"] = args ? args.networkId : undefined;
            resourceInputs["noGateway"] = args ? args.noGateway : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["serviceName"] = args ? args.serviceName : undefined;
            resourceInputs["start"] = args ? args.start : undefined;
            resourceInputs["cidr"] = undefined /*out*/;
            resourceInputs["gatewayIp"] = undefined /*out*/;
            resourceInputs["ipPools"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(NetworkPrivateSubnet.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering NetworkPrivateSubnet resources.
 */
export interface NetworkPrivateSubnetState {
    /**
     * Ip Block representing the subnet cidr.
     */
    cidr?: pulumi.Input<string>;
    /**
     * Enable DHCP.
     * Changing this forces a new resource to be created. Defaults to false.
     * _
     */
    dhcp?: pulumi.Input<boolean>;
    /**
     * Last ip for this region.
     * Changing this value recreates the subnet.
     */
    end?: pulumi.Input<string>;
    /**
     * The IP of the gateway
     */
    gatewayIp?: pulumi.Input<string>;
    /**
     * List of ip pools allocated in the subnet.
     * * `ip_pools/network` - Global network with cidr.
     * * `ip_pools/region` - Region where this subnet is created.
     * * `ip_pools/dhcp` - DHCP enabled.
     * * `ip_pools/end` - Last ip for this region.
     * * `ip_pools/start` - First ip for this region.
     */
    ipPools?: pulumi.Input<pulumi.Input<inputs.CloudProject.NetworkPrivateSubnetIpPool>[]>;
    /**
     * Global network in CIDR format.
     * Changing this value recreates the subnet
     */
    network?: pulumi.Input<string>;
    /**
     * The id of the network.
     * Changing this forces a new resource to be created.
     */
    networkId?: pulumi.Input<string>;
    /**
     * Set to true if you don't want to set a default gateway IP.
     * Changing this value recreates the resource. Defaults to false.
     */
    noGateway?: pulumi.Input<boolean>;
    /**
     * The region in which the network subnet will be created.
     * Ex.: "GRA1". Changing this value recreates the resource.
     */
    region?: pulumi.Input<string>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName?: pulumi.Input<string>;
    /**
     * First ip for this region.
     * Changing this value recreates the subnet.
     */
    start?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a NetworkPrivateSubnet resource.
 */
export interface NetworkPrivateSubnetArgs {
    /**
     * Enable DHCP.
     * Changing this forces a new resource to be created. Defaults to false.
     * _
     */
    dhcp?: pulumi.Input<boolean>;
    /**
     * Last ip for this region.
     * Changing this value recreates the subnet.
     */
    end: pulumi.Input<string>;
    /**
     * Global network in CIDR format.
     * Changing this value recreates the subnet
     */
    network: pulumi.Input<string>;
    /**
     * The id of the network.
     * Changing this forces a new resource to be created.
     */
    networkId: pulumi.Input<string>;
    /**
     * Set to true if you don't want to set a default gateway IP.
     * Changing this value recreates the resource. Defaults to false.
     */
    noGateway?: pulumi.Input<boolean>;
    /**
     * The region in which the network subnet will be created.
     * Ex.: "GRA1". Changing this value recreates the resource.
     */
    region: pulumi.Input<string>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName: pulumi.Input<string>;
    /**
     * First ip for this region.
     * Changing this value recreates the subnet.
     */
    start: pulumi.Input<string>;
}
