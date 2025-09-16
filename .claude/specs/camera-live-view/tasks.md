# Tasks - Camera Live View

## Overview
This document defines the atomic implementation tasks for the camera live view feature. Each task is designed to be completable in 15-30 minutes by an experienced developer and touches 1-3 related files maximum. Tasks follow the component structure defined in design.md and leverage existing infrastructure from structure.md.

## Prerequisites
- Python 3.13.5 environment set up
- Project directory structure created per structure.md
- Environment variables configured (UNIFIVIDEO_HOST, UNIFIVIDEO_USERNAME, UNIFIVIDEO_PASSWORD)
- Required dependencies installed (FreeSimpleGUI, python-vlc, requests)

## Task Breakdown

### Phase 1: Foundation and Utilities (Leverage Existing Infrastructure)

#### Task 1.1: Create Core Directory Structure
- [x] 1.1. Create main source directories (`src/`, `tests/`, `config/`) per structure.md conventions
- [ ] **Files**: Create directories only, no files
- [ ] **Requirements**: Supports FR-all (foundational structure)
- [ ] **Leverages**: Directory organization from structure.md

#### Task 1.2: Create Module Package Structure
- [ ] 1.2. Create module directories (`src/api/`, `src/gui/`, `src/video/`, `src/models/`, `src/utils/`)
- [ ] **Files**: Module directories only
- [ ] **Requirements**: Supports FR-all (module organization)
- [ ] **Leverages**: Module patterns from structure.md

#### Task 1.3: Add Package Init Files
- [ ] 1.3. Create `__init__.py` files in all package directories
- [ ] **Files**: `src/__init__.py`, `src/api/__init__.py`, `src/gui/__init__.py`, `src/video/__init__.py`, `src/models/__init__.py`, `src/utils/__init__.py`
- [ ] **Requirements**: Supports Python package structure
- [ ] **Leverages**: Package import patterns from structure.md

#### Task 1.4: Create Configuration Manager Base
- [ ] 1.4. Create configuration utility class in `src/utils/config.py`
- [ ] **Files**: `src/utils/config.py`
- [ ] **Requirements**: Addresses TR-4 configuration management
- [ ] **Leverages**: Configuration patterns from structure.md

#### Task 1.5: Add Environment Variable Loading
- [ ] 1.5. Add environment variable loading to ConfigManager in `src/utils/config.py`
- [ ] **Files**: `src/utils/config.py` (enhancement)
- [ ] **Requirements**: Addresses NFR-16 credential storage
- [ ] **Leverages**: Environment handling patterns from structure.md

#### Task 1.6: Add Settings File Parsing
- [ ] 1.6. Add settings.ini parsing capability to ConfigManager in `src/utils/config.py`
- [ ] **Files**: `src/utils/config.py` (enhancement)
- [ ] **Requirements**: Addresses TR-4 runtime settings
- [ ] **Leverages**: File parsing utilities from structure.md

#### Task 1.7: Create Logger Infrastructure Base
- [ ] 1.7. Create logging utility class in `src/utils/logger.py`
- [ ] **Files**: `src/utils/logger.py`
- [ ] **Requirements**: Supports comprehensive logging from TR-4
- [ ] **Leverages**: Logging configuration patterns from structure.md

#### Task 1.8: Add Log Level Configuration
- [ ] 1.8. Add log level and output configuration to Logger in `src/utils/logger.py`
- [ ] **Files**: `src/utils/logger.py` (enhancement)
- [ ] **Requirements**: Supports debugging and monitoring
- [ ] **Leverages**: Logging hierarchy from structure.md

#### Task 1.9: Create Camera Data Model
- [ ] 1.9. Create Camera model class in `src/models/camera.py`
- [ ] **Files**: `src/models/camera.py`
- [ ] **Requirements**: Supports camera management from FR-1
- [ ] **Leverages**: Model patterns from structure.md

#### Task 1.10: Add Camera Status Enumeration
- [ ] 1.10. Add CameraStatus enum to `src/models/camera.py`
- [ ] **Files**: `src/models/camera.py` (enhancement)
- [ ] **Requirements**: Supports camera status tracking from NFR-12
- [ ] **Leverages**: Enum patterns from structure.md

