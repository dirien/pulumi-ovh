// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Ovh.IpLoadBalancing
{
    /// <summary>
    /// Creates a backend HTTP server group (frontend) to be used by loadbalancing frontend(s)
    /// 
    /// ## Example Usage
    /// 
    /// ### With HTTP Header
    /// </summary>
    [OvhResourceType("ovh:IpLoadBalancing/httpFrontend:HttpFrontend")]
    public partial class HttpFrontend : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Restrict IP Load Balancing access to these ip block. No restriction if null. List of IP blocks.
        /// </summary>
        [Output("allowedSources")]
        public Output<ImmutableArray<string>> AllowedSources { get; private set; } = null!;

        /// <summary>
        /// Only attach frontend on these ip. No restriction if null. List of Ip blocks.
        /// </summary>
        [Output("dedicatedIpfos")]
        public Output<ImmutableArray<string>> DedicatedIpfos { get; private set; } = null!;

        /// <summary>
        /// Default TCP Farm of your frontend
        /// </summary>
        [Output("defaultFarmId")]
        public Output<int> DefaultFarmId { get; private set; } = null!;

        /// <summary>
        /// Default ssl served to your customer
        /// </summary>
        [Output("defaultSslId")]
        public Output<int> DefaultSslId { get; private set; } = null!;

        /// <summary>
        /// Disable your frontend. Default: 'false'
        /// </summary>
        [Output("disabled")]
        public Output<bool?> Disabled { get; private set; } = null!;

        /// <summary>
        /// Human readable name for your frontend, this field is for you
        /// </summary>
        [Output("displayName")]
        public Output<string?> DisplayName { get; private set; } = null!;

        /// <summary>
        /// HTTP Strict Transport Security. Default: 'false'
        /// </summary>
        [Output("hsts")]
        public Output<bool?> Hsts { get; private set; } = null!;

        /// <summary>
        /// HTTP headers to add to the frontend. List of string.
        /// </summary>
        [Output("httpHeaders")]
        public Output<ImmutableArray<string>> HttpHeaders { get; private set; } = null!;

        /// <summary>
        /// Port(s) attached to your frontend. Supports single port (numerical value),
        /// range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
        /// and/or 'range'. Each port must be in the [1;49151] range
        /// </summary>
        [Output("port")]
        public Output<string> Port { get; private set; } = null!;

        /// <summary>
        /// Redirection HTTP'
        /// </summary>
        [Output("redirectLocation")]
        public Output<string?> RedirectLocation { get; private set; } = null!;

        /// <summary>
        /// The internal name of your IP load balancing
        /// </summary>
        [Output("serviceName")]
        public Output<string> ServiceName { get; private set; } = null!;

        /// <summary>
        /// SSL deciphering. Default: 'false'
        /// </summary>
        [Output("ssl")]
        public Output<bool?> Ssl { get; private set; } = null!;

        /// <summary>
        /// Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
        /// </summary>
        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a HttpFrontend resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public HttpFrontend(string name, HttpFrontendArgs args, CustomResourceOptions? options = null)
            : base("ovh:IpLoadBalancing/httpFrontend:HttpFrontend", name, args ?? new HttpFrontendArgs(), MakeResourceOptions(options, ""))
        {
        }

        private HttpFrontend(string name, Input<string> id, HttpFrontendState? state = null, CustomResourceOptions? options = null)
            : base("ovh:IpLoadBalancing/httpFrontend:HttpFrontend", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/dirien/pulumi-ovh",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing HttpFrontend resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static HttpFrontend Get(string name, Input<string> id, HttpFrontendState? state = null, CustomResourceOptions? options = null)
        {
            return new HttpFrontend(name, id, state, options);
        }
    }

    public sealed class HttpFrontendArgs : global::Pulumi.ResourceArgs
    {
        [Input("allowedSources")]
        private InputList<string>? _allowedSources;

        /// <summary>
        /// Restrict IP Load Balancing access to these ip block. No restriction if null. List of IP blocks.
        /// </summary>
        public InputList<string> AllowedSources
        {
            get => _allowedSources ?? (_allowedSources = new InputList<string>());
            set => _allowedSources = value;
        }

        [Input("dedicatedIpfos")]
        private InputList<string>? _dedicatedIpfos;

        /// <summary>
        /// Only attach frontend on these ip. No restriction if null. List of Ip blocks.
        /// </summary>
        public InputList<string> DedicatedIpfos
        {
            get => _dedicatedIpfos ?? (_dedicatedIpfos = new InputList<string>());
            set => _dedicatedIpfos = value;
        }

        /// <summary>
        /// Default TCP Farm of your frontend
        /// </summary>
        [Input("defaultFarmId")]
        public Input<int>? DefaultFarmId { get; set; }

        /// <summary>
        /// Default ssl served to your customer
        /// </summary>
        [Input("defaultSslId")]
        public Input<int>? DefaultSslId { get; set; }

        /// <summary>
        /// Disable your frontend. Default: 'false'
        /// </summary>
        [Input("disabled")]
        public Input<bool>? Disabled { get; set; }

        /// <summary>
        /// Human readable name for your frontend, this field is for you
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// HTTP Strict Transport Security. Default: 'false'
        /// </summary>
        [Input("hsts")]
        public Input<bool>? Hsts { get; set; }

        [Input("httpHeaders")]
        private InputList<string>? _httpHeaders;

        /// <summary>
        /// HTTP headers to add to the frontend. List of string.
        /// </summary>
        public InputList<string> HttpHeaders
        {
            get => _httpHeaders ?? (_httpHeaders = new InputList<string>());
            set => _httpHeaders = value;
        }

        /// <summary>
        /// Port(s) attached to your frontend. Supports single port (numerical value),
        /// range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
        /// and/or 'range'. Each port must be in the [1;49151] range
        /// </summary>
        [Input("port", required: true)]
        public Input<string> Port { get; set; } = null!;

        /// <summary>
        /// Redirection HTTP'
        /// </summary>
        [Input("redirectLocation")]
        public Input<string>? RedirectLocation { get; set; }

        /// <summary>
        /// The internal name of your IP load balancing
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        /// <summary>
        /// SSL deciphering. Default: 'false'
        /// </summary>
        [Input("ssl")]
        public Input<bool>? Ssl { get; set; }

        /// <summary>
        /// Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
        /// </summary>
        [Input("zone", required: true)]
        public Input<string> Zone { get; set; } = null!;

        public HttpFrontendArgs()
        {
        }
        public static new HttpFrontendArgs Empty => new HttpFrontendArgs();
    }

    public sealed class HttpFrontendState : global::Pulumi.ResourceArgs
    {
        [Input("allowedSources")]
        private InputList<string>? _allowedSources;

        /// <summary>
        /// Restrict IP Load Balancing access to these ip block. No restriction if null. List of IP blocks.
        /// </summary>
        public InputList<string> AllowedSources
        {
            get => _allowedSources ?? (_allowedSources = new InputList<string>());
            set => _allowedSources = value;
        }

        [Input("dedicatedIpfos")]
        private InputList<string>? _dedicatedIpfos;

        /// <summary>
        /// Only attach frontend on these ip. No restriction if null. List of Ip blocks.
        /// </summary>
        public InputList<string> DedicatedIpfos
        {
            get => _dedicatedIpfos ?? (_dedicatedIpfos = new InputList<string>());
            set => _dedicatedIpfos = value;
        }

        /// <summary>
        /// Default TCP Farm of your frontend
        /// </summary>
        [Input("defaultFarmId")]
        public Input<int>? DefaultFarmId { get; set; }

        /// <summary>
        /// Default ssl served to your customer
        /// </summary>
        [Input("defaultSslId")]
        public Input<int>? DefaultSslId { get; set; }

        /// <summary>
        /// Disable your frontend. Default: 'false'
        /// </summary>
        [Input("disabled")]
        public Input<bool>? Disabled { get; set; }

        /// <summary>
        /// Human readable name for your frontend, this field is for you
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// HTTP Strict Transport Security. Default: 'false'
        /// </summary>
        [Input("hsts")]
        public Input<bool>? Hsts { get; set; }

        [Input("httpHeaders")]
        private InputList<string>? _httpHeaders;

        /// <summary>
        /// HTTP headers to add to the frontend. List of string.
        /// </summary>
        public InputList<string> HttpHeaders
        {
            get => _httpHeaders ?? (_httpHeaders = new InputList<string>());
            set => _httpHeaders = value;
        }

        /// <summary>
        /// Port(s) attached to your frontend. Supports single port (numerical value),
        /// range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
        /// and/or 'range'. Each port must be in the [1;49151] range
        /// </summary>
        [Input("port")]
        public Input<string>? Port { get; set; }

        /// <summary>
        /// Redirection HTTP'
        /// </summary>
        [Input("redirectLocation")]
        public Input<string>? RedirectLocation { get; set; }

        /// <summary>
        /// The internal name of your IP load balancing
        /// </summary>
        [Input("serviceName")]
        public Input<string>? ServiceName { get; set; }

        /// <summary>
        /// SSL deciphering. Default: 'false'
        /// </summary>
        [Input("ssl")]
        public Input<bool>? Ssl { get; set; }

        /// <summary>
        /// Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public HttpFrontendState()
        {
        }
        public static new HttpFrontendState Empty => new HttpFrontendState();
    }
}
