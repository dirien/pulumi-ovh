// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vrack

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type VrackOrder struct {
	// date
	Date *string `pulumi:"date"`
	// Information about a Bill entry
	Details []VrackOrderDetail `pulumi:"details"`
	// expiration date
	ExpirationDate *string `pulumi:"expirationDate"`
	// order id
	OrderId *int `pulumi:"orderId"`
}

// VrackOrderInput is an input type that accepts VrackOrderArgs and VrackOrderOutput values.
// You can construct a concrete instance of `VrackOrderInput` via:
//
//	VrackOrderArgs{...}
type VrackOrderInput interface {
	pulumi.Input

	ToVrackOrderOutput() VrackOrderOutput
	ToVrackOrderOutputWithContext(context.Context) VrackOrderOutput
}

type VrackOrderArgs struct {
	// date
	Date pulumi.StringPtrInput `pulumi:"date"`
	// Information about a Bill entry
	Details VrackOrderDetailArrayInput `pulumi:"details"`
	// expiration date
	ExpirationDate pulumi.StringPtrInput `pulumi:"expirationDate"`
	// order id
	OrderId pulumi.IntPtrInput `pulumi:"orderId"`
}

func (VrackOrderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*VrackOrder)(nil)).Elem()
}

func (i VrackOrderArgs) ToVrackOrderOutput() VrackOrderOutput {
	return i.ToVrackOrderOutputWithContext(context.Background())
}

func (i VrackOrderArgs) ToVrackOrderOutputWithContext(ctx context.Context) VrackOrderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VrackOrderOutput)
}

// VrackOrderArrayInput is an input type that accepts VrackOrderArray and VrackOrderArrayOutput values.
// You can construct a concrete instance of `VrackOrderArrayInput` via:
//
//	VrackOrderArray{ VrackOrderArgs{...} }
type VrackOrderArrayInput interface {
	pulumi.Input

	ToVrackOrderArrayOutput() VrackOrderArrayOutput
	ToVrackOrderArrayOutputWithContext(context.Context) VrackOrderArrayOutput
}

type VrackOrderArray []VrackOrderInput

func (VrackOrderArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]VrackOrder)(nil)).Elem()
}

func (i VrackOrderArray) ToVrackOrderArrayOutput() VrackOrderArrayOutput {
	return i.ToVrackOrderArrayOutputWithContext(context.Background())
}

func (i VrackOrderArray) ToVrackOrderArrayOutputWithContext(ctx context.Context) VrackOrderArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VrackOrderArrayOutput)
}

type VrackOrderOutput struct{ *pulumi.OutputState }

func (VrackOrderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*VrackOrder)(nil)).Elem()
}

func (o VrackOrderOutput) ToVrackOrderOutput() VrackOrderOutput {
	return o
}

func (o VrackOrderOutput) ToVrackOrderOutputWithContext(ctx context.Context) VrackOrderOutput {
	return o
}

// date
func (o VrackOrderOutput) Date() pulumi.StringPtrOutput {
	return o.ApplyT(func(v VrackOrder) *string { return v.Date }).(pulumi.StringPtrOutput)
}

// Information about a Bill entry
func (o VrackOrderOutput) Details() VrackOrderDetailArrayOutput {
	return o.ApplyT(func(v VrackOrder) []VrackOrderDetail { return v.Details }).(VrackOrderDetailArrayOutput)
}

// expiration date
func (o VrackOrderOutput) ExpirationDate() pulumi.StringPtrOutput {
	return o.ApplyT(func(v VrackOrder) *string { return v.ExpirationDate }).(pulumi.StringPtrOutput)
}

// order id
func (o VrackOrderOutput) OrderId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v VrackOrder) *int { return v.OrderId }).(pulumi.IntPtrOutput)
}

type VrackOrderArrayOutput struct{ *pulumi.OutputState }

func (VrackOrderArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]VrackOrder)(nil)).Elem()
}

func (o VrackOrderArrayOutput) ToVrackOrderArrayOutput() VrackOrderArrayOutput {
	return o
}

func (o VrackOrderArrayOutput) ToVrackOrderArrayOutputWithContext(ctx context.Context) VrackOrderArrayOutput {
	return o
}

