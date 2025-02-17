// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dedicated

import (
	"context"
	"reflect"

	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Import
//
// Dedicated servers can be imported using the `service_name`.
//
// Using the following configuration:
//
// hcl
//
// import {
//
//	to = ovh_dedicated_server.server
//
//	id = "<service name>"
//
// }
//
// You can then run:
//
// bash
//
// $ pulumi preview -generate-config-out=dedicated.tf
//
// $ pulumi up
//
// The file `dedicated.tf` will then contain the imported resource's configuration, that can be copied next to the `import` block above.
//
// See https://developer.hashicorp.com/terraform/language/import/generating-configuration for more details.
type Server struct {
	pulumi.CustomResourceState

	// Dedicated AZ localisation
	AvailabilityZone pulumi.StringOutput `pulumi:"availabilityZone"`
	// Boot id of the server
	BootId pulumi.Float64Output `pulumi:"bootId"`
	// Boot script of the server
	BootScript pulumi.StringOutput `pulumi:"bootScript"`
	// Dedicated server commercial range
	CommercialRange pulumi.StringOutput `pulumi:"commercialRange"`
	// Dedicated datacenter localisation (bhs1,bhs2,...)
	Datacenter pulumi.StringOutput `pulumi:"datacenter"`
	// A structure describing informations about installation custom
	Details ServerDetailsPtrOutput `pulumi:"details"`
	// Resource display name
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// Path of the EFI bootloader
	EfiBootloaderPath pulumi.StringOutput `pulumi:"efiBootloaderPath"`
	// IAM resource information
	Iam ServerIamOutput `pulumi:"iam"`
	// Dedicated server ip (IPv4)
	Ip pulumi.StringOutput `pulumi:"ip"`
	// Link speed of the server
	LinkSpeed pulumi.Float64Output `pulumi:"linkSpeed"`
	// Icmp monitoring state
	Monitoring pulumi.BoolOutput `pulumi:"monitoring"`
	// Dedicated server name
	Name             pulumi.StringOutput `pulumi:"name"`
	NewUpgradeSystem pulumi.BoolOutput   `pulumi:"newUpgradeSystem"`
	// Prevent datacenter intervention
	NoIntervention pulumi.BoolOutput `pulumi:"noIntervention"`
	// Details about an Order
	Order ServerOrderOutput `pulumi:"order"`
	// Operating system
	Os pulumi.StringOutput `pulumi:"os"`
	// OVH subsidiaries
	OvhSubsidiary pulumi.StringPtrOutput `pulumi:"ovhSubsidiary"`
	// Partition scheme name
	PartitionSchemeName pulumi.StringPtrOutput      `pulumi:"partitionSchemeName"`
	PlanOptions         ServerPlanOptionArrayOutput `pulumi:"planOptions"`
	Plans               ServerPlanArrayOutput       `pulumi:"plans"`
	// Power state of the server (poweron, poweroff)
	PowerState pulumi.StringOutput `pulumi:"powerState"`
	// Does this server have professional use option
	ProfessionalUse pulumi.BoolOutput `pulumi:"professionalUse"`
	// Rack id of the server
	Rack pulumi.StringOutput `pulumi:"rack"`
	// Dedicated region localisation
	Region pulumi.StringOutput `pulumi:"region"`
	// Rescue mail of the server
	RescueMail pulumi.StringOutput `pulumi:"rescueMail"`
	// Public SSH Key used in the rescue mode
	RescueSshKey pulumi.StringOutput `pulumi:"rescueSshKey"`
	// Dedicated server reverse
	Reverse pulumi.StringOutput `pulumi:"reverse"`
	// Root device of the server
	RootDevice pulumi.StringOutput `pulumi:"rootDevice"`
	// Server id
	ServerId pulumi.Float64Output `pulumi:"serverId"`
	// The serviceName of your dedicated server
	ServiceName pulumi.StringOutput `pulumi:"serviceName"`
	// All states a Dedicated can be in (error, hacked, hackedBlocked, ok)
	State pulumi.StringOutput `pulumi:"state"`
	// Dedicated server support level (critical, fastpath, gs, pro)
	SupportLevel pulumi.StringOutput `pulumi:"supportLevel"`
	// Template name
	TemplateName pulumi.StringPtrOutput `pulumi:"templateName"`
	// Metadata
	UserMetadatas ServerUserMetadataArrayOutput `pulumi:"userMetadatas"`
}

// NewServer registers a new resource with the given unique name, arguments, and options.
func NewServer(ctx *pulumi.Context,
	name string, args *ServerArgs, opts ...pulumi.ResourceOption) (*Server, error) {
	if args == nil {
		args = &ServerArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Server
	err := ctx.RegisterResource("ovh:Dedicated/server:Server", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetServer gets an existing Server resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServer(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServerState, opts ...pulumi.ResourceOption) (*Server, error) {
	var resource Server
	err := ctx.ReadResource("ovh:Dedicated/server:Server", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Server resources.
type serverState struct {
	// Dedicated AZ localisation
	AvailabilityZone *string `pulumi:"availabilityZone"`
	// Boot id of the server
	BootId *float64 `pulumi:"bootId"`
	// Boot script of the server
	BootScript *string `pulumi:"bootScript"`
	// Dedicated server commercial range
	CommercialRange *string `pulumi:"commercialRange"`
	// Dedicated datacenter localisation (bhs1,bhs2,...)
	Datacenter *string `pulumi:"datacenter"`
	// A structure describing informations about installation custom
	Details *ServerDetails `pulumi:"details"`
	// Resource display name
	DisplayName *string `pulumi:"displayName"`
	// Path of the EFI bootloader
	EfiBootloaderPath *string `pulumi:"efiBootloaderPath"`
	// IAM resource information
	Iam *ServerIam `pulumi:"iam"`
	// Dedicated server ip (IPv4)
	Ip *string `pulumi:"ip"`
	// Link speed of the server
	LinkSpeed *float64 `pulumi:"linkSpeed"`
	// Icmp monitoring state
	Monitoring *bool `pulumi:"monitoring"`
	// Dedicated server name
	Name             *string `pulumi:"name"`
	NewUpgradeSystem *bool   `pulumi:"newUpgradeSystem"`
	// Prevent datacenter intervention
	NoIntervention *bool `pulumi:"noIntervention"`
	// Details about an Order
	Order *ServerOrder `pulumi:"order"`
	// Operating system
	Os *string `pulumi:"os"`
	// OVH subsidiaries
	OvhSubsidiary *string `pulumi:"ovhSubsidiary"`
	// Partition scheme name
	PartitionSchemeName *string            `pulumi:"partitionSchemeName"`
	PlanOptions         []ServerPlanOption `pulumi:"planOptions"`
	Plans               []ServerPlan       `pulumi:"plans"`
	// Power state of the server (poweron, poweroff)
	PowerState *string `pulumi:"powerState"`
	// Does this server have professional use option
	ProfessionalUse *bool `pulumi:"professionalUse"`
	// Rack id of the server
	Rack *string `pulumi:"rack"`
	// Dedicated region localisation
	Region *string `pulumi:"region"`
	// Rescue mail of the server
	RescueMail *string `pulumi:"rescueMail"`
	// Public SSH Key used in the rescue mode
	RescueSshKey *string `pulumi:"rescueSshKey"`
	// Dedicated server reverse
	Reverse *string `pulumi:"reverse"`
	// Root device of the server
	RootDevice *string `pulumi:"rootDevice"`
	// Server id
	ServerId *float64 `pulumi:"serverId"`
	// The serviceName of your dedicated server
	ServiceName *string `pulumi:"serviceName"`
	// All states a Dedicated can be in (error, hacked, hackedBlocked, ok)
	State *string `pulumi:"state"`
	// Dedicated server support level (critical, fastpath, gs, pro)
	SupportLevel *string `pulumi:"supportLevel"`
	// Template name
	TemplateName *string `pulumi:"templateName"`
	// Metadata
	UserMetadatas []ServerUserMetadata `pulumi:"userMetadatas"`
}

type ServerState struct {
	// Dedicated AZ localisation
	AvailabilityZone pulumi.StringPtrInput
	// Boot id of the server
	BootId pulumi.Float64PtrInput
	// Boot script of the server
	BootScript pulumi.StringPtrInput
	// Dedicated server commercial range
	CommercialRange pulumi.StringPtrInput
	// Dedicated datacenter localisation (bhs1,bhs2,...)
	Datacenter pulumi.StringPtrInput
	// A structure describing informations about installation custom
	Details ServerDetailsPtrInput
	// Resource display name
	DisplayName pulumi.StringPtrInput
	// Path of the EFI bootloader
	EfiBootloaderPath pulumi.StringPtrInput
	// IAM resource information
	Iam ServerIamPtrInput
	// Dedicated server ip (IPv4)
	Ip pulumi.StringPtrInput
	// Link speed of the server
	LinkSpeed pulumi.Float64PtrInput
	// Icmp monitoring state
	Monitoring pulumi.BoolPtrInput
	// Dedicated server name
	Name             pulumi.StringPtrInput
	NewUpgradeSystem pulumi.BoolPtrInput
	// Prevent datacenter intervention
	NoIntervention pulumi.BoolPtrInput
	// Details about an Order
	Order ServerOrderPtrInput
	// Operating system
	Os pulumi.StringPtrInput
	// OVH subsidiaries
	OvhSubsidiary pulumi.StringPtrInput
	// Partition scheme name
	PartitionSchemeName pulumi.StringPtrInput
	PlanOptions         ServerPlanOptionArrayInput
	Plans               ServerPlanArrayInput
	// Power state of the server (poweron, poweroff)
	PowerState pulumi.StringPtrInput
	// Does this server have professional use option
	ProfessionalUse pulumi.BoolPtrInput
	// Rack id of the server
	Rack pulumi.StringPtrInput
	// Dedicated region localisation
	Region pulumi.StringPtrInput
	// Rescue mail of the server
	RescueMail pulumi.StringPtrInput
	// Public SSH Key used in the rescue mode
	RescueSshKey pulumi.StringPtrInput
	// Dedicated server reverse
	Reverse pulumi.StringPtrInput
	// Root device of the server
	RootDevice pulumi.StringPtrInput
	// Server id
	ServerId pulumi.Float64PtrInput
	// The serviceName of your dedicated server
	ServiceName pulumi.StringPtrInput
	// All states a Dedicated can be in (error, hacked, hackedBlocked, ok)
	State pulumi.StringPtrInput
	// Dedicated server support level (critical, fastpath, gs, pro)
	SupportLevel pulumi.StringPtrInput
	// Template name
	TemplateName pulumi.StringPtrInput
	// Metadata
	UserMetadatas ServerUserMetadataArrayInput
}

func (ServerState) ElementType() reflect.Type {
	return reflect.TypeOf((*serverState)(nil)).Elem()
}

type serverArgs struct {
	// Boot id of the server
	BootId *float64 `pulumi:"bootId"`
	// Boot script of the server
	BootScript *string `pulumi:"bootScript"`
	// A structure describing informations about installation custom
	Details *ServerDetails `pulumi:"details"`
	// Resource display name
	DisplayName *string `pulumi:"displayName"`
	// Path of the EFI bootloader
	EfiBootloaderPath *string `pulumi:"efiBootloaderPath"`
	// Icmp monitoring state
	Monitoring *bool `pulumi:"monitoring"`
	// Prevent datacenter intervention
	NoIntervention *bool `pulumi:"noIntervention"`
	// OVH subsidiaries
	OvhSubsidiary *string `pulumi:"ovhSubsidiary"`
	// Partition scheme name
	PartitionSchemeName *string            `pulumi:"partitionSchemeName"`
	PlanOptions         []ServerPlanOption `pulumi:"planOptions"`
	Plans               []ServerPlan       `pulumi:"plans"`
	// Rescue mail of the server
	RescueMail *string `pulumi:"rescueMail"`
	// Public SSH Key used in the rescue mode
	RescueSshKey *string `pulumi:"rescueSshKey"`
	// Root device of the server
	RootDevice *string `pulumi:"rootDevice"`
	// All states a Dedicated can be in (error, hacked, hackedBlocked, ok)
	State *string `pulumi:"state"`
	// Template name
	TemplateName *string `pulumi:"templateName"`
	// Metadata
	UserMetadatas []ServerUserMetadata `pulumi:"userMetadatas"`
}

// The set of arguments for constructing a Server resource.
type ServerArgs struct {
	// Boot id of the server
	BootId pulumi.Float64PtrInput
	// Boot script of the server
	BootScript pulumi.StringPtrInput
	// A structure describing informations about installation custom
	Details ServerDetailsPtrInput
	// Resource display name
	DisplayName pulumi.StringPtrInput
	// Path of the EFI bootloader
	EfiBootloaderPath pulumi.StringPtrInput
	// Icmp monitoring state
	Monitoring pulumi.BoolPtrInput
	// Prevent datacenter intervention
	NoIntervention pulumi.BoolPtrInput
	// OVH subsidiaries
	OvhSubsidiary pulumi.StringPtrInput
	// Partition scheme name
	PartitionSchemeName pulumi.StringPtrInput
	PlanOptions         ServerPlanOptionArrayInput
	Plans               ServerPlanArrayInput
	// Rescue mail of the server
	RescueMail pulumi.StringPtrInput
	// Public SSH Key used in the rescue mode
	RescueSshKey pulumi.StringPtrInput
	// Root device of the server
	RootDevice pulumi.StringPtrInput
	// All states a Dedicated can be in (error, hacked, hackedBlocked, ok)
	State pulumi.StringPtrInput
	// Template name
	TemplateName pulumi.StringPtrInput
	// Metadata
	UserMetadatas ServerUserMetadataArrayInput
}

func (ServerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serverArgs)(nil)).Elem()
}

type ServerInput interface {
	pulumi.Input

	ToServerOutput() ServerOutput
	ToServerOutputWithContext(ctx context.Context) ServerOutput
}

func (*Server) ElementType() reflect.Type {
	return reflect.TypeOf((**Server)(nil)).Elem()
}

func (i *Server) ToServerOutput() ServerOutput {
	return i.ToServerOutputWithContext(context.Background())
}

func (i *Server) ToServerOutputWithContext(ctx context.Context) ServerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServerOutput)
}

// ServerArrayInput is an input type that accepts ServerArray and ServerArrayOutput values.
// You can construct a concrete instance of `ServerArrayInput` via:
//
//	ServerArray{ ServerArgs{...} }
type ServerArrayInput interface {
	pulumi.Input

	ToServerArrayOutput() ServerArrayOutput
	ToServerArrayOutputWithContext(context.Context) ServerArrayOutput
}

type ServerArray []ServerInput

func (ServerArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Server)(nil)).Elem()
}

