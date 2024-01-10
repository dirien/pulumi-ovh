// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package domain

import (
	"context"
	"reflect"

	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

type ZoneOrder struct {
	// date
	Date *string `pulumi:"date"`
	// Information about a Bill entry
	Details []ZoneOrderDetail `pulumi:"details"`
	// expiration date
	ExpirationDate *string `pulumi:"expirationDate"`
	// order id
	OrderId *int `pulumi:"orderId"`
}

// ZoneOrderInput is an input type that accepts ZoneOrderArgs and ZoneOrderOutput values.
// You can construct a concrete instance of `ZoneOrderInput` via:
//
//	ZoneOrderArgs{...}
type ZoneOrderInput interface {
	pulumi.Input

	ToZoneOrderOutput() ZoneOrderOutput
	ToZoneOrderOutputWithContext(context.Context) ZoneOrderOutput
}

type ZoneOrderArgs struct {
	// date
	Date pulumi.StringPtrInput `pulumi:"date"`
	// Information about a Bill entry
	Details ZoneOrderDetailArrayInput `pulumi:"details"`
	// expiration date
	ExpirationDate pulumi.StringPtrInput `pulumi:"expirationDate"`
	// order id
	OrderId pulumi.IntPtrInput `pulumi:"orderId"`
}

func (ZoneOrderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ZoneOrder)(nil)).Elem()
}

func (i ZoneOrderArgs) ToZoneOrderOutput() ZoneOrderOutput {
	return i.ToZoneOrderOutputWithContext(context.Background())
}

func (i ZoneOrderArgs) ToZoneOrderOutputWithContext(ctx context.Context) ZoneOrderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZoneOrderOutput)
}

// ZoneOrderArrayInput is an input type that accepts ZoneOrderArray and ZoneOrderArrayOutput values.
// You can construct a concrete instance of `ZoneOrderArrayInput` via:
//
//	ZoneOrderArray{ ZoneOrderArgs{...} }
type ZoneOrderArrayInput interface {
	pulumi.Input

	ToZoneOrderArrayOutput() ZoneOrderArrayOutput
	ToZoneOrderArrayOutputWithContext(context.Context) ZoneOrderArrayOutput
}

type ZoneOrderArray []ZoneOrderInput

func (ZoneOrderArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ZoneOrder)(nil)).Elem()
}

func (i ZoneOrderArray) ToZoneOrderArrayOutput() ZoneOrderArrayOutput {
	return i.ToZoneOrderArrayOutputWithContext(context.Background())
}

func (i ZoneOrderArray) ToZoneOrderArrayOutputWithContext(ctx context.Context) ZoneOrderArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZoneOrderArrayOutput)
}

type ZoneOrderOutput struct{ *pulumi.OutputState }

func (ZoneOrderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ZoneOrder)(nil)).Elem()
}

func (o ZoneOrderOutput) ToZoneOrderOutput() ZoneOrderOutput {
	return o
}

func (o ZoneOrderOutput) ToZoneOrderOutputWithContext(ctx context.Context) ZoneOrderOutput {
	return o
}

// date
func (o ZoneOrderOutput) Date() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ZoneOrder) *string { return v.Date }).(pulumi.StringPtrOutput)
}

// Information about a Bill entry
func (o ZoneOrderOutput) Details() ZoneOrderDetailArrayOutput {
	return o.ApplyT(func(v ZoneOrder) []ZoneOrderDetail { return v.Details }).(ZoneOrderDetailArrayOutput)
}

// expiration date
func (o ZoneOrderOutput) ExpirationDate() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ZoneOrder) *string { return v.ExpirationDate }).(pulumi.StringPtrOutput)
}

// order id
func (o ZoneOrderOutput) OrderId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v ZoneOrder) *int { return v.OrderId }).(pulumi.IntPtrOutput)
}

type ZoneOrderArrayOutput struct{ *pulumi.OutputState }

func (ZoneOrderArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ZoneOrder)(nil)).Elem()
}

func (o ZoneOrderArrayOutput) ToZoneOrderArrayOutput() ZoneOrderArrayOutput {
	return o
}

