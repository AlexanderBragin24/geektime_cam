"""
Recording data model for the live view application.

This module defines the recording data model with properties for recording
metadata, playback information, and file management.
"""

from dataclasses import dataclass
from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum


class RecordingType(Enum):
    """Types of recordings."""
    MOTION = "motion"
    CONTINUOUS = "continuous"
    MANUAL = "manual"
    SCHEDULED = "scheduled"


class RecordingStatus(Enum):
    """Recording status."""
    AVAILABLE = "available"
    RECORDING = "recording"
    PROCESSING = "processing"
    CORRUPTED = "corrupted"
    DELETED = "deleted"


@dataclass
class Recording:
    """Recording data model."""

    # Basic recording information
    recording_id: str
    camera_id: str
    camera_name: str

    # Timing information
    start_time: datetime
    end_time: Optional[datetime] = None
    duration_seconds: Optional[int] = None

    # Recording properties
    recording_type: RecordingType = RecordingType.MOTION
    status: RecordingStatus = RecordingStatus.AVAILABLE

    # File information
    file_size_bytes: Optional[int] = None
    file_path: Optional[str] = None
    thumbnail_path: Optional[str] = None

    # Video properties
    width: Optional[int] = None
    height: Optional[int] = None
    fps: Optional[int] = None
    bitrate: Optional[int] = None
    codec: Optional[str] = None

    # Motion detection metadata
    motion_events: Optional[list] = None
    motion_score: Optional[float] = None

    # Additional metadata
    metadata: Dict[str, Any] = None

    def __post_init__(self):
        """Initialize default values after dataclass creation."""
        if self.metadata is None:
            self.metadata = {}
        if self.motion_events is None:
            self.motion_events = []

        # Calculate duration if not provided
        if self.duration_seconds is None and self.end_time:
            delta = self.end_time - self.start_time
            self.duration_seconds = int(delta.total_seconds())

    @property
    def is_active(self) -> bool:
        """Check if recording is currently active.

        Returns:
            True if recording is in progress, False otherwise
        """
        return self.status == RecordingStatus.RECORDING

    @property
    def is_available(self) -> bool:
        """Check if recording is available for playback.

        Returns:
            True if recording can be played, False otherwise
        """
        return self.status == RecordingStatus.AVAILABLE

    @property
    def formatted_duration(self) -> str:
        """Get formatted duration string.

        Returns:
            Formatted duration (e.g., "1h 23m 45s")
        """
        if not self.duration_seconds:
            return "Unknown"

        # TODO: Format duration in human readable format
        hours = self.duration_seconds // 3600
        minutes = (self.duration_seconds % 3600) // 60
        seconds = self.duration_seconds % 60

        if hours > 0:
            return f"{hours}h {minutes}m {seconds}s"
        elif minutes > 0:
            return f"{minutes}m {seconds}s"
        else:
            return f"{seconds}s"

    @property
    def formatted_file_size(self) -> str:
        """Get formatted file size string.

        Returns:
            Formatted file size (e.g., "1.5 MB")
        """
        if not self.file_size_bytes:
            return "Unknown"

        # TODO: Format file size in human readable format
        # Simple implementation - could be moved to helpers
        for unit in ['B', 'KB', 'MB', 'GB']:
            if self.file_size_bytes < 1024.0:
                return f"{self.file_size_bytes:.1f} {unit}"
            self.file_size_bytes /= 1024.0
        return f"{self.file_size_bytes:.1f} TB"

    def has_motion_events(self) -> bool:
        """Check if recording has motion events.

        Returns:
            True if motion events are present, False otherwise
        """
        return bool(self.motion_events and len(self.motion_events) > 0)

    def get_download_url(self, base_url: str) -> str:
        """Get download URL for the recording.

        Args:
            base_url: Base URL of the UniFi Video server

        Returns:
            Complete download URL for the recording
        """
        # TODO: Construct download URL based on API specification
        return f"{base_url}/api/2.0/recording/{self.recording_id}/download"

    def to_dict(self) -> Dict[str, Any]:
        """Convert recording to dictionary representation.

        Returns:
            Dictionary representation of recording
        """
        # TODO: Convert recording object to dictionary
        # TODO: Handle datetime serialization
        pass

    @classmethod
    def from_api_response(cls, api_data: Dict[str, Any]) -> 'Recording':
        """Create recording instance from API response data.

        Args:
            api_data: Recording data from UniFi Video API

        Returns:
            Recording instance
        """
        # TODO: Parse API response and create recording instance
        # TODO: Handle datetime parsing
        # TODO: Handle missing or optional fields
        pass