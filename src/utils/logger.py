"""
Logging setup and configuration for the camera live view application.

This module provides centralized logging configuration with support for
different log levels, file rotation, and console output.
"""

import logging
import logging.config
import os
from pathlib import Path
from typing import Optional


def setup_logging(config_file: str = "config/logging.conf",
                 log_level: str = "INFO",
                 log_dir: str = "logs") -> logging.Logger:
    """Setup application logging configuration.

    Args:
        config_file: Path to logging configuration file
        log_level: Default log level if config file not found
        log_dir: Directory for log files

    Returns:
        Configured logger instance
    """
    # Ensure log directory exists
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)

    config_path = Path(config_file)

    if config_path.exists():
        # Load logging configuration from file
        try:
            logging.config.fileConfig(config_path, disable_existing_loggers=False)
        except Exception as e:
            # Fallback to basic configuration
            _setup_basic_logging(log_level, log_dir)
    else:
        # Create default logging configuration
        _setup_basic_logging(log_level, log_dir)
        _create_default_logging_config(config_path)

    return logging.getLogger("geektime_cam")


def _setup_basic_logging(log_level: str, log_dir: str):
    """Setup basic logging configuration.

    Args:
        log_level: Logging level
        log_dir: Directory for log files
    """
    # TODO: Configure basic logging with console and file handlers
    # TODO: Set appropriate formatting
    # TODO: Configure log rotation
    pass


def _create_default_logging_config(config_path: Path):
    """Create default logging configuration file.

    Args:
        config_path: Path where to create the configuration file
    """
    # TODO: Create default logging.conf file
    # TODO: Include console and file handlers
    # TODO: Set appropriate formatters
    pass


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance with the specified name.

    Args:
        name: Logger name (usually module name)

    Returns:
        Logger instance
    """
    return logging.getLogger(f"geektime_cam.{name}")


class PerformanceLogger:
    """Context manager for performance logging."""

    def __init__(self, operation_name: str, logger: Optional[logging.Logger] = None):
        """Initialize performance logger.

        Args:
            operation_name: Name of the operation being timed
            logger: Logger instance to use
        """
        self.operation_name = operation_name
        self.logger = logger or get_logger("performance")
        self.start_time = None

    def __enter__(self):
        """Start timing the operation."""
        import time
        self.start_time = time.time()
        self.logger.debug(f"Starting operation: {self.operation_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """End timing and log the duration."""
        import time
        duration = time.time() - self.start_time
        if exc_type is None:
            self.logger.debug(f"Completed operation: {self.operation_name} in {duration:.3f}s")
        else:
            self.logger.error(f"Failed operation: {self.operation_name} after {duration:.3f}s")