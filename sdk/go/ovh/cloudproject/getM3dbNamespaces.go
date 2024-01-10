// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudproject

import (
	"context"
	"reflect"

	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to get the list of namespaces of a M3DB cluster associated with a public cloud project.
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
//			namespaces, err := CloudProject.GetM3dbNamespaces(ctx, &cloudproject.GetM3dbNamespacesArgs{
//				ServiceName: "XXX",
//				ClusterId:   "YYY",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			ctx.Export("namespaceIds", namespaces.NamespaceIds)
//			return nil
//		})
//	}
//
// ```
func GetM3dbNamespaces(ctx *pulumi.Context, args *GetM3dbNamespacesArgs, opts ...pulumi.InvokeOption) (*GetM3dbNamespacesResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetM3dbNamespacesResult
	err := ctx.Invoke("ovh:CloudProject/getM3dbNamespaces:getM3dbNamespaces", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getM3dbNamespaces.
type GetM3dbNamespacesArgs struct {
	// Cluster ID
	ClusterId string `pulumi:"clusterId"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName string `pulumi:"serviceName"`
}

// A collection of values returned by getM3dbNamespaces.
type GetM3dbNamespacesResult struct {
	// See Argument Reference above.
	ClusterId string `pulumi:"clusterId"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The list of namespaces ids of the M3DB cluster associated with the project.
	NamespaceIds []string `pulumi:"namespaceIds"`
	// See Argument Reference above.
	ServiceName string `pulumi:"serviceName"`
}

func GetM3dbNamespacesOutput(ctx *pulumi.Context, args GetM3dbNamespacesOutputArgs, opts ...pulumi.InvokeOption) GetM3dbNamespacesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetM3dbNamespacesResult, error) {
			args := v.(GetM3dbNamespacesArgs)
			r, err := GetM3dbNamespaces(ctx, &args, opts...)
			var s GetM3dbNamespacesResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetM3dbNamespacesResultOutput)
}

// A collection of arguments for invoking getM3dbNamespaces.
type GetM3dbNamespacesOutputArgs struct {
	// Cluster ID
	ClusterId pulumi.StringInput `pulumi:"clusterId"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName pulumi.StringInput `pulumi:"serviceName"`
}

func (GetM3dbNamespacesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetM3dbNamespacesArgs)(nil)).Elem()
}

// A collection of values returned by getM3dbNamespaces.
type GetM3dbNamespacesResultOutput struct{ *pulumi.OutputState }

func (GetM3dbNamespacesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetM3dbNamespacesResult)(nil)).Elem()
}

func (o GetM3dbNamespacesResultOutput) ToGetM3dbNamespacesResultOutput() GetM3dbNamespacesResultOutput {
	return o
}

func (o GetM3dbNamespacesResultOutput) ToGetM3dbNamespacesResultOutputWithContext(ctx context.Context) GetM3dbNamespacesResultOutput {
	return o
}

// See Argument Reference above.
func (o GetM3dbNamespacesResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v GetM3dbNamespacesResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetM3dbNamespacesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetM3dbNamespacesResult) string { return v.Id }).(pulumi.StringOutput)
}

// The list of namespaces ids of the M3DB cluster associated with the project.
func (o GetM3dbNamespacesResultOutput) NamespaceIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetM3dbNamespacesResult) []string { return v.NamespaceIds }).(pulumi.StringArrayOutput)
}

// See Argument Reference above.
func (o GetM3dbNamespacesResultOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v GetM3dbNamespacesResult) string { return v.ServiceName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetM3dbNamespacesResultOutput{})
}