func (o VrackOrderArrayOutput) Index(i pulumi.IntInput) VrackOrderOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) VrackOrder {
		return vs[0].([]VrackOrder)[vs[1].(int)]
	}).(VrackOrderOutput)
}

type VrackOrderDetail struct {
	// yourvrackdescription
	Description *string `pulumi:"description"`
	// expiration date
	Domain *string `pulumi:"domain"`
	// order detail id
	OrderDetailId *int `pulumi:"orderDetailId"`
	// quantity
	Quantity *string `pulumi:"quantity"`
}

// VrackOrderDetailInput is an input type that accepts VrackOrderDetailArgs and VrackOrderDetailOutput values.
// You can construct a concrete instance of `VrackOrderDetailInput` via:
//
//	VrackOrderDetailArgs{...}
type VrackOrderDetailInput interface {
	pulumi.Input

	ToVrackOrderDetailOutput() VrackOrderDetailOutput
	ToVrackOrderDetailOutputWithContext(context.Context) VrackOrderDetailOutput
}

type VrackOrderDetailArgs struct {
	// yourvrackdescription
	Description pulumi.StringPtrInput `pulumi:"description"`
	// expiration date
	Domain pulumi.StringPtrInput `pulumi:"domain"`
	// order detail id
	OrderDetailId pulumi.IntPtrInput `pulumi:"orderDetailId"`
	// quantity
	Quantity pulumi.StringPtrInput `pulumi:"quantity"`
}

func (VrackOrderDetailArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*VrackOrderDetail)(nil)).Elem()
}

func (i VrackOrderDetailArgs) ToVrackOrderDetailOutput() VrackOrderDetailOutput {
	return i.ToVrackOrderDetailOutputWithContext(context.Background())
}

func (i VrackOrderDetailArgs) ToVrackOrderDetailOutputWithContext(ctx context.Context) VrackOrderDetailOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VrackOrderDetailOutput)
}

// VrackOrderDetailArrayInput is an input type that accepts VrackOrderDetailArray and VrackOrderDetailArrayOutput values.
// You can construct a concrete instance of `VrackOrderDetailArrayInput` via:
//
//	VrackOrderDetailArray{ VrackOrderDetailArgs{...} }
type VrackOrderDetailArrayInput interface {
	pulumi.Input

	ToVrackOrderDetailArrayOutput() VrackOrderDetailArrayOutput
	ToVrackOrderDetailArrayOutputWithContext(context.Context) VrackOrderDetailArrayOutput
}

type VrackOrderDetailArray []VrackOrderDetailInput

func (VrackOrderDetailArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]VrackOrderDetail)(nil)).Elem()
}

func (i VrackOrderDetailArray) ToVrackOrderDetailArrayOutput() VrackOrderDetailArrayOutput {
	return i.ToVrackOrderDetailArrayOutputWithContext(context.Background())
}

func (i VrackOrderDetailArray) ToVrackOrderDetailArrayOutputWithContext(ctx context.Context) VrackOrderDetailArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VrackOrderDetailArrayOutput)
}

type VrackOrderDetailOutput struct{ *pulumi.OutputState }

func (VrackOrderDetailOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*VrackOrderDetail)(nil)).Elem()
}

func (o VrackOrderDetailOutput) ToVrackOrderDetailOutput() VrackOrderDetailOutput {
	return o
}

func (o VrackOrderDetailOutput) ToVrackOrderDetailOutputWithContext(ctx context.Context) VrackOrderDetailOutput {
	return o
}

// yourvrackdescription
func (o VrackOrderDetailOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v VrackOrderDetail) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// expiration date
func (o VrackOrderDetailOutput) Domain() pulumi.StringPtrOutput {
	return o.ApplyT(func(v VrackOrderDetail) *string { return v.Domain }).(pulumi.StringPtrOutput)
}

// order detail id
func (o VrackOrderDetailOutput) OrderDetailId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v VrackOrderDetail) *int { return v.OrderDetailId }).(pulumi.IntPtrOutput)
}

