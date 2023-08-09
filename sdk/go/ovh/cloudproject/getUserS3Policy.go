// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudproject

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get the S3 Policy of a public cloud project user. The policy can be set by using the `CloudProject.S3Policy` resource.
//
// ## Example Usage
func GetUserS3Policy(ctx *pulumi.Context, args *GetUserS3PolicyArgs, opts ...pulumi.InvokeOption) (*GetUserS3PolicyResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv GetUserS3PolicyResult
	err := ctx.Invoke("ovh:CloudProject/getUserS3Policy:getUserS3Policy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getUserS3Policy.
type GetUserS3PolicyArgs struct {
	// The ID of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName string `pulumi:"serviceName"`
	// The ID of a public cloud project's user.
	UserId string `pulumi:"userId"`
}

// A collection of values returned by getUserS3Policy.
type GetUserS3PolicyResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// (Required) The policy document. This is a JSON formatted string.
	Policy      string `pulumi:"policy"`
	ServiceName string `pulumi:"serviceName"`
	UserId      string `pulumi:"userId"`
}

func GetUserS3PolicyOutput(ctx *pulumi.Context, args GetUserS3PolicyOutputArgs, opts ...pulumi.InvokeOption) GetUserS3PolicyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetUserS3PolicyResult, error) {
			args := v.(GetUserS3PolicyArgs)
			r, err := GetUserS3Policy(ctx, &args, opts...)
			var s GetUserS3PolicyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetUserS3PolicyResultOutput)
}

// A collection of arguments for invoking getUserS3Policy.
type GetUserS3PolicyOutputArgs struct {
	// The ID of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName pulumi.StringInput `pulumi:"serviceName"`
	// The ID of a public cloud project's user.
	UserId pulumi.StringInput `pulumi:"userId"`
}

func (GetUserS3PolicyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetUserS3PolicyArgs)(nil)).Elem()
}

// A collection of values returned by getUserS3Policy.
type GetUserS3PolicyResultOutput struct{ *pulumi.OutputState }

func (GetUserS3PolicyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetUserS3PolicyResult)(nil)).Elem()
}

func (o GetUserS3PolicyResultOutput) ToGetUserS3PolicyResultOutput() GetUserS3PolicyResultOutput {
	return o
}

func (o GetUserS3PolicyResultOutput) ToGetUserS3PolicyResultOutputWithContext(ctx context.Context) GetUserS3PolicyResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetUserS3PolicyResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetUserS3PolicyResult) string { return v.Id }).(pulumi.StringOutput)
}

// (Required) The policy document. This is a JSON formatted string.
func (o GetUserS3PolicyResultOutput) Policy() pulumi.StringOutput {
	return o.ApplyT(func(v GetUserS3PolicyResult) string { return v.Policy }).(pulumi.StringOutput)
}

func (o GetUserS3PolicyResultOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v GetUserS3PolicyResult) string { return v.ServiceName }).(pulumi.StringOutput)
}

func (o GetUserS3PolicyResultOutput) UserId() pulumi.StringOutput {
	return o.ApplyT(func(v GetUserS3PolicyResult) string { return v.UserId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetUserS3PolicyResultOutput{})
}
