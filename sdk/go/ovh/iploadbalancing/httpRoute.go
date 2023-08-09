// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iploadbalancing

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manage HTTP route for a loadbalancer service
//
// ## Example Usage
//
// Route which redirect all url to https.
type HttpRoute struct {
	pulumi.CustomResourceState

	// Action triggered when all rules match
	Action HttpRouteActionOutput `pulumi:"action"`
	// Human readable name for your route, this field is for you
	DisplayName pulumi.StringPtrOutput `pulumi:"displayName"`
	// Route traffic for this frontend
	FrontendId pulumi.IntOutput `pulumi:"frontendId"`
	// List of rules to match to trigger action
	Rules HttpRouteRuleTypeArrayOutput `pulumi:"rules"`
	// The internal name of your IP load balancing
	ServiceName pulumi.StringOutput `pulumi:"serviceName"`
	// HTTP status code for "redirect" and "reject" actions
	Status pulumi.StringOutput `pulumi:"status"`
	// Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
	Weight pulumi.IntOutput `pulumi:"weight"`
}

// NewHttpRoute registers a new resource with the given unique name, arguments, and options.
func NewHttpRoute(ctx *pulumi.Context,
	name string, args *HttpRouteArgs, opts ...pulumi.ResourceOption) (*HttpRoute, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Action == nil {
		return nil, errors.New("invalid value for required argument 'Action'")
	}
	if args.ServiceName == nil {
		return nil, errors.New("invalid value for required argument 'ServiceName'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource HttpRoute
	err := ctx.RegisterResource("ovh:IpLoadBalancing/httpRoute:HttpRoute", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHttpRoute gets an existing HttpRoute resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHttpRoute(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HttpRouteState, opts ...pulumi.ResourceOption) (*HttpRoute, error) {
	var resource HttpRoute
	err := ctx.ReadResource("ovh:IpLoadBalancing/httpRoute:HttpRoute", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering HttpRoute resources.
type httpRouteState struct {
	// Action triggered when all rules match
	Action *HttpRouteAction `pulumi:"action"`
	// Human readable name for your route, this field is for you
	DisplayName *string `pulumi:"displayName"`
	// Route traffic for this frontend
	FrontendId *int `pulumi:"frontendId"`
	// List of rules to match to trigger action
	Rules []HttpRouteRuleType `pulumi:"rules"`
	// The internal name of your IP load balancing
	ServiceName *string `pulumi:"serviceName"`
	// HTTP status code for "redirect" and "reject" actions
	Status *string `pulumi:"status"`
	// Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
	Weight *int `pulumi:"weight"`
}

type HttpRouteState struct {
	// Action triggered when all rules match
	Action HttpRouteActionPtrInput
	// Human readable name for your route, this field is for you
	DisplayName pulumi.StringPtrInput
	// Route traffic for this frontend
	FrontendId pulumi.IntPtrInput
	// List of rules to match to trigger action
	Rules HttpRouteRuleTypeArrayInput
	// The internal name of your IP load balancing
	ServiceName pulumi.StringPtrInput
	// HTTP status code for "redirect" and "reject" actions
	Status pulumi.StringPtrInput
	// Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
	Weight pulumi.IntPtrInput
}

func (HttpRouteState) ElementType() reflect.Type {
	return reflect.TypeOf((*httpRouteState)(nil)).Elem()
}

type httpRouteArgs struct {
	// Action triggered when all rules match
	Action HttpRouteAction `pulumi:"action"`
	// Human readable name for your route, this field is for you
	DisplayName *string `pulumi:"displayName"`
	// Route traffic for this frontend
	FrontendId *int `pulumi:"frontendId"`
	// The internal name of your IP load balancing
	ServiceName string `pulumi:"serviceName"`
	// Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
	Weight *int `pulumi:"weight"`
}

// The set of arguments for constructing a HttpRoute resource.
type HttpRouteArgs struct {
	// Action triggered when all rules match
	Action HttpRouteActionInput
	// Human readable name for your route, this field is for you
	DisplayName pulumi.StringPtrInput
	// Route traffic for this frontend
	FrontendId pulumi.IntPtrInput
	// The internal name of your IP load balancing
	ServiceName pulumi.StringInput
	// Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
	Weight pulumi.IntPtrInput
}

func (HttpRouteArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*httpRouteArgs)(nil)).Elem()
}

type HttpRouteInput interface {
	pulumi.Input

	ToHttpRouteOutput() HttpRouteOutput
	ToHttpRouteOutputWithContext(ctx context.Context) HttpRouteOutput
}

func (*HttpRoute) ElementType() reflect.Type {
	return reflect.TypeOf((**HttpRoute)(nil)).Elem()
}

func (i *HttpRoute) ToHttpRouteOutput() HttpRouteOutput {
	return i.ToHttpRouteOutputWithContext(context.Background())
}

func (i *HttpRoute) ToHttpRouteOutputWithContext(ctx context.Context) HttpRouteOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HttpRouteOutput)
}

// HttpRouteArrayInput is an input type that accepts HttpRouteArray and HttpRouteArrayOutput values.
// You can construct a concrete instance of `HttpRouteArrayInput` via:
//
//	HttpRouteArray{ HttpRouteArgs{...} }
type HttpRouteArrayInput interface {
	pulumi.Input

	ToHttpRouteArrayOutput() HttpRouteArrayOutput
	ToHttpRouteArrayOutputWithContext(context.Context) HttpRouteArrayOutput
}

type HttpRouteArray []HttpRouteInput

func (HttpRouteArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*HttpRoute)(nil)).Elem()
}

