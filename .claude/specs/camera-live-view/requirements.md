# Requirements - Camera Live View

## Introduction
This document defines the requirements for implementing the real-time camera live view feature that allows security personnel to monitor multiple UniFi Video cameras simultaneously with audio control and flexible display options. The feature enables multi-camera surveillance monitoring through a desktop GUI application that integrates with existing UniFi Video NVR systems, providing essential live monitoring capabilities for business security operations.

## Alignment with Product Vision
This camera live view feature directly supports the core product vision objectives from product.md:
- **Efficient Multi-Camera Surveillance Monitoring**: Enables real-time viewing of multiple camera streams simultaneously
- **Streamlined Security Operations Workflow**: Provides intuitive interface for security personnel with minimal learning curve
- **Quick Incident Response**: Low-latency live streaming ensures rapid response to security events
- **Professional Security Focus**: Designed specifically for security personnel and surveillance operators in business environments
- **Business Security Enhancement**: Integrates with existing UniFi Video infrastructure to maximize security coverage

## Functional Requirements

### FR-1: Camera Selection and Management
**As a** security operator
**I want** to select which cameras to display using checkboxes
**So that** I can customize my monitoring view to focus on relevant security areas

### FR-2: Grid View Display
**As a** security operator
**I want** to view all selected cameras in a grid layout with equal-sized displays
**So that** I can quickly scan all monitored areas at once

### FR-3: Focus View Display
**As a** security operator
**I want** to switch to a single-camera enlarged view mode
**So that** I can examine specific areas in detail when needed

### FR-4: Audio Control Management
**As a** security operator
**I want** to enable audio from one selected camera while keeping others muted
**So that** I can listen to audio from a specific area without audio interference

### FR-5: Stream Quality and Performance
**As a** security operator
**I want** reliable, low-latency video streams
**So that** I can respond quickly to security incidents in real-time

### FR-6: Authentication and Connection
**As a** security operator
**I want** to automatically authenticate with the UniFi Video system using stored credentials
**So that** I can access camera streams without manual login processes

## Acceptance Criteria

### AC-1: Camera Selection Interface
**WHEN** the live view interface is displayed
**THEN** all available cameras from the UniFi Video system are listed with checkboxes
**AND** each checkbox allows independent selection/deselection of cameras
**AND** selected cameras immediately appear in the display grid
**AND** deselected cameras are immediately removed from the display grid

### AC-2: Grid View Layout
**WHEN** multiple cameras are selected in grid view mode
**THEN** all cameras are displayed in an automatically arranged grid layout
**AND** each camera display shows equal-sized video feeds
**AND** the grid adjusts automatically based on the number of selected cameras
**AND** each camera display shows the camera name/identifier

### AC-3: Focus View Mode
**WHEN** a security operator switches to focus view mode
**THEN** a single selected camera is displayed in enlarged format
**AND** the operator can switch between different cameras for focus viewing
**AND** the transition between cameras is smooth and immediate
**AND** the enlarged view maintains proper aspect ratio

### AC-4: Audio Management
**WHEN** multiple cameras are streaming
**THEN** all cameras are muted by default
**AND** only one camera can have audio enabled at a time
**AND** enabling audio on one camera automatically mutes all others
**AND** audio control is clearly indicated in the interface
**AND** audio switching is immediate without stream interruption

### AC-5: Stream Performance
**WHEN** live streams are active
**THEN** video latency is less than 3 seconds from real-time
**AND** video maintains stable frame rate without frequent freezing
**AND** stream reconnection is automatic when network issues occur
**AND** multiple simultaneous streams do not significantly impact system performance

### AC-6: Authentication Integration
**WHEN** the application starts
**THEN** authentication with UniFi Video API happens automatically using environment credentials
**AND** successful authentication enables access to camera lists and streams
**AND** authentication failures are clearly reported to the user
**AND** session management handles cookie expiration gracefully

### AC-7: Error Handling and Recovery
**WHEN** network connectivity issues occur
**THEN** the system attempts automatic reconnection
**AND** users are notified of connection status changes
**AND** partial connectivity (some cameras working) is handled gracefully
**AND** error messages are clear and actionable for security operators

## Non-Functional Requirements

### Performance Requirements
- **NFR-1**: Video streams must maintain latency under 3 seconds from real-time
- **NFR-2**: System must support at least 4 simultaneous camera streams without performance degradation
- **NFR-3**: Video playback must maintain stable 15+ FPS for security monitoring needs
- **NFR-4**: User interface actions (view changes, audio switching) must respond within 1 second
- **NFR-5**: Memory usage must remain stable during extended operation periods (8+ hours)

### Reliability Requirements
- **NFR-6**: System must automatically attempt reconnection when network issues occur
- **NFR-7**: Stream failures must not affect other functioning camera streams
- **NFR-8**: Application must gracefully handle partial connectivity scenarios
- **NFR-9**: Session management must handle authentication cookie expiration automatically
- **NFR-10**: System must provide >99% uptime during normal operation conditions

### Usability Requirements
- **NFR-11**: Interface must require minimal training for security operators
- **NFR-12**: Visual indicators must clearly show camera status, audio state, and connection health
- **NFR-13**: Grid layout must automatically adjust based on number of selected cameras
- **NFR-14**: View mode transitions must be smooth and immediate
- **NFR-15**: Error messages must be clear and actionable for non-technical security operators