func (o ZoneOrderArrayOutput) ToZoneOrderArrayOutputWithContext(ctx context.Context) ZoneOrderArrayOutput {
	return o
}

func (o ZoneOrderArrayOutput) Index(i pulumi.IntInput) ZoneOrderOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ZoneOrder {
		return vs[0].([]ZoneOrder)[vs[1].(int)]
	}).(ZoneOrderOutput)
}

type ZoneOrderDetail struct {
	// description
	Description *string `pulumi:"description"`
	// expiration date
	Domain *string `pulumi:"domain"`
	// order detail id
	OrderDetailId *int `pulumi:"orderDetailId"`
	// quantity
	Quantity *string `pulumi:"quantity"`
}

// ZoneOrderDetailInput is an input type that accepts ZoneOrderDetailArgs and ZoneOrderDetailOutput values.
// You can construct a concrete instance of `ZoneOrderDetailInput` via:
//
//	ZoneOrderDetailArgs{...}
type ZoneOrderDetailInput interface {
	pulumi.Input

	ToZoneOrderDetailOutput() ZoneOrderDetailOutput
	ToZoneOrderDetailOutputWithContext(context.Context) ZoneOrderDetailOutput
}

type ZoneOrderDetailArgs struct {
	// description
	Description pulumi.StringPtrInput `pulumi:"description"`
	// expiration date
	Domain pulumi.StringPtrInput `pulumi:"domain"`
	// order detail id
	OrderDetailId pulumi.IntPtrInput `pulumi:"orderDetailId"`
	// quantity
	Quantity pulumi.StringPtrInput `pulumi:"quantity"`
}

func (ZoneOrderDetailArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ZoneOrderDetail)(nil)).Elem()
}

func (i ZoneOrderDetailArgs) ToZoneOrderDetailOutput() ZoneOrderDetailOutput {
	return i.ToZoneOrderDetailOutputWithContext(context.Background())
}

func (i ZoneOrderDetailArgs) ToZoneOrderDetailOutputWithContext(ctx context.Context) ZoneOrderDetailOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZoneOrderDetailOutput)
}

// ZoneOrderDetailArrayInput is an input type that accepts ZoneOrderDetailArray and ZoneOrderDetailArrayOutput values.
// You can construct a concrete instance of `ZoneOrderDetailArrayInput` via:
//
//	ZoneOrderDetailArray{ ZoneOrderDetailArgs{...} }
type ZoneOrderDetailArrayInput interface {
	pulumi.Input

	ToZoneOrderDetailArrayOutput() ZoneOrderDetailArrayOutput
	ToZoneOrderDetailArrayOutputWithContext(context.Context) ZoneOrderDetailArrayOutput
}

type ZoneOrderDetailArray []ZoneOrderDetailInput

func (ZoneOrderDetailArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ZoneOrderDetail)(nil)).Elem()
}

func (i ZoneOrderDetailArray) ToZoneOrderDetailArrayOutput() ZoneOrderDetailArrayOutput {
	return i.ToZoneOrderDetailArrayOutputWithContext(context.Background())
}

func (i ZoneOrderDetailArray) ToZoneOrderDetailArrayOutputWithContext(ctx context.Context) ZoneOrderDetailArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZoneOrderDetailArrayOutput)
}

type ZoneOrderDetailOutput struct{ *pulumi.OutputState }

func (ZoneOrderDetailOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ZoneOrderDetail)(nil)).Elem()
}

func (o ZoneOrderDetailOutput) ToZoneOrderDetailOutput() ZoneOrderDetailOutput {
	return o
}

func (o ZoneOrderDetailOutput) ToZoneOrderDetailOutputWithContext(ctx context.Context) ZoneOrderDetailOutput {
	return o
}

// description
func (o ZoneOrderDetailOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ZoneOrderDetail) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// expiration date
func (o ZoneOrderDetailOutput) Domain() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ZoneOrderDetail) *string { return v.Domain }).(pulumi.StringPtrOutput)
}

// order detail id
func (o ZoneOrderDetailOutput) OrderDetailId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v ZoneOrderDetail) *int { return v.OrderDetailId }).(pulumi.IntPtrOutput)
}

