// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Frontegg.Inputs
{

    public sealed class WorkspaceFacebookSocialLoginGetArgs : Pulumi.ResourceArgs
    {
        [Input("clientId", required: true)]
        public Input<string> ClientId { get; set; } = null!;

        [Input("redirectUrl", required: true)]
        public Input<string> RedirectUrl { get; set; } = null!;

        [Input("secret", required: true)]
        public Input<string> Secret { get; set; } = null!;

        public WorkspaceFacebookSocialLoginGetArgs()
        {
        }
    }
}
