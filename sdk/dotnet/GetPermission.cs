// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Frontegg
{
    public static class GetPermission
    {
        public static Task<GetPermissionResult> InvokeAsync(GetPermissionArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPermissionResult>("frontegg:index/getPermission:getPermission", args ?? new GetPermissionArgs(), options.WithDefaults());

        public static Output<GetPermissionResult> Invoke(GetPermissionInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetPermissionResult>("frontegg:index/getPermission:getPermission", args ?? new GetPermissionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPermissionArgs : Pulumi.InvokeArgs
    {
        [Input("key", required: true)]
        public string Key { get; set; } = null!;

        public GetPermissionArgs()
        {
        }
    }

    public sealed class GetPermissionInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        public GetPermissionInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetPermissionResult
    {
        public readonly string CategoryId;
        public readonly string CreatedAt;
        public readonly string Description;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Key;
        public readonly string Name;

        [OutputConstructor]
        private GetPermissionResult(
            string categoryId,

            string createdAt,

            string description,

            string id,

            string key,

            string name)
        {
            CategoryId = categoryId;
            CreatedAt = createdAt;
            Description = description;
            Id = id;
            Key = key;
            Name = name;
        }
    }
}