func (i ServerArray) ToServerArrayOutput() ServerArrayOutput {
	return i.ToServerArrayOutputWithContext(context.Background())
}

func (i ServerArray) ToServerArrayOutputWithContext(ctx context.Context) ServerArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServerArrayOutput)
}

// ServerMapInput is an input type that accepts ServerMap and ServerMapOutput values.
// You can construct a concrete instance of `ServerMapInput` via:
//
//	ServerMap{ "key": ServerArgs{...} }
type ServerMapInput interface {
	pulumi.Input

	ToServerMapOutput() ServerMapOutput
	ToServerMapOutputWithContext(context.Context) ServerMapOutput
}

type ServerMap map[string]ServerInput

func (ServerMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Server)(nil)).Elem()
}

func (i ServerMap) ToServerMapOutput() ServerMapOutput {
	return i.ToServerMapOutputWithContext(context.Background())
}

func (i ServerMap) ToServerMapOutputWithContext(ctx context.Context) ServerMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServerMapOutput)
}

type ServerOutput struct{ *pulumi.OutputState }

func (ServerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Server)(nil)).Elem()
}

func (o ServerOutput) ToServerOutput() ServerOutput {
	return o
}

func (o ServerOutput) ToServerOutputWithContext(ctx context.Context) ServerOutput {
	return o
}