func (i HttpRouteArray) ToHttpRouteArrayOutput() HttpRouteArrayOutput {
	return i.ToHttpRouteArrayOutputWithContext(context.Background())
}

func (i HttpRouteArray) ToHttpRouteArrayOutputWithContext(ctx context.Context) HttpRouteArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HttpRouteArrayOutput)
}

// HttpRouteMapInput is an input type that accepts HttpRouteMap and HttpRouteMapOutput values.
// You can construct a concrete instance of `HttpRouteMapInput` via:
//
//	HttpRouteMap{ "key": HttpRouteArgs{...} }
type HttpRouteMapInput interface {
	pulumi.Input

	ToHttpRouteMapOutput() HttpRouteMapOutput
	ToHttpRouteMapOutputWithContext(context.Context) HttpRouteMapOutput
}

type HttpRouteMap map[string]HttpRouteInput

func (HttpRouteMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*HttpRoute)(nil)).Elem()
}

func (i HttpRouteMap) ToHttpRouteMapOutput() HttpRouteMapOutput {
	return i.ToHttpRouteMapOutputWithContext(context.Background())
}

func (i HttpRouteMap) ToHttpRouteMapOutputWithContext(ctx context.Context) HttpRouteMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HttpRouteMapOutput)
}

type HttpRouteOutput struct{ *pulumi.OutputState }

func (HttpRouteOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**HttpRoute)(nil)).Elem()
}

func (o HttpRouteOutput) ToHttpRouteOutput() HttpRouteOutput {
	return o
}

func (o HttpRouteOutput) ToHttpRouteOutputWithContext(ctx context.Context) HttpRouteOutput {
	return o
}

// Action triggered when all rules match
func (o HttpRouteOutput) Action() HttpRouteActionOutput {
	return o.ApplyT(func(v *HttpRoute) HttpRouteActionOutput { return v.Action }).(HttpRouteActionOutput)
}

// Human readable name for your route, this field is for you
func (o HttpRouteOutput) DisplayName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *HttpRoute) pulumi.StringPtrOutput { return v.DisplayName }).(pulumi.StringPtrOutput)
}

// Route traffic for this frontend
func (o HttpRouteOutput) FrontendId() pulumi.IntOutput {
	return o.ApplyT(func(v *HttpRoute) pulumi.IntOutput { return v.FrontendId }).(pulumi.IntOutput)
}

// List of rules to match to trigger action
func (o HttpRouteOutput) Rules() HttpRouteRuleTypeArrayOutput {
	return o.ApplyT(func(v *HttpRoute) HttpRouteRuleTypeArrayOutput { return v.Rules }).(HttpRouteRuleTypeArrayOutput)
}

// The internal name of your IP load balancing
func (o HttpRouteOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v *HttpRoute) pulumi.StringOutput { return v.ServiceName }).(pulumi.StringOutput)
}

// HTTP status code for "redirect" and "reject" actions
func (o HttpRouteOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *HttpRoute) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

// Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
func (o HttpRouteOutput) Weight() pulumi.IntOutput {
	return o.ApplyT(func(v *HttpRoute) pulumi.IntOutput { return v.Weight }).(pulumi.IntOutput)
}

type HttpRouteArrayOutput struct{ *pulumi.OutputState }

func (HttpRouteArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*HttpRoute)(nil)).Elem()
}

func (o HttpRouteArrayOutput) ToHttpRouteArrayOutput() HttpRouteArrayOutput {
	return o
}

func (o HttpRouteArrayOutput) ToHttpRouteArrayOutputWithContext(ctx context.Context) HttpRouteArrayOutput {
	return o
}

func (o HttpRouteArrayOutput) Index(i pulumi.IntInput) HttpRouteOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *HttpRoute {
		return vs[0].([]*HttpRoute)[vs[1].(int)]
	}).(HttpRouteOutput)
}

type HttpRouteMapOutput struct{ *pulumi.OutputState }

func (HttpRouteMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*HttpRoute)(nil)).Elem()
}

func (o HttpRouteMapOutput) ToHttpRouteMapOutput() HttpRouteMapOutput {
	return o
}

func (o HttpRouteMapOutput) ToHttpRouteMapOutputWithContext(ctx context.Context) HttpRouteMapOutput {
	return o
}

func (o HttpRouteMapOutput) MapIndex(k pulumi.StringInput) HttpRouteOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *HttpRoute {
		return vs[0].(map[string]*HttpRoute)[vs[1].(string)]
	}).(HttpRouteOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*HttpRouteInput)(nil)).Elem(), &HttpRoute{})
	pulumi.RegisterInputType(reflect.TypeOf((*HttpRouteArrayInput)(nil)).Elem(), HttpRouteArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*HttpRouteMapInput)(nil)).Elem(), HttpRouteMap{})
	pulumi.RegisterOutputType(HttpRouteOutput{})
	pulumi.RegisterOutputType(HttpRouteArrayOutput{})
	pulumi.RegisterOutputType(HttpRouteMapOutput{})
}
