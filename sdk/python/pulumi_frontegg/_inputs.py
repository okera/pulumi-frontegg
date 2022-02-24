# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'WorkspaceAdminPortalArgs',
    'WorkspaceAdminPortalPaletteArgs',
    'WorkspaceAuthPolicyArgs',
    'WorkspaceCaptchaPolicyArgs',
    'WorkspaceFacebookSocialLoginArgs',
    'WorkspaceGithubSocialLoginArgs',
    'WorkspaceGoogleSocialLoginArgs',
    'WorkspaceHostedLoginArgs',
    'WorkspaceLockoutPolicyArgs',
    'WorkspaceMfaAuthenticationAppArgs',
    'WorkspaceMfaPolicyArgs',
    'WorkspaceMicrosoftSocialLoginArgs',
    'WorkspacePasswordPolicyArgs',
    'WorkspacePwnedPasswordEmailArgs',
    'WorkspaceResetPasswordEmailArgs',
    'WorkspaceSamlArgs',
    'WorkspaceUserActivationEmailArgs',
    'WorkspaceUserInvitationEmailArgs',
]

@pulumi.input_type
class WorkspaceAdminPortalArgs:
    def __init__(__self__, *,
                 enable_account_settings: pulumi.Input[bool],
                 enable_api_tokens: pulumi.Input[bool],
                 enable_audit_logs: pulumi.Input[bool],
                 enable_personal_api_tokens: pulumi.Input[bool],
                 enable_privacy: pulumi.Input[bool],
                 enable_profile: pulumi.Input[bool],
                 enable_roles: pulumi.Input[bool],
                 enable_security: pulumi.Input[bool],
                 enable_sso: pulumi.Input[bool],
                 enable_subscriptions: pulumi.Input[bool],
                 enable_usage: pulumi.Input[bool],
                 enable_users: pulumi.Input[bool],
                 enable_webhooks: pulumi.Input[bool],
                 palette: pulumi.Input['WorkspaceAdminPortalPaletteArgs']):
        pulumi.set(__self__, "enable_account_settings", enable_account_settings)
        pulumi.set(__self__, "enable_api_tokens", enable_api_tokens)
        pulumi.set(__self__, "enable_audit_logs", enable_audit_logs)
        pulumi.set(__self__, "enable_personal_api_tokens", enable_personal_api_tokens)
        pulumi.set(__self__, "enable_privacy", enable_privacy)
        pulumi.set(__self__, "enable_profile", enable_profile)
        pulumi.set(__self__, "enable_roles", enable_roles)
        pulumi.set(__self__, "enable_security", enable_security)
        pulumi.set(__self__, "enable_sso", enable_sso)
        pulumi.set(__self__, "enable_subscriptions", enable_subscriptions)
        pulumi.set(__self__, "enable_usage", enable_usage)
        pulumi.set(__self__, "enable_users", enable_users)
        pulumi.set(__self__, "enable_webhooks", enable_webhooks)
        pulumi.set(__self__, "palette", palette)

    @property
    @pulumi.getter(name="enableAccountSettings")
    def enable_account_settings(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable_account_settings")

    @enable_account_settings.setter
    def enable_account_settings(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_account_settings", value)

    @property
    @pulumi.getter(name="enableApiTokens")
    def enable_api_tokens(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable_api_tokens")

    @enable_api_tokens.setter
    def enable_api_tokens(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_api_tokens", value)

    @property
    @pulumi.getter(name="enableAuditLogs")
    def enable_audit_logs(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable_audit_logs")

    @enable_audit_logs.setter
    def enable_audit_logs(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_audit_logs", value)

    @property
    @pulumi.getter(name="enablePersonalApiTokens")
    def enable_personal_api_tokens(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable_personal_api_tokens")

    @enable_personal_api_tokens.setter
    def enable_personal_api_tokens(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_personal_api_tokens", value)

    @property
    @pulumi.getter(name="enablePrivacy")
    def enable_privacy(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable_privacy")

    @enable_privacy.setter
    def enable_privacy(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_privacy", value)

    @property
    @pulumi.getter(name="enableProfile")
    def enable_profile(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable_profile")

    @enable_profile.setter
    def enable_profile(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_profile", value)

    @property
    @pulumi.getter(name="enableRoles")
    def enable_roles(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable_roles")

    @enable_roles.setter
    def enable_roles(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_roles", value)

    @property
    @pulumi.getter(name="enableSecurity")
    def enable_security(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable_security")

    @enable_security.setter
    def enable_security(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_security", value)

    @property
    @pulumi.getter(name="enableSso")
    def enable_sso(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable_sso")

    @enable_sso.setter
    def enable_sso(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_sso", value)

    @property
    @pulumi.getter(name="enableSubscriptions")
    def enable_subscriptions(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable_subscriptions")

    @enable_subscriptions.setter
    def enable_subscriptions(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_subscriptions", value)

    @property
    @pulumi.getter(name="enableUsage")
    def enable_usage(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable_usage")

    @enable_usage.setter
    def enable_usage(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_usage", value)

    @property
    @pulumi.getter(name="enableUsers")
    def enable_users(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable_users")

    @enable_users.setter
    def enable_users(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_users", value)

    @property
    @pulumi.getter(name="enableWebhooks")
    def enable_webhooks(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable_webhooks")

    @enable_webhooks.setter
    def enable_webhooks(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_webhooks", value)

    @property
    @pulumi.getter
    def palette(self) -> pulumi.Input['WorkspaceAdminPortalPaletteArgs']:
        return pulumi.get(self, "palette")

    @palette.setter
    def palette(self, value: pulumi.Input['WorkspaceAdminPortalPaletteArgs']):
        pulumi.set(self, "palette", value)


@pulumi.input_type
class WorkspaceAdminPortalPaletteArgs:
    def __init__(__self__, *,
                 error: pulumi.Input[str],
                 info: pulumi.Input[str],
                 primary: pulumi.Input[str],
                 primary_text: pulumi.Input[str],
                 secondary: pulumi.Input[str],
                 secondary_text: pulumi.Input[str],
                 success: pulumi.Input[str],
                 warning: pulumi.Input[str]):
        pulumi.set(__self__, "error", error)
        pulumi.set(__self__, "info", info)
        pulumi.set(__self__, "primary", primary)
        pulumi.set(__self__, "primary_text", primary_text)
        pulumi.set(__self__, "secondary", secondary)
        pulumi.set(__self__, "secondary_text", secondary_text)
        pulumi.set(__self__, "success", success)
        pulumi.set(__self__, "warning", warning)

    @property
    @pulumi.getter
    def error(self) -> pulumi.Input[str]:
        return pulumi.get(self, "error")

    @error.setter
    def error(self, value: pulumi.Input[str]):
        pulumi.set(self, "error", value)

    @property
    @pulumi.getter
    def info(self) -> pulumi.Input[str]:
        return pulumi.get(self, "info")

    @info.setter
    def info(self, value: pulumi.Input[str]):
        pulumi.set(self, "info", value)

    @property
    @pulumi.getter
    def primary(self) -> pulumi.Input[str]:
        return pulumi.get(self, "primary")

    @primary.setter
    def primary(self, value: pulumi.Input[str]):
        pulumi.set(self, "primary", value)

    @property
    @pulumi.getter(name="primaryText")
    def primary_text(self) -> pulumi.Input[str]:
        return pulumi.get(self, "primary_text")

    @primary_text.setter
    def primary_text(self, value: pulumi.Input[str]):
        pulumi.set(self, "primary_text", value)

    @property
    @pulumi.getter
    def secondary(self) -> pulumi.Input[str]:
        return pulumi.get(self, "secondary")

    @secondary.setter
    def secondary(self, value: pulumi.Input[str]):
        pulumi.set(self, "secondary", value)

    @property
    @pulumi.getter(name="secondaryText")
    def secondary_text(self) -> pulumi.Input[str]:
        return pulumi.get(self, "secondary_text")

    @secondary_text.setter
    def secondary_text(self, value: pulumi.Input[str]):
        pulumi.set(self, "secondary_text", value)

    @property
    @pulumi.getter
    def success(self) -> pulumi.Input[str]:
        return pulumi.get(self, "success")

    @success.setter
    def success(self, value: pulumi.Input[str]):
        pulumi.set(self, "success", value)

    @property
    @pulumi.getter
    def warning(self) -> pulumi.Input[str]:
        return pulumi.get(self, "warning")

    @warning.setter
    def warning(self, value: pulumi.Input[str]):
        pulumi.set(self, "warning", value)


@pulumi.input_type
class WorkspaceAuthPolicyArgs:
    def __init__(__self__, *,
                 allow_signups: pulumi.Input[bool],
                 allow_unverified_users: pulumi.Input[bool],
                 enable_api_tokens: pulumi.Input[bool],
                 enable_roles: pulumi.Input[bool],
                 jwt_access_token_expiration: pulumi.Input[int],
                 jwt_refresh_token_expiration: pulumi.Input[int],
                 same_site_cookie_policy: pulumi.Input[str],
                 jwt_algorithm: Optional[pulumi.Input[str]] = None,
                 jwt_public_key: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "allow_signups", allow_signups)
        pulumi.set(__self__, "allow_unverified_users", allow_unverified_users)
        pulumi.set(__self__, "enable_api_tokens", enable_api_tokens)
        pulumi.set(__self__, "enable_roles", enable_roles)
        pulumi.set(__self__, "jwt_access_token_expiration", jwt_access_token_expiration)
        pulumi.set(__self__, "jwt_refresh_token_expiration", jwt_refresh_token_expiration)
        pulumi.set(__self__, "same_site_cookie_policy", same_site_cookie_policy)
        if jwt_algorithm is not None:
            pulumi.set(__self__, "jwt_algorithm", jwt_algorithm)
        if jwt_public_key is not None:
            pulumi.set(__self__, "jwt_public_key", jwt_public_key)

    @property
    @pulumi.getter(name="allowSignups")
    def allow_signups(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "allow_signups")

    @allow_signups.setter
    def allow_signups(self, value: pulumi.Input[bool]):
        pulumi.set(self, "allow_signups", value)

    @property
    @pulumi.getter(name="allowUnverifiedUsers")
    def allow_unverified_users(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "allow_unverified_users")

    @allow_unverified_users.setter
    def allow_unverified_users(self, value: pulumi.Input[bool]):
        pulumi.set(self, "allow_unverified_users", value)

    @property
    @pulumi.getter(name="enableApiTokens")
    def enable_api_tokens(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable_api_tokens")

    @enable_api_tokens.setter
    def enable_api_tokens(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_api_tokens", value)

    @property
    @pulumi.getter(name="enableRoles")
    def enable_roles(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable_roles")

    @enable_roles.setter
    def enable_roles(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_roles", value)

    @property
    @pulumi.getter(name="jwtAccessTokenExpiration")
    def jwt_access_token_expiration(self) -> pulumi.Input[int]:
        return pulumi.get(self, "jwt_access_token_expiration")

    @jwt_access_token_expiration.setter
    def jwt_access_token_expiration(self, value: pulumi.Input[int]):
        pulumi.set(self, "jwt_access_token_expiration", value)

    @property
    @pulumi.getter(name="jwtRefreshTokenExpiration")
    def jwt_refresh_token_expiration(self) -> pulumi.Input[int]:
        return pulumi.get(self, "jwt_refresh_token_expiration")

    @jwt_refresh_token_expiration.setter
    def jwt_refresh_token_expiration(self, value: pulumi.Input[int]):
        pulumi.set(self, "jwt_refresh_token_expiration", value)

    @property
    @pulumi.getter(name="sameSiteCookiePolicy")
    def same_site_cookie_policy(self) -> pulumi.Input[str]:
        return pulumi.get(self, "same_site_cookie_policy")

    @same_site_cookie_policy.setter
    def same_site_cookie_policy(self, value: pulumi.Input[str]):
        pulumi.set(self, "same_site_cookie_policy", value)

    @property
    @pulumi.getter(name="jwtAlgorithm")
    def jwt_algorithm(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "jwt_algorithm")

    @jwt_algorithm.setter
    def jwt_algorithm(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "jwt_algorithm", value)

    @property
    @pulumi.getter(name="jwtPublicKey")
    def jwt_public_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "jwt_public_key")

    @jwt_public_key.setter
    def jwt_public_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "jwt_public_key", value)


@pulumi.input_type
class WorkspaceCaptchaPolicyArgs:
    def __init__(__self__, *,
                 min_score: pulumi.Input[float],
                 secret_key: pulumi.Input[str],
                 site_key: pulumi.Input[str],
                 ignored_emails: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        pulumi.set(__self__, "min_score", min_score)
        pulumi.set(__self__, "secret_key", secret_key)
        pulumi.set(__self__, "site_key", site_key)
        if ignored_emails is not None:
            pulumi.set(__self__, "ignored_emails", ignored_emails)

    @property
    @pulumi.getter(name="minScore")
    def min_score(self) -> pulumi.Input[float]:
        return pulumi.get(self, "min_score")

    @min_score.setter
    def min_score(self, value: pulumi.Input[float]):
        pulumi.set(self, "min_score", value)

    @property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "secret_key")

    @secret_key.setter
    def secret_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret_key", value)

    @property
    @pulumi.getter(name="siteKey")
    def site_key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "site_key")

    @site_key.setter
    def site_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "site_key", value)

    @property
    @pulumi.getter(name="ignoredEmails")
    def ignored_emails(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "ignored_emails")

    @ignored_emails.setter
    def ignored_emails(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ignored_emails", value)


@pulumi.input_type
class WorkspaceFacebookSocialLoginArgs:
    def __init__(__self__, *,
                 client_id: pulumi.Input[str],
                 redirect_url: pulumi.Input[str],
                 secret: pulumi.Input[str]):
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "redirect_url", redirect_url)
        pulumi.set(__self__, "secret", secret)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> pulumi.Input[str]:
        return pulumi.get(self, "redirect_url")

    @redirect_url.setter
    def redirect_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "redirect_url", value)

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Input[str]:
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret", value)


@pulumi.input_type
class WorkspaceGithubSocialLoginArgs:
    def __init__(__self__, *,
                 client_id: pulumi.Input[str],
                 redirect_url: pulumi.Input[str],
                 secret: pulumi.Input[str]):
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "redirect_url", redirect_url)
        pulumi.set(__self__, "secret", secret)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> pulumi.Input[str]:
        return pulumi.get(self, "redirect_url")

    @redirect_url.setter
    def redirect_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "redirect_url", value)

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Input[str]:
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret", value)


@pulumi.input_type
class WorkspaceGoogleSocialLoginArgs:
    def __init__(__self__, *,
                 client_id: pulumi.Input[str],
                 redirect_url: pulumi.Input[str],
                 secret: pulumi.Input[str]):
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "redirect_url", redirect_url)
        pulumi.set(__self__, "secret", secret)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> pulumi.Input[str]:
        return pulumi.get(self, "redirect_url")

    @redirect_url.setter
    def redirect_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "redirect_url", value)

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Input[str]:
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret", value)


@pulumi.input_type
class WorkspaceHostedLoginArgs:
    def __init__(__self__, *,
                 allowed_redirect_urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        if allowed_redirect_urls is not None:
            pulumi.set(__self__, "allowed_redirect_urls", allowed_redirect_urls)

    @property
    @pulumi.getter(name="allowedRedirectUrls")
    def allowed_redirect_urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "allowed_redirect_urls")

    @allowed_redirect_urls.setter
    def allowed_redirect_urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_redirect_urls", value)


@pulumi.input_type
class WorkspaceLockoutPolicyArgs:
    def __init__(__self__, *,
                 max_attempts: pulumi.Input[int]):
        pulumi.set(__self__, "max_attempts", max_attempts)

    @property
    @pulumi.getter(name="maxAttempts")
    def max_attempts(self) -> pulumi.Input[int]:
        return pulumi.get(self, "max_attempts")

    @max_attempts.setter
    def max_attempts(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_attempts", value)


@pulumi.input_type
class WorkspaceMfaAuthenticationAppArgs:
    def __init__(__self__, *,
                 service_name: pulumi.Input[str]):
        pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)


@pulumi.input_type
class WorkspaceMfaPolicyArgs:
    def __init__(__self__, *,
                 allow_remember_device: pulumi.Input[bool],
                 device_expiration: pulumi.Input[int],
                 enforce: pulumi.Input[str]):
        pulumi.set(__self__, "allow_remember_device", allow_remember_device)
        pulumi.set(__self__, "device_expiration", device_expiration)
        pulumi.set(__self__, "enforce", enforce)

    @property
    @pulumi.getter(name="allowRememberDevice")
    def allow_remember_device(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "allow_remember_device")

    @allow_remember_device.setter
    def allow_remember_device(self, value: pulumi.Input[bool]):
        pulumi.set(self, "allow_remember_device", value)

    @property
    @pulumi.getter(name="deviceExpiration")
    def device_expiration(self) -> pulumi.Input[int]:
        return pulumi.get(self, "device_expiration")

    @device_expiration.setter
    def device_expiration(self, value: pulumi.Input[int]):
        pulumi.set(self, "device_expiration", value)

    @property
    @pulumi.getter
    def enforce(self) -> pulumi.Input[str]:
        return pulumi.get(self, "enforce")

    @enforce.setter
    def enforce(self, value: pulumi.Input[str]):
        pulumi.set(self, "enforce", value)


@pulumi.input_type
class WorkspaceMicrosoftSocialLoginArgs:
    def __init__(__self__, *,
                 client_id: pulumi.Input[str],
                 redirect_url: pulumi.Input[str],
                 secret: pulumi.Input[str]):
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "redirect_url", redirect_url)
        pulumi.set(__self__, "secret", secret)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> pulumi.Input[str]:
        return pulumi.get(self, "redirect_url")

    @redirect_url.setter
    def redirect_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "redirect_url", value)

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Input[str]:
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret", value)


@pulumi.input_type
class WorkspacePasswordPolicyArgs:
    def __init__(__self__, *,
                 allow_passphrases: pulumi.Input[bool],
                 history: pulumi.Input[int],
                 max_length: pulumi.Input[int],
                 min_length: pulumi.Input[int],
                 min_phrase_length: pulumi.Input[int],
                 min_tests: pulumi.Input[int]):
        pulumi.set(__self__, "allow_passphrases", allow_passphrases)
        pulumi.set(__self__, "history", history)
        pulumi.set(__self__, "max_length", max_length)
        pulumi.set(__self__, "min_length", min_length)
        pulumi.set(__self__, "min_phrase_length", min_phrase_length)
        pulumi.set(__self__, "min_tests", min_tests)

    @property
    @pulumi.getter(name="allowPassphrases")
    def allow_passphrases(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "allow_passphrases")

    @allow_passphrases.setter
    def allow_passphrases(self, value: pulumi.Input[bool]):
        pulumi.set(self, "allow_passphrases", value)

    @property
    @pulumi.getter
    def history(self) -> pulumi.Input[int]:
        return pulumi.get(self, "history")

    @history.setter
    def history(self, value: pulumi.Input[int]):
        pulumi.set(self, "history", value)

    @property
    @pulumi.getter(name="maxLength")
    def max_length(self) -> pulumi.Input[int]:
        return pulumi.get(self, "max_length")

    @max_length.setter
    def max_length(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_length", value)

    @property
    @pulumi.getter(name="minLength")
    def min_length(self) -> pulumi.Input[int]:
        return pulumi.get(self, "min_length")

    @min_length.setter
    def min_length(self, value: pulumi.Input[int]):
        pulumi.set(self, "min_length", value)

    @property
    @pulumi.getter(name="minPhraseLength")
    def min_phrase_length(self) -> pulumi.Input[int]:
        return pulumi.get(self, "min_phrase_length")

    @min_phrase_length.setter
    def min_phrase_length(self, value: pulumi.Input[int]):
        pulumi.set(self, "min_phrase_length", value)

    @property
    @pulumi.getter(name="minTests")
    def min_tests(self) -> pulumi.Input[int]:
        return pulumi.get(self, "min_tests")

    @min_tests.setter
    def min_tests(self, value: pulumi.Input[int]):
        pulumi.set(self, "min_tests", value)


@pulumi.input_type
class WorkspacePwnedPasswordEmailArgs:
    def __init__(__self__, *,
                 from_address: pulumi.Input[str],
                 from_name: pulumi.Input[str],
                 html_template: pulumi.Input[str],
                 subject: pulumi.Input[str],
                 redirect_url: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "from_address", from_address)
        pulumi.set(__self__, "from_name", from_name)
        pulumi.set(__self__, "html_template", html_template)
        pulumi.set(__self__, "subject", subject)
        if redirect_url is not None:
            pulumi.set(__self__, "redirect_url", redirect_url)

    @property
    @pulumi.getter(name="fromAddress")
    def from_address(self) -> pulumi.Input[str]:
        return pulumi.get(self, "from_address")

    @from_address.setter
    def from_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "from_address", value)

    @property
    @pulumi.getter(name="fromName")
    def from_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "from_name")

    @from_name.setter
    def from_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "from_name", value)

    @property
    @pulumi.getter(name="htmlTemplate")
    def html_template(self) -> pulumi.Input[str]:
        return pulumi.get(self, "html_template")

    @html_template.setter
    def html_template(self, value: pulumi.Input[str]):
        pulumi.set(self, "html_template", value)

    @property
    @pulumi.getter
    def subject(self) -> pulumi.Input[str]:
        return pulumi.get(self, "subject")

    @subject.setter
    def subject(self, value: pulumi.Input[str]):
        pulumi.set(self, "subject", value)

    @property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "redirect_url")

    @redirect_url.setter
    def redirect_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "redirect_url", value)


@pulumi.input_type
class WorkspaceResetPasswordEmailArgs:
    def __init__(__self__, *,
                 from_address: pulumi.Input[str],
                 from_name: pulumi.Input[str],
                 html_template: pulumi.Input[str],
                 subject: pulumi.Input[str],
                 redirect_url: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "from_address", from_address)
        pulumi.set(__self__, "from_name", from_name)
        pulumi.set(__self__, "html_template", html_template)
        pulumi.set(__self__, "subject", subject)
        if redirect_url is not None:
            pulumi.set(__self__, "redirect_url", redirect_url)

    @property
    @pulumi.getter(name="fromAddress")
    def from_address(self) -> pulumi.Input[str]:
        return pulumi.get(self, "from_address")

    @from_address.setter
    def from_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "from_address", value)

    @property
    @pulumi.getter(name="fromName")
    def from_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "from_name")

    @from_name.setter
    def from_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "from_name", value)

    @property
    @pulumi.getter(name="htmlTemplate")
    def html_template(self) -> pulumi.Input[str]:
        return pulumi.get(self, "html_template")

    @html_template.setter
    def html_template(self, value: pulumi.Input[str]):
        pulumi.set(self, "html_template", value)

    @property
    @pulumi.getter
    def subject(self) -> pulumi.Input[str]:
        return pulumi.get(self, "subject")

    @subject.setter
    def subject(self, value: pulumi.Input[str]):
        pulumi.set(self, "subject", value)

    @property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "redirect_url")

    @redirect_url.setter
    def redirect_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "redirect_url", value)


@pulumi.input_type
class WorkspaceSamlArgs:
    def __init__(__self__, *,
                 acs_url: pulumi.Input[str],
                 sp_entity_id: pulumi.Input[str]):
        pulumi.set(__self__, "acs_url", acs_url)
        pulumi.set(__self__, "sp_entity_id", sp_entity_id)

    @property
    @pulumi.getter(name="acsUrl")
    def acs_url(self) -> pulumi.Input[str]:
        return pulumi.get(self, "acs_url")

    @acs_url.setter
    def acs_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "acs_url", value)

    @property
    @pulumi.getter(name="spEntityId")
    def sp_entity_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "sp_entity_id")

    @sp_entity_id.setter
    def sp_entity_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "sp_entity_id", value)


@pulumi.input_type
class WorkspaceUserActivationEmailArgs:
    def __init__(__self__, *,
                 from_address: pulumi.Input[str],
                 from_name: pulumi.Input[str],
                 html_template: pulumi.Input[str],
                 subject: pulumi.Input[str],
                 redirect_url: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "from_address", from_address)
        pulumi.set(__self__, "from_name", from_name)
        pulumi.set(__self__, "html_template", html_template)
        pulumi.set(__self__, "subject", subject)
        if redirect_url is not None:
            pulumi.set(__self__, "redirect_url", redirect_url)

    @property
    @pulumi.getter(name="fromAddress")
    def from_address(self) -> pulumi.Input[str]:
        return pulumi.get(self, "from_address")

    @from_address.setter
    def from_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "from_address", value)

    @property
    @pulumi.getter(name="fromName")
    def from_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "from_name")

    @from_name.setter
    def from_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "from_name", value)

    @property
    @pulumi.getter(name="htmlTemplate")
    def html_template(self) -> pulumi.Input[str]:
        return pulumi.get(self, "html_template")

    @html_template.setter
    def html_template(self, value: pulumi.Input[str]):
        pulumi.set(self, "html_template", value)

    @property
    @pulumi.getter
    def subject(self) -> pulumi.Input[str]:
        return pulumi.get(self, "subject")

    @subject.setter
    def subject(self, value: pulumi.Input[str]):
        pulumi.set(self, "subject", value)

    @property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "redirect_url")

    @redirect_url.setter
    def redirect_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "redirect_url", value)


@pulumi.input_type
class WorkspaceUserInvitationEmailArgs:
    def __init__(__self__, *,
                 from_address: pulumi.Input[str],
                 from_name: pulumi.Input[str],
                 html_template: pulumi.Input[str],
                 subject: pulumi.Input[str],
                 redirect_url: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "from_address", from_address)
        pulumi.set(__self__, "from_name", from_name)
        pulumi.set(__self__, "html_template", html_template)
        pulumi.set(__self__, "subject", subject)
        if redirect_url is not None:
            pulumi.set(__self__, "redirect_url", redirect_url)

    @property
    @pulumi.getter(name="fromAddress")
    def from_address(self) -> pulumi.Input[str]:
        return pulumi.get(self, "from_address")

    @from_address.setter
    def from_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "from_address", value)

    @property
    @pulumi.getter(name="fromName")
    def from_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "from_name")

    @from_name.setter
    def from_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "from_name", value)

    @property
    @pulumi.getter(name="htmlTemplate")
    def html_template(self) -> pulumi.Input[str]:
        return pulumi.get(self, "html_template")

    @html_template.setter
    def html_template(self, value: pulumi.Input[str]):
        pulumi.set(self, "html_template", value)

    @property
    @pulumi.getter
    def subject(self) -> pulumi.Input[str]:
        return pulumi.get(self, "subject")

    @subject.setter
    def subject(self, value: pulumi.Input[str]):
        pulumi.set(self, "subject", value)

    @property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "redirect_url")

    @redirect_url.setter
    def redirect_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "redirect_url", value)


