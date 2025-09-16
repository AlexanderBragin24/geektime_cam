# Product Vision - GeekTime Cam

## Overview
Multi-camera surveillance viewer application for UniFi Video NVR systems, designed for business security monitoring and management.

## Target Users
- **Primary**: Security personnel and surveillance operators
- **Secondary**: Business administrators managing security systems
- **Use Case**: Professional business surveillance monitoring with real-time and historical video review capabilities

## Core Features

### Live Monitoring Mode
- Real-time video streaming from multiple UniFi cameras
- Selective camera viewing with checkbox controls
- Audio management (muted by default, selectable single camera audio)
- Dual view modes: grid view (all cameras equal size) and focus view (single camera enlarged)
- Motion detection based recording integration

### Playback Mode
- Historical video review with time period selection
- Multi-camera synchronized playback
- Timeline scrubber for temporal navigation
- Motion event based playback (skips empty periods)
- Selective camera playback with checkbox controls

### Technical Capabilities
- Cookie-based authentication with UniFi Video API 2.0
- RTSP/RTMP streaming protocol support
- Motion detection event filtering
- Real-time stream switching and audio control

## Business Objectives
- Provide efficient multi-camera surveillance monitoring
- Enable quick historical incident review
- Streamline security operations workflow
- Reduce time to identify and investigate security events

## Success Metrics
- Stable multi-camera streaming performance
- Intuitive operation for security personnel
- Reliable historical playback functionality
- Minimal learning curve for new operators

## Constraints
- Windows deployment environment
- UniFi Video NVR system dependency
- Motion detection based recording limitation
- Single audio stream limitation (one camera at a time)