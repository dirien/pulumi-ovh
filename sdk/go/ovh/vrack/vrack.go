// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vrack

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Example Usage
type Vrack struct {
	pulumi.CustomResourceState

	// yourvrackdescription
	Description pulumi.StringOutput `pulumi:"description"`
	// yourvrackname
	Name pulumi.StringOutput `pulumi:"name"`
	// Details about an Order
	Orders VrackOrderArrayOutput `pulumi:"orders"`
	// OVHcloud Subsidiary
	OvhSubsidiary pulumi.StringOutput `pulumi:"ovhSubsidiary"`
	// Ovh payment mode
	//
	// Deprecated: This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
	PaymentMean pulumi.StringPtrOutput `pulumi:"paymentMean"`
	// Product Plan to order
	Plan VrackPlanOutput `pulumi:"plan"`
	// Product Plan to order
	PlanOptions VrackPlanOptionArrayOutput `pulumi:"planOptions"`
	// The internal name of your vrack
	ServiceName pulumi.StringOutput `pulumi:"serviceName"`
	// The URN of the vrack, used with IAM permissions
	Urn pulumi.StringOutput `pulumi:"urn"`
}

// NewVrack registers a new resource with the given unique name, arguments, and options.
func NewVrack(ctx *pulumi.Context,
	name string, args *VrackArgs, opts ...pulumi.ResourceOption) (*Vrack, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.OvhSubsidiary == nil {
		return nil, errors.New("invalid value for required argument 'OvhSubsidiary'")
	}
	if args.Plan == nil {
		return nil, errors.New("invalid value for required argument 'Plan'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource Vrack
	err := ctx.RegisterResource("ovh:Vrack/vrack:Vrack", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVrack gets an existing Vrack resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVrack(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VrackState, opts ...pulumi.ResourceOption) (*Vrack, error) {
	var resource Vrack
	err := ctx.ReadResource("ovh:Vrack/vrack:Vrack", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Vrack resources.
type vrackState struct {
	// yourvrackdescription
	Description *string `pulumi:"description"`
	// yourvrackname
	Name *string `pulumi:"name"`
	// Details about an Order
	Orders []VrackOrder `pulumi:"orders"`
	// OVHcloud Subsidiary
	OvhSubsidiary *string `pulumi:"ovhSubsidiary"`
	// Ovh payment mode
	//
	// Deprecated: This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
	PaymentMean *string `pulumi:"paymentMean"`
	// Product Plan to order
	Plan *VrackPlan `pulumi:"plan"`
	// Product Plan to order
	PlanOptions []VrackPlanOption `pulumi:"planOptions"`
	// The internal name of your vrack
	ServiceName *string `pulumi:"serviceName"`
	// The URN of the vrack, used with IAM permissions
	Urn *string `pulumi:"urn"`
}

type VrackState struct {
	// yourvrackdescription
	Description pulumi.StringPtrInput
	// yourvrackname
	Name pulumi.StringPtrInput
	// Details about an Order
	Orders VrackOrderArrayInput
	// OVHcloud Subsidiary
	OvhSubsidiary pulumi.StringPtrInput
	// Ovh payment mode
	//
	// Deprecated: This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
	PaymentMean pulumi.StringPtrInput
	// Product Plan to order
	Plan VrackPlanPtrInput
	// Product Plan to order
	PlanOptions VrackPlanOptionArrayInput
	// The internal name of your vrack
	ServiceName pulumi.StringPtrInput
	// The URN of the vrack, used with IAM permissions
	Urn pulumi.StringPtrInput
}

func (VrackState) ElementType() reflect.Type {
	return reflect.TypeOf((*vrackState)(nil)).Elem()
}

type vrackArgs struct {
	// yourvrackdescription
	Description *string `pulumi:"description"`
	// yourvrackname
	Name *string `pulumi:"name"`
	// OVHcloud Subsidiary
	OvhSubsidiary string `pulumi:"ovhSubsidiary"`
	// Ovh payment mode
	//
	// Deprecated: This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
	PaymentMean *string `pulumi:"paymentMean"`
	// Product Plan to order
	Plan VrackPlan `pulumi:"plan"`
	// Product Plan to order
	PlanOptions []VrackPlanOption `pulumi:"planOptions"`
}

// The set of arguments for constructing a Vrack resource.
type VrackArgs struct {
	// yourvrackdescription
	Description pulumi.StringPtrInput
	// yourvrackname
	Name pulumi.StringPtrInput
	// OVHcloud Subsidiary
	OvhSubsidiary pulumi.StringInput
	// Ovh payment mode
	//
	// Deprecated: This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
	PaymentMean pulumi.StringPtrInput
	// Product Plan to order
	Plan VrackPlanInput
	// Product Plan to order
	PlanOptions VrackPlanOptionArrayInput
}

func (VrackArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vrackArgs)(nil)).Elem()
}

type VrackInput interface {
	pulumi.Input

	ToVrackOutput() VrackOutput
	ToVrackOutputWithContext(ctx context.Context) VrackOutput
}

func (*Vrack) ElementType() reflect.Type {
	return reflect.TypeOf((**Vrack)(nil)).Elem()
}

func (i *Vrack) ToVrackOutput() VrackOutput {
	return i.ToVrackOutputWithContext(context.Background())
}

func (i *Vrack) ToVrackOutputWithContext(ctx context.Context) VrackOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VrackOutput)
}

// VrackArrayInput is an input type that accepts VrackArray and VrackArrayOutput values.
// You can construct a concrete instance of `VrackArrayInput` via:
//
//	VrackArray{ VrackArgs{...} }
type VrackArrayInput interface {
	pulumi.Input

	ToVrackArrayOutput() VrackArrayOutput
	ToVrackArrayOutputWithContext(context.Context) VrackArrayOutput
}

type VrackArray []VrackInput

func (VrackArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Vrack)(nil)).Elem()
}

