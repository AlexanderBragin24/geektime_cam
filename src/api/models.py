"""
Data models for API responses from UniFi Video server.

This module defines data classes and models for structured handling of
API responses from the UniFi Video server endpoints.
"""

from dataclasses import dataclass
from typing import List, Optional, Dict, Any


@dataclass
class ServerInfo:
    """Server information model."""
    # TODO: Define server info fields based on API response
    pass


@dataclass
class CameraInfo:
    """Camera information model."""
    # TODO: Define camera info fields based on API response
    pass


@dataclass
class RecordingInfo:
    """Recording information model."""
    # TODO: Define recording info fields based on API response
    pass


@dataclass
class StreamInfo:
    """Stream information model."""
    # TODO: Define stream info fields based on API response
    pass