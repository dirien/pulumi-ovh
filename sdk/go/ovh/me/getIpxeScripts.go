// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package me

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to retrieve a list of the names of the account's IPXE Scripts.
//
// ## Example Usage
func GetIpxeScripts(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetIpxeScriptsResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv GetIpxeScriptsResult
	err := ctx.Invoke("ovh:Me/getIpxeScripts:getIpxeScripts", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getIpxeScripts.
type GetIpxeScriptsResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The list of the names of all the IPXE Scripts.
	Results []string `pulumi:"results"`
}
