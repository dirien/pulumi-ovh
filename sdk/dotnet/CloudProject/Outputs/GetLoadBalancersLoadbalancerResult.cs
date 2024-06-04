// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh.CloudProject.Outputs
{

    [OutputType]
    public sealed class GetLoadBalancersLoadbalancerResult
    {
        /// <summary>
        /// Date of creation of the loadbalancer
        /// </summary>
        public readonly string CreatedAt;
        /// <summary>
        /// ID of the flavor
        /// </summary>
        public readonly string FlavorId;
        /// <summary>
        /// Information about the floating IP
        /// </summary>
        public readonly Outputs.GetLoadBalancersLoadbalancerFloatingIpResult FloatingIp;
        /// <summary>
        /// ID of the floating IP
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Name of the loadbalancer
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Operating status of the loadbalancer
        /// </summary>
        public readonly string OperatingStatus;
        /// <summary>
        /// Provisioning status of the loadbalancer
        /// </summary>
        public readonly string ProvisioningStatus;
        /// <summary>
        /// Region of the loadbalancer
        /// </summary>
        public readonly string Region;
        /// <summary>
        /// Last update date of the loadbalancer
        /// </summary>
        public readonly string UpdatedAt;
        /// <summary>
        /// IP address of the Virtual IP
        /// </summary>
        public readonly string VipAddress;
        /// <summary>
        /// Openstack ID of the network for the Virtual IP
        /// </summary>
        public readonly string VipNetworkId;
        /// <summary>
        /// ID of the subnet for the Virtual IP
        /// </summary>
        public readonly string VipSubnetId;

        [OutputConstructor]
        private GetLoadBalancersLoadbalancerResult(
            string createdAt,

            string flavorId,

            Outputs.GetLoadBalancersLoadbalancerFloatingIpResult floatingIp,

            string id,

            string name,

            string operatingStatus,

            string provisioningStatus,

            string region,

            string updatedAt,

            string vipAddress,

            string vipNetworkId,

            string vipSubnetId)
        {
            CreatedAt = createdAt;
            FlavorId = flavorId;
            FloatingIp = floatingIp;
            Id = id;
            Name = name;
            OperatingStatus = operatingStatus;
            ProvisioningStatus = provisioningStatus;
            Region = region;
            UpdatedAt = updatedAt;
            VipAddress = vipAddress;
            VipNetworkId = vipNetworkId;
            VipSubnetId = vipSubnetId;
        }
    }
}
