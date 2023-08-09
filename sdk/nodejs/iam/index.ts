// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { GetPoliciesResult } from "./getPolicies";
export const getPolicies: typeof import("./getPolicies").getPolicies = null as any;
utilities.lazyLoad(exports, ["getPolicies"], () => require("./getPolicies"));

export { GetPolicyArgs, GetPolicyResult, GetPolicyOutputArgs } from "./getPolicy";
export const getPolicy: typeof import("./getPolicy").getPolicy = null as any;
export const getPolicyOutput: typeof import("./getPolicy").getPolicyOutput = null as any;
utilities.lazyLoad(exports, ["getPolicy","getPolicyOutput"], () => require("./getPolicy"));

export { GetReferenceActionsArgs, GetReferenceActionsResult, GetReferenceActionsOutputArgs } from "./getReferenceActions";
export const getReferenceActions: typeof import("./getReferenceActions").getReferenceActions = null as any;
export const getReferenceActionsOutput: typeof import("./getReferenceActions").getReferenceActionsOutput = null as any;
utilities.lazyLoad(exports, ["getReferenceActions","getReferenceActionsOutput"], () => require("./getReferenceActions"));

export { GetReferenceResourceTypeResult } from "./getReferenceResourceType";
export const getReferenceResourceType: typeof import("./getReferenceResourceType").getReferenceResourceType = null as any;
utilities.lazyLoad(exports, ["getReferenceResourceType"], () => require("./getReferenceResourceType"));

export { PolicyArgs, PolicyState } from "./policy";
export type Policy = import("./policy").Policy;
export const Policy: typeof import("./policy").Policy = null as any;
utilities.lazyLoad(exports, ["Policy"], () => require("./policy"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "ovh:Iam/policy:Policy":
                return new Policy(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("ovh", "Iam/policy", _module)
