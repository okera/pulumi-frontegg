// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getPermission(args: GetPermissionArgs, opts?: pulumi.InvokeOptions): Promise<GetPermissionResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("frontegg:index/getPermission:getPermission", {
        "key": args.key,
    }, opts);
}

/**
 * A collection of arguments for invoking getPermission.
 */
export interface GetPermissionArgs {
    key: string;
}

/**
 * A collection of values returned by getPermission.
 */
export interface GetPermissionResult {
    readonly categoryId: string;
    readonly createdAt: string;
    readonly description: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly key: string;
    readonly name: string;
}

export function getPermissionOutput(args: GetPermissionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPermissionResult> {
    return pulumi.output(args).apply(a => getPermission(a, opts))
}

/**
 * A collection of arguments for invoking getPermission.
 */
export interface GetPermissionOutputArgs {
    key: pulumi.Input<string>;
}