// quantity
func (o ZoneOrderDetailOutput) Quantity() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ZoneOrderDetail) *string { return v.Quantity }).(pulumi.StringPtrOutput)
}

type ZoneOrderDetailArrayOutput struct{ *pulumi.OutputState }

func (ZoneOrderDetailArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ZoneOrderDetail)(nil)).Elem()
}

func (o ZoneOrderDetailArrayOutput) ToZoneOrderDetailArrayOutput() ZoneOrderDetailArrayOutput {
	return o
}

func (o ZoneOrderDetailArrayOutput) ToZoneOrderDetailArrayOutputWithContext(ctx context.Context) ZoneOrderDetailArrayOutput {
	return o
}

func (o ZoneOrderDetailArrayOutput) Index(i pulumi.IntInput) ZoneOrderDetailOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ZoneOrderDetail {
		return vs[0].([]ZoneOrderDetail)[vs[1].(int)]
	}).(ZoneOrderDetailOutput)
}

type ZonePlan struct {
	// Catalog name
	CatalogName *string `pulumi:"catalogName"`
	// Representation of a configuration item for personalizing product
	Configurations []ZonePlanConfiguration `pulumi:"configurations"`
	// duration
	Duration string `pulumi:"duration"`
	// Plan code
	PlanCode string `pulumi:"planCode"`
	// Pricing model identifier
	PricingMode string `pulumi:"pricingMode"`
}

// ZonePlanInput is an input type that accepts ZonePlanArgs and ZonePlanOutput values.
// You can construct a concrete instance of `ZonePlanInput` via:
//
//	ZonePlanArgs{...}
type ZonePlanInput interface {
	pulumi.Input

	ToZonePlanOutput() ZonePlanOutput
	ToZonePlanOutputWithContext(context.Context) ZonePlanOutput
}

type ZonePlanArgs struct {
	// Catalog name
	CatalogName pulumi.StringPtrInput `pulumi:"catalogName"`
	// Representation of a configuration item for personalizing product
	Configurations ZonePlanConfigurationArrayInput `pulumi:"configurations"`
	// duration
	Duration pulumi.StringInput `pulumi:"duration"`
	// Plan code
	PlanCode pulumi.StringInput `pulumi:"planCode"`
	// Pricing model identifier
	PricingMode pulumi.StringInput `pulumi:"pricingMode"`
}

func (ZonePlanArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ZonePlan)(nil)).Elem()
}

func (i ZonePlanArgs) ToZonePlanOutput() ZonePlanOutput {
	return i.ToZonePlanOutputWithContext(context.Background())
}

func (i ZonePlanArgs) ToZonePlanOutputWithContext(ctx context.Context) ZonePlanOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZonePlanOutput)
}

func (i ZonePlanArgs) ToZonePlanPtrOutput() ZonePlanPtrOutput {
	return i.ToZonePlanPtrOutputWithContext(context.Background())
}

func (i ZonePlanArgs) ToZonePlanPtrOutputWithContext(ctx context.Context) ZonePlanPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZonePlanOutput).ToZonePlanPtrOutputWithContext(ctx)
}

// ZonePlanPtrInput is an input type that accepts ZonePlanArgs, ZonePlanPtr and ZonePlanPtrOutput values.
// You can construct a concrete instance of `ZonePlanPtrInput` via:
//
//	        ZonePlanArgs{...}
//
//	or:
//
//	        nil
type ZonePlanPtrInput interface {
	pulumi.Input

	ToZonePlanPtrOutput() ZonePlanPtrOutput
	ToZonePlanPtrOutputWithContext(context.Context) ZonePlanPtrOutput
}

type zonePlanPtrType ZonePlanArgs

func ZonePlanPtr(v *ZonePlanArgs) ZonePlanPtrInput {
	return (*zonePlanPtrType)(v)
}

func (*zonePlanPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**ZonePlan)(nil)).Elem()
}

func (i *zonePlanPtrType) ToZonePlanPtrOutput() ZonePlanPtrOutput {
	return i.ToZonePlanPtrOutputWithContext(context.Background())
}

