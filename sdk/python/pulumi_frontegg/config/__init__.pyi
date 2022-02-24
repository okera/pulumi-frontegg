# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

apiBaseUrl: Optional[str]
"""
The Frontegg api url. Override to change region. Defaults to EU url.
"""

clientId: Optional[str]
"""
The client ID for a Frontegg portal API key.
"""

portalBaseUrl: Optional[str]
"""
The Frontegg portal url. Override to change region. Defaults to EU url.
"""

secretKey: Optional[str]
"""
The corresponding secret key for the API key.
"""
