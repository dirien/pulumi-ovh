// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.CloudProject.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class NetworkPrivateSubnetV2HostRoute {
    private String destination;
    private String nexthop;

    private NetworkPrivateSubnetV2HostRoute() {}
    public String destination() {
        return this.destination;
    }
    public String nexthop() {
        return this.nexthop;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(NetworkPrivateSubnetV2HostRoute defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String destination;
        private String nexthop;
        public Builder() {}
        public Builder(NetworkPrivateSubnetV2HostRoute defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.destination = defaults.destination;
    	      this.nexthop = defaults.nexthop;
        }

        @CustomType.Setter
        public Builder destination(String destination) {
            if (destination == null) {
              throw new MissingRequiredPropertyException("NetworkPrivateSubnetV2HostRoute", "destination");
            }
            this.destination = destination;
            return this;
        }
        @CustomType.Setter
        public Builder nexthop(String nexthop) {
            if (nexthop == null) {
              throw new MissingRequiredPropertyException("NetworkPrivateSubnetV2HostRoute", "nexthop");
            }
            this.nexthop = nexthop;
            return this;
        }
        public NetworkPrivateSubnetV2HostRoute build() {
            final var _resultValue = new NetworkPrivateSubnetV2HostRoute();
            _resultValue.destination = destination;
            _resultValue.nexthop = nexthop;
            return _resultValue;
        }
    }
}
