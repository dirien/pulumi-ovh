// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vrack

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/scraly/pulumi-ovh/sdk/go/ovh"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "ovh:Vrack/cloudProject:CloudProject":
		r = &CloudProject{}
	case "ovh:Vrack/dedicatedServer:DedicatedServer":
		r = &DedicatedServer{}
	case "ovh:Vrack/dedicatedServerInterface:DedicatedServerInterface":
		r = &DedicatedServerInterface{}
	case "ovh:Vrack/ipAddress:IpAddress":
		r = &IpAddress{}
	case "ovh:Vrack/ipLoadbalancing:IpLoadbalancing":
		r = &IpLoadbalancing{}
	case "ovh:Vrack/vrack:Vrack":
		r = &Vrack{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := ovh.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"ovh",
		"Vrack/cloudProject",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ovh",
		"Vrack/dedicatedServer",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ovh",
		"Vrack/dedicatedServerInterface",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ovh",
		"Vrack/ipAddress",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ovh",
		"Vrack/ipLoadbalancing",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ovh",
		"Vrack/vrack",
		&module{version},
	)
}
