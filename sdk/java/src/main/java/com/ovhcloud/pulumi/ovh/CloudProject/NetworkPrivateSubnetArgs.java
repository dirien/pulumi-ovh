// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.CloudProject;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class NetworkPrivateSubnetArgs extends com.pulumi.resources.ResourceArgs {

    public static final NetworkPrivateSubnetArgs Empty = new NetworkPrivateSubnetArgs();

    /**
     * Enable DHCP.
     * Changing this forces a new resource to be created. Defaults to false.
     * 
     */
    @Import(name="dhcp")
    private @Nullable Output<Boolean> dhcp;

    /**
     * @return Enable DHCP.
     * Changing this forces a new resource to be created. Defaults to false.
     * 
     */
    public Optional<Output<Boolean>> dhcp() {
        return Optional.ofNullable(this.dhcp);
    }

    /**
     * Last ip for this region.
     * Changing this value recreates the subnet.
     * 
     */
    @Import(name="end", required=true)
    private Output<String> end;

    /**
     * @return Last ip for this region.
     * Changing this value recreates the subnet.
     * 
     */
    public Output<String> end() {
        return this.end;
    }

    /**
     * Global network in CIDR format.
     * Changing this value recreates the subnet
     * 
     */
    @Import(name="network", required=true)
    private Output<String> network;

    /**
     * @return Global network in CIDR format.
     * Changing this value recreates the subnet
     * 
     */
    public Output<String> network() {
        return this.network;
    }

    /**
     * The id of the network.
     * Changing this forces a new resource to be created.
     * 
     */
    @Import(name="networkId", required=true)
    private Output<String> networkId;

    /**
     * @return The id of the network.
     * Changing this forces a new resource to be created.
     * 
     */
    public Output<String> networkId() {
        return this.networkId;
    }

    /**
     * Set to true if you don&#39;t want to set a default gateway IP.
     * Changing this value recreates the resource. Defaults to false.
     * 
     */
    @Import(name="noGateway")
    private @Nullable Output<Boolean> noGateway;

    /**
     * @return Set to true if you don&#39;t want to set a default gateway IP.
     * Changing this value recreates the resource. Defaults to false.
     * 
     */
    public Optional<Output<Boolean>> noGateway() {
        return Optional.ofNullable(this.noGateway);
    }

    /**
     * The region in which the network subnet will be created.
     * Ex.: &#34;GRA1&#34;. Changing this value recreates the resource.
     * 
     */
    @Import(name="region", required=true)
    private Output<String> region;

    /**
     * @return The region in which the network subnet will be created.
     * Ex.: &#34;GRA1&#34;. Changing this value recreates the resource.
     * 
     */
    public Output<String> region() {
        return this.region;
    }

    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     * 
     */
    @Import(name="serviceName", required=true)
    private Output<String> serviceName;

    /**
     * @return The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     * 
     */
    public Output<String> serviceName() {
        return this.serviceName;
    }

    /**
     * First ip for this region.
     * Changing this value recreates the subnet.
     * 
     */
    @Import(name="start", required=true)
    private Output<String> start;

    /**
     * @return First ip for this region.
     * Changing this value recreates the subnet.
     * 
     */
    public Output<String> start() {
        return this.start;
    }

    private NetworkPrivateSubnetArgs() {}

    private NetworkPrivateSubnetArgs(NetworkPrivateSubnetArgs $) {
        this.dhcp = $.dhcp;
        this.end = $.end;
        this.network = $.network;
        this.networkId = $.networkId;
        this.noGateway = $.noGateway;
        this.region = $.region;
        this.serviceName = $.serviceName;
        this.start = $.start;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(NetworkPrivateSubnetArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private NetworkPrivateSubnetArgs $;

        public Builder() {
            $ = new NetworkPrivateSubnetArgs();
        }

        public Builder(NetworkPrivateSubnetArgs defaults) {
            $ = new NetworkPrivateSubnetArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param dhcp Enable DHCP.
         * Changing this forces a new resource to be created. Defaults to false.
         * 
         * @return builder
         * 
         */
        public Builder dhcp(@Nullable Output<Boolean> dhcp) {
            $.dhcp = dhcp;
            return this;
        }

        /**
         * @param dhcp Enable DHCP.
         * Changing this forces a new resource to be created. Defaults to false.
         * 
         * @return builder
         * 
         */
        public Builder dhcp(Boolean dhcp) {
            return dhcp(Output.of(dhcp));
        }

        /**
         * @param end Last ip for this region.
         * Changing this value recreates the subnet.
         * 
         * @return builder
         * 
         */
        public Builder end(Output<String> end) {
            $.end = end;
            return this;
        }

        /**
         * @param end Last ip for this region.
         * Changing this value recreates the subnet.
         * 
         * @return builder
         * 
         */
        public Builder end(String end) {
            return end(Output.of(end));
        }

        /**
         * @param network Global network in CIDR format.
         * Changing this value recreates the subnet
         * 
         * @return builder
         * 
         */
        public Builder network(Output<String> network) {
            $.network = network;
            return this;
        }

        /**
         * @param network Global network in CIDR format.
         * Changing this value recreates the subnet
         * 
         * @return builder
         * 
         */
        public Builder network(String network) {
            return network(Output.of(network));
        }

        /**
         * @param networkId The id of the network.
         * Changing this forces a new resource to be created.
         * 
         * @return builder
         * 
         */
        public Builder networkId(Output<String> networkId) {
            $.networkId = networkId;
            return this;
        }

        /**
         * @param networkId The id of the network.
         * Changing this forces a new resource to be created.
         * 
         * @return builder
         * 
         */
        public Builder networkId(String networkId) {
            return networkId(Output.of(networkId));
        }

        /**
         * @param noGateway Set to true if you don&#39;t want to set a default gateway IP.
         * Changing this value recreates the resource. Defaults to false.
         * 
         * @return builder
         * 
         */
        public Builder noGateway(@Nullable Output<Boolean> noGateway) {
            $.noGateway = noGateway;
            return this;
        }

        /**
         * @param noGateway Set to true if you don&#39;t want to set a default gateway IP.
         * Changing this value recreates the resource. Defaults to false.
         * 
         * @return builder
         * 
         */
        public Builder noGateway(Boolean noGateway) {
            return noGateway(Output.of(noGateway));
        }

        /**
         * @param region The region in which the network subnet will be created.
         * Ex.: &#34;GRA1&#34;. Changing this value recreates the resource.
         * 
         * @return builder
         * 
         */
        public Builder region(Output<String> region) {
            $.region = region;
            return this;
        }

        /**
         * @param region The region in which the network subnet will be created.
         * Ex.: &#34;GRA1&#34;. Changing this value recreates the resource.
         * 
         * @return builder
         * 
         */
        public Builder region(String region) {
            return region(Output.of(region));
        }

        /**
         * @param serviceName The id of the public cloud project. If omitted,
         * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
         * 
         * @return builder
         * 
         */
        public Builder serviceName(Output<String> serviceName) {
            $.serviceName = serviceName;
            return this;
        }

        /**
         * @param serviceName The id of the public cloud project. If omitted,
         * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
         * 
         * @return builder
         * 
         */
        public Builder serviceName(String serviceName) {
            return serviceName(Output.of(serviceName));
        }

        /**
         * @param start First ip for this region.
         * Changing this value recreates the subnet.
         * 
         * @return builder
         * 
         */
        public Builder start(Output<String> start) {
            $.start = start;
            return this;
        }

        /**
         * @param start First ip for this region.
         * Changing this value recreates the subnet.
         * 
         * @return builder
         * 
         */
        public Builder start(String start) {
            return start(Output.of(start));
        }

        public NetworkPrivateSubnetArgs build() {
            if ($.end == null) {
                throw new MissingRequiredPropertyException("NetworkPrivateSubnetArgs", "end");
            }
            if ($.network == null) {
                throw new MissingRequiredPropertyException("NetworkPrivateSubnetArgs", "network");
            }
            if ($.networkId == null) {
                throw new MissingRequiredPropertyException("NetworkPrivateSubnetArgs", "networkId");
            }
            if ($.region == null) {
                throw new MissingRequiredPropertyException("NetworkPrivateSubnetArgs", "region");
            }
            if ($.serviceName == null) {
                throw new MissingRequiredPropertyException("NetworkPrivateSubnetArgs", "serviceName");
            }
            if ($.start == null) {
                throw new MissingRequiredPropertyException("NetworkPrivateSubnetArgs", "start");
            }
            return $;
        }
    }

}