// quantity
func (o VrackOrderDetailOutput) Quantity() pulumi.StringPtrOutput {
	return o.ApplyT(func(v VrackOrderDetail) *string { return v.Quantity }).(pulumi.StringPtrOutput)
}

type VrackOrderDetailArrayOutput struct{ *pulumi.OutputState }

func (VrackOrderDetailArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]VrackOrderDetail)(nil)).Elem()
}

func (o VrackOrderDetailArrayOutput) ToVrackOrderDetailArrayOutput() VrackOrderDetailArrayOutput {
	return o
}

func (o VrackOrderDetailArrayOutput) ToVrackOrderDetailArrayOutputWithContext(ctx context.Context) VrackOrderDetailArrayOutput {
	return o
}

func (o VrackOrderDetailArrayOutput) Index(i pulumi.IntInput) VrackOrderDetailOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) VrackOrderDetail {
		return vs[0].([]VrackOrderDetail)[vs[1].(int)]
	}).(VrackOrderDetailOutput)
}

type VrackPlan struct {
	// Catalog name
	CatalogName *string `pulumi:"catalogName"`
	// Representation of a configuration item for personalizing product
	Configurations []VrackPlanConfiguration `pulumi:"configurations"`
	// duration
	Duration string `pulumi:"duration"`
	// Plan code
	PlanCode string `pulumi:"planCode"`
	// Pricing model identifier
	PricingMode string `pulumi:"pricingMode"`
}

// VrackPlanInput is an input type that accepts VrackPlanArgs and VrackPlanOutput values.
// You can construct a concrete instance of `VrackPlanInput` via:
//
//	VrackPlanArgs{...}
type VrackPlanInput interface {
	pulumi.Input

	ToVrackPlanOutput() VrackPlanOutput
	ToVrackPlanOutputWithContext(context.Context) VrackPlanOutput
}

type VrackPlanArgs struct {
	// Catalog name
	CatalogName pulumi.StringPtrInput `pulumi:"catalogName"`
	// Representation of a configuration item for personalizing product
	Configurations VrackPlanConfigurationArrayInput `pulumi:"configurations"`
	// duration
	Duration pulumi.StringInput `pulumi:"duration"`
	// Plan code
	PlanCode pulumi.StringInput `pulumi:"planCode"`
	// Pricing model identifier
	PricingMode pulumi.StringInput `pulumi:"pricingMode"`
}

func (VrackPlanArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*VrackPlan)(nil)).Elem()
}

func (i VrackPlanArgs) ToVrackPlanOutput() VrackPlanOutput {
	return i.ToVrackPlanOutputWithContext(context.Background())
}

func (i VrackPlanArgs) ToVrackPlanOutputWithContext(ctx context.Context) VrackPlanOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VrackPlanOutput)
}

func (i VrackPlanArgs) ToVrackPlanPtrOutput() VrackPlanPtrOutput {
	return i.ToVrackPlanPtrOutputWithContext(context.Background())
}

func (i VrackPlanArgs) ToVrackPlanPtrOutputWithContext(ctx context.Context) VrackPlanPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VrackPlanOutput).ToVrackPlanPtrOutputWithContext(ctx)
}

// VrackPlanPtrInput is an input type that accepts VrackPlanArgs, VrackPlanPtr and VrackPlanPtrOutput values.
// You can construct a concrete instance of `VrackPlanPtrInput` via:
//
//	        VrackPlanArgs{...}
//
//	or:
//
//	        nil
type VrackPlanPtrInput interface {
	pulumi.Input

	ToVrackPlanPtrOutput() VrackPlanPtrOutput
	ToVrackPlanPtrOutputWithContext(context.Context) VrackPlanPtrOutput
}

type vrackPlanPtrType VrackPlanArgs

func VrackPlanPtr(v *VrackPlanArgs) VrackPlanPtrInput {
	return (*vrackPlanPtrType)(v)
}

func (*vrackPlanPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**VrackPlan)(nil)).Elem()
}

func (i *vrackPlanPtrType) ToVrackPlanPtrOutput() VrackPlanPtrOutput {
	return i.ToVrackPlanPtrOutputWithContext(context.Background())
}

func (i *vrackPlanPtrType) ToVrackPlanPtrOutputWithContext(ctx context.Context) VrackPlanPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VrackPlanPtrOutput)
}

