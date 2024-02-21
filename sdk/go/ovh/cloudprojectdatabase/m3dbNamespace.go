// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudprojectdatabase

import (
	"context"
	"reflect"

	"errors"
	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a namespace for a M3DB cluster associated with a public cloud project.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/ovh/pulumi-ovh/sdk/go/ovh/CloudProjectDatabase"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			m3db, err := CloudProjectDatabase.GetDatabase(ctx, &cloudprojectdatabase.GetDatabaseArgs{
//				ServiceName: "XXX",
//				Engine:      "m3db",
//				Id:          "ZZZ",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			_, err = CloudProjectDatabase.NewM3DbNamespace(ctx, "namespace", &CloudProjectDatabase.M3DbNamespaceArgs{
//				ServiceName:             *pulumi.String(m3db.ServiceName),
//				ClusterId:               *pulumi.String(m3db.Id),
//				Resolution:              pulumi.String("P2D"),
//				RetentionPeriodDuration: pulumi.String("PT48H"),
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
// OVHcloud Managed M3DB clusters namespaces can be imported using the `service_name`, `cluster_id` and `id` of the namespace, separated by "/" E.g.,
//
//	bash
//
// ```sh
// $ pulumi import ovh:CloudProjectDatabase/m3DbNamespace:M3DbNamespace my_namespace service_name/cluster_id/id
// ```
type M3DbNamespace struct {
	pulumi.CustomResourceState

	// Cluster ID.
	ClusterId pulumi.StringOutput `pulumi:"clusterId"`
	// Name of the namespace.
	Name pulumi.StringOutput `pulumi:"name"`
	// Resolution for an aggregated namespace. Should follow Rfc3339 e.g P2D, PT48H.
	Resolution pulumi.StringOutput `pulumi:"resolution"`
	// Controls how long we wait before expiring stale data. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBlockDataExpirationDuration pulumi.StringPtrOutput `pulumi:"retentionBlockDataExpirationDuration"`
	// Controls how long to keep a block in memory before flushing to a fileset on disk. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBlockSizeDuration pulumi.StringOutput `pulumi:"retentionBlockSizeDuration"`
	// Controls how far into the future writes to the namespace will be accepted. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBufferFutureDuration pulumi.StringPtrOutput `pulumi:"retentionBufferFutureDuration"`
	// Controls how far into the past writes to the namespace will be accepted. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBufferPastDuration pulumi.StringPtrOutput `pulumi:"retentionBufferPastDuration"`
	// Controls the duration of time that M3DB will retain data for the namespace. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionPeriodDuration pulumi.StringOutput `pulumi:"retentionPeriodDuration"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName pulumi.StringOutput `pulumi:"serviceName"`
	// Defines whether M3DB will create snapshot files for this namespace.
	SnapshotEnabled pulumi.BoolPtrOutput `pulumi:"snapshotEnabled"`
	// Type of namespace.
	Type pulumi.StringOutput `pulumi:"type"`
	// Defines whether M3DB will include writes to this namespace in the commit log.
	WritesToCommitLogEnabled pulumi.BoolPtrOutput `pulumi:"writesToCommitLogEnabled"`
}

// NewM3DbNamespace registers a new resource with the given unique name, arguments, and options.
func NewM3DbNamespace(ctx *pulumi.Context,
	name string, args *M3DbNamespaceArgs, opts ...pulumi.ResourceOption) (*M3DbNamespace, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ClusterId == nil {
		return nil, errors.New("invalid value for required argument 'ClusterId'")
	}
	if args.Resolution == nil {
		return nil, errors.New("invalid value for required argument 'Resolution'")
	}
	if args.RetentionPeriodDuration == nil {
		return nil, errors.New("invalid value for required argument 'RetentionPeriodDuration'")
	}
	if args.ServiceName == nil {
		return nil, errors.New("invalid value for required argument 'ServiceName'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource M3DbNamespace
	err := ctx.RegisterResource("ovh:CloudProjectDatabase/m3DbNamespace:M3DbNamespace", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetM3DbNamespace gets an existing M3DbNamespace resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetM3DbNamespace(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *M3DbNamespaceState, opts ...pulumi.ResourceOption) (*M3DbNamespace, error) {
	var resource M3DbNamespace
	err := ctx.ReadResource("ovh:CloudProjectDatabase/m3DbNamespace:M3DbNamespace", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering M3DbNamespace resources.
type m3dbNamespaceState struct {
	// Cluster ID.
	ClusterId *string `pulumi:"clusterId"`
	// Name of the namespace.
	Name *string `pulumi:"name"`
	// Resolution for an aggregated namespace. Should follow Rfc3339 e.g P2D, PT48H.
	Resolution *string `pulumi:"resolution"`
	// Controls how long we wait before expiring stale data. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBlockDataExpirationDuration *string `pulumi:"retentionBlockDataExpirationDuration"`
	// Controls how long to keep a block in memory before flushing to a fileset on disk. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBlockSizeDuration *string `pulumi:"retentionBlockSizeDuration"`
	// Controls how far into the future writes to the namespace will be accepted. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBufferFutureDuration *string `pulumi:"retentionBufferFutureDuration"`
	// Controls how far into the past writes to the namespace will be accepted. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBufferPastDuration *string `pulumi:"retentionBufferPastDuration"`
	// Controls the duration of time that M3DB will retain data for the namespace. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionPeriodDuration *string `pulumi:"retentionPeriodDuration"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName *string `pulumi:"serviceName"`
	// Defines whether M3DB will create snapshot files for this namespace.
	SnapshotEnabled *bool `pulumi:"snapshotEnabled"`
	// Type of namespace.
	Type *string `pulumi:"type"`
	// Defines whether M3DB will include writes to this namespace in the commit log.
	WritesToCommitLogEnabled *bool `pulumi:"writesToCommitLogEnabled"`
}

type M3DbNamespaceState struct {
	// Cluster ID.
	ClusterId pulumi.StringPtrInput
	// Name of the namespace.
	Name pulumi.StringPtrInput
	// Resolution for an aggregated namespace. Should follow Rfc3339 e.g P2D, PT48H.
	Resolution pulumi.StringPtrInput
	// Controls how long we wait before expiring stale data. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBlockDataExpirationDuration pulumi.StringPtrInput
	// Controls how long to keep a block in memory before flushing to a fileset on disk. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBlockSizeDuration pulumi.StringPtrInput
	// Controls how far into the future writes to the namespace will be accepted. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBufferFutureDuration pulumi.StringPtrInput
	// Controls how far into the past writes to the namespace will be accepted. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBufferPastDuration pulumi.StringPtrInput
	// Controls the duration of time that M3DB will retain data for the namespace. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionPeriodDuration pulumi.StringPtrInput
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName pulumi.StringPtrInput
	// Defines whether M3DB will create snapshot files for this namespace.
	SnapshotEnabled pulumi.BoolPtrInput
	// Type of namespace.
	Type pulumi.StringPtrInput
	// Defines whether M3DB will include writes to this namespace in the commit log.
	WritesToCommitLogEnabled pulumi.BoolPtrInput
}

func (M3DbNamespaceState) ElementType() reflect.Type {
	return reflect.TypeOf((*m3dbNamespaceState)(nil)).Elem()
}

type m3dbNamespaceArgs struct {
	// Cluster ID.
	ClusterId string `pulumi:"clusterId"`
	// Name of the namespace.
	Name *string `pulumi:"name"`
	// Resolution for an aggregated namespace. Should follow Rfc3339 e.g P2D, PT48H.
	Resolution string `pulumi:"resolution"`
	// Controls how long we wait before expiring stale data. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBlockDataExpirationDuration *string `pulumi:"retentionBlockDataExpirationDuration"`
	// Controls how long to keep a block in memory before flushing to a fileset on disk. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBlockSizeDuration *string `pulumi:"retentionBlockSizeDuration"`
	// Controls how far into the future writes to the namespace will be accepted. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBufferFutureDuration *string `pulumi:"retentionBufferFutureDuration"`
	// Controls how far into the past writes to the namespace will be accepted. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBufferPastDuration *string `pulumi:"retentionBufferPastDuration"`
	// Controls the duration of time that M3DB will retain data for the namespace. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionPeriodDuration string `pulumi:"retentionPeriodDuration"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName string `pulumi:"serviceName"`
	// Defines whether M3DB will create snapshot files for this namespace.
	SnapshotEnabled *bool `pulumi:"snapshotEnabled"`
	// Defines whether M3DB will include writes to this namespace in the commit log.
	WritesToCommitLogEnabled *bool `pulumi:"writesToCommitLogEnabled"`
}

// The set of arguments for constructing a M3DbNamespace resource.
type M3DbNamespaceArgs struct {
	// Cluster ID.
	ClusterId pulumi.StringInput
	// Name of the namespace.
	Name pulumi.StringPtrInput
	// Resolution for an aggregated namespace. Should follow Rfc3339 e.g P2D, PT48H.
	Resolution pulumi.StringInput
	// Controls how long we wait before expiring stale data. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBlockDataExpirationDuration pulumi.StringPtrInput
	// Controls how long to keep a block in memory before flushing to a fileset on disk. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBlockSizeDuration pulumi.StringPtrInput
	// Controls how far into the future writes to the namespace will be accepted. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBufferFutureDuration pulumi.StringPtrInput
	// Controls how far into the past writes to the namespace will be accepted. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionBufferPastDuration pulumi.StringPtrInput
	// Controls the duration of time that M3DB will retain data for the namespace. Should follow Rfc3339 e.g P2D, PT48H.
	RetentionPeriodDuration pulumi.StringInput
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName pulumi.StringInput
	// Defines whether M3DB will create snapshot files for this namespace.
	SnapshotEnabled pulumi.BoolPtrInput
	// Defines whether M3DB will include writes to this namespace in the commit log.
	WritesToCommitLogEnabled pulumi.BoolPtrInput
}

func (M3DbNamespaceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*m3dbNamespaceArgs)(nil)).Elem()
}

type M3DbNamespaceInput interface {
	pulumi.Input

	ToM3DbNamespaceOutput() M3DbNamespaceOutput
	ToM3DbNamespaceOutputWithContext(ctx context.Context) M3DbNamespaceOutput
}

func (*M3DbNamespace) ElementType() reflect.Type {
	return reflect.TypeOf((**M3DbNamespace)(nil)).Elem()
}

func (i *M3DbNamespace) ToM3DbNamespaceOutput() M3DbNamespaceOutput {
	return i.ToM3DbNamespaceOutputWithContext(context.Background())
}

func (i *M3DbNamespace) ToM3DbNamespaceOutputWithContext(ctx context.Context) M3DbNamespaceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(M3DbNamespaceOutput)
}

// M3DbNamespaceArrayInput is an input type that accepts M3DbNamespaceArray and M3DbNamespaceArrayOutput values.
// You can construct a concrete instance of `M3DbNamespaceArrayInput` via:
//
//	M3DbNamespaceArray{ M3DbNamespaceArgs{...} }
type M3DbNamespaceArrayInput interface {
	pulumi.Input

	ToM3DbNamespaceArrayOutput() M3DbNamespaceArrayOutput
	ToM3DbNamespaceArrayOutputWithContext(context.Context) M3DbNamespaceArrayOutput
}

type M3DbNamespaceArray []M3DbNamespaceInput

func (M3DbNamespaceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*M3DbNamespace)(nil)).Elem()
}

func (i M3DbNamespaceArray) ToM3DbNamespaceArrayOutput() M3DbNamespaceArrayOutput {
	return i.ToM3DbNamespaceArrayOutputWithContext(context.Background())
}

func (i M3DbNamespaceArray) ToM3DbNamespaceArrayOutputWithContext(ctx context.Context) M3DbNamespaceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(M3DbNamespaceArrayOutput)
}

// M3DbNamespaceMapInput is an input type that accepts M3DbNamespaceMap and M3DbNamespaceMapOutput values.
// You can construct a concrete instance of `M3DbNamespaceMapInput` via:
//
//	M3DbNamespaceMap{ "key": M3DbNamespaceArgs{...} }
type M3DbNamespaceMapInput interface {
	pulumi.Input

	ToM3DbNamespaceMapOutput() M3DbNamespaceMapOutput
	ToM3DbNamespaceMapOutputWithContext(context.Context) M3DbNamespaceMapOutput
}

type M3DbNamespaceMap map[string]M3DbNamespaceInput

func (M3DbNamespaceMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*M3DbNamespace)(nil)).Elem()
}

