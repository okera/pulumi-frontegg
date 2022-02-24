module github.com/okera/pulumi-frontegg/provider

go 1.16

replace (
	github.com/frontegg/terraform-provider-frontegg => github.com/okera/terraform-provider-frontegg v0.2.21-0.20220224223401-a56b002fb4f7
	github.com/hashicorp/go-getter v1.5.0 => github.com/hashicorp/go-getter v1.4.0
	github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20211230170131-3a7c83bfab87
)

require (
	github.com/frontegg/terraform-provider-frontegg v0.2.20
	github.com/hashicorp/terraform-plugin-sdk v1.9.1 // indirect
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.19.0
	github.com/pulumi/pulumi/sdk/v3 v3.25.0
)
