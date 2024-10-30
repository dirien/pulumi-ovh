// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.Dbaas.inputs;

import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetLogsOutputOpenSearchIndexPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetLogsOutputOpenSearchIndexPlainArgs Empty = new GetLogsOutputOpenSearchIndexPlainArgs();

    /**
     * Index name
     * 
     */
    @Import(name="name", required=true)
    private String name;

    /**
     * @return Index name
     * 
     */
    public String name() {
        return this.name;
    }

    /**
     * Number of shard
     * 
     */
    @Import(name="nbShard")
    private @Nullable Integer nbShard;

    /**
     * @return Number of shard
     * 
     */
    public Optional<Integer> nbShard() {
        return Optional.ofNullable(this.nbShard);
    }

    /**
     * The service name. It&#39;s the ID of your Logs Data Platform instance.
     * 
     */
    @Import(name="serviceName", required=true)
    private String serviceName;

    /**
     * @return The service name. It&#39;s the ID of your Logs Data Platform instance.
     * 
     */
    public String serviceName() {
        return this.serviceName;
    }

    private GetLogsOutputOpenSearchIndexPlainArgs() {}

    private GetLogsOutputOpenSearchIndexPlainArgs(GetLogsOutputOpenSearchIndexPlainArgs $) {
        this.name = $.name;
        this.nbShard = $.nbShard;
        this.serviceName = $.serviceName;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetLogsOutputOpenSearchIndexPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetLogsOutputOpenSearchIndexPlainArgs $;

        public Builder() {
            $ = new GetLogsOutputOpenSearchIndexPlainArgs();
        }

        public Builder(GetLogsOutputOpenSearchIndexPlainArgs defaults) {
            $ = new GetLogsOutputOpenSearchIndexPlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param name Index name
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            $.name = name;
            return this;
        }

        /**
         * @param nbShard Number of shard
         * 
         * @return builder
         * 
         */
        public Builder nbShard(@Nullable Integer nbShard) {
            $.nbShard = nbShard;
            return this;
        }

        /**
         * @param serviceName The service name. It&#39;s the ID of your Logs Data Platform instance.
         * 
         * @return builder
         * 
         */
        public Builder serviceName(String serviceName) {
            $.serviceName = serviceName;
            return this;
        }

        public GetLogsOutputOpenSearchIndexPlainArgs build() {
            if ($.name == null) {
                throw new MissingRequiredPropertyException("GetLogsOutputOpenSearchIndexPlainArgs", "name");
            }
            if ($.serviceName == null) {
                throw new MissingRequiredPropertyException("GetLogsOutputOpenSearchIndexPlainArgs", "serviceName");
            }
            return $;
        }
    }

}