type VrackPlanOutput struct{ *pulumi.OutputState }

func (VrackPlanOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*VrackPlan)(nil)).Elem()
}

func (o VrackPlanOutput) ToVrackPlanOutput() VrackPlanOutput {
	return o
}

func (o VrackPlanOutput) ToVrackPlanOutputWithContext(ctx context.Context) VrackPlanOutput {
	return o
}

func (o VrackPlanOutput) ToVrackPlanPtrOutput() VrackPlanPtrOutput {
	return o.ToVrackPlanPtrOutputWithContext(context.Background())
}

func (o VrackPlanOutput) ToVrackPlanPtrOutputWithContext(ctx context.Context) VrackPlanPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v VrackPlan) *VrackPlan {
		return &v
	}).(VrackPlanPtrOutput)
}

// Catalog name
func (o VrackPlanOutput) CatalogName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v VrackPlan) *string { return v.CatalogName }).(pulumi.StringPtrOutput)
}

// Representation of a configuration item for personalizing product
func (o VrackPlanOutput) Configurations() VrackPlanConfigurationArrayOutput {
	return o.ApplyT(func(v VrackPlan) []VrackPlanConfiguration { return v.Configurations }).(VrackPlanConfigurationArrayOutput)
}

// duration
func (o VrackPlanOutput) Duration() pulumi.StringOutput {
	return o.ApplyT(func(v VrackPlan) string { return v.Duration }).(pulumi.StringOutput)
}

// Plan code
func (o VrackPlanOutput) PlanCode() pulumi.StringOutput {
	return o.ApplyT(func(v VrackPlan) string { return v.PlanCode }).(pulumi.StringOutput)
}

// Pricing model identifier
func (o VrackPlanOutput) PricingMode() pulumi.StringOutput {
	return o.ApplyT(func(v VrackPlan) string { return v.PricingMode }).(pulumi.StringOutput)
}

type VrackPlanPtrOutput struct{ *pulumi.OutputState }

func (VrackPlanPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VrackPlan)(nil)).Elem()
}

func (o VrackPlanPtrOutput) ToVrackPlanPtrOutput() VrackPlanPtrOutput {
	return o
}

func (o VrackPlanPtrOutput) ToVrackPlanPtrOutputWithContext(ctx context.Context) VrackPlanPtrOutput {
	return o
}

func (o VrackPlanPtrOutput) Elem() VrackPlanOutput {
	return o.ApplyT(func(v *VrackPlan) VrackPlan {
		if v != nil {
			return *v
		}
		var ret VrackPlan
		return ret
	}).(VrackPlanOutput)
}

// Catalog name
func (o VrackPlanPtrOutput) CatalogName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VrackPlan) *string {
		if v == nil {
			return nil
		}
		return v.CatalogName
	}).(pulumi.StringPtrOutput)
}

// Representation of a configuration item for personalizing product
func (o VrackPlanPtrOutput) Configurations() VrackPlanConfigurationArrayOutput {
	return o.ApplyT(func(v *VrackPlan) []VrackPlanConfiguration {
		if v == nil {
			return nil
		}
		return v.Configurations
	}).(VrackPlanConfigurationArrayOutput)
}

// duration
func (o VrackPlanPtrOutput) Duration() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VrackPlan) *string {
		if v == nil {
			return nil
		}
		return &v.Duration
	}).(pulumi.StringPtrOutput)
}

// Plan code
func (o VrackPlanPtrOutput) PlanCode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VrackPlan) *string {
		if v == nil {
			return nil
		}
		return &v.PlanCode
	}).(pulumi.StringPtrOutput)
}

// Pricing model identifier
func (o VrackPlanPtrOutput) PricingMode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VrackPlan) *string {
		if v == nil {
			return nil
		}
		return &v.PricingMode
	}).(pulumi.StringPtrOutput)
}

type VrackPlanConfiguration struct {
	// Identifier of the resource
	Label string `pulumi:"label"`
	// Path to the resource in API.OVH.COM
	Value string `pulumi:"value"`
}