// Dedicated AZ localisation
func (o ServerOutput) AvailabilityZone() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.AvailabilityZone }).(pulumi.StringOutput)
}

// Boot id of the server
func (o ServerOutput) BootId() pulumi.Float64Output {
	return o.ApplyT(func(v *Server) pulumi.Float64Output { return v.BootId }).(pulumi.Float64Output)
}

// Boot script of the server
func (o ServerOutput) BootScript() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.BootScript }).(pulumi.StringOutput)
}

// Dedicated server commercial range
func (o ServerOutput) CommercialRange() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.CommercialRange }).(pulumi.StringOutput)
}

// Dedicated datacenter localisation (bhs1,bhs2,...)
func (o ServerOutput) Datacenter() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.Datacenter }).(pulumi.StringOutput)
}

// A structure describing informations about installation custom
func (o ServerOutput) Details() ServerDetailsPtrOutput {
	return o.ApplyT(func(v *Server) ServerDetailsPtrOutput { return v.Details }).(ServerDetailsPtrOutput)
}

// Resource display name
func (o ServerOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.DisplayName }).(pulumi.StringOutput)
}

// Path of the EFI bootloader
func (o ServerOutput) EfiBootloaderPath() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.EfiBootloaderPath }).(pulumi.StringOutput)
}

