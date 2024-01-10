// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudproject

import (
	"context"
	"reflect"

	"errors"
	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a private network in a public cloud project.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/ovh/pulumi-ovh/sdk/go/ovh/CloudProject"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := CloudProject.NewNetworkPrivate(ctx, "net", &CloudProject.NetworkPrivateArgs{
//				Regions: pulumi.StringArray{
//					pulumi.String("GRA1"),
//					pulumi.String("BHS1"),
//				},
//				ServiceName: pulumi.String("XXXXXX"),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// Private network in a public cloud project can be imported using the `service_name` and the `network_id`, separated by "/" E.g., bash
//
// ```sh
//
//	$ pulumi import ovh:CloudProject/networkPrivate:NetworkPrivate mynet ookie9mee8Shaeghaeleeju7Xeghohv6e/pn-12345678
//
// ```
type NetworkPrivate struct {
	pulumi.CustomResourceState

	// The name of the network.
	Name pulumi.StringOutput `pulumi:"name"`
	// an array of valid OVHcloud public cloud region ID in which the network
	// will be available. Ex.: "GRA1". Defaults to all public cloud regions.
	Regions pulumi.StringArrayOutput `pulumi:"regions"`
	// A map representing information about the region.
	// * `regions_attributes/region` - The id of the region.
	// * `regions_attributes/status` - The status of the network in the region.
	// * `regions_attributes/openstackid` - The private network id in the region.
	RegionsAttributes NetworkPrivateRegionsAttributeArrayOutput `pulumi:"regionsAttributes"`
	// (Deprecated) A map representing the status of the network per region.
	// * `regions_status/region` - (Deprecated) The id of the region.
	// * `regions_status/status` - (Deprecated) The status of the network in the region.
	//
	// Deprecated: use the regions_attributes field instead
	RegionsStatuses NetworkPrivateRegionsStatusArrayOutput `pulumi:"regionsStatuses"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName pulumi.StringOutput `pulumi:"serviceName"`
	// the status of the network. should be normally set to 'ACTIVE'.
	Status pulumi.StringOutput `pulumi:"status"`
	// the type of the network. Either 'private' or 'public'.
	Type pulumi.StringOutput `pulumi:"type"`
	// a vlan id to associate with the network.
	// Changing this value recreates the resource. Defaults to 0.
	VlanId pulumi.IntPtrOutput `pulumi:"vlanId"`
}

// NewNetworkPrivate registers a new resource with the given unique name, arguments, and options.
func NewNetworkPrivate(ctx *pulumi.Context,
	name string, args *NetworkPrivateArgs, opts ...pulumi.ResourceOption) (*NetworkPrivate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ServiceName == nil {
		return nil, errors.New("invalid value for required argument 'ServiceName'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource NetworkPrivate
	err := ctx.RegisterResource("ovh:CloudProject/networkPrivate:NetworkPrivate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNetworkPrivate gets an existing NetworkPrivate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNetworkPrivate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NetworkPrivateState, opts ...pulumi.ResourceOption) (*NetworkPrivate, error) {
	var resource NetworkPrivate
	err := ctx.ReadResource("ovh:CloudProject/networkPrivate:NetworkPrivate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NetworkPrivate resources.
type networkPrivateState struct {
	// The name of the network.
	Name *string `pulumi:"name"`
	// an array of valid OVHcloud public cloud region ID in which the network
	// will be available. Ex.: "GRA1". Defaults to all public cloud regions.
	Regions []string `pulumi:"regions"`
	// A map representing information about the region.
	// * `regions_attributes/region` - The id of the region.
	// * `regions_attributes/status` - The status of the network in the region.
	// * `regions_attributes/openstackid` - The private network id in the region.
	RegionsAttributes []NetworkPrivateRegionsAttribute `pulumi:"regionsAttributes"`
	// (Deprecated) A map representing the status of the network per region.
	// * `regions_status/region` - (Deprecated) The id of the region.
	// * `regions_status/status` - (Deprecated) The status of the network in the region.
	//
	// Deprecated: use the regions_attributes field instead
	RegionsStatuses []NetworkPrivateRegionsStatus `pulumi:"regionsStatuses"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName *string `pulumi:"serviceName"`
	// the status of the network. should be normally set to 'ACTIVE'.
	Status *string `pulumi:"status"`
	// the type of the network. Either 'private' or 'public'.
	Type *string `pulumi:"type"`
	// a vlan id to associate with the network.
	// Changing this value recreates the resource. Defaults to 0.
	VlanId *int `pulumi:"vlanId"`
}

type NetworkPrivateState struct {
	// The name of the network.
	Name pulumi.StringPtrInput
	// an array of valid OVHcloud public cloud region ID in which the network
	// will be available. Ex.: "GRA1". Defaults to all public cloud regions.
	Regions pulumi.StringArrayInput
	// A map representing information about the region.
	// * `regions_attributes/region` - The id of the region.
	// * `regions_attributes/status` - The status of the network in the region.
	// * `regions_attributes/openstackid` - The private network id in the region.
	RegionsAttributes NetworkPrivateRegionsAttributeArrayInput
	// (Deprecated) A map representing the status of the network per region.
	// * `regions_status/region` - (Deprecated) The id of the region.
	// * `regions_status/status` - (Deprecated) The status of the network in the region.
	//
	// Deprecated: use the regions_attributes field instead
	RegionsStatuses NetworkPrivateRegionsStatusArrayInput
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName pulumi.StringPtrInput
	// the status of the network. should be normally set to 'ACTIVE'.
	Status pulumi.StringPtrInput
	// the type of the network. Either 'private' or 'public'.
	Type pulumi.StringPtrInput
	// a vlan id to associate with the network.
	// Changing this value recreates the resource. Defaults to 0.
	VlanId pulumi.IntPtrInput
}

func (NetworkPrivateState) ElementType() reflect.Type {
	return reflect.TypeOf((*networkPrivateState)(nil)).Elem()
}

type networkPrivateArgs struct {
	// The name of the network.
	Name *string `pulumi:"name"`
	// an array of valid OVHcloud public cloud region ID in which the network
	// will be available. Ex.: "GRA1". Defaults to all public cloud regions.
	Regions []string `pulumi:"regions"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName string `pulumi:"serviceName"`
	// a vlan id to associate with the network.
	// Changing this value recreates the resource. Defaults to 0.
	VlanId *int `pulumi:"vlanId"`
}

// The set of arguments for constructing a NetworkPrivate resource.
type NetworkPrivateArgs struct {
	// The name of the network.
	Name pulumi.StringPtrInput
	// an array of valid OVHcloud public cloud region ID in which the network
	// will be available. Ex.: "GRA1". Defaults to all public cloud regions.
	Regions pulumi.StringArrayInput
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName pulumi.StringInput
	// a vlan id to associate with the network.
	// Changing this value recreates the resource. Defaults to 0.
	VlanId pulumi.IntPtrInput
}

func (NetworkPrivateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*networkPrivateArgs)(nil)).Elem()
}

type NetworkPrivateInput interface {
	pulumi.Input

	ToNetworkPrivateOutput() NetworkPrivateOutput
	ToNetworkPrivateOutputWithContext(ctx context.Context) NetworkPrivateOutput
}

func (*NetworkPrivate) ElementType() reflect.Type {
	return reflect.TypeOf((**NetworkPrivate)(nil)).Elem()
}

func (i *NetworkPrivate) ToNetworkPrivateOutput() NetworkPrivateOutput {
	return i.ToNetworkPrivateOutputWithContext(context.Background())
}

func (i *NetworkPrivate) ToNetworkPrivateOutputWithContext(ctx context.Context) NetworkPrivateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkPrivateOutput)
}

// NetworkPrivateArrayInput is an input type that accepts NetworkPrivateArray and NetworkPrivateArrayOutput values.
// You can construct a concrete instance of `NetworkPrivateArrayInput` via:
//
//	NetworkPrivateArray{ NetworkPrivateArgs{...} }
type NetworkPrivateArrayInput interface {
	pulumi.Input

	ToNetworkPrivateArrayOutput() NetworkPrivateArrayOutput
	ToNetworkPrivateArrayOutputWithContext(context.Context) NetworkPrivateArrayOutput
}

type NetworkPrivateArray []NetworkPrivateInput

func (NetworkPrivateArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*NetworkPrivate)(nil)).Elem()
}

func (i NetworkPrivateArray) ToNetworkPrivateArrayOutput() NetworkPrivateArrayOutput {
	return i.ToNetworkPrivateArrayOutputWithContext(context.Background())
}

func (i NetworkPrivateArray) ToNetworkPrivateArrayOutputWithContext(ctx context.Context) NetworkPrivateArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkPrivateArrayOutput)
}

// NetworkPrivateMapInput is an input type that accepts NetworkPrivateMap and NetworkPrivateMapOutput values.
// You can construct a concrete instance of `NetworkPrivateMapInput` via:
//
//	NetworkPrivateMap{ "key": NetworkPrivateArgs{...} }
type NetworkPrivateMapInput interface {
	pulumi.Input

	ToNetworkPrivateMapOutput() NetworkPrivateMapOutput
	ToNetworkPrivateMapOutputWithContext(context.Context) NetworkPrivateMapOutput
}

type NetworkPrivateMap map[string]NetworkPrivateInput

func (NetworkPrivateMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*NetworkPrivate)(nil)).Elem()
}

func (i NetworkPrivateMap) ToNetworkPrivateMapOutput() NetworkPrivateMapOutput {
	return i.ToNetworkPrivateMapOutputWithContext(context.Background())
}

func (i NetworkPrivateMap) ToNetworkPrivateMapOutputWithContext(ctx context.Context) NetworkPrivateMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkPrivateMapOutput)
}

type NetworkPrivateOutput struct{ *pulumi.OutputState }

func (NetworkPrivateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**NetworkPrivate)(nil)).Elem()
}

func (o NetworkPrivateOutput) ToNetworkPrivateOutput() NetworkPrivateOutput {
	return o
}

func (o NetworkPrivateOutput) ToNetworkPrivateOutputWithContext(ctx context.Context) NetworkPrivateOutput {
	return o
}

// The name of the network.
func (o NetworkPrivateOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkPrivate) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// an array of valid OVHcloud public cloud region ID in which the network
// will be available. Ex.: "GRA1". Defaults to all public cloud regions.
func (o NetworkPrivateOutput) Regions() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *NetworkPrivate) pulumi.StringArrayOutput { return v.Regions }).(pulumi.StringArrayOutput)
}

// A map representing information about the region.
// * `regions_attributes/region` - The id of the region.
// * `regions_attributes/status` - The status of the network in the region.
// * `regions_attributes/openstackid` - The private network id in the region.
func (o NetworkPrivateOutput) RegionsAttributes() NetworkPrivateRegionsAttributeArrayOutput {
	return o.ApplyT(func(v *NetworkPrivate) NetworkPrivateRegionsAttributeArrayOutput { return v.RegionsAttributes }).(NetworkPrivateRegionsAttributeArrayOutput)
}

// (Deprecated) A map representing the status of the network per region.
// * `regions_status/region` - (Deprecated) The id of the region.
// * `regions_status/status` - (Deprecated) The status of the network in the region.
//
// Deprecated: use the regions_attributes field instead
func (o NetworkPrivateOutput) RegionsStatuses() NetworkPrivateRegionsStatusArrayOutput {
	return o.ApplyT(func(v *NetworkPrivate) NetworkPrivateRegionsStatusArrayOutput { return v.RegionsStatuses }).(NetworkPrivateRegionsStatusArrayOutput)
}

// The id of the public cloud project. If omitted,
// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
func (o NetworkPrivateOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkPrivate) pulumi.StringOutput { return v.ServiceName }).(pulumi.StringOutput)
}

// the status of the network. should be normally set to 'ACTIVE'.
func (o NetworkPrivateOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkPrivate) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

// the type of the network. Either 'private' or 'public'.
func (o NetworkPrivateOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkPrivate) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

// a vlan id to associate with the network.
// Changing this value recreates the resource. Defaults to 0.
func (o NetworkPrivateOutput) VlanId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *NetworkPrivate) pulumi.IntPtrOutput { return v.VlanId }).(pulumi.IntPtrOutput)
}

type NetworkPrivateArrayOutput struct{ *pulumi.OutputState }

func (NetworkPrivateArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*NetworkPrivate)(nil)).Elem()
}

func (o NetworkPrivateArrayOutput) ToNetworkPrivateArrayOutput() NetworkPrivateArrayOutput {
	return o
}

func (o NetworkPrivateArrayOutput) ToNetworkPrivateArrayOutputWithContext(ctx context.Context) NetworkPrivateArrayOutput {
	return o
}

func (o NetworkPrivateArrayOutput) Index(i pulumi.IntInput) NetworkPrivateOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *NetworkPrivate {
		return vs[0].([]*NetworkPrivate)[vs[1].(int)]
	}).(NetworkPrivateOutput)
}

type NetworkPrivateMapOutput struct{ *pulumi.OutputState }

func (NetworkPrivateMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*NetworkPrivate)(nil)).Elem()
}

func (o NetworkPrivateMapOutput) ToNetworkPrivateMapOutput() NetworkPrivateMapOutput {
	return o
}

func (o NetworkPrivateMapOutput) ToNetworkPrivateMapOutputWithContext(ctx context.Context) NetworkPrivateMapOutput {
	return o
}

func (o NetworkPrivateMapOutput) MapIndex(k pulumi.StringInput) NetworkPrivateOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *NetworkPrivate {
		return vs[0].(map[string]*NetworkPrivate)[vs[1].(string)]
	}).(NetworkPrivateOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkPrivateInput)(nil)).Elem(), &NetworkPrivate{})
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkPrivateArrayInput)(nil)).Elem(), NetworkPrivateArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkPrivateMapInput)(nil)).Elem(), NetworkPrivateMap{})
	pulumi.RegisterOutputType(NetworkPrivateOutput{})
	pulumi.RegisterOutputType(NetworkPrivateArrayOutput{})
	pulumi.RegisterOutputType(NetworkPrivateMapOutput{})
}