// VrackPlanConfigurationInput is an input type that accepts VrackPlanConfigurationArgs and VrackPlanConfigurationOutput values.
// You can construct a concrete instance of `VrackPlanConfigurationInput` via:
//
//	VrackPlanConfigurationArgs{...}
type VrackPlanConfigurationInput interface {
	pulumi.Input

	ToVrackPlanConfigurationOutput() VrackPlanConfigurationOutput
	ToVrackPlanConfigurationOutputWithContext(context.Context) VrackPlanConfigurationOutput
}

type VrackPlanConfigurationArgs struct {
	// Identifier of the resource
	Label pulumi.StringInput `pulumi:"label"`
	// Path to the resource in API.OVH.COM
	Value pulumi.StringInput `pulumi:"value"`
}

func (VrackPlanConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*VrackPlanConfiguration)(nil)).Elem()
}

func (i VrackPlanConfigurationArgs) ToVrackPlanConfigurationOutput() VrackPlanConfigurationOutput {
	return i.ToVrackPlanConfigurationOutputWithContext(context.Background())
}

func (i VrackPlanConfigurationArgs) ToVrackPlanConfigurationOutputWithContext(ctx context.Context) VrackPlanConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VrackPlanConfigurationOutput)
}

// VrackPlanConfigurationArrayInput is an input type that accepts VrackPlanConfigurationArray and VrackPlanConfigurationArrayOutput values.
// You can construct a concrete instance of `VrackPlanConfigurationArrayInput` via:
//
//	VrackPlanConfigurationArray{ VrackPlanConfigurationArgs{...} }
type VrackPlanConfigurationArrayInput interface {
	pulumi.Input

	ToVrackPlanConfigurationArrayOutput() VrackPlanConfigurationArrayOutput
	ToVrackPlanConfigurationArrayOutputWithContext(context.Context) VrackPlanConfigurationArrayOutput
}

type VrackPlanConfigurationArray []VrackPlanConfigurationInput

func (VrackPlanConfigurationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]VrackPlanConfiguration)(nil)).Elem()
}

func (i VrackPlanConfigurationArray) ToVrackPlanConfigurationArrayOutput() VrackPlanConfigurationArrayOutput {
	return i.ToVrackPlanConfigurationArrayOutputWithContext(context.Background())
}

func (i VrackPlanConfigurationArray) ToVrackPlanConfigurationArrayOutputWithContext(ctx context.Context) VrackPlanConfigurationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VrackPlanConfigurationArrayOutput)
}

type VrackPlanConfigurationOutput struct{ *pulumi.OutputState }

func (VrackPlanConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*VrackPlanConfiguration)(nil)).Elem()
}

func (o VrackPlanConfigurationOutput) ToVrackPlanConfigurationOutput() VrackPlanConfigurationOutput {
	return o
}

func (o VrackPlanConfigurationOutput) ToVrackPlanConfigurationOutputWithContext(ctx context.Context) VrackPlanConfigurationOutput {
	return o
}

// Identifier of the resource
func (o VrackPlanConfigurationOutput) Label() pulumi.StringOutput {
	return o.ApplyT(func(v VrackPlanConfiguration) string { return v.Label }).(pulumi.StringOutput)
}

// Path to the resource in API.OVH.COM
func (o VrackPlanConfigurationOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v VrackPlanConfiguration) string { return v.Value }).(pulumi.StringOutput)
}

type VrackPlanConfigurationArrayOutput struct{ *pulumi.OutputState }

func (VrackPlanConfigurationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]VrackPlanConfiguration)(nil)).Elem()
}

func (o VrackPlanConfigurationArrayOutput) ToVrackPlanConfigurationArrayOutput() VrackPlanConfigurationArrayOutput {
	return o
}

func (o VrackPlanConfigurationArrayOutput) ToVrackPlanConfigurationArrayOutputWithContext(ctx context.Context) VrackPlanConfigurationArrayOutput {
	return o
}

func (o VrackPlanConfigurationArrayOutput) Index(i pulumi.IntInput) VrackPlanConfigurationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) VrackPlanConfiguration {
		return vs[0].([]VrackPlanConfiguration)[vs[1].(int)]
	}).(VrackPlanConfigurationOutput)
}

