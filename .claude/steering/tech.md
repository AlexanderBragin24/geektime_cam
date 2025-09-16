# Technology Stack - GeekTime Cam

## Core Technologies

### Programming Language
- **Python 3.13.5** - Primary development language
- **Type Hints** - Use throughout codebase for better maintainability
- **PEP 8** - Follow Python style guide conventions

### GUI Framework
- **FreeSimpleGUI** - Main GUI library for user interface
- **Tkinter** - Underlying GUI framework (Fork from PySimpleGUI backend)
- **Canvas widgets** - For video display integration

### Video/Audio Processing
- **python-vlc** - Primary library for video/audio streaming
- **VLC Media Player** - Backend for RTSP/RTMP stream handling
- **Audio control** - Per-stream muting and audio selection

### API Integration
- **requests** - HTTP client for UniFi Video API 2.0
- **Cookie-based auth** - JSESSIONID_AV authentication
- **JSON processing** - Standard library json module

### Development Environment
- **Platform**: Windows (primary deployment target)
- **IDE**: Any Python-compatible IDE
- **Package Management**: pip/requirements.txt

## API Architecture

### UniFi Video API 2.0 Integration
- **Base URL**: Configurable via environment variables
- **Authentication**: Cookie-based (JSESSIONID_AV)
- **Endpoints**:
  - `/api/2.0/login` - Authentication
  - `/api/2.0/server/` - Server information
  - `/api/2.0/camera/` - Camera management
  - `/api/2.0/recording/` - Recording access
  - `/api/2.0/snapshot/camera/` - Live snapshots
  - `/api/2.0/stream/` - Stream URLs

### Streaming Protocols

## Configuration Management
- **Environment Variables**: Credentials and server configuration
- **Configuration files**: Application settings and preferences
- **Runtime settings**: Camera selections and view preferences

## Performance Considerations
- **Multi-threading**: Independent camera stream handling
- **Async operations**: Non-blocking GUI operations
- **Memory management**: Efficient video buffer handling
- **Stream optimization**: Adaptive quality based on available bandwidth

## Security Requirements
- **Credential protection**: Environment variable storage
- **Secure connections**: HTTPS/TLS for API communication
- **Session management**: Proper cookie handling and expiration
- **Input validation**: API response validation and error handling

## Error Handling
- **API errors**: Structured error response handling
- **Stream failures**: Automatic reconnection attempts
- **GUI exceptions**: User-friendly error messages
- **Logging**: Comprehensive error and operation logging

## Testing Strategy
- **Unit tests**: Core functionality and API integration
- **Integration tests**: Full workflow testing
- **Manual testing**: GUI and streaming verification
- **Error scenario testing**: Network failures and API errors