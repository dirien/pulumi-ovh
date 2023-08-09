// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudprojectdatabase

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to get information about a user of a postgresql cluster associated with a public cloud project.
//
// ## Example Usage
func LookupPostgresSqlUser(ctx *pulumi.Context, args *LookupPostgresSqlUserArgs, opts ...pulumi.InvokeOption) (*LookupPostgresSqlUserResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupPostgresSqlUserResult
	err := ctx.Invoke("ovh:CloudProjectDatabase/getPostgresSqlUser:getPostgresSqlUser", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPostgresSqlUser.
type LookupPostgresSqlUserArgs struct {
	// Cluster ID
	ClusterId string `pulumi:"clusterId"`
	// Name of the user.
	Name string `pulumi:"name"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName string `pulumi:"serviceName"`
}

// A collection of values returned by getPostgresSqlUser.
type LookupPostgresSqlUserResult struct {
	// See Argument Reference above.
	ClusterId string `pulumi:"clusterId"`
	// Date of the creation of the user.
	CreatedAt string `pulumi:"createdAt"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Name of the user.
	Name string `pulumi:"name"`
	// Roles the user belongs to.
	Roles []string `pulumi:"roles"`
	// Current status of the user.
	ServiceName string `pulumi:"serviceName"`
	// Current status of the user.
	Status string `pulumi:"status"`
}

func LookupPostgresSqlUserOutput(ctx *pulumi.Context, args LookupPostgresSqlUserOutputArgs, opts ...pulumi.InvokeOption) LookupPostgresSqlUserResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupPostgresSqlUserResult, error) {
			args := v.(LookupPostgresSqlUserArgs)
			r, err := LookupPostgresSqlUser(ctx, &args, opts...)
			var s LookupPostgresSqlUserResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupPostgresSqlUserResultOutput)
}

// A collection of arguments for invoking getPostgresSqlUser.
type LookupPostgresSqlUserOutputArgs struct {
	// Cluster ID
	ClusterId pulumi.StringInput `pulumi:"clusterId"`
	// Name of the user.
	Name pulumi.StringInput `pulumi:"name"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName pulumi.StringInput `pulumi:"serviceName"`
}

func (LookupPostgresSqlUserOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPostgresSqlUserArgs)(nil)).Elem()
}

// A collection of values returned by getPostgresSqlUser.
type LookupPostgresSqlUserResultOutput struct{ *pulumi.OutputState }

func (LookupPostgresSqlUserResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPostgresSqlUserResult)(nil)).Elem()
}

func (o LookupPostgresSqlUserResultOutput) ToLookupPostgresSqlUserResultOutput() LookupPostgresSqlUserResultOutput {
	return o
}

func (o LookupPostgresSqlUserResultOutput) ToLookupPostgresSqlUserResultOutputWithContext(ctx context.Context) LookupPostgresSqlUserResultOutput {
	return o
}

// See Argument Reference above.
func (o LookupPostgresSqlUserResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPostgresSqlUserResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

// Date of the creation of the user.
func (o LookupPostgresSqlUserResultOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPostgresSqlUserResult) string { return v.CreatedAt }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupPostgresSqlUserResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPostgresSqlUserResult) string { return v.Id }).(pulumi.StringOutput)
}

// Name of the user.
func (o LookupPostgresSqlUserResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPostgresSqlUserResult) string { return v.Name }).(pulumi.StringOutput)
}

// Roles the user belongs to.
func (o LookupPostgresSqlUserResultOutput) Roles() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupPostgresSqlUserResult) []string { return v.Roles }).(pulumi.StringArrayOutput)
}

// Current status of the user.
func (o LookupPostgresSqlUserResultOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPostgresSqlUserResult) string { return v.ServiceName }).(pulumi.StringOutput)
}

// Current status of the user.
func (o LookupPostgresSqlUserResultOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPostgresSqlUserResult) string { return v.Status }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPostgresSqlUserResultOutput{})
}
