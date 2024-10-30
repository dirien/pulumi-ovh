// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package order

import (
	"context"
	"reflect"

	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to retrieve information of order cart product plan.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/ovh/pulumi-ovh/sdk/go/ovh/Me"
//	"github.com/ovh/pulumi-ovh/sdk/go/ovh/Order"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			myaccount, err := Me.GetMe(ctx, map[string]interface{}{}, nil)
//			if err != nil {
//				return err
//			}
//			mycart, err := Order.GetCart(ctx, &order.GetCartArgs{
//				OvhSubsidiary: myaccount.OvhSubsidiary,
//			}, nil)
//			if err != nil {
//				return err
//			}
//			_, err = Order.GetCartProductPlan(ctx, &order.GetCartProductPlanArgs{
//				CartId:        mycart.Id,
//				PriceCapacity: "renew",
//				Product:       "cloud",
//				PlanCode:      "project",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetCartProductPlan(ctx *pulumi.Context, args *GetCartProductPlanArgs, opts ...pulumi.InvokeOption) (*GetCartProductPlanResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetCartProductPlanResult
	err := ctx.Invoke("ovh:Order/getCartProductPlan:getCartProductPlan", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getCartProductPlan.
type GetCartProductPlanArgs struct {
	// Cart identifier
	CartId string `pulumi:"cartId"`
	// Catalog name
	CatalogName *string `pulumi:"catalogName"`
	// Product offer identifier
	PlanCode string `pulumi:"planCode"`
	// Capacity of the pricing (type of pricing)
	PriceCapacity string `pulumi:"priceCapacity"`
	// Product
	Product string `pulumi:"product"`
}

// A collection of values returned by getCartProductPlan.
type GetCartProductPlanResult struct {
	CartId      string  `pulumi:"cartId"`
	CatalogName *string `pulumi:"catalogName"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Product offer identifier
	PlanCode      string `pulumi:"planCode"`
	PriceCapacity string `pulumi:"priceCapacity"`
	// Prices of the product offer
	Prices  []GetCartProductPlanPrice `pulumi:"prices"`
	Product string                    `pulumi:"product"`
	// Name of the product
	ProductName string `pulumi:"productName"`
	// Product type
	ProductType string `pulumi:"productType"`
	// Selected Price according to capacity
	SelectedPrices []GetCartProductPlanSelectedPrice `pulumi:"selectedPrices"`
}

func GetCartProductPlanOutput(ctx *pulumi.Context, args GetCartProductPlanOutputArgs, opts ...pulumi.InvokeOption) GetCartProductPlanResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetCartProductPlanResultOutput, error) {
			args := v.(GetCartProductPlanArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv GetCartProductPlanResult
			secret, err := ctx.InvokePackageRaw("ovh:Order/getCartProductPlan:getCartProductPlan", args, &rv, "", opts...)
			if err != nil {
				return GetCartProductPlanResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(GetCartProductPlanResultOutput)
			if secret {
				return pulumi.ToSecret(output).(GetCartProductPlanResultOutput), nil
			}
			return output, nil
		}).(GetCartProductPlanResultOutput)
}

// A collection of arguments for invoking getCartProductPlan.
type GetCartProductPlanOutputArgs struct {
	// Cart identifier
	CartId pulumi.StringInput `pulumi:"cartId"`
	// Catalog name
	CatalogName pulumi.StringPtrInput `pulumi:"catalogName"`
	// Product offer identifier
	PlanCode pulumi.StringInput `pulumi:"planCode"`
	// Capacity of the pricing (type of pricing)
	PriceCapacity pulumi.StringInput `pulumi:"priceCapacity"`
	// Product
	Product pulumi.StringInput `pulumi:"product"`
}

func (GetCartProductPlanOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetCartProductPlanArgs)(nil)).Elem()
}

// A collection of values returned by getCartProductPlan.
type GetCartProductPlanResultOutput struct{ *pulumi.OutputState }

func (GetCartProductPlanResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetCartProductPlanResult)(nil)).Elem()
}

func (o GetCartProductPlanResultOutput) ToGetCartProductPlanResultOutput() GetCartProductPlanResultOutput {
	return o
}

func (o GetCartProductPlanResultOutput) ToGetCartProductPlanResultOutputWithContext(ctx context.Context) GetCartProductPlanResultOutput {
	return o
}

func (o GetCartProductPlanResultOutput) CartId() pulumi.StringOutput {
	return o.ApplyT(func(v GetCartProductPlanResult) string { return v.CartId }).(pulumi.StringOutput)
}

func (o GetCartProductPlanResultOutput) CatalogName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetCartProductPlanResult) *string { return v.CatalogName }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetCartProductPlanResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetCartProductPlanResult) string { return v.Id }).(pulumi.StringOutput)
}

// Product offer identifier
func (o GetCartProductPlanResultOutput) PlanCode() pulumi.StringOutput {
	return o.ApplyT(func(v GetCartProductPlanResult) string { return v.PlanCode }).(pulumi.StringOutput)
}

func (o GetCartProductPlanResultOutput) PriceCapacity() pulumi.StringOutput {
	return o.ApplyT(func(v GetCartProductPlanResult) string { return v.PriceCapacity }).(pulumi.StringOutput)
}

// Prices of the product offer
func (o GetCartProductPlanResultOutput) Prices() GetCartProductPlanPriceArrayOutput {
	return o.ApplyT(func(v GetCartProductPlanResult) []GetCartProductPlanPrice { return v.Prices }).(GetCartProductPlanPriceArrayOutput)
}

func (o GetCartProductPlanResultOutput) Product() pulumi.StringOutput {
	return o.ApplyT(func(v GetCartProductPlanResult) string { return v.Product }).(pulumi.StringOutput)
}

// Name of the product
func (o GetCartProductPlanResultOutput) ProductName() pulumi.StringOutput {
	return o.ApplyT(func(v GetCartProductPlanResult) string { return v.ProductName }).(pulumi.StringOutput)
}

// Product type
func (o GetCartProductPlanResultOutput) ProductType() pulumi.StringOutput {
	return o.ApplyT(func(v GetCartProductPlanResult) string { return v.ProductType }).(pulumi.StringOutput)
}

// Selected Price according to capacity
func (o GetCartProductPlanResultOutput) SelectedPrices() GetCartProductPlanSelectedPriceArrayOutput {
	return o.ApplyT(func(v GetCartProductPlanResult) []GetCartProductPlanSelectedPrice { return v.SelectedPrices }).(GetCartProductPlanSelectedPriceArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetCartProductPlanResultOutput{})
}
