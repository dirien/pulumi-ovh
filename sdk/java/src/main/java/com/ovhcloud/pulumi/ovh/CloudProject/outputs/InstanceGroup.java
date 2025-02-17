// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.CloudProject.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class InstanceGroup {
    /**
     * @return Group id
     * 
     */
    private @Nullable String groupId;

    private InstanceGroup() {}
    /**
     * @return Group id
     * 
     */
    public Optional<String> groupId() {
        return Optional.ofNullable(this.groupId);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(InstanceGroup defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable String groupId;
        public Builder() {}
        public Builder(InstanceGroup defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.groupId = defaults.groupId;
        }

        @CustomType.Setter
        public Builder groupId(@Nullable String groupId) {

            this.groupId = groupId;
            return this;
        }
        public InstanceGroup build() {
            final var _resultValue = new InstanceGroup();
            _resultValue.groupId = groupId;
            return _resultValue;
        }
    }
}