func (i M3DbNamespaceMap) ToM3DbNamespaceMapOutput() M3DbNamespaceMapOutput {
	return i.ToM3DbNamespaceMapOutputWithContext(context.Background())
}

func (i M3DbNamespaceMap) ToM3DbNamespaceMapOutputWithContext(ctx context.Context) M3DbNamespaceMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(M3DbNamespaceMapOutput)
}

type M3DbNamespaceOutput struct{ *pulumi.OutputState }

func (M3DbNamespaceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**M3DbNamespace)(nil)).Elem()
}

func (o M3DbNamespaceOutput) ToM3DbNamespaceOutput() M3DbNamespaceOutput {
	return o
}

func (o M3DbNamespaceOutput) ToM3DbNamespaceOutputWithContext(ctx context.Context) M3DbNamespaceOutput {
	return o
}

// Cluster ID.
func (o M3DbNamespaceOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v *M3DbNamespace) pulumi.StringOutput { return v.ClusterId }).(pulumi.StringOutput)
}

// Name of the namespace.
func (o M3DbNamespaceOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *M3DbNamespace) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Resolution for an aggregated namespace. Should follow Rfc3339 e.g P2D, PT48H.
func (o M3DbNamespaceOutput) Resolution() pulumi.StringOutput {
	return o.ApplyT(func(v *M3DbNamespace) pulumi.StringOutput { return v.Resolution }).(pulumi.StringOutput)
}

