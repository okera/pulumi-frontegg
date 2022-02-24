// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export * from "./allowedOrigin";
export * from "./getPermission";
export * from "./permission";
export * from "./permissionCategory";
export * from "./provider";
export * from "./redirectUri";
export * from "./role";
export * from "./tenant";
export * from "./webhook";
export * from "./workspace";

// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

// Import resources to register:
import { AllowedOrigin } from "./allowedOrigin";
import { Permission } from "./permission";
import { PermissionCategory } from "./permissionCategory";
import { RedirectUri } from "./redirectUri";
import { Role } from "./role";
import { Tenant } from "./tenant";
import { Webhook } from "./webhook";
import { Workspace } from "./workspace";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "frontegg:index/allowedOrigin:AllowedOrigin":
                return new AllowedOrigin(name, <any>undefined, { urn })
            case "frontegg:index/permission:Permission":
                return new Permission(name, <any>undefined, { urn })
            case "frontegg:index/permissionCategory:PermissionCategory":
                return new PermissionCategory(name, <any>undefined, { urn })
            case "frontegg:index/redirectUri:RedirectUri":
                return new RedirectUri(name, <any>undefined, { urn })
            case "frontegg:index/role:Role":
                return new Role(name, <any>undefined, { urn })
            case "frontegg:index/tenant:Tenant":
                return new Tenant(name, <any>undefined, { urn })
            case "frontegg:index/webhook:Webhook":
                return new Webhook(name, <any>undefined, { urn })
            case "frontegg:index/workspace:Workspace":
                return new Workspace(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("frontegg", "index/allowedOrigin", _module)
pulumi.runtime.registerResourceModule("frontegg", "index/permission", _module)
pulumi.runtime.registerResourceModule("frontegg", "index/permissionCategory", _module)
pulumi.runtime.registerResourceModule("frontegg", "index/redirectUri", _module)
pulumi.runtime.registerResourceModule("frontegg", "index/role", _module)
pulumi.runtime.registerResourceModule("frontegg", "index/tenant", _module)
pulumi.runtime.registerResourceModule("frontegg", "index/webhook", _module)
pulumi.runtime.registerResourceModule("frontegg", "index/workspace", _module)

import { Provider } from "./provider";

pulumi.runtime.registerResourcePackage("frontegg", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:frontegg") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
