// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iploadbalancing

import (
	"context"
	"reflect"

	"errors"
	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a backend server group (farm) to be used by loadbalancing frontend(s)
//
// ## Example Usage
//
// <!--Start PulumiCodeChooser -->
// ```go
// package main
//
// import (
//
//	"github.com/ovh/pulumi-ovh/sdk/go/ovh/IpLoadBalancing"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			lb, err := IpLoadBalancing.GetIpLoadBalancing(ctx, &iploadbalancing.GetIpLoadBalancingArgs{
//				ServiceName: pulumi.StringRef("ip-1.2.3.4"),
//				State:       pulumi.StringRef("ok"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			_, err = IpLoadBalancing.NewTcpFarm(ctx, "farmname", &IpLoadBalancing.TcpFarmArgs{
//				DisplayName: pulumi.String("ingress-8080-gra"),
//				ServiceName: *pulumi.String(lb.ServiceName),
//				Zone:        pulumi.String("GRA"),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
// <!--End PulumiCodeChooser -->
//
// ## Import
//
// TCP Farm can be imported using the following format `serviceName` and the `id` of the farm, separated by "/" e.g.
type TcpFarm struct {
	pulumi.CustomResourceState

	// Load balancing algorithm. `roundrobin` if null (`first`, `leastconn`, `roundrobin`, `source`)
	Balance pulumi.StringPtrOutput `pulumi:"balance"`
	// Readable label for loadbalancer farm
	DisplayName pulumi.StringPtrOutput `pulumi:"displayName"`
	// Port for backends to receive traffic on.
	Port pulumi.IntPtrOutput `pulumi:"port"`
	// define a backend healthcheck probe
	Probe TcpFarmProbePtrOutput `pulumi:"probe"`
	// The internal name of your IP load balancing
	ServiceName pulumi.StringOutput `pulumi:"serviceName"`
	// Stickiness type. No stickiness if null (`sourceIp`)
	Stickiness pulumi.StringPtrOutput `pulumi:"stickiness"`
	// Internal Load Balancer identifier of the vRack private network to attach to your farm, mandatory when your Load Balancer is attached to a vRack
	VrackNetworkId pulumi.IntPtrOutput `pulumi:"vrackNetworkId"`
	// Zone where the farm will be defined (ie. `GRA`, `BHS` also supports `ALL`)
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewTcpFarm registers a new resource with the given unique name, arguments, and options.
func NewTcpFarm(ctx *pulumi.Context,
	name string, args *TcpFarmArgs, opts ...pulumi.ResourceOption) (*TcpFarm, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ServiceName == nil {
		return nil, errors.New("invalid value for required argument 'ServiceName'")
	}
	if args.Zone == nil {
		return nil, errors.New("invalid value for required argument 'Zone'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource TcpFarm
	err := ctx.RegisterResource("ovh:IpLoadBalancing/tcpFarm:TcpFarm", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTcpFarm gets an existing TcpFarm resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTcpFarm(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TcpFarmState, opts ...pulumi.ResourceOption) (*TcpFarm, error) {
	var resource TcpFarm
	err := ctx.ReadResource("ovh:IpLoadBalancing/tcpFarm:TcpFarm", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TcpFarm resources.
type tcpFarmState struct {
	// Load balancing algorithm. `roundrobin` if null (`first`, `leastconn`, `roundrobin`, `source`)
	Balance *string `pulumi:"balance"`
	// Readable label for loadbalancer farm
	DisplayName *string `pulumi:"displayName"`
	// Port for backends to receive traffic on.
	Port *int `pulumi:"port"`
	// define a backend healthcheck probe
	Probe *TcpFarmProbe `pulumi:"probe"`
	// The internal name of your IP load balancing
	ServiceName *string `pulumi:"serviceName"`
	// Stickiness type. No stickiness if null (`sourceIp`)
	Stickiness *string `pulumi:"stickiness"`
	// Internal Load Balancer identifier of the vRack private network to attach to your farm, mandatory when your Load Balancer is attached to a vRack
	VrackNetworkId *int `pulumi:"vrackNetworkId"`
	// Zone where the farm will be defined (ie. `GRA`, `BHS` also supports `ALL`)
	Zone *string `pulumi:"zone"`
}

type TcpFarmState struct {
	// Load balancing algorithm. `roundrobin` if null (`first`, `leastconn`, `roundrobin`, `source`)
	Balance pulumi.StringPtrInput
	// Readable label for loadbalancer farm
	DisplayName pulumi.StringPtrInput
	// Port for backends to receive traffic on.
	Port pulumi.IntPtrInput
	// define a backend healthcheck probe
	Probe TcpFarmProbePtrInput
	// The internal name of your IP load balancing
	ServiceName pulumi.StringPtrInput
	// Stickiness type. No stickiness if null (`sourceIp`)
	Stickiness pulumi.StringPtrInput
	// Internal Load Balancer identifier of the vRack private network to attach to your farm, mandatory when your Load Balancer is attached to a vRack
	VrackNetworkId pulumi.IntPtrInput
	// Zone where the farm will be defined (ie. `GRA`, `BHS` also supports `ALL`)
	Zone pulumi.StringPtrInput
}

func (TcpFarmState) ElementType() reflect.Type {
	return reflect.TypeOf((*tcpFarmState)(nil)).Elem()
}

type tcpFarmArgs struct {
	// Load balancing algorithm. `roundrobin` if null (`first`, `leastconn`, `roundrobin`, `source`)
	Balance *string `pulumi:"balance"`
	// Readable label for loadbalancer farm
	DisplayName *string `pulumi:"displayName"`
	// Port for backends to receive traffic on.
	Port *int `pulumi:"port"`
	// define a backend healthcheck probe
	Probe *TcpFarmProbe `pulumi:"probe"`
	// The internal name of your IP load balancing
	ServiceName string `pulumi:"serviceName"`
	// Stickiness type. No stickiness if null (`sourceIp`)
	Stickiness *string `pulumi:"stickiness"`
	// Internal Load Balancer identifier of the vRack private network to attach to your farm, mandatory when your Load Balancer is attached to a vRack
	VrackNetworkId *int `pulumi:"vrackNetworkId"`
	// Zone where the farm will be defined (ie. `GRA`, `BHS` also supports `ALL`)
	Zone string `pulumi:"zone"`
}

// The set of arguments for constructing a TcpFarm resource.
type TcpFarmArgs struct {
	// Load balancing algorithm. `roundrobin` if null (`first`, `leastconn`, `roundrobin`, `source`)
	Balance pulumi.StringPtrInput
	// Readable label for loadbalancer farm
	DisplayName pulumi.StringPtrInput
	// Port for backends to receive traffic on.
	Port pulumi.IntPtrInput
	// define a backend healthcheck probe
	Probe TcpFarmProbePtrInput
	// The internal name of your IP load balancing
	ServiceName pulumi.StringInput
	// Stickiness type. No stickiness if null (`sourceIp`)
	Stickiness pulumi.StringPtrInput
	// Internal Load Balancer identifier of the vRack private network to attach to your farm, mandatory when your Load Balancer is attached to a vRack
	VrackNetworkId pulumi.IntPtrInput
	// Zone where the farm will be defined (ie. `GRA`, `BHS` also supports `ALL`)
	Zone pulumi.StringInput
}

func (TcpFarmArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*tcpFarmArgs)(nil)).Elem()
}

type TcpFarmInput interface {
	pulumi.Input

	ToTcpFarmOutput() TcpFarmOutput
	ToTcpFarmOutputWithContext(ctx context.Context) TcpFarmOutput
}

func (*TcpFarm) ElementType() reflect.Type {
	return reflect.TypeOf((**TcpFarm)(nil)).Elem()
}

func (i *TcpFarm) ToTcpFarmOutput() TcpFarmOutput {
	return i.ToTcpFarmOutputWithContext(context.Background())
}

func (i *TcpFarm) ToTcpFarmOutputWithContext(ctx context.Context) TcpFarmOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TcpFarmOutput)
}

// TcpFarmArrayInput is an input type that accepts TcpFarmArray and TcpFarmArrayOutput values.
// You can construct a concrete instance of `TcpFarmArrayInput` via:
//
//	TcpFarmArray{ TcpFarmArgs{...} }
type TcpFarmArrayInput interface {
	pulumi.Input

	ToTcpFarmArrayOutput() TcpFarmArrayOutput
	ToTcpFarmArrayOutputWithContext(context.Context) TcpFarmArrayOutput
}

type TcpFarmArray []TcpFarmInput

func (TcpFarmArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*TcpFarm)(nil)).Elem()
}

func (i TcpFarmArray) ToTcpFarmArrayOutput() TcpFarmArrayOutput {
	return i.ToTcpFarmArrayOutputWithContext(context.Background())
}

func (i TcpFarmArray) ToTcpFarmArrayOutputWithContext(ctx context.Context) TcpFarmArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TcpFarmArrayOutput)
}