// Controls how long we wait before expiring stale data. Should follow Rfc3339 e.g P2D, PT48H.
func (o M3DbNamespaceOutput) RetentionBlockDataExpirationDuration() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *M3DbNamespace) pulumi.StringPtrOutput { return v.RetentionBlockDataExpirationDuration }).(pulumi.StringPtrOutput)
}

// Controls how long to keep a block in memory before flushing to a fileset on disk. Should follow Rfc3339 e.g P2D, PT48H.
func (o M3DbNamespaceOutput) RetentionBlockSizeDuration() pulumi.StringOutput {
	return o.ApplyT(func(v *M3DbNamespace) pulumi.StringOutput { return v.RetentionBlockSizeDuration }).(pulumi.StringOutput)
}

// Controls how far into the future writes to the namespace will be accepted. Should follow Rfc3339 e.g P2D, PT48H.
func (o M3DbNamespaceOutput) RetentionBufferFutureDuration() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *M3DbNamespace) pulumi.StringPtrOutput { return v.RetentionBufferFutureDuration }).(pulumi.StringPtrOutput)
}

// Controls how far into the past writes to the namespace will be accepted. Should follow Rfc3339 e.g P2D, PT48H.
func (o M3DbNamespaceOutput) RetentionBufferPastDuration() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *M3DbNamespace) pulumi.StringPtrOutput { return v.RetentionBufferPastDuration }).(pulumi.StringPtrOutput)
}