// IAM resource information
func (o ServerOutput) Iam() ServerIamOutput {
	return o.ApplyT(func(v *Server) ServerIamOutput { return v.Iam }).(ServerIamOutput)
}

// Dedicated server ip (IPv4)
func (o ServerOutput) Ip() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.Ip }).(pulumi.StringOutput)
}

// Link speed of the server
func (o ServerOutput) LinkSpeed() pulumi.Float64Output {
	return o.ApplyT(func(v *Server) pulumi.Float64Output { return v.LinkSpeed }).(pulumi.Float64Output)
}

// Icmp monitoring state
func (o ServerOutput) Monitoring() pulumi.BoolOutput {
	return o.ApplyT(func(v *Server) pulumi.BoolOutput { return v.Monitoring }).(pulumi.BoolOutput)
}

// Dedicated server name
func (o ServerOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o ServerOutput) NewUpgradeSystem() pulumi.BoolOutput {
	return o.ApplyT(func(v *Server) pulumi.BoolOutput { return v.NewUpgradeSystem }).(pulumi.BoolOutput)
}

// Prevent datacenter intervention
func (o ServerOutput) NoIntervention() pulumi.BoolOutput {
	return o.ApplyT(func(v *Server) pulumi.BoolOutput { return v.NoIntervention }).(pulumi.BoolOutput)
}