func (i *zonePlanPtrType) ToZonePlanPtrOutputWithContext(ctx context.Context) ZonePlanPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZonePlanPtrOutput)
}

type ZonePlanOutput struct{ *pulumi.OutputState }

func (ZonePlanOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ZonePlan)(nil)).Elem()
}

func (o ZonePlanOutput) ToZonePlanOutput() ZonePlanOutput {
	return o
}

func (o ZonePlanOutput) ToZonePlanOutputWithContext(ctx context.Context) ZonePlanOutput {
	return o
}

func (o ZonePlanOutput) ToZonePlanPtrOutput() ZonePlanPtrOutput {
	return o.ToZonePlanPtrOutputWithContext(context.Background())
}

func (o ZonePlanOutput) ToZonePlanPtrOutputWithContext(ctx context.Context) ZonePlanPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ZonePlan) *ZonePlan {
		return &v
	}).(ZonePlanPtrOutput)
}

// Catalog name
func (o ZonePlanOutput) CatalogName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ZonePlan) *string { return v.CatalogName }).(pulumi.StringPtrOutput)
}

// Representation of a configuration item for personalizing product
func (o ZonePlanOutput) Configurations() ZonePlanConfigurationArrayOutput {
	return o.ApplyT(func(v ZonePlan) []ZonePlanConfiguration { return v.Configurations }).(ZonePlanConfigurationArrayOutput)
}

// duration
func (o ZonePlanOutput) Duration() pulumi.StringOutput {
	return o.ApplyT(func(v ZonePlan) string { return v.Duration }).(pulumi.StringOutput)
}

// Plan code
func (o ZonePlanOutput) PlanCode() pulumi.StringOutput {
	return o.ApplyT(func(v ZonePlan) string { return v.PlanCode }).(pulumi.StringOutput)
}

// Pricing model identifier
func (o ZonePlanOutput) PricingMode() pulumi.StringOutput {
	return o.ApplyT(func(v ZonePlan) string { return v.PricingMode }).(pulumi.StringOutput)
}

type ZonePlanPtrOutput struct{ *pulumi.OutputState }

func (ZonePlanPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ZonePlan)(nil)).Elem()
}

func (o ZonePlanPtrOutput) ToZonePlanPtrOutput() ZonePlanPtrOutput {
	return o
}

func (o ZonePlanPtrOutput) ToZonePlanPtrOutputWithContext(ctx context.Context) ZonePlanPtrOutput {
	return o
}

func (o ZonePlanPtrOutput) Elem() ZonePlanOutput {
	return o.ApplyT(func(v *ZonePlan) ZonePlan {
		if v != nil {
			return *v
		}
		var ret ZonePlan
		return ret
	}).(ZonePlanOutput)
}

// Catalog name
func (o ZonePlanPtrOutput) CatalogName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ZonePlan) *string {
		if v == nil {
			return nil
		}
		return v.CatalogName
	}).(pulumi.StringPtrOutput)
}

// Representation of a configuration item for personalizing product
func (o ZonePlanPtrOutput) Configurations() ZonePlanConfigurationArrayOutput {
	return o.ApplyT(func(v *ZonePlan) []ZonePlanConfiguration {
		if v == nil {
			return nil
		}
		return v.Configurations
	}).(ZonePlanConfigurationArrayOutput)
}

// duration
func (o ZonePlanPtrOutput) Duration() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ZonePlan) *string {
		if v == nil {
			return nil
		}
		return &v.Duration
	}).(pulumi.StringPtrOutput)
}

// Plan code
func (o ZonePlanPtrOutput) PlanCode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ZonePlan) *string {
		if v == nil {
			return nil
		}
		return &v.PlanCode
	}).(pulumi.StringPtrOutput)
}

// Pricing model identifier
func (o ZonePlanPtrOutput) PricingMode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ZonePlan) *string {
		if v == nil {
			return nil
		}
		return &v.PricingMode
	}).(pulumi.StringPtrOutput)
}

type ZonePlanConfiguration struct {
	// Identifier of the resource
	Label string `pulumi:"label"`
	// Path to the resource in API.OVH.COM
	Value string `pulumi:"value"`
}

