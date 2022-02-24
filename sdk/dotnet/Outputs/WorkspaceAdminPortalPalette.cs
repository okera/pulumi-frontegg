// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Frontegg.Outputs
{

    [OutputType]
    public sealed class WorkspaceAdminPortalPalette
    {
        public readonly string Error;
        public readonly string Info;
        public readonly string Primary;
        public readonly string PrimaryText;
        public readonly string Secondary;
        public readonly string SecondaryText;
        public readonly string Success;
        public readonly string Warning;

        [OutputConstructor]
        private WorkspaceAdminPortalPalette(
            string error,

            string info,

            string primary,

            string primaryText,

            string secondary,

            string secondaryText,

            string success,

            string warning)
        {
            Error = error;
            Info = info;
            Primary = primary;
            PrimaryText = primaryText;
            Secondary = secondary;
            SecondaryText = secondaryText;
            Success = success;
            Warning = warning;
        }
    }
}