// Details about an Order
func (o ServerOutput) Order() ServerOrderOutput {
	return o.ApplyT(func(v *Server) ServerOrderOutput { return v.Order }).(ServerOrderOutput)
}

// Operating system
func (o ServerOutput) Os() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.Os }).(pulumi.StringOutput)
}

// OVH subsidiaries
func (o ServerOutput) OvhSubsidiary() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Server) pulumi.StringPtrOutput { return v.OvhSubsidiary }).(pulumi.StringPtrOutput)
}

// Partition scheme name
func (o ServerOutput) PartitionSchemeName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Server) pulumi.StringPtrOutput { return v.PartitionSchemeName }).(pulumi.StringPtrOutput)
}

func (o ServerOutput) PlanOptions() ServerPlanOptionArrayOutput {
	return o.ApplyT(func(v *Server) ServerPlanOptionArrayOutput { return v.PlanOptions }).(ServerPlanOptionArrayOutput)
}

func (o ServerOutput) Plans() ServerPlanArrayOutput {
	return o.ApplyT(func(v *Server) ServerPlanArrayOutput { return v.Plans }).(ServerPlanArrayOutput)
}

// Power state of the server (poweron, poweroff)
func (o ServerOutput) PowerState() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.PowerState }).(pulumi.StringOutput)
}