#### Task 1.11: Create StreamInfo Data Model
- [ ] 1.11. Create StreamInfo model class in `src/models/streaming.py`
- [ ] **Files**: `src/models/streaming.py`
- [ ] **Requirements**: Supports stream performance monitoring from FR-5, NFR-3
- [ ] **Leverages**: Model patterns from structure.md

### Phase 2: API Integration Layer

#### Task 2.1: Create Authentication Manager Base
- [ ] 2.1. Create AuthManager class in `src/api/auth.py`
- [ ] **Files**: `src/api/auth.py`
- [ ] **Requirements**: Addresses FR-6 authentication
- [ ] **Leverages**: HTTP session patterns from structure.md

#### Task 2.2: Add Cookie Authentication
- [ ] 2.2. Add cookie-based authentication to AuthManager in `src/api/auth.py`
- [ ] **Files**: `src/api/auth.py` (enhancement)
- [ ] **Requirements**: Addresses AC-6 session management, NFR-16 credential storage
- [ ] **Leverages**: Security patterns from structure.md

#### Task 2.3: Add Session Management
- [ ] 2.3. Add session expiry and renewal to AuthManager in `src/api/auth.py`
- [ ] **Files**: `src/api/auth.py` (enhancement)
- [ ] **Requirements**: Addresses NFR-9 automatic session renewal
- [ ] **Leverages**: Session handling patterns from structure.md

#### Task 2.4: Create UniFi Video Client Base
- [ ] 2.4. Create UniFiClient class in `src/api/client.py`
- [ ] **Files**: `src/api/client.py`
- [ ] **Requirements**: Addresses TR-1 API integration
- [ ] **Leverages**: RESTful client patterns from structure.md

#### Task 2.5: Add Login Endpoint
- [ ] 2.5. Add login functionality to UniFiClient in `src/api/client.py`
- [ ] **Files**: `src/api/client.py` (enhancement)
- [ ] **Requirements**: Addresses AC-6 authentication integration
- [ ] **Leverages**: API patterns from unifivideo1.apib

#### Task 2.6: Add Camera Discovery
- [ ] 2.6. Add camera discovery endpoint to UniFiClient in `src/api/client.py`
- [ ] **Files**: `src/api/client.py` (enhancement)
- [ ] **Requirements**: Addresses FR-1 camera selection, AC-1 camera listing
- [ ] **Leverages**: API patterns from unifivideo1.apib

#### Task 2.7: Add Stream URL Retrieval
- [ ] 2.7. Add stream URL endpoint to UniFiClient in `src/api/client.py`
- [ ] **Files**: `src/api/client.py` (enhancement)
- [ ] **Requirements**: Addresses FR-5 stream quality, TR-2 video streaming
- [ ] **Leverages**: API patterns from unifivideo1.apib

#### Task 2.3: Add API Response Models
- [ ] Create API response models in `src/api/models.py`
- [ ] **Files**: `src/api/models.py`
- [ ] **Features**: Data classes for login response, camera list, stream URLs
- [ ] **Requirements**: Supports API response validation from TR-1
- [ ] **Leverages**: Model validation patterns from structure.md

#### Task 2.4: Implement API Error Handling
- [ ] Add API-specific error handling to `src/api/client.py`
- [ ] **Files**: `src/api/client.py` (enhancement)
- [ ] **Features**: Network retry logic, session expiry handling, rate limiting
- [ ] **Requirements**: Addresses AC-7 error handling and recovery
- [ ] **Leverages**: Error hierarchy from structure.md (GeekTimeCamError, APIError)

### Phase 3: Video Processing Layer

#### Task 3.1: Create VLC Camera Player
- [ ] Implement individual camera player in `src/video/player.py`
- [ ] **Files**: `src/video/player.py`
- [ ] **Features**: VLC MediaPlayer wrapper, RTSP stream handling, canvas embedding
- [ ] **Requirements**: Addresses TR-2 video streaming technology
- [ ] **Leverages**: Threading patterns from structure.md

#### Task 3.2: Implement Audio Controller
- [ ] Create audio management in `src/video/audio_controller.py`
- [ ] **Files**: `src/video/audio_controller.py`
- [ ] **Features**: Single-stream audio enforcement, mute/unmute, audio switching
- [ ] **Requirements**: Addresses FR-4 audio control and AC-4 audio management
- [ ] **Leverages**: State management patterns from structure.md

