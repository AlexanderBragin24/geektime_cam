"""
Camera data model for the live view application.

This module defines the camera data model with properties for camera
information, streaming capabilities, and current state.
"""

from dataclasses import dataclass
from typing import Optional, List, Dict, Any
from enum import Enum


class CameraState(Enum):
    """Camera operational states."""
    ONLINE = "online"
    OFFLINE = "offline"
    RECORDING = "recording"
    MOTION_DETECTED = "motion_detected"
    ERROR = "error"


class RecordingMode(Enum):
    """Camera recording modes."""
    NEVER = "never"
    ALWAYS = "always"
    MOTION = "motion"
    SCHEDULED = "scheduled"


@dataclass
class StreamInfo:
    """Information about a camera stream."""
    channel: int
    width: int
    height: int
    fps: int
    bitrate: int
    codec: str
    url: str


@dataclass
class Camera:
    """Camera data model."""

    # Basic camera information
    camera_id: str
    name: str
    mac_address: str
    model: str
    firmware_version: str

    # Network information
    ip_address: str
    port: int

    # Status information
    state: CameraState
    is_connected: bool
    last_seen: Optional[str] = None

    # Recording settings
    recording_mode: RecordingMode = RecordingMode.MOTION
    is_recording: bool = False

    # Stream information
    streams: List[StreamInfo] = None

    # Additional properties
    properties: Dict[str, Any] = None

    def __post_init__(self):
        """Initialize default values after dataclass creation."""
        if self.streams is None:
            self.streams = []
        if self.properties is None:
            self.properties = {}

    @property
    def is_online(self) -> bool:
        """Check if camera is online.

        Returns:
            True if camera is online, False otherwise
        """
        return self.state == CameraState.ONLINE and self.is_connected

    @property
    def primary_stream(self) -> Optional[StreamInfo]:
        """Get the primary (highest quality) stream.

        Returns:
            Primary stream info or None if no streams available
        """
        if not self.streams:
            return None
        # TODO: Return highest quality stream (highest resolution/bitrate)
        return self.streams[0] if self.streams else None

    @property
    def secondary_stream(self) -> Optional[StreamInfo]:
        """Get the secondary (lower quality) stream.

        Returns:
            Secondary stream info or None if not available
        """
        if len(self.streams) < 2:
            return None
        # TODO: Return lower quality stream for bandwidth saving
        return self.streams[1] if len(self.streams) > 1 else None

    def get_stream_by_channel(self, channel: int) -> Optional[StreamInfo]:
        """Get stream information by channel number.

        Args:
            channel: Stream channel number

        Returns:
            Stream info for the specified channel or None if not found
        """
        # TODO: Find and return stream by channel number
        for stream in self.streams:
            if stream.channel == channel:
                return stream
        return None

    def update_state(self, new_state: CameraState):
        """Update camera state.

        Args:
            new_state: New camera state
        """
        # TODO: Update state and trigger any necessary callbacks
        self.state = new_state

    def update_connection_status(self, connected: bool):
        """Update camera connection status.

        Args:
            connected: Connection status
        """
        # TODO: Update connection status and related state
        self.is_connected = connected
        if not connected and self.state == CameraState.ONLINE:
            self.state = CameraState.OFFLINE

    def to_dict(self) -> Dict[str, Any]:
        """Convert camera to dictionary representation.

        Returns:
            Dictionary representation of camera
        """
        # TODO: Convert camera object to dictionary
        pass

    @classmethod
    def from_api_response(cls, api_data: Dict[str, Any]) -> 'Camera':
        """Create camera instance from API response data.

        Args:
            api_data: Camera data from UniFi Video API

        Returns:
            Camera instance
        """
        # TODO: Parse API response and create camera instance
        # TODO: Handle missing or optional fields
        pass