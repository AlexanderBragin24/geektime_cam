# Project Structure - GeekTime Cam

## Directory Organization

```
geektime_cam/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   ├── client.py          # UniFi Video API client
│   │   ├── models.py          # Data models for API responses
│   │   └── auth.py            # Authentication handling
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── main_window.py     # Main application window
│   │   ├── camera_grid.py     # Camera display grid
│   │   ├── controls.py        # GUI controls and widgets
│   │   └── dialogs.py         # Modal dialogs and settings
│   ├── video/
│   │   ├── __init__.py
│   │   ├── player.py          # VLC media player wrapper
│   │   ├── stream_manager.py  # Stream coordination
│   │   └── audio_controller.py # Audio management
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py          # Configuration management
│   │   ├── logger.py          # Logging setup
│   │   └── helpers.py         # Utility functions
│   └── models/
│       ├── __init__.py
│       ├── camera.py          # Camera data model
│       ├── recording.py       # Recording data model
│       └── timeline.py        # Playback timeline model
├── tests/
│   ├── __init__.py
│   ├── test_api/
│   │   ├── test_client.py
│   │   └── test_auth.py
│   ├── test_gui/
│   │   └── test_controls.py
│   ├── test_video/
│   │   └── test_player.py
│   └── fixtures/
│       └── mock_responses.py
├── config/
│   ├── settings.ini           # Application settings
│   └── logging.conf           # Logging configuration
├── docs/
│   └── unifivideo1.apib       # API documentation
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
├── .gitignore
├── README.md
└── CLAUDE.md                 # Development guidelines
```

## Naming Conventions

### Files and Directories
- **Snake_case** for Python files and directories
- **Lowercase** for package directories
- **CamelCase** for class names
- **UPPERCASE** for constants

### Code Conventions
- **Function names**: `snake_case`
- **Variable names**: `snake_case`
- **Class names**: `CamelCase`
- **Constants**: `UPPER_CASE`
- **Private methods**: `_leading_underscore`

### API Integration Patterns
- **Response models**: Match API structure with Python naming
- **Error handling**: Consistent exception hierarchy
- **Configuration keys**: `SECTION.key_name` format

## Module Responsibilities

### API Module (`src/api/`)
- **client.py**: Main API client with session management
- **models.py**: Pydantic models for API responses
- **auth.py**: Authentication flow and cookie management

### GUI Module (`src/gui/`)
- **main_window.py**: Primary application window and layout
- **camera_grid.py**: Video display grid management
- **controls.py**: Control panels and user interactions
- **dialogs.py**: Settings, login, and configuration dialogs

### Video Module (`src/video/`)
- **player.py**: VLC media player abstraction
- **stream_manager.py**: Multi-stream coordination and lifecycle
- **audio_controller.py**: Audio routing and mute management

### Utils Module (`src/utils/`)
- **config.py**: Configuration loading and management
- **logger.py**: Logging configuration and utilities
- **helpers.py**: Common utility functions

### Models Module (`src/models/`)
- **camera.py**: Camera entity and state management
- **recording.py**: Recording metadata and access
- **timeline.py**: Playback timeline and synchronization

## Testing Patterns

### Test Structure
- Mirror source structure in `tests/` directory
- `test_` prefix for all test files
- `Test` prefix for test classes
- `test_` prefix for test methods

### Test Categories
- **Unit tests**: Individual function/method testing
- **Integration tests**: API and component interaction
- **GUI tests**: User interface validation
- **Mock data**: Consistent test fixtures

## Configuration Management

### Environment Variables
- `UNIFIVIDEO_HOST` - NVR server address
- `UNIFIVIDEO_USERNAME` - API username
- `UNIFIVIDEO_PASSWORD` - API password
- `LOG_LEVEL` - Application logging level

### Settings Files
- **settings.ini**: User preferences and application settings
- **logging.conf**: Logging configuration and output settings
- **.env**: Local environment variable overrides

## Import Patterns

### Internal Imports
```python
# Relative imports within package
from .models import Camera
from ..api.client import UniFiVideoClient

# Absolute imports from project root
from src.utils.config import get_setting
from src.models.camera import Camera
```

### External Dependencies
```python
# Standard library first
import os
import json
from typing import List, Dict, Optional

# Third-party libraries second
import vlc
import PySimpleGUI as sg
import requests

# Local imports last
from src.api.client import UniFiVideoClient
```

## Error Handling Conventions

### Exception Hierarchy
- **Base**: `GeekTimeCamError`
- **API errors**: `APIError`, `AuthenticationError`
- **Video errors**: `StreamError`, `PlayerError`
- **GUI errors**: `GUIError`, `ConfigurationError`

### Logging Standards
- **DEBUG**: Detailed operation information
- **INFO**: Normal operation milestones
- **WARNING**: Recoverable issues
- **ERROR**: Operation failures
- **CRITICAL**: Application-level failures