// ZonePlanConfigurationInput is an input type that accepts ZonePlanConfigurationArgs and ZonePlanConfigurationOutput values.
// You can construct a concrete instance of `ZonePlanConfigurationInput` via:
//
//	ZonePlanConfigurationArgs{...}
type ZonePlanConfigurationInput interface {
	pulumi.Input

	ToZonePlanConfigurationOutput() ZonePlanConfigurationOutput
	ToZonePlanConfigurationOutputWithContext(context.Context) ZonePlanConfigurationOutput
}

type ZonePlanConfigurationArgs struct {
	// Identifier of the resource
	Label pulumi.StringInput `pulumi:"label"`
	// Path to the resource in API.OVH.COM
	Value pulumi.StringInput `pulumi:"value"`
}

func (ZonePlanConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ZonePlanConfiguration)(nil)).Elem()
}

func (i ZonePlanConfigurationArgs) ToZonePlanConfigurationOutput() ZonePlanConfigurationOutput {
	return i.ToZonePlanConfigurationOutputWithContext(context.Background())
}

func (i ZonePlanConfigurationArgs) ToZonePlanConfigurationOutputWithContext(ctx context.Context) ZonePlanConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZonePlanConfigurationOutput)
}

// ZonePlanConfigurationArrayInput is an input type that accepts ZonePlanConfigurationArray and ZonePlanConfigurationArrayOutput values.
// You can construct a concrete instance of `ZonePlanConfigurationArrayInput` via:
//
//	ZonePlanConfigurationArray{ ZonePlanConfigurationArgs{...} }
type ZonePlanConfigurationArrayInput interface {
	pulumi.Input

	ToZonePlanConfigurationArrayOutput() ZonePlanConfigurationArrayOutput
	ToZonePlanConfigurationArrayOutputWithContext(context.Context) ZonePlanConfigurationArrayOutput
}

type ZonePlanConfigurationArray []ZonePlanConfigurationInput

func (ZonePlanConfigurationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ZonePlanConfiguration)(nil)).Elem()
}

func (i ZonePlanConfigurationArray) ToZonePlanConfigurationArrayOutput() ZonePlanConfigurationArrayOutput {
	return i.ToZonePlanConfigurationArrayOutputWithContext(context.Background())
}

func (i ZonePlanConfigurationArray) ToZonePlanConfigurationArrayOutputWithContext(ctx context.Context) ZonePlanConfigurationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZonePlanConfigurationArrayOutput)
}

type ZonePlanConfigurationOutput struct{ *pulumi.OutputState }

func (ZonePlanConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ZonePlanConfiguration)(nil)).Elem()
}

func (o ZonePlanConfigurationOutput) ToZonePlanConfigurationOutput() ZonePlanConfigurationOutput {
	return o
}

func (o ZonePlanConfigurationOutput) ToZonePlanConfigurationOutputWithContext(ctx context.Context) ZonePlanConfigurationOutput {
	return o
}

// Identifier of the resource
func (o ZonePlanConfigurationOutput) Label() pulumi.StringOutput {
	return o.ApplyT(func(v ZonePlanConfiguration) string { return v.Label }).(pulumi.StringOutput)
}

// Path to the resource in API.OVH.COM
func (o ZonePlanConfigurationOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v ZonePlanConfiguration) string { return v.Value }).(pulumi.StringOutput)
}

type ZonePlanConfigurationArrayOutput struct{ *pulumi.OutputState }

func (ZonePlanConfigurationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ZonePlanConfiguration)(nil)).Elem()
}

func (o ZonePlanConfigurationArrayOutput) ToZonePlanConfigurationArrayOutput() ZonePlanConfigurationArrayOutput {
	return o
}

func (o ZonePlanConfigurationArrayOutput) ToZonePlanConfigurationArrayOutputWithContext(ctx context.Context) ZonePlanConfigurationArrayOutput {
	return o
}

func (o ZonePlanConfigurationArrayOutput) Index(i pulumi.IntInput) ZonePlanConfigurationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ZonePlanConfiguration {
		return vs[0].([]ZonePlanConfiguration)[vs[1].(int)]
	}).(ZonePlanConfigurationOutput)
}

