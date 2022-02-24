// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Frontegg.Inputs
{

    public sealed class WorkspaceUserActivationEmailGetArgs : Pulumi.ResourceArgs
    {
        [Input("fromAddress", required: true)]
        public Input<string> FromAddress { get; set; } = null!;

        [Input("fromName", required: true)]
        public Input<string> FromName { get; set; } = null!;

        [Input("htmlTemplate", required: true)]
        public Input<string> HtmlTemplate { get; set; } = null!;

        [Input("redirectUrl")]
        public Input<string>? RedirectUrl { get; set; }

        [Input("subject", required: true)]
        public Input<string> Subject { get; set; } = null!;

        public WorkspaceUserActivationEmailGetArgs()
        {
        }
    }
}