type VrackPlanOption struct {
	// Catalog name
	CatalogName *string `pulumi:"catalogName"`
	// Representation of a configuration item for personalizing product
	Configurations []VrackPlanOptionConfiguration `pulumi:"configurations"`
	// duration
	Duration string `pulumi:"duration"`
	// Plan code
	PlanCode string `pulumi:"planCode"`
	// Pricing model identifier
	PricingMode string `pulumi:"pricingMode"`
}

// VrackPlanOptionInput is an input type that accepts VrackPlanOptionArgs and VrackPlanOptionOutput values.
// You can construct a concrete instance of `VrackPlanOptionInput` via:
//
//	VrackPlanOptionArgs{...}
type VrackPlanOptionInput interface {
	pulumi.Input

	ToVrackPlanOptionOutput() VrackPlanOptionOutput
	ToVrackPlanOptionOutputWithContext(context.Context) VrackPlanOptionOutput
}

type VrackPlanOptionArgs struct {
	// Catalog name
	CatalogName pulumi.StringPtrInput `pulumi:"catalogName"`
	// Representation of a configuration item for personalizing product
	Configurations VrackPlanOptionConfigurationArrayInput `pulumi:"configurations"`
	// duration
	Duration pulumi.StringInput `pulumi:"duration"`
	// Plan code
	PlanCode pulumi.StringInput `pulumi:"planCode"`
	// Pricing model identifier
	PricingMode pulumi.StringInput `pulumi:"pricingMode"`
}

func (VrackPlanOptionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*VrackPlanOption)(nil)).Elem()
}

func (i VrackPlanOptionArgs) ToVrackPlanOptionOutput() VrackPlanOptionOutput {
	return i.ToVrackPlanOptionOutputWithContext(context.Background())
}

func (i VrackPlanOptionArgs) ToVrackPlanOptionOutputWithContext(ctx context.Context) VrackPlanOptionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VrackPlanOptionOutput)
}

// VrackPlanOptionArrayInput is an input type that accepts VrackPlanOptionArray and VrackPlanOptionArrayOutput values.
// You can construct a concrete instance of `VrackPlanOptionArrayInput` via:
//
//	VrackPlanOptionArray{ VrackPlanOptionArgs{...} }
type VrackPlanOptionArrayInput interface {
	pulumi.Input

	ToVrackPlanOptionArrayOutput() VrackPlanOptionArrayOutput
	ToVrackPlanOptionArrayOutputWithContext(context.Context) VrackPlanOptionArrayOutput
}

type VrackPlanOptionArray []VrackPlanOptionInput

func (VrackPlanOptionArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]VrackPlanOption)(nil)).Elem()
}

func (i VrackPlanOptionArray) ToVrackPlanOptionArrayOutput() VrackPlanOptionArrayOutput {
	return i.ToVrackPlanOptionArrayOutputWithContext(context.Background())
}

func (i VrackPlanOptionArray) ToVrackPlanOptionArrayOutputWithContext(ctx context.Context) VrackPlanOptionArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VrackPlanOptionArrayOutput)
}

type VrackPlanOptionOutput struct{ *pulumi.OutputState }

func (VrackPlanOptionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*VrackPlanOption)(nil)).Elem()
}

func (o VrackPlanOptionOutput) ToVrackPlanOptionOutput() VrackPlanOptionOutput {
	return o
}

func (o VrackPlanOptionOutput) ToVrackPlanOptionOutputWithContext(ctx context.Context) VrackPlanOptionOutput {
	return o
}

// Catalog name
func (o VrackPlanOptionOutput) CatalogName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v VrackPlanOption) *string { return v.CatalogName }).(pulumi.StringPtrOutput)
}

// Representation of a configuration item for personalizing product
func (o VrackPlanOptionOutput) Configurations() VrackPlanOptionConfigurationArrayOutput {
	return o.ApplyT(func(v VrackPlanOption) []VrackPlanOptionConfiguration { return v.Configurations }).(VrackPlanOptionConfigurationArrayOutput)
}

// duration
func (o VrackPlanOptionOutput) Duration() pulumi.StringOutput {
	return o.ApplyT(func(v VrackPlanOption) string { return v.Duration }).(pulumi.StringOutput)
}