// TcpFarmMapInput is an input type that accepts TcpFarmMap and TcpFarmMapOutput values.
// You can construct a concrete instance of `TcpFarmMapInput` via:
//
//	TcpFarmMap{ "key": TcpFarmArgs{...} }
type TcpFarmMapInput interface {
	pulumi.Input

	ToTcpFarmMapOutput() TcpFarmMapOutput
	ToTcpFarmMapOutputWithContext(context.Context) TcpFarmMapOutput
}

type TcpFarmMap map[string]TcpFarmInput

func (TcpFarmMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*TcpFarm)(nil)).Elem()
}

func (i TcpFarmMap) ToTcpFarmMapOutput() TcpFarmMapOutput {
	return i.ToTcpFarmMapOutputWithContext(context.Background())
}

func (i TcpFarmMap) ToTcpFarmMapOutputWithContext(ctx context.Context) TcpFarmMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TcpFarmMapOutput)
}

type TcpFarmOutput struct{ *pulumi.OutputState }

func (TcpFarmOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TcpFarm)(nil)).Elem()
}

func (o TcpFarmOutput) ToTcpFarmOutput() TcpFarmOutput {
	return o
}

func (o TcpFarmOutput) ToTcpFarmOutputWithContext(ctx context.Context) TcpFarmOutput {
	return o
}

