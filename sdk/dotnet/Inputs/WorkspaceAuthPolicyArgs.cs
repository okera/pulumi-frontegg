// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Frontegg.Inputs
{

    public sealed class WorkspaceAuthPolicyArgs : Pulumi.ResourceArgs
    {
        [Input("allowSignups", required: true)]
        public Input<bool> AllowSignups { get; set; } = null!;

        [Input("allowUnverifiedUsers", required: true)]
        public Input<bool> AllowUnverifiedUsers { get; set; } = null!;

        [Input("enableApiTokens", required: true)]
        public Input<bool> EnableApiTokens { get; set; } = null!;

        [Input("enableRoles", required: true)]
        public Input<bool> EnableRoles { get; set; } = null!;

        [Input("jwtAccessTokenExpiration", required: true)]
        public Input<int> JwtAccessTokenExpiration { get; set; } = null!;

        [Input("jwtAlgorithm")]
        public Input<string>? JwtAlgorithm { get; set; }

        [Input("jwtPublicKey")]
        public Input<string>? JwtPublicKey { get; set; }

        [Input("jwtRefreshTokenExpiration", required: true)]
        public Input<int> JwtRefreshTokenExpiration { get; set; } = null!;

        [Input("sameSiteCookiePolicy", required: true)]
        public Input<string> SameSiteCookiePolicy { get; set; } = null!;

        public WorkspaceAuthPolicyArgs()
        {
        }
    }
}