// Plan code
func (o VrackPlanOptionOutput) PlanCode() pulumi.StringOutput {
	return o.ApplyT(func(v VrackPlanOption) string { return v.PlanCode }).(pulumi.StringOutput)
}

// Pricing model identifier
func (o VrackPlanOptionOutput) PricingMode() pulumi.StringOutput {
	return o.ApplyT(func(v VrackPlanOption) string { return v.PricingMode }).(pulumi.StringOutput)
}

type VrackPlanOptionArrayOutput struct{ *pulumi.OutputState }

func (VrackPlanOptionArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]VrackPlanOption)(nil)).Elem()
}

func (o VrackPlanOptionArrayOutput) ToVrackPlanOptionArrayOutput() VrackPlanOptionArrayOutput {
	return o
}

func (o VrackPlanOptionArrayOutput) ToVrackPlanOptionArrayOutputWithContext(ctx context.Context) VrackPlanOptionArrayOutput {
	return o
}

func (o VrackPlanOptionArrayOutput) Index(i pulumi.IntInput) VrackPlanOptionOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) VrackPlanOption {
		return vs[0].([]VrackPlanOption)[vs[1].(int)]
	}).(VrackPlanOptionOutput)
}

type VrackPlanOptionConfiguration struct {
	// Identifier of the resource
	Label string `pulumi:"label"`
	// Path to the resource in API.OVH.COM
	Value string `pulumi:"value"`
}

// VrackPlanOptionConfigurationInput is an input type that accepts VrackPlanOptionConfigurationArgs and VrackPlanOptionConfigurationOutput values.
// You can construct a concrete instance of `VrackPlanOptionConfigurationInput` via:
//
//	VrackPlanOptionConfigurationArgs{...}
type VrackPlanOptionConfigurationInput interface {
	pulumi.Input

	ToVrackPlanOptionConfigurationOutput() VrackPlanOptionConfigurationOutput
	ToVrackPlanOptionConfigurationOutputWithContext(context.Context) VrackPlanOptionConfigurationOutput
}

type VrackPlanOptionConfigurationArgs struct {
	// Identifier of the resource
	Label pulumi.StringInput `pulumi:"label"`
	// Path to the resource in API.OVH.COM
	Value pulumi.StringInput `pulumi:"value"`
}

func (VrackPlanOptionConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*VrackPlanOptionConfiguration)(nil)).Elem()
}

func (i VrackPlanOptionConfigurationArgs) ToVrackPlanOptionConfigurationOutput() VrackPlanOptionConfigurationOutput {
	return i.ToVrackPlanOptionConfigurationOutputWithContext(context.Background())
}

func (i VrackPlanOptionConfigurationArgs) ToVrackPlanOptionConfigurationOutputWithContext(ctx context.Context) VrackPlanOptionConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VrackPlanOptionConfigurationOutput)
}

// VrackPlanOptionConfigurationArrayInput is an input type that accepts VrackPlanOptionConfigurationArray and VrackPlanOptionConfigurationArrayOutput values.
// You can construct a concrete instance of `VrackPlanOptionConfigurationArrayInput` via:
//
//	VrackPlanOptionConfigurationArray{ VrackPlanOptionConfigurationArgs{...} }
type VrackPlanOptionConfigurationArrayInput interface {
	pulumi.Input

	ToVrackPlanOptionConfigurationArrayOutput() VrackPlanOptionConfigurationArrayOutput
	ToVrackPlanOptionConfigurationArrayOutputWithContext(context.Context) VrackPlanOptionConfigurationArrayOutput
}

type VrackPlanOptionConfigurationArray []VrackPlanOptionConfigurationInput

func (VrackPlanOptionConfigurationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]VrackPlanOptionConfiguration)(nil)).Elem()
}

func (i VrackPlanOptionConfigurationArray) ToVrackPlanOptionConfigurationArrayOutput() VrackPlanOptionConfigurationArrayOutput {
	return i.ToVrackPlanOptionConfigurationArrayOutputWithContext(context.Background())
}