// Load balancing algorithm. `roundrobin` if null (`first`, `leastconn`, `roundrobin`, `source`)
func (o TcpFarmOutput) Balance() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *TcpFarm) pulumi.StringPtrOutput { return v.Balance }).(pulumi.StringPtrOutput)
}

// Readable label for loadbalancer farm
func (o TcpFarmOutput) DisplayName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *TcpFarm) pulumi.StringPtrOutput { return v.DisplayName }).(pulumi.StringPtrOutput)
}

// Port for backends to receive traffic on.
func (o TcpFarmOutput) Port() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *TcpFarm) pulumi.IntPtrOutput { return v.Port }).(pulumi.IntPtrOutput)
}

// define a backend healthcheck probe
func (o TcpFarmOutput) Probe() TcpFarmProbePtrOutput {
	return o.ApplyT(func(v *TcpFarm) TcpFarmProbePtrOutput { return v.Probe }).(TcpFarmProbePtrOutput)
}

// The internal name of your IP load balancing
func (o TcpFarmOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v *TcpFarm) pulumi.StringOutput { return v.ServiceName }).(pulumi.StringOutput)
}

// Stickiness type. No stickiness if null (`sourceIp`)
func (o TcpFarmOutput) Stickiness() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *TcpFarm) pulumi.StringPtrOutput { return v.Stickiness }).(pulumi.StringPtrOutput)
}

// Internal Load Balancer identifier of the vRack private network to attach to your farm, mandatory when your Load Balancer is attached to a vRack
func (o TcpFarmOutput) VrackNetworkId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *TcpFarm) pulumi.IntPtrOutput { return v.VrackNetworkId }).(pulumi.IntPtrOutput)
}

// Zone where the farm will be defined (ie. `GRA`, `BHS` also supports `ALL`)
func (o TcpFarmOutput) Zone() pulumi.StringOutput {
	return o.ApplyT(func(v *TcpFarm) pulumi.StringOutput { return v.Zone }).(pulumi.StringOutput)
}

type TcpFarmArrayOutput struct{ *pulumi.OutputState }

func (TcpFarmArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*TcpFarm)(nil)).Elem()
}

func (o TcpFarmArrayOutput) ToTcpFarmArrayOutput() TcpFarmArrayOutput {
	return o
}

func (o TcpFarmArrayOutput) ToTcpFarmArrayOutputWithContext(ctx context.Context) TcpFarmArrayOutput {
	return o
}

func (o TcpFarmArrayOutput) Index(i pulumi.IntInput) TcpFarmOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *TcpFarm {
		return vs[0].([]*TcpFarm)[vs[1].(int)]
	}).(TcpFarmOutput)
}

type TcpFarmMapOutput struct{ *pulumi.OutputState }

func (TcpFarmMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*TcpFarm)(nil)).Elem()
}

func (o TcpFarmMapOutput) ToTcpFarmMapOutput() TcpFarmMapOutput {
	return o
}

func (o TcpFarmMapOutput) ToTcpFarmMapOutputWithContext(ctx context.Context) TcpFarmMapOutput {
	return o
}

func (o TcpFarmMapOutput) MapIndex(k pulumi.StringInput) TcpFarmOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *TcpFarm {
		return vs[0].(map[string]*TcpFarm)[vs[1].(string)]
	}).(TcpFarmOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TcpFarmInput)(nil)).Elem(), &TcpFarm{})
	pulumi.RegisterInputType(reflect.TypeOf((*TcpFarmArrayInput)(nil)).Elem(), TcpFarmArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*TcpFarmMapInput)(nil)).Elem(), TcpFarmMap{})
	pulumi.RegisterOutputType(TcpFarmOutput{})
	pulumi.RegisterOutputType(TcpFarmArrayOutput{})
	pulumi.RegisterOutputType(TcpFarmMapOutput{})
}
