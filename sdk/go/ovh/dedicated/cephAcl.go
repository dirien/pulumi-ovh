// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dedicated

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Add a new access ACL for the given network/mask.
//
// ## Example Usage
type CephAcl struct {
	pulumi.CustomResourceState

	// IP family. `IPv4` or `IPv6`
	Family pulumi.StringOutput `pulumi:"family"`
	// The network mask to apply
	Netmask pulumi.StringOutput `pulumi:"netmask"`
	// The network IP to authorize
	Network pulumi.StringOutput `pulumi:"network"`
	// The internal name of your dedicated CEPH
	ServiceName pulumi.StringOutput `pulumi:"serviceName"`
}

// NewCephAcl registers a new resource with the given unique name, arguments, and options.
func NewCephAcl(ctx *pulumi.Context,
	name string, args *CephAclArgs, opts ...pulumi.ResourceOption) (*CephAcl, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Netmask == nil {
		return nil, errors.New("invalid value for required argument 'Netmask'")
	}
	if args.Network == nil {
		return nil, errors.New("invalid value for required argument 'Network'")
	}
	if args.ServiceName == nil {
		return nil, errors.New("invalid value for required argument 'ServiceName'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource CephAcl
	err := ctx.RegisterResource("ovh:Dedicated/cephAcl:CephAcl", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCephAcl gets an existing CephAcl resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCephAcl(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CephAclState, opts ...pulumi.ResourceOption) (*CephAcl, error) {
	var resource CephAcl
	err := ctx.ReadResource("ovh:Dedicated/cephAcl:CephAcl", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CephAcl resources.
type cephAclState struct {
	// IP family. `IPv4` or `IPv6`
	Family *string `pulumi:"family"`
	// The network mask to apply
	Netmask *string `pulumi:"netmask"`
	// The network IP to authorize
	Network *string `pulumi:"network"`
	// The internal name of your dedicated CEPH
	ServiceName *string `pulumi:"serviceName"`
}

type CephAclState struct {
	// IP family. `IPv4` or `IPv6`
	Family pulumi.StringPtrInput
	// The network mask to apply
	Netmask pulumi.StringPtrInput
	// The network IP to authorize
	Network pulumi.StringPtrInput
	// The internal name of your dedicated CEPH
	ServiceName pulumi.StringPtrInput
}

func (CephAclState) ElementType() reflect.Type {
	return reflect.TypeOf((*cephAclState)(nil)).Elem()
}

type cephAclArgs struct {
	// The network mask to apply
	Netmask string `pulumi:"netmask"`
	// The network IP to authorize
	Network string `pulumi:"network"`
	// The internal name of your dedicated CEPH
	ServiceName string `pulumi:"serviceName"`
}

// The set of arguments for constructing a CephAcl resource.
type CephAclArgs struct {
	// The network mask to apply
	Netmask pulumi.StringInput
	// The network IP to authorize
	Network pulumi.StringInput
	// The internal name of your dedicated CEPH
	ServiceName pulumi.StringInput
}

func (CephAclArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*cephAclArgs)(nil)).Elem()
}

type CephAclInput interface {
	pulumi.Input

	ToCephAclOutput() CephAclOutput
	ToCephAclOutputWithContext(ctx context.Context) CephAclOutput
}

func (*CephAcl) ElementType() reflect.Type {
	return reflect.TypeOf((**CephAcl)(nil)).Elem()
}

func (i *CephAcl) ToCephAclOutput() CephAclOutput {
	return i.ToCephAclOutputWithContext(context.Background())
}

func (i *CephAcl) ToCephAclOutputWithContext(ctx context.Context) CephAclOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CephAclOutput)
}

// CephAclArrayInput is an input type that accepts CephAclArray and CephAclArrayOutput values.
// You can construct a concrete instance of `CephAclArrayInput` via:
//
//	CephAclArray{ CephAclArgs{...} }
type CephAclArrayInput interface {
	pulumi.Input

	ToCephAclArrayOutput() CephAclArrayOutput
	ToCephAclArrayOutputWithContext(context.Context) CephAclArrayOutput
}

type CephAclArray []CephAclInput

func (CephAclArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CephAcl)(nil)).Elem()
}