type ZonePlanOption struct {
	// Catalog name
	CatalogName *string `pulumi:"catalogName"`
	// Representation of a configuration item for personalizing product
	Configurations []ZonePlanOptionConfiguration `pulumi:"configurations"`
	// duration
	Duration string `pulumi:"duration"`
	// Plan code
	PlanCode string `pulumi:"planCode"`
	// Pricing model identifier
	PricingMode string `pulumi:"pricingMode"`
}

// ZonePlanOptionInput is an input type that accepts ZonePlanOptionArgs and ZonePlanOptionOutput values.
// You can construct a concrete instance of `ZonePlanOptionInput` via:
//
//	ZonePlanOptionArgs{...}
type ZonePlanOptionInput interface {
	pulumi.Input

	ToZonePlanOptionOutput() ZonePlanOptionOutput
	ToZonePlanOptionOutputWithContext(context.Context) ZonePlanOptionOutput
}

type ZonePlanOptionArgs struct {
	// Catalog name
	CatalogName pulumi.StringPtrInput `pulumi:"catalogName"`
	// Representation of a configuration item for personalizing product
	Configurations ZonePlanOptionConfigurationArrayInput `pulumi:"configurations"`
	// duration
	Duration pulumi.StringInput `pulumi:"duration"`
	// Plan code
	PlanCode pulumi.StringInput `pulumi:"planCode"`
	// Pricing model identifier
	PricingMode pulumi.StringInput `pulumi:"pricingMode"`
}

func (ZonePlanOptionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ZonePlanOption)(nil)).Elem()
}

func (i ZonePlanOptionArgs) ToZonePlanOptionOutput() ZonePlanOptionOutput {
	return i.ToZonePlanOptionOutputWithContext(context.Background())
}

func (i ZonePlanOptionArgs) ToZonePlanOptionOutputWithContext(ctx context.Context) ZonePlanOptionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZonePlanOptionOutput)
}

// ZonePlanOptionArrayInput is an input type that accepts ZonePlanOptionArray and ZonePlanOptionArrayOutput values.
// You can construct a concrete instance of `ZonePlanOptionArrayInput` via:
//
//	ZonePlanOptionArray{ ZonePlanOptionArgs{...} }
type ZonePlanOptionArrayInput interface {
	pulumi.Input

	ToZonePlanOptionArrayOutput() ZonePlanOptionArrayOutput
	ToZonePlanOptionArrayOutputWithContext(context.Context) ZonePlanOptionArrayOutput
}

type ZonePlanOptionArray []ZonePlanOptionInput

func (ZonePlanOptionArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ZonePlanOption)(nil)).Elem()
}

func (i ZonePlanOptionArray) ToZonePlanOptionArrayOutput() ZonePlanOptionArrayOutput {
	return i.ToZonePlanOptionArrayOutputWithContext(context.Background())
}

func (i ZonePlanOptionArray) ToZonePlanOptionArrayOutputWithContext(ctx context.Context) ZonePlanOptionArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZonePlanOptionArrayOutput)
}

type ZonePlanOptionOutput struct{ *pulumi.OutputState }

func (ZonePlanOptionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ZonePlanOption)(nil)).Elem()
}

func (o ZonePlanOptionOutput) ToZonePlanOptionOutput() ZonePlanOptionOutput {
	return o
}

func (o ZonePlanOptionOutput) ToZonePlanOptionOutputWithContext(ctx context.Context) ZonePlanOptionOutput {
	return o
}

// Catalog name
func (o ZonePlanOptionOutput) CatalogName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ZonePlanOption) *string { return v.CatalogName }).(pulumi.StringPtrOutput)
}

// Representation of a configuration item for personalizing product
func (o ZonePlanOptionOutput) Configurations() ZonePlanOptionConfigurationArrayOutput {
	return o.ApplyT(func(v ZonePlanOption) []ZonePlanOptionConfiguration { return v.Configurations }).(ZonePlanOptionConfigurationArrayOutput)
}

// duration
func (o ZonePlanOptionOutput) Duration() pulumi.StringOutput {
	return o.ApplyT(func(v ZonePlanOption) string { return v.Duration }).(pulumi.StringOutput)
}