func (i VrackArray) ToVrackArrayOutput() VrackArrayOutput {
	return i.ToVrackArrayOutputWithContext(context.Background())
}

func (i VrackArray) ToVrackArrayOutputWithContext(ctx context.Context) VrackArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VrackArrayOutput)
}

// VrackMapInput is an input type that accepts VrackMap and VrackMapOutput values.
// You can construct a concrete instance of `VrackMapInput` via:
//
//	VrackMap{ "key": VrackArgs{...} }
type VrackMapInput interface {
	pulumi.Input

	ToVrackMapOutput() VrackMapOutput
	ToVrackMapOutputWithContext(context.Context) VrackMapOutput
}

type VrackMap map[string]VrackInput

func (VrackMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Vrack)(nil)).Elem()
}

func (i VrackMap) ToVrackMapOutput() VrackMapOutput {
	return i.ToVrackMapOutputWithContext(context.Background())
}

func (i VrackMap) ToVrackMapOutputWithContext(ctx context.Context) VrackMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VrackMapOutput)
}

type VrackOutput struct{ *pulumi.OutputState }

func (VrackOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Vrack)(nil)).Elem()
}

func (o VrackOutput) ToVrackOutput() VrackOutput {
	return o
}

func (o VrackOutput) ToVrackOutputWithContext(ctx context.Context) VrackOutput {
	return o
}

// yourvrackdescription
func (o VrackOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *Vrack) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// yourvrackname
func (o VrackOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Vrack) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Details about an Order
func (o VrackOutput) Orders() VrackOrderArrayOutput {
	return o.ApplyT(func(v *Vrack) VrackOrderArrayOutput { return v.Orders }).(VrackOrderArrayOutput)
}

// OVHcloud Subsidiary
func (o VrackOutput) OvhSubsidiary() pulumi.StringOutput {
	return o.ApplyT(func(v *Vrack) pulumi.StringOutput { return v.OvhSubsidiary }).(pulumi.StringOutput)
}

// Ovh payment mode
//
// Deprecated: This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
func (o VrackOutput) PaymentMean() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Vrack) pulumi.StringPtrOutput { return v.PaymentMean }).(pulumi.StringPtrOutput)
}

// Product Plan to order
func (o VrackOutput) Plan() VrackPlanOutput {
	return o.ApplyT(func(v *Vrack) VrackPlanOutput { return v.Plan }).(VrackPlanOutput)
}

// Product Plan to order
func (o VrackOutput) PlanOptions() VrackPlanOptionArrayOutput {
	return o.ApplyT(func(v *Vrack) VrackPlanOptionArrayOutput { return v.PlanOptions }).(VrackPlanOptionArrayOutput)
}

// The internal name of your vrack
func (o VrackOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v *Vrack) pulumi.StringOutput { return v.ServiceName }).(pulumi.StringOutput)
}

// The URN of the vrack, used with IAM permissions
func (o VrackOutput) Urn() pulumi.StringOutput {
	return o.ApplyT(func(v *Vrack) pulumi.StringOutput { return v.Urn }).(pulumi.StringOutput)
}

type VrackArrayOutput struct{ *pulumi.OutputState }

func (VrackArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Vrack)(nil)).Elem()
}

func (o VrackArrayOutput) ToVrackArrayOutput() VrackArrayOutput {
	return o
}

func (o VrackArrayOutput) ToVrackArrayOutputWithContext(ctx context.Context) VrackArrayOutput {
	return o
}

func (o VrackArrayOutput) Index(i pulumi.IntInput) VrackOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Vrack {
		return vs[0].([]*Vrack)[vs[1].(int)]
	}).(VrackOutput)
}

type VrackMapOutput struct{ *pulumi.OutputState }

func (VrackMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Vrack)(nil)).Elem()
}

func (o VrackMapOutput) ToVrackMapOutput() VrackMapOutput {
	return o
}

func (o VrackMapOutput) ToVrackMapOutputWithContext(ctx context.Context) VrackMapOutput {
	return o
}

func (o VrackMapOutput) MapIndex(k pulumi.StringInput) VrackOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Vrack {
		return vs[0].(map[string]*Vrack)[vs[1].(string)]
	}).(VrackOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VrackInput)(nil)).Elem(), &Vrack{})
	pulumi.RegisterInputType(reflect.TypeOf((*VrackArrayInput)(nil)).Elem(), VrackArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*VrackMapInput)(nil)).Elem(), VrackMap{})
	pulumi.RegisterOutputType(VrackOutput{})
	pulumi.RegisterOutputType(VrackArrayOutput{})
	pulumi.RegisterOutputType(VrackMapOutput{})
}
