// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudproject

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to retrieve the list of all the S3 accessKeyId associated with a public cloud project's user.
//
// ## Example Usage
func GetUserS3Credentials(ctx *pulumi.Context, args *GetUserS3CredentialsArgs, opts ...pulumi.InvokeOption) (*GetUserS3CredentialsResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv GetUserS3CredentialsResult
	err := ctx.Invoke("ovh:CloudProject/getUserS3Credentials:getUserS3Credentials", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getUserS3Credentials.
type GetUserS3CredentialsArgs struct {
	// The ID of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName string `pulumi:"serviceName"`
	// The ID of a public cloud project's user.
	UserId string `pulumi:"userId"`
}

// A collection of values returned by getUserS3Credentials.
type GetUserS3CredentialsResult struct {
	// The list of the Access Key ID associated with this user.
	AccessKeyIds []string `pulumi:"accessKeyIds"`
	// The provider-assigned unique ID for this managed resource.
	Id          string `pulumi:"id"`
	ServiceName string `pulumi:"serviceName"`
	UserId      string `pulumi:"userId"`
}

func GetUserS3CredentialsOutput(ctx *pulumi.Context, args GetUserS3CredentialsOutputArgs, opts ...pulumi.InvokeOption) GetUserS3CredentialsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetUserS3CredentialsResult, error) {
			args := v.(GetUserS3CredentialsArgs)
			r, err := GetUserS3Credentials(ctx, &args, opts...)
			var s GetUserS3CredentialsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetUserS3CredentialsResultOutput)
}

// A collection of arguments for invoking getUserS3Credentials.
type GetUserS3CredentialsOutputArgs struct {
	// The ID of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName pulumi.StringInput `pulumi:"serviceName"`
	// The ID of a public cloud project's user.
	UserId pulumi.StringInput `pulumi:"userId"`
}

func (GetUserS3CredentialsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetUserS3CredentialsArgs)(nil)).Elem()
}

// A collection of values returned by getUserS3Credentials.
type GetUserS3CredentialsResultOutput struct{ *pulumi.OutputState }

func (GetUserS3CredentialsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetUserS3CredentialsResult)(nil)).Elem()
}

func (o GetUserS3CredentialsResultOutput) ToGetUserS3CredentialsResultOutput() GetUserS3CredentialsResultOutput {
	return o
}

func (o GetUserS3CredentialsResultOutput) ToGetUserS3CredentialsResultOutputWithContext(ctx context.Context) GetUserS3CredentialsResultOutput {
	return o
}

// The list of the Access Key ID associated with this user.
func (o GetUserS3CredentialsResultOutput) AccessKeyIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetUserS3CredentialsResult) []string { return v.AccessKeyIds }).(pulumi.StringArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetUserS3CredentialsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetUserS3CredentialsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetUserS3CredentialsResultOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v GetUserS3CredentialsResult) string { return v.ServiceName }).(pulumi.StringOutput)
}

func (o GetUserS3CredentialsResultOutput) UserId() pulumi.StringOutput {
	return o.ApplyT(func(v GetUserS3CredentialsResult) string { return v.UserId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetUserS3CredentialsResultOutput{})
}