// Plan code
func (o ZonePlanOptionOutput) PlanCode() pulumi.StringOutput {
	return o.ApplyT(func(v ZonePlanOption) string { return v.PlanCode }).(pulumi.StringOutput)
}

// Pricing model identifier
func (o ZonePlanOptionOutput) PricingMode() pulumi.StringOutput {
	return o.ApplyT(func(v ZonePlanOption) string { return v.PricingMode }).(pulumi.StringOutput)
}

type ZonePlanOptionArrayOutput struct{ *pulumi.OutputState }

func (ZonePlanOptionArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ZonePlanOption)(nil)).Elem()
}

func (o ZonePlanOptionArrayOutput) ToZonePlanOptionArrayOutput() ZonePlanOptionArrayOutput {
	return o
}

func (o ZonePlanOptionArrayOutput) ToZonePlanOptionArrayOutputWithContext(ctx context.Context) ZonePlanOptionArrayOutput {
	return o
}

func (o ZonePlanOptionArrayOutput) Index(i pulumi.IntInput) ZonePlanOptionOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ZonePlanOption {
		return vs[0].([]ZonePlanOption)[vs[1].(int)]
	}).(ZonePlanOptionOutput)
}

type ZonePlanOptionConfiguration struct {
	// Identifier of the resource
	Label string `pulumi:"label"`
	// Path to the resource in API.OVH.COM
	Value string `pulumi:"value"`
}

// ZonePlanOptionConfigurationInput is an input type that accepts ZonePlanOptionConfigurationArgs and ZonePlanOptionConfigurationOutput values.
// You can construct a concrete instance of `ZonePlanOptionConfigurationInput` via:
//
//	ZonePlanOptionConfigurationArgs{...}
type ZonePlanOptionConfigurationInput interface {
	pulumi.Input

	ToZonePlanOptionConfigurationOutput() ZonePlanOptionConfigurationOutput
	ToZonePlanOptionConfigurationOutputWithContext(context.Context) ZonePlanOptionConfigurationOutput
}

type ZonePlanOptionConfigurationArgs struct {
	// Identifier of the resource
	Label pulumi.StringInput `pulumi:"label"`
	// Path to the resource in API.OVH.COM
	Value pulumi.StringInput `pulumi:"value"`
}

func (ZonePlanOptionConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ZonePlanOptionConfiguration)(nil)).Elem()
}

func (i ZonePlanOptionConfigurationArgs) ToZonePlanOptionConfigurationOutput() ZonePlanOptionConfigurationOutput {
	return i.ToZonePlanOptionConfigurationOutputWithContext(context.Background())
}

func (i ZonePlanOptionConfigurationArgs) ToZonePlanOptionConfigurationOutputWithContext(ctx context.Context) ZonePlanOptionConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZonePlanOptionConfigurationOutput)
}

// ZonePlanOptionConfigurationArrayInput is an input type that accepts ZonePlanOptionConfigurationArray and ZonePlanOptionConfigurationArrayOutput values.
// You can construct a concrete instance of `ZonePlanOptionConfigurationArrayInput` via:
//
//	ZonePlanOptionConfigurationArray{ ZonePlanOptionConfigurationArgs{...} }
type ZonePlanOptionConfigurationArrayInput interface {
	pulumi.Input

	ToZonePlanOptionConfigurationArrayOutput() ZonePlanOptionConfigurationArrayOutput
	ToZonePlanOptionConfigurationArrayOutputWithContext(context.Context) ZonePlanOptionConfigurationArrayOutput
}

type ZonePlanOptionConfigurationArray []ZonePlanOptionConfigurationInput

func (ZonePlanOptionConfigurationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ZonePlanOptionConfiguration)(nil)).Elem()
}

func (i ZonePlanOptionConfigurationArray) ToZonePlanOptionConfigurationArrayOutput() ZonePlanOptionConfigurationArrayOutput {
	return i.ToZonePlanOptionConfigurationArrayOutputWithContext(context.Background())
}

