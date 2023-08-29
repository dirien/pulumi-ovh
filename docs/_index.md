---
title: OVH
meta_desc: Provides an overview of the OVH Provider for Pulumi.
layout: overview
---

The `OVH` provider for Pulumi can be used to provision any of the resources available in [OVHcloud](https://www.ovhcloud.com/fr/).
The `OVH` provider must be configured with credentials to deploy and update resources in `OVH`.

## Information

Note that the [lbrlabs Pulumi OVH provider](https://github.com/lbrlabs/pulumi-ovh) is replaced by this official one.

## Example

{{< chooser language "go,typescript,python" >}}
{{% choosable language go %}}

```golang
// Deploy a new Kubernetes cluster
myKube, err := cloudproject.NewKube(ctx, "my_desired_cluster", &cloudproject.KubeArgs{
    ServiceName: pulumi.String("xxxxxxxxxxxxx-xxxx-xxxx-xxxxxxxxx"),
    Name:        pulumi.String("my_desired_cluster"),
    Region:      pulumi.String("GRA5"),
})
if err != nil {
    return err
}

// Export kubeconfig file to a secret
ctx.Export("kubeconfig", pulumi.ToSecret(myKube.Kubeconfig))
```

{{% choosable language python %}}

```python
"""Get a Kubernetes cluster version"""
import pulumi
import scraly_pulumi_ovh as ovh

config = pulumi.Config();
service_name = config.require('serviceName')

print(service_name);

my_kube_cluster = ovh.cloudproject.get_kube(service_name=service_name,
    kube_id="xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx");
pulumi.export("version", my_kube_cluster.version)
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

import * as ovh from "@scraly/pulumi-ovh"

let config = new pulumi.Config();
let serviceName = config.require("serviceName")

console.log(serviceName)

// Get a Kubernetes cluster version
let myKubeCluster = ovh.cloudproject.getKube({
    serviceName: serviceName,
    kubeId: "xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx"
}) 
```

{{% /choosable %}}

{{< /chooser >}}
