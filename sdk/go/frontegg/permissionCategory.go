// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package frontegg

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type PermissionCategory struct {
	pulumi.CustomResourceState

	// The timestamp at which the permission category was created.
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// A human-readable description of the permission category.
	Description pulumi.StringOutput `pulumi:"description"`
	// A human-readable name for the permission category.
	Name pulumi.StringOutput `pulumi:"name"`
}

// NewPermissionCategory registers a new resource with the given unique name, arguments, and options.
func NewPermissionCategory(ctx *pulumi.Context,
	name string, args *PermissionCategoryArgs, opts ...pulumi.ResourceOption) (*PermissionCategory, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Description == nil {
		return nil, errors.New("invalid value for required argument 'Description'")
	}
	var resource PermissionCategory
	err := ctx.RegisterResource("frontegg:index/permissionCategory:PermissionCategory", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPermissionCategory gets an existing PermissionCategory resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPermissionCategory(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PermissionCategoryState, opts ...pulumi.ResourceOption) (*PermissionCategory, error) {
	var resource PermissionCategory
	err := ctx.ReadResource("frontegg:index/permissionCategory:PermissionCategory", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PermissionCategory resources.
type permissionCategoryState struct {
	// The timestamp at which the permission category was created.
	CreatedAt *string `pulumi:"createdAt"`
	// A human-readable description of the permission category.
	Description *string `pulumi:"description"`
	// A human-readable name for the permission category.
	Name *string `pulumi:"name"`
}

type PermissionCategoryState struct {
	// The timestamp at which the permission category was created.
	CreatedAt pulumi.StringPtrInput
	// A human-readable description of the permission category.
	Description pulumi.StringPtrInput
	// A human-readable name for the permission category.
	Name pulumi.StringPtrInput
}

func (PermissionCategoryState) ElementType() reflect.Type {
	return reflect.TypeOf((*permissionCategoryState)(nil)).Elem()
}

type permissionCategoryArgs struct {
	// A human-readable description of the permission category.
	Description string `pulumi:"description"`
	// A human-readable name for the permission category.
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a PermissionCategory resource.
type PermissionCategoryArgs struct {
	// A human-readable description of the permission category.
	Description pulumi.StringInput
	// A human-readable name for the permission category.
	Name pulumi.StringPtrInput
}

func (PermissionCategoryArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*permissionCategoryArgs)(nil)).Elem()
}

type PermissionCategoryInput interface {
	pulumi.Input

	ToPermissionCategoryOutput() PermissionCategoryOutput
	ToPermissionCategoryOutputWithContext(ctx context.Context) PermissionCategoryOutput
}

func (*PermissionCategory) ElementType() reflect.Type {
	return reflect.TypeOf((**PermissionCategory)(nil)).Elem()
}

func (i *PermissionCategory) ToPermissionCategoryOutput() PermissionCategoryOutput {
	return i.ToPermissionCategoryOutputWithContext(context.Background())
}

func (i *PermissionCategory) ToPermissionCategoryOutputWithContext(ctx context.Context) PermissionCategoryOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PermissionCategoryOutput)
}

// PermissionCategoryArrayInput is an input type that accepts PermissionCategoryArray and PermissionCategoryArrayOutput values.
// You can construct a concrete instance of `PermissionCategoryArrayInput` via:
//
//          PermissionCategoryArray{ PermissionCategoryArgs{...} }
type PermissionCategoryArrayInput interface {
	pulumi.Input

	ToPermissionCategoryArrayOutput() PermissionCategoryArrayOutput
	ToPermissionCategoryArrayOutputWithContext(context.Context) PermissionCategoryArrayOutput
}

type PermissionCategoryArray []PermissionCategoryInput

func (PermissionCategoryArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*PermissionCategory)(nil)).Elem()
}

func (i PermissionCategoryArray) ToPermissionCategoryArrayOutput() PermissionCategoryArrayOutput {
	return i.ToPermissionCategoryArrayOutputWithContext(context.Background())
}

func (i PermissionCategoryArray) ToPermissionCategoryArrayOutputWithContext(ctx context.Context) PermissionCategoryArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PermissionCategoryArrayOutput)
}

// PermissionCategoryMapInput is an input type that accepts PermissionCategoryMap and PermissionCategoryMapOutput values.
// You can construct a concrete instance of `PermissionCategoryMapInput` via:
//
//          PermissionCategoryMap{ "key": PermissionCategoryArgs{...} }
type PermissionCategoryMapInput interface {
	pulumi.Input

	ToPermissionCategoryMapOutput() PermissionCategoryMapOutput
	ToPermissionCategoryMapOutputWithContext(context.Context) PermissionCategoryMapOutput
}

type PermissionCategoryMap map[string]PermissionCategoryInput

func (PermissionCategoryMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*PermissionCategory)(nil)).Elem()
}

func (i PermissionCategoryMap) ToPermissionCategoryMapOutput() PermissionCategoryMapOutput {
	return i.ToPermissionCategoryMapOutputWithContext(context.Background())
}

func (i PermissionCategoryMap) ToPermissionCategoryMapOutputWithContext(ctx context.Context) PermissionCategoryMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PermissionCategoryMapOutput)
}

type PermissionCategoryOutput struct{ *pulumi.OutputState }

func (PermissionCategoryOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PermissionCategory)(nil)).Elem()
}

func (o PermissionCategoryOutput) ToPermissionCategoryOutput() PermissionCategoryOutput {
	return o
}

func (o PermissionCategoryOutput) ToPermissionCategoryOutputWithContext(ctx context.Context) PermissionCategoryOutput {
	return o
}

type PermissionCategoryArrayOutput struct{ *pulumi.OutputState }

func (PermissionCategoryArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*PermissionCategory)(nil)).Elem()
}

func (o PermissionCategoryArrayOutput) ToPermissionCategoryArrayOutput() PermissionCategoryArrayOutput {
	return o
}

func (o PermissionCategoryArrayOutput) ToPermissionCategoryArrayOutputWithContext(ctx context.Context) PermissionCategoryArrayOutput {
	return o
}

func (o PermissionCategoryArrayOutput) Index(i pulumi.IntInput) PermissionCategoryOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *PermissionCategory {
		return vs[0].([]*PermissionCategory)[vs[1].(int)]
	}).(PermissionCategoryOutput)
}

type PermissionCategoryMapOutput struct{ *pulumi.OutputState }

func (PermissionCategoryMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*PermissionCategory)(nil)).Elem()
}

func (o PermissionCategoryMapOutput) ToPermissionCategoryMapOutput() PermissionCategoryMapOutput {
	return o
}

func (o PermissionCategoryMapOutput) ToPermissionCategoryMapOutputWithContext(ctx context.Context) PermissionCategoryMapOutput {
	return o
}

func (o PermissionCategoryMapOutput) MapIndex(k pulumi.StringInput) PermissionCategoryOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *PermissionCategory {
		return vs[0].(map[string]*PermissionCategory)[vs[1].(string)]
	}).(PermissionCategoryOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PermissionCategoryInput)(nil)).Elem(), &PermissionCategory{})
	pulumi.RegisterInputType(reflect.TypeOf((*PermissionCategoryArrayInput)(nil)).Elem(), PermissionCategoryArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*PermissionCategoryMapInput)(nil)).Elem(), PermissionCategoryMap{})
	pulumi.RegisterOutputType(PermissionCategoryOutput{})
	pulumi.RegisterOutputType(PermissionCategoryArrayOutput{})
	pulumi.RegisterOutputType(PermissionCategoryMapOutput{})
}