// Does this server have professional use option
func (o ServerOutput) ProfessionalUse() pulumi.BoolOutput {
	return o.ApplyT(func(v *Server) pulumi.BoolOutput { return v.ProfessionalUse }).(pulumi.BoolOutput)
}

// Rack id of the server
func (o ServerOutput) Rack() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.Rack }).(pulumi.StringOutput)
}

// Dedicated region localisation
func (o ServerOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.Region }).(pulumi.StringOutput)
}

// Rescue mail of the server
func (o ServerOutput) RescueMail() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.RescueMail }).(pulumi.StringOutput)
}

// Public SSH Key used in the rescue mode
func (o ServerOutput) RescueSshKey() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.RescueSshKey }).(pulumi.StringOutput)
}

// Dedicated server reverse
func (o ServerOutput) Reverse() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.Reverse }).(pulumi.StringOutput)
}

// Root device of the server
func (o ServerOutput) RootDevice() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.RootDevice }).(pulumi.StringOutput)
}

// Server id
func (o ServerOutput) ServerId() pulumi.Float64Output {
	return o.ApplyT(func(v *Server) pulumi.Float64Output { return v.ServerId }).(pulumi.Float64Output)
}

// The serviceName of your dedicated server
func (o ServerOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.ServiceName }).(pulumi.StringOutput)
}

// All states a Dedicated can be in (error, hacked, hackedBlocked, ok)
func (o ServerOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

// Dedicated server support level (critical, fastpath, gs, pro)
func (o ServerOutput) SupportLevel() pulumi.StringOutput {
	return o.ApplyT(func(v *Server) pulumi.StringOutput { return v.SupportLevel }).(pulumi.StringOutput)
}

// Template name
func (o ServerOutput) TemplateName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Server) pulumi.StringPtrOutput { return v.TemplateName }).(pulumi.StringPtrOutput)
}

// Metadata
func (o ServerOutput) UserMetadatas() ServerUserMetadataArrayOutput {
	return o.ApplyT(func(v *Server) ServerUserMetadataArrayOutput { return v.UserMetadatas }).(ServerUserMetadataArrayOutput)
}

type ServerArrayOutput struct{ *pulumi.OutputState }

func (ServerArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Server)(nil)).Elem()
}

func (o ServerArrayOutput) ToServerArrayOutput() ServerArrayOutput {
	return o
}

func (o ServerArrayOutput) ToServerArrayOutputWithContext(ctx context.Context) ServerArrayOutput {
	return o
}

func (o ServerArrayOutput) Index(i pulumi.IntInput) ServerOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Server {
		return vs[0].([]*Server)[vs[1].(int)]
	}).(ServerOutput)
}

type ServerMapOutput struct{ *pulumi.OutputState }

func (ServerMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Server)(nil)).Elem()
}

func (o ServerMapOutput) ToServerMapOutput() ServerMapOutput {
	return o
}

func (o ServerMapOutput) ToServerMapOutputWithContext(ctx context.Context) ServerMapOutput {
	return o
}

func (o ServerMapOutput) MapIndex(k pulumi.StringInput) ServerOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Server {
		return vs[0].(map[string]*Server)[vs[1].(string)]
	}).(ServerOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ServerInput)(nil)).Elem(), &Server{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServerArrayInput)(nil)).Elem(), ServerArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServerMapInput)(nil)).Elem(), ServerMap{})
	pulumi.RegisterOutputType(ServerOutput{})
	pulumi.RegisterOutputType(ServerArrayOutput{})
	pulumi.RegisterOutputType(ServerMapOutput{})
}