// Controls the duration of time that M3DB will retain data for the namespace. Should follow Rfc3339 e.g P2D, PT48H.
func (o M3DbNamespaceOutput) RetentionPeriodDuration() pulumi.StringOutput {
	return o.ApplyT(func(v *M3DbNamespace) pulumi.StringOutput { return v.RetentionPeriodDuration }).(pulumi.StringOutput)
}

// The id of the public cloud project. If omitted,
// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
func (o M3DbNamespaceOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v *M3DbNamespace) pulumi.StringOutput { return v.ServiceName }).(pulumi.StringOutput)
}

// Defines whether M3DB will create snapshot files for this namespace.
func (o M3DbNamespaceOutput) SnapshotEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *M3DbNamespace) pulumi.BoolPtrOutput { return v.SnapshotEnabled }).(pulumi.BoolPtrOutput)
}

// Type of namespace.
func (o M3DbNamespaceOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *M3DbNamespace) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

// Defines whether M3DB will include writes to this namespace in the commit log.
func (o M3DbNamespaceOutput) WritesToCommitLogEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *M3DbNamespace) pulumi.BoolPtrOutput { return v.WritesToCommitLogEnabled }).(pulumi.BoolPtrOutput)
}

type M3DbNamespaceArrayOutput struct{ *pulumi.OutputState }

func (M3DbNamespaceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*M3DbNamespace)(nil)).Elem()
}

func (o M3DbNamespaceArrayOutput) ToM3DbNamespaceArrayOutput() M3DbNamespaceArrayOutput {
	return o
}

func (o M3DbNamespaceArrayOutput) ToM3DbNamespaceArrayOutputWithContext(ctx context.Context) M3DbNamespaceArrayOutput {
	return o
}

func (o M3DbNamespaceArrayOutput) Index(i pulumi.IntInput) M3DbNamespaceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *M3DbNamespace {
		return vs[0].([]*M3DbNamespace)[vs[1].(int)]
	}).(M3DbNamespaceOutput)
}

type M3DbNamespaceMapOutput struct{ *pulumi.OutputState }

func (M3DbNamespaceMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*M3DbNamespace)(nil)).Elem()
}

func (o M3DbNamespaceMapOutput) ToM3DbNamespaceMapOutput() M3DbNamespaceMapOutput {
	return o
}

func (o M3DbNamespaceMapOutput) ToM3DbNamespaceMapOutputWithContext(ctx context.Context) M3DbNamespaceMapOutput {
	return o
}

func (o M3DbNamespaceMapOutput) MapIndex(k pulumi.StringInput) M3DbNamespaceOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *M3DbNamespace {
		return vs[0].(map[string]*M3DbNamespace)[vs[1].(string)]
	}).(M3DbNamespaceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*M3DbNamespaceInput)(nil)).Elem(), &M3DbNamespace{})
	pulumi.RegisterInputType(reflect.TypeOf((*M3DbNamespaceArrayInput)(nil)).Elem(), M3DbNamespaceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*M3DbNamespaceMapInput)(nil)).Elem(), M3DbNamespaceMap{})
	pulumi.RegisterOutputType(M3DbNamespaceOutput{})
	pulumi.RegisterOutputType(M3DbNamespaceArrayOutput{})
	pulumi.RegisterOutputType(M3DbNamespaceMapOutput{})
}
