// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ovh

import (
	"context"
	"reflect"

	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to get the list of Vrack network ids available for your IPLoadbalancer associated with your OVHcloud account.
//
// ## Example Usage
//
// <!--Start PulumiCodeChooser -->
// ```go
// package main
//
// import (
//
//	"github.com/ovh/pulumi-ovh/sdk/go/ovh"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := ovh.GetVrackNetworks(ctx, &ovh.GetVrackNetworksArgs{
//				ServiceName: "XXXXXX",
//				Subnet:      pulumi.StringRef("10.0.0.0/24"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
// <!--End PulumiCodeChooser -->
func GetVrackNetworks(ctx *pulumi.Context, args *GetVrackNetworksArgs, opts ...pulumi.InvokeOption) (*GetVrackNetworksResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetVrackNetworksResult
	err := ctx.Invoke("ovh:index/getVrackNetworks:getVrackNetworks", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVrackNetworks.
type GetVrackNetworksArgs struct {
	// The internal name of your IP load balancing
	ServiceName string `pulumi:"serviceName"`
	// Filters networks on the subnet.
	Subnet *string `pulumi:"subnet"`
	// Filters networks on the vlan id.
	VlanId *int `pulumi:"vlanId"`
}

// A collection of values returned by getVrackNetworks.
type GetVrackNetworksResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The list of vrack network ids.
	Results     []int   `pulumi:"results"`
	ServiceName string  `pulumi:"serviceName"`
	Subnet      *string `pulumi:"subnet"`
	VlanId      *int    `pulumi:"vlanId"`
}

func GetVrackNetworksOutput(ctx *pulumi.Context, args GetVrackNetworksOutputArgs, opts ...pulumi.InvokeOption) GetVrackNetworksResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetVrackNetworksResult, error) {
			args := v.(GetVrackNetworksArgs)
			r, err := GetVrackNetworks(ctx, &args, opts...)
			var s GetVrackNetworksResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetVrackNetworksResultOutput)
}

// A collection of arguments for invoking getVrackNetworks.
type GetVrackNetworksOutputArgs struct {
	// The internal name of your IP load balancing
	ServiceName pulumi.StringInput `pulumi:"serviceName"`
	// Filters networks on the subnet.
	Subnet pulumi.StringPtrInput `pulumi:"subnet"`
	// Filters networks on the vlan id.
	VlanId pulumi.IntPtrInput `pulumi:"vlanId"`
}

func (GetVrackNetworksOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetVrackNetworksArgs)(nil)).Elem()
}

// A collection of values returned by getVrackNetworks.
type GetVrackNetworksResultOutput struct{ *pulumi.OutputState }

func (GetVrackNetworksResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetVrackNetworksResult)(nil)).Elem()
}

func (o GetVrackNetworksResultOutput) ToGetVrackNetworksResultOutput() GetVrackNetworksResultOutput {
	return o
}

func (o GetVrackNetworksResultOutput) ToGetVrackNetworksResultOutputWithContext(ctx context.Context) GetVrackNetworksResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetVrackNetworksResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetVrackNetworksResult) string { return v.Id }).(pulumi.StringOutput)
}

// The list of vrack network ids.
func (o GetVrackNetworksResultOutput) Results() pulumi.IntArrayOutput {
	return o.ApplyT(func(v GetVrackNetworksResult) []int { return v.Results }).(pulumi.IntArrayOutput)
}

func (o GetVrackNetworksResultOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v GetVrackNetworksResult) string { return v.ServiceName }).(pulumi.StringOutput)
}

func (o GetVrackNetworksResultOutput) Subnet() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetVrackNetworksResult) *string { return v.Subnet }).(pulumi.StringPtrOutput)
}

func (o GetVrackNetworksResultOutput) VlanId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v GetVrackNetworksResult) *int { return v.VlanId }).(pulumi.IntPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetVrackNetworksResultOutput{})
}