func (i ZonePlanOptionConfigurationArray) ToZonePlanOptionConfigurationArrayOutputWithContext(ctx context.Context) ZonePlanOptionConfigurationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZonePlanOptionConfigurationArrayOutput)
}

type ZonePlanOptionConfigurationOutput struct{ *pulumi.OutputState }

func (ZonePlanOptionConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ZonePlanOptionConfiguration)(nil)).Elem()
}

func (o ZonePlanOptionConfigurationOutput) ToZonePlanOptionConfigurationOutput() ZonePlanOptionConfigurationOutput {
	return o
}

func (o ZonePlanOptionConfigurationOutput) ToZonePlanOptionConfigurationOutputWithContext(ctx context.Context) ZonePlanOptionConfigurationOutput {
	return o
}

// Identifier of the resource
func (o ZonePlanOptionConfigurationOutput) Label() pulumi.StringOutput {
	return o.ApplyT(func(v ZonePlanOptionConfiguration) string { return v.Label }).(pulumi.StringOutput)
}

// Path to the resource in API.OVH.COM
func (o ZonePlanOptionConfigurationOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v ZonePlanOptionConfiguration) string { return v.Value }).(pulumi.StringOutput)
}

type ZonePlanOptionConfigurationArrayOutput struct{ *pulumi.OutputState }

func (ZonePlanOptionConfigurationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ZonePlanOptionConfiguration)(nil)).Elem()
}

func (o ZonePlanOptionConfigurationArrayOutput) ToZonePlanOptionConfigurationArrayOutput() ZonePlanOptionConfigurationArrayOutput {
	return o
}

func (o ZonePlanOptionConfigurationArrayOutput) ToZonePlanOptionConfigurationArrayOutputWithContext(ctx context.Context) ZonePlanOptionConfigurationArrayOutput {
	return o
}

func (o ZonePlanOptionConfigurationArrayOutput) Index(i pulumi.IntInput) ZonePlanOptionConfigurationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ZonePlanOptionConfiguration {
		return vs[0].([]ZonePlanOptionConfiguration)[vs[1].(int)]
	}).(ZonePlanOptionConfigurationOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ZoneOrderInput)(nil)).Elem(), ZoneOrderArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZoneOrderArrayInput)(nil)).Elem(), ZoneOrderArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZoneOrderDetailInput)(nil)).Elem(), ZoneOrderDetailArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZoneOrderDetailArrayInput)(nil)).Elem(), ZoneOrderDetailArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZonePlanInput)(nil)).Elem(), ZonePlanArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZonePlanPtrInput)(nil)).Elem(), ZonePlanArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZonePlanConfigurationInput)(nil)).Elem(), ZonePlanConfigurationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZonePlanConfigurationArrayInput)(nil)).Elem(), ZonePlanConfigurationArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZonePlanOptionInput)(nil)).Elem(), ZonePlanOptionArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZonePlanOptionArrayInput)(nil)).Elem(), ZonePlanOptionArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZonePlanOptionConfigurationInput)(nil)).Elem(), ZonePlanOptionConfigurationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZonePlanOptionConfigurationArrayInput)(nil)).Elem(), ZonePlanOptionConfigurationArray{})
	pulumi.RegisterOutputType(ZoneOrderOutput{})
	pulumi.RegisterOutputType(ZoneOrderArrayOutput{})
	pulumi.RegisterOutputType(ZoneOrderDetailOutput{})
	pulumi.RegisterOutputType(ZoneOrderDetailArrayOutput{})
	pulumi.RegisterOutputType(ZonePlanOutput{})
	pulumi.RegisterOutputType(ZonePlanPtrOutput{})
	pulumi.RegisterOutputType(ZonePlanConfigurationOutput{})
	pulumi.RegisterOutputType(ZonePlanConfigurationArrayOutput{})
	pulumi.RegisterOutputType(ZonePlanOptionOutput{})
	pulumi.RegisterOutputType(ZonePlanOptionArrayOutput{})
	pulumi.RegisterOutputType(ZonePlanOptionConfigurationOutput{})
	pulumi.RegisterOutputType(ZonePlanOptionConfigurationArrayOutput{})
}