func (i VrackPlanOptionConfigurationArray) ToVrackPlanOptionConfigurationArrayOutputWithContext(ctx context.Context) VrackPlanOptionConfigurationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VrackPlanOptionConfigurationArrayOutput)
}

type VrackPlanOptionConfigurationOutput struct{ *pulumi.OutputState }

func (VrackPlanOptionConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*VrackPlanOptionConfiguration)(nil)).Elem()
}

func (o VrackPlanOptionConfigurationOutput) ToVrackPlanOptionConfigurationOutput() VrackPlanOptionConfigurationOutput {
	return o
}

func (o VrackPlanOptionConfigurationOutput) ToVrackPlanOptionConfigurationOutputWithContext(ctx context.Context) VrackPlanOptionConfigurationOutput {
	return o
}

// Identifier of the resource
func (o VrackPlanOptionConfigurationOutput) Label() pulumi.StringOutput {
	return o.ApplyT(func(v VrackPlanOptionConfiguration) string { return v.Label }).(pulumi.StringOutput)
}

// Path to the resource in API.OVH.COM
func (o VrackPlanOptionConfigurationOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v VrackPlanOptionConfiguration) string { return v.Value }).(pulumi.StringOutput)
}

type VrackPlanOptionConfigurationArrayOutput struct{ *pulumi.OutputState }

func (VrackPlanOptionConfigurationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]VrackPlanOptionConfiguration)(nil)).Elem()
}

func (o VrackPlanOptionConfigurationArrayOutput) ToVrackPlanOptionConfigurationArrayOutput() VrackPlanOptionConfigurationArrayOutput {
	return o
}

func (o VrackPlanOptionConfigurationArrayOutput) ToVrackPlanOptionConfigurationArrayOutputWithContext(ctx context.Context) VrackPlanOptionConfigurationArrayOutput {
	return o
}

func (o VrackPlanOptionConfigurationArrayOutput) Index(i pulumi.IntInput) VrackPlanOptionConfigurationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) VrackPlanOptionConfiguration {
		return vs[0].([]VrackPlanOptionConfiguration)[vs[1].(int)]
	}).(VrackPlanOptionConfigurationOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VrackOrderInput)(nil)).Elem(), VrackOrderArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*VrackOrderArrayInput)(nil)).Elem(), VrackOrderArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*VrackOrderDetailInput)(nil)).Elem(), VrackOrderDetailArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*VrackOrderDetailArrayInput)(nil)).Elem(), VrackOrderDetailArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*VrackPlanInput)(nil)).Elem(), VrackPlanArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*VrackPlanPtrInput)(nil)).Elem(), VrackPlanArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*VrackPlanConfigurationInput)(nil)).Elem(), VrackPlanConfigurationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*VrackPlanConfigurationArrayInput)(nil)).Elem(), VrackPlanConfigurationArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*VrackPlanOptionInput)(nil)).Elem(), VrackPlanOptionArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*VrackPlanOptionArrayInput)(nil)).Elem(), VrackPlanOptionArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*VrackPlanOptionConfigurationInput)(nil)).Elem(), VrackPlanOptionConfigurationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*VrackPlanOptionConfigurationArrayInput)(nil)).Elem(), VrackPlanOptionConfigurationArray{})
	pulumi.RegisterOutputType(VrackOrderOutput{})
	pulumi.RegisterOutputType(VrackOrderArrayOutput{})
	pulumi.RegisterOutputType(VrackOrderDetailOutput{})
	pulumi.RegisterOutputType(VrackOrderDetailArrayOutput{})
	pulumi.RegisterOutputType(VrackPlanOutput{})
	pulumi.RegisterOutputType(VrackPlanPtrOutput{})
	pulumi.RegisterOutputType(VrackPlanConfigurationOutput{})
	pulumi.RegisterOutputType(VrackPlanConfigurationArrayOutput{})
	pulumi.RegisterOutputType(VrackPlanOptionOutput{})
	pulumi.RegisterOutputType(VrackPlanOptionArrayOutput{})
	pulumi.RegisterOutputType(VrackPlanOptionConfigurationOutput{})
	pulumi.RegisterOutputType(VrackPlanOptionConfigurationArrayOutput{})
}