#### Task 3.3: Create Stream Manager
- [ ] Implement multi-stream coordinator in `src/video/stream_manager.py`
- [ ] **Files**: `src/video/stream_manager.py`
- [ ] **Features**: Stream lifecycle, multiple camera coordination, performance monitoring
- [ ] **Requirements**: Addresses FR-5 stream performance and NFR-1 latency requirements
- [ ] **Leverages**: Threading and resource management patterns from structure.md

#### Task 3.4: Add Stream Error Recovery
- [ ] Enhance StreamManager with error recovery in `src/video/stream_manager.py`
- [ ] **Files**: `src/video/stream_manager.py` (enhancement)
- [ ] **Features**: Automatic reconnection, stream restart, fallback to snapshots
- [ ] **Requirements**: Addresses AC-7 error handling and NFR-6 reliability
- [ ] **Leverages**: Error handling patterns from structure.md

### Phase 4: GUI Interface Layer

#### Task 4.1: Create Main Application Window
- [ ] Implement primary window in `src/gui/main_window.py`
- [ ] **Files**: `src/gui/main_window.py`
- [ ] **Features**: FreeSimpleGUI window initialization, layout management, event handling
- [ ] **Requirements**: Addresses TR-3 GUI framework integration
- [ ] **Leverages**: Configuration from ConfigManager utility

#### Task 4.2: Implement Camera Grid Layout
- [ ] Create grid display manager in `src/gui/camera_grid.py`
- [ ] **Files**: `src/gui/camera_grid.py`
- [ ] **Features**: Dynamic grid calculation, Canvas widget management, layout updates
- [ ] **Requirements**: Addresses FR-2 grid view and AC-2 grid layout
- [ ] **Leverages**: Layout utility functions from structure.md helpers

#### Task 4.3: Create Camera Selection Controls
- [ ] Implement user controls in `src/gui/controls.py`
- [ ] **Files**: `src/gui/controls.py`
- [ ] **Features**: Camera checkboxes, audio selector, view mode toggles, status indicators
- [ ] **Requirements**: Addresses FR-1 camera selection and AC-1 selection interface
- [ ] **Leverages**: Event handling patterns from structure.md

#### Task 4.4: Add View Mode Switching
- [ ] Enhance MainWindow with view modes in `src/gui/main_window.py`
- [ ] **Files**: `src/gui/main_window.py` (enhancement)
- [ ] **Features**: Grid/focus view switching, camera focus selection, layout adaptation
- [ ] **Requirements**: Addresses FR-3 focus view and AC-3 focus mode
- [ ] **Leverages**: Configuration persistence from ConfigManager

#### Task 4.5: Implement Status Indicators
- [ ] Add status display to controls in `src/gui/controls.py`
- [ ] **Files**: `src/gui/controls.py` (enhancement)
- [ ] **Features**: Connection status, stream health, audio indicators, error messages
- [ ] **Requirements**: Addresses NFR-12 visual indicators and user feedback
- [ ] **Leverages**: Logging infrastructure for status updates

### Phase 5: Integration and Application Entry

#### Task 5.1: Create Application Entry Point
- [ ] Implement main application in `src/main.py`
- [ ] **Files**: `src/main.py`
- [ ] **Features**: Application initialization, component wiring, cleanup on exit
- [ ] **Requirements**: Addresses application lifecycle management
- [ ] **Leverages**: All previous components and ConfigManager

#### Task 5.2: Integrate Components
- [ ] Wire components together in `src/main.py`
- [ ] **Files**: `src/main.py` (enhancement)
- [ ] **Features**: Dependency injection, component communication, event coordination
- [ ] **Requirements**: Addresses complete feature integration
- [ ] **Leverages**: All implemented components and error handling

#### Task 5.3: Add Application Configuration
- [ ] Create configuration files in `config/` directory
- [ ] **Files**: `config/settings.ini`, `config/logging.conf`
- [ ] **Features**: Default settings, logging configuration, environment template
- [ ] **Requirements**: Addresses TR-4 configuration management
- [ ] **Leverages**: Configuration patterns from structure.md

