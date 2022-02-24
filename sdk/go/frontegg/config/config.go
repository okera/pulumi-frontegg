// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

// The Frontegg api url. Override to change region. Defaults to EU url.
func GetApiBaseUrl(ctx *pulumi.Context) string {
	return config.Get(ctx, "frontegg:apiBaseUrl")
}

// The client ID for a Frontegg portal API key.
func GetClientId(ctx *pulumi.Context) string {
	return config.Get(ctx, "frontegg:clientId")
}

// The Frontegg portal url. Override to change region. Defaults to EU url.
func GetPortalBaseUrl(ctx *pulumi.Context) string {
	return config.Get(ctx, "frontegg:portalBaseUrl")
}

// The corresponding secret key for the API key.
func GetSecretKey(ctx *pulumi.Context) string {
	return config.Get(ctx, "frontegg:secretKey")
}
