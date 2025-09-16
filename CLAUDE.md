# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains API documentation for Unifi Video API version 2.0, documented in API Blueprint format (`.apib`). The project is a single documentation file that describes the RESTful API endpoints for managing Unifi Video servers, cameras, users, and recordings.

## Project Structure

- `unifivideo1.apib` - Complete API documentation in API Blueprint format covering:
  - Authentication using cookies (`JSESSIONID_AV`)
  - Server configuration and settings
  - User management and preferences
  - Camera management and configuration
  - Recording access and downloads
  - Live streaming endpoints

## Development Commands

This repository contains only documentation and does not have build scripts, package managers, or test frameworks. The primary file is meant to be consumed by API Blueprint tools or documentation generators.

## API Documentation Structure

The API documentation follows these key patterns:

### Authentication
- Uses cookie-based authentication with `JSESSIONID_AV`
- Login endpoint: `POST /api/2.0/login`
- All subsequent requests must include the authentication cookie

### Endpoint Patterns
- Server Info: `/api/2.0/server/(ServerId)`
- User Info: `/api/2.0/user/(UserId)`
- Camera Info: `/api/2.0/camera/(CameraId)`
- Recordings: `/api/2.0/recording/(RecordingId)`
- Snapshots: `/api/2.0/snapshot/camera/(CameraId)`
- Streams: `/api/2.0/stream/(CameraId)/(Channel)/url`

### Common Response Format
```json
{
  "data": [
    { /* response objects */ }
  ]
}
```

### Error Handling
- Returns 400 status for validation failures
- Error response includes `failedFieldName` and `fieldErrorCode`
- Missing required fields are clearly identified

## Key API Features

1. **Server Management** - Configure recording settings, system settings, email settings, and alert preferences
2. **User Management** - Manage user accounts, notification subscriptions, and access permissions
3. **Camera Control** - Get camera info, update settings, enable/disable recording modes
4. **Media Access** - Download recordings, get live snapshots, access streaming URLs
5. **Recording Management** - Access recording metadata and download video files

## Working with This Documentation

When making changes to the API documentation:
- Follow the existing API Blueprint format and structure
- Maintain consistent URL patterns and parameter naming
- Include complete request/response examples with realistic data
- Document all required headers (especially authentication cookies)
- Specify correct HTTP methods and status codes
- Include error response examples where applicable