func (i CephAclArray) ToCephAclArrayOutput() CephAclArrayOutput {
	return i.ToCephAclArrayOutputWithContext(context.Background())
}

func (i CephAclArray) ToCephAclArrayOutputWithContext(ctx context.Context) CephAclArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CephAclArrayOutput)
}

// CephAclMapInput is an input type that accepts CephAclMap and CephAclMapOutput values.
// You can construct a concrete instance of `CephAclMapInput` via:
//
//	CephAclMap{ "key": CephAclArgs{...} }
type CephAclMapInput interface {
	pulumi.Input

	ToCephAclMapOutput() CephAclMapOutput
	ToCephAclMapOutputWithContext(context.Context) CephAclMapOutput
}

type CephAclMap map[string]CephAclInput

func (CephAclMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CephAcl)(nil)).Elem()
}

func (i CephAclMap) ToCephAclMapOutput() CephAclMapOutput {
	return i.ToCephAclMapOutputWithContext(context.Background())
}

func (i CephAclMap) ToCephAclMapOutputWithContext(ctx context.Context) CephAclMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CephAclMapOutput)
}

type CephAclOutput struct{ *pulumi.OutputState }

func (CephAclOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CephAcl)(nil)).Elem()
}

func (o CephAclOutput) ToCephAclOutput() CephAclOutput {
	return o
}

func (o CephAclOutput) ToCephAclOutputWithContext(ctx context.Context) CephAclOutput {
	return o
}

// IP family. `IPv4` or `IPv6`
func (o CephAclOutput) Family() pulumi.StringOutput {
	return o.ApplyT(func(v *CephAcl) pulumi.StringOutput { return v.Family }).(pulumi.StringOutput)
}

// The network mask to apply
func (o CephAclOutput) Netmask() pulumi.StringOutput {
	return o.ApplyT(func(v *CephAcl) pulumi.StringOutput { return v.Netmask }).(pulumi.StringOutput)
}

// The network IP to authorize
func (o CephAclOutput) Network() pulumi.StringOutput {
	return o.ApplyT(func(v *CephAcl) pulumi.StringOutput { return v.Network }).(pulumi.StringOutput)
}

// The internal name of your dedicated CEPH
func (o CephAclOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v *CephAcl) pulumi.StringOutput { return v.ServiceName }).(pulumi.StringOutput)
}

type CephAclArrayOutput struct{ *pulumi.OutputState }

func (CephAclArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CephAcl)(nil)).Elem()
}

func (o CephAclArrayOutput) ToCephAclArrayOutput() CephAclArrayOutput {
	return o
}

func (o CephAclArrayOutput) ToCephAclArrayOutputWithContext(ctx context.Context) CephAclArrayOutput {
	return o
}

func (o CephAclArrayOutput) Index(i pulumi.IntInput) CephAclOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *CephAcl {
		return vs[0].([]*CephAcl)[vs[1].(int)]
	}).(CephAclOutput)
}

type CephAclMapOutput struct{ *pulumi.OutputState }

func (CephAclMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CephAcl)(nil)).Elem()
}

func (o CephAclMapOutput) ToCephAclMapOutput() CephAclMapOutput {
	return o
}

func (o CephAclMapOutput) ToCephAclMapOutputWithContext(ctx context.Context) CephAclMapOutput {
	return o
}

func (o CephAclMapOutput) MapIndex(k pulumi.StringInput) CephAclOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *CephAcl {
		return vs[0].(map[string]*CephAcl)[vs[1].(string)]
	}).(CephAclOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CephAclInput)(nil)).Elem(), &CephAcl{})
	pulumi.RegisterInputType(reflect.TypeOf((*CephAclArrayInput)(nil)).Elem(), CephAclArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*CephAclMapInput)(nil)).Elem(), CephAclMap{})
	pulumi.RegisterOutputType(CephAclOutput{})
	pulumi.RegisterOutputType(CephAclArrayOutput{})
	pulumi.RegisterOutputType(CephAclMapOutput{})
}
