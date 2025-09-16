"""
Mock API responses and test fixtures for unit tests.

This module provides mock responses for UniFi Video API endpoints
and common test fixtures used across test modules.
"""

from datetime import datetime, timedelta
from typing import Dict, List, Any


class MockAPIResponses:
    """Mock responses for UniFi Video API endpoints."""

    @staticmethod
    def login_success() -> Dict[str, Any]:
        """Mock successful login response."""
        return {
            "meta": {"rc": "ok"},
            "data": []
        }

    @staticmethod
    def login_failure() -> Dict[str, Any]:
        """Mock failed login response."""
        return {
            "meta": {
                "rc": "error",
                "msg": "Invalid username or password"
            },
            "data": []
        }

    @staticmethod
    def server_info() -> Dict[str, Any]:
        """Mock server information response."""
        return {
            "meta": {"rc": "ok"},
            "data": [{
                "_id": "server001",
                "name": "UniFi Video Server",
                "version": "3.10.13",
                "uptime": 86400,
                "storageInfo": {
                    "totalSpaceBytes": 1000000000000,
                    "usedSpaceBytes": 500000000000
                }
            }]
        }

    @staticmethod
    def camera_list() -> Dict[str, Any]:
        """Mock camera list response."""
        return {
            "meta": {"rc": "ok"},
            "data": [
                {
                    "_id": "camera001",
                    "name": "Front Door Camera",
                    "mac": "AA:BB:CC:DD:EE:FF",
                    "model": "UVC-G3-DOME",
                    "firmwareVersion": "4.25.3",
                    "ip": "192.168.1.100",
                    "port": 80,
                    "state": "CONNECTED",
                    "lastSeen": int(datetime.now().timestamp()),
                    "recordingSettings": {
                        "fullTimeRecordEnabled": False,
                        "motionRecordEnabled": True
                    },
                    "channels": [
                        {
                            "id": 0,
                            "name": "High",
                            "width": 1920,
                            "height": 1080,
                            "fps": 25,
                            "bitrate": 2000,
                            "codec": "h264"
                        },
                        {
                            "id": 1,
                            "name": "Medium",
                            "width": 1280,
                            "height": 720,
                            "fps": 15,
                            "bitrate": 1000,
                            "codec": "h264"
                        }
                    ]
                },
                {
                    "_id": "camera002",
                    "name": "Backyard Camera",
                    "mac": "FF:EE:DD:CC:BB:AA",
                    "model": "UVC-G3-BULLET",
                    "firmwareVersion": "4.25.3",
                    "ip": "192.168.1.101",
                    "port": 80,
                    "state": "CONNECTED",
                    "lastSeen": int(datetime.now().timestamp()),
                    "recordingSettings": {
                        "fullTimeRecordEnabled": True,
                        "motionRecordEnabled": True
                    },
                    "channels": [
                        {
                            "id": 0,
                            "name": "High",
                            "width": 1920,
                            "height": 1080,
                            "fps": 25,
                            "bitrate": 2000,
                            "codec": "h264"
                        }
                    ]
                }
            ]
        }

    @staticmethod
    def stream_url(camera_id: str, channel: int = 0) -> Dict[str, Any]:
        """Mock stream URL response."""
        return {
            "meta": {"rc": "ok"},
            "data": [{
                "url": f"rtsp://192.168.1.100:7447/{camera_id}_{channel}_avc_1920x1080_25fps"
            }]
        }

    @staticmethod
    def recordings_list(camera_id: str) -> Dict[str, Any]:
        """Mock recordings list response."""
        now = datetime.now()
        recordings = []

        # Generate some mock recordings
        for i in range(5):
            start_time = now - timedelta(hours=i+1)
            end_time = start_time + timedelta(minutes=30)

            recordings.append({
                "_id": f"recording{i:03d}",
                "cameraId": camera_id,
                "startTime": int(start_time.timestamp() * 1000),
                "endTime": int(end_time.timestamp() * 1000),
                "type": "motion" if i % 2 == 0 else "continuous",
                "locked": False,
                "inProgress": False,
                "eventType": "motionRecording",
                "rec": {
                    "filename": f"recording{i:03d}.mp4",
                    "filesize": 50000000 + (i * 10000000)
                }
            })

        return {
            "meta": {"rc": "ok"},
            "data": recordings
        }

    @staticmethod
    def snapshot_url(camera_id: str) -> str:
        """Mock snapshot URL."""
        return f"https://192.168.1.1:7443/api/2.0/snapshot/camera/{camera_id}?ts={int(datetime.now().timestamp())}"


class TestFixtures:
    """Common test fixtures and helper data."""

    @staticmethod
    def sample_camera_data() -> Dict[str, Any]:
        """Sample camera data for testing."""
        return {
            "camera_id": "camera001",
            "name": "Test Camera",
            "mac_address": "AA:BB:CC:DD:EE:FF",
            "model": "UVC-G3-DOME",
            "firmware_version": "4.25.3",
            "ip_address": "192.168.1.100",
            "port": 80,
            "is_connected": True,
            "recording_mode": "motion"
        }

    @staticmethod
    def sample_recording_data() -> Dict[str, Any]:
        """Sample recording data for testing."""
        now = datetime.now()
        return {
            "recording_id": "recording001",
            "camera_id": "camera001",
            "camera_name": "Test Camera",
            "start_time": now - timedelta(hours=1),
            "end_time": now - timedelta(minutes=30),
            "recording_type": "motion",
            "file_size_bytes": 50000000,
            "width": 1920,
            "height": 1080,
            "fps": 25
        }

    @staticmethod
    def sample_stream_info() -> Dict[str, Any]:
        """Sample stream information for testing."""
        return {
            "channel": 0,
            "width": 1920,
            "height": 1080,
            "fps": 25,
            "bitrate": 2000,
            "codec": "h264",
            "url": "rtsp://192.168.1.100:7447/camera001_0_avc_1920x1080_25fps"
        }

    @staticmethod
    def sample_timeline_events() -> List[Dict[str, Any]]:
        """Sample timeline events for testing."""
        now = datetime.now()
        return [
            {
                "timestamp": now - timedelta(minutes=45),
                "event_type": "motion",
                "duration_seconds": 30,
                "metadata": {"score": 0.8}
            },
            {
                "timestamp": now - timedelta(minutes=30),
                "event_type": "motion",
                "duration_seconds": 60,
                "metadata": {"score": 0.9}
            },
            {
                "timestamp": now - timedelta(minutes=15),
                "event_type": "recording_start",
                "metadata": {"recording_id": "recording001"}
            }
        ]


# HTTP status codes for testing
HTTP_STATUS = {
    "OK": 200,
    "BAD_REQUEST": 400,
    "UNAUTHORIZED": 401,
    "FORBIDDEN": 403,
    "NOT_FOUND": 404,
    "INTERNAL_SERVER_ERROR": 500
}

# Common test URLs
TEST_URLS = {
    "SERVER_BASE": "https://192.168.1.1:7443",
    "LOGIN": "https://192.168.1.1:7443/api/2.0/login",
    "CAMERAS": "https://192.168.1.1:7443/api/2.0/camera",
    "RECORDINGS": "https://192.168.1.1:7443/api/2.0/recording"
}