### Security Requirements
- **NFR-16**: Credentials must be stored in environment variables only (no embedded secrets)
- **NFR-17**: All API communications must use HTTPS/TLS when supported by UniFi Video system
- **NFR-18**: No local recording or storage of video streams is permitted
- **NFR-19**: Authentication must integrate with existing UniFi Video access control
- **NFR-20**: Session data must be properly cleared on application termination

## Technical Requirements

### TR-1: API Integration
- **Integration Point**: UniFi Video API 2.0 with cookie-based authentication (JSESSIONID_AV)
- **Endpoints Required**:
  - `/api/2.0/login` for authentication
  - `/api/2.0/camera/` for camera discovery and information
  - `/api/2.0/stream/` for RTSP/RTMP stream URLs
  - `/api/2.0/snapshot/camera/` for fallback static images
- **Authentication**: Environment variable-based credential storage
- **Session Management**: Automatic cookie handling and session renewal

### TR-2: Video Streaming Technology
- **Primary Library**: python-vlc for audio/video streaming
- **Stream Protocols**: RTSP/RTMP support for live video feeds
- **Performance**: Multi-threaded stream handling for independent camera processing
- **Audio Processing**: Per-stream audio control with VLC audio routing

### TR-3: GUI Framework Integration
- **Framework**: FreeSimpleGUI (fork of PySimpleGUI) with Tkinter backend
- **Video Integration**: Canvas widgets for embedding VLC media players
- **Layout Management**: Dynamic grid layout with responsive resizing
- **User Controls**: Checkbox selection, radio buttons for view modes, audio controls

### TR-4: Configuration and Settings
- **Environment Variables**:
  - `UNIFIVIDEO_HOST` - NVR server address
  - `UNIFIVIDEO_USERNAME` - API username
  - `UNIFIVIDEO_PASSWORD` - API password
- **Runtime Settings**: Camera selection preferences, view mode persistence
- **Logging**: Comprehensive operation and error logging

### TR-5: Performance and Resource Management
- **Memory Management**: Efficient video buffer handling for multiple streams
- **CPU Optimization**: Independent threading for each camera stream
- **Network Optimization**: Adaptive stream quality based on bandwidth
- **Resource Cleanup**: Proper stream termination and memory cleanup

## Constraints

### C-1: Platform and Environment
- **Operating System**: Windows-only deployment requirement
- **Python Version**: Python 3.13.5 with type hints throughout
- **Dependencies**: Must use FreeSimpleGUI and python-vlc as core technologies

### C-2: UniFi Video System Dependencies
- **API Version**: Must work with UniFi Video API 2.0 specification
- **Network Requirements**: Requires network access to UniFi Video NVR system
- **Authentication**: Limited to cookie-based authentication method
- **Stream Availability**: Dependent on camera motion detection recording settings

### C-3: Audio and Video Limitations
- **Single Audio Stream**: Only one camera can output audio at a time
- **Stream Protocol**: Limited to RTSP/RTMP protocols supported by UniFi Video
- **Real-time Constraints**: Live streaming only (no immediate playback functionality)
- **Video Quality**: Dependent on UniFi Video system stream quality settings

### C-4: User Interface Constraints
- **Display Technology**: Must integrate VLC players within FreeSimpleGUI canvas widgets
- **Layout Constraints**: Grid view limited by available screen real estate
- **Input Methods**: Desktop GUI interaction only (no mobile/web interface)
- **Accessibility**: Standard desktop accessibility features only

### C-5: Security and Compliance
- **Credential Storage**: Environment variables only (no embedded credentials)
- **Network Security**: Depends on UniFi Video system security configuration
- **Data Protection**: No local recording or storage of video streams
- **Access Control**: Authentication through UniFi Video system only

## Dependencies

### External Dependencies
- **UniFi Video NVR System**: Operational NVR with API 2.0 enabled
- **Network Connectivity**: Stable network connection to NVR system
- **Camera Hardware**: Configured UniFi cameras with streaming enabled
- **System Resources**: Adequate CPU/memory for multiple video streams

### Technical Dependencies
- **Python 3.13.5**: Core runtime environment
- **FreeSimpleGUI**: GUI framework for user interface
- **python-vlc**: Video/audio streaming library
- **requests**: HTTP client for API communication
- **VLC Media Player**: Backend media player for stream handling

## Success Criteria

### Functional Success
- [ ] Successfully authenticate with UniFi Video API using environment credentials
- [ ] Display list of available cameras with selection controls
- [ ] Stream multiple cameras simultaneously in grid view
- [ ] Switch between grid and focus view modes seamlessly
- [ ] Control audio output from individual cameras
- [ ] Handle network interruptions with automatic reconnection

### Performance Success
- [ ] Support at least 4 simultaneous camera streams without performance degradation
- [ ] Maintain video latency under 3 seconds for real-time monitoring
- [ ] Provide stable 15+ FPS video playback for security monitoring needs
- [ ] Respond to user interface actions (view changes, audio switching) within 1 second

### User Experience Success
- [ ] Intuitive interface requiring minimal training for security operators
- [ ] Clear visual indicators for camera status, audio state, and connection health
- [ ] Reliable operation during 8+ hour security shifts
- [ ] Minimal system resource impact allowing concurrent use of other security tools