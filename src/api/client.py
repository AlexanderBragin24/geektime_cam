"""
UniFi Video API client for camera management and streaming.

This module provides the main API client for communicating with UniFi Video servers,
handling authentication, camera discovery, and stream management.
"""


class UniFiVideoClient:
    """Main API client for UniFi Video server communication."""

    def __init__(self, server_url: str):
        """Initialize the API client.

        Args:
            server_url: The base URL of the UniFi Video server
        """
        self.server_url = server_url
        self.session_id = None

    # TODO: Implement authentication methods
    # TODO: Implement camera discovery
    # TODO: Implement stream URL retrieval
    # TODO: Implement server info retrieval
    pass