#### Task 5.4: Implement Graceful Shutdown
- [ ] Add cleanup and shutdown handling to `src/main.py`
- [ ] **Files**: `src/main.py` (enhancement)
- [ ] **Features**: Stream cleanup, resource disposal, session logout
- [ ] **Requirements**: Addresses NFR-20 session cleanup and resource management
- [ ] **Leverages**: Error handling and logging infrastructure

### Phase 6: Testing and Validation

#### Task 6.1: Create Unit Tests for API Layer
- [ ] Implement API tests in `tests/test_api/`
- [ ] **Files**: `tests/test_api/test_client.py`, `tests/test_api/test_auth.py`
- [ ] **Features**: Authentication tests, API client tests, mock responses
- [ ] **Requirements**: Addresses unit testing strategy from tech.md
- [ ] **Leverages**: Test structure patterns from structure.md

#### Task 6.2: Create Unit Tests for Video Layer
- [ ] Implement video tests in `tests/test_video/`
- [ ] **Files**: `tests/test_video/test_player.py`, `tests/test_video/test_stream_manager.py`
- [ ] **Features**: VLC integration tests, stream management tests, audio control tests
- [ ] **Requirements**: Addresses video streaming testing requirements
- [ ] **Leverages**: Mock fixtures from structure.md

#### Task 6.3: Create GUI Integration Tests
- [ ] Implement GUI tests in `tests/test_gui/`
- [ ] **Files**: `tests/test_gui/test_controls.py`, `tests/test_gui/test_main_window.py`
- [ ] **Features**: User interaction tests, layout tests, component integration
- [ ] **Requirements**: Addresses GUI validation from testing strategy
- [ ] **Leverages**: Test patterns from structure.md

#### Task 6.4: Create Test Fixtures and Mock Data
- [ ] Implement test fixtures in `tests/fixtures/`
- [ ] **Files**: `tests/fixtures/mock_responses.py`, `tests/fixtures/test_data.py`
- [ ] **Features**: Mock API responses, test camera data, configuration fixtures
- [ ] **Requirements**: Supports comprehensive testing coverage
- [ ] **Leverages**: Mock data patterns from structure.md

## Dependencies

### Task Dependencies
- **Phase 1** must complete before Phase 2 (foundation for API layer)
- **Phase 2** must complete before Phase 3 (API client needed for streams)
- **Phase 3** must complete before Phase 4 (video components needed for GUI)
- **Phase 4** must complete before Phase 5 (GUI components needed for integration)
- **Phase 5** must complete before Phase 6 (working application needed for testing)

### External Dependencies
- **UniFi Video NVR System**: Required for API testing and integration
- **VLC Media Player**: Must be installed on development system
- **Python Environment**: Python 3.13.5 with required packages
- **Network Access**: Connection to UniFi Video system for development testing

## Success Criteria

### Functional Completion
- [ ] All 6 functional requirements (FR-1 through FR-6) implemented and tested
- [ ] All 7 acceptance criteria (AC-1 through AC-7) verified
- [ ] All 20 non-functional requirements (NFR-1 through NFR-20) addressed

### Technical Validation
- [ ] Authentication working with UniFi Video API 2.0
- [ ] Multiple camera streams displaying simultaneously
- [ ] Audio control switching between cameras
- [ ] Grid and focus view modes functional
- [ ] Error handling and recovery working
- [ ] Performance targets met (<3s latency, 4+ streams)

### Code Quality
- [ ] All components follow structure.md conventions
- [ ] Type hints used throughout per tech.md requirements
- [ ] Comprehensive unit test coverage
- [ ] Logging and error handling implemented
- [ ] Configuration management working
- [ ] Clean shutdown and resource cleanup

## Implementation Notes

### Atomic Task Guidelines
- Each task should touch 1-3 files maximum
- Tasks are designed for 15-30 minute completion time
- Every task references specific requirements
- All tasks identify existing components to leverage
- Task order ensures proper dependency management

### Code Reuse Strategy
- Leverage ConfigManager, Logger, and Helpers from utils module
- Follow model patterns from structure.md
- Use established error hierarchy
- Build upon existing test structure
- Maintain consistency with project conventions