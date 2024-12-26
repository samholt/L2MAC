"""
logging.py

This module provides utilities for setting up logging in multiprocessing 
environments. It includes functions to generate log file paths and create 
loggers that support both console and file output. These utilities are designed 
to facilitate structured and consistent logging across different processes.

Key Functions:
1. **generate_log_file_path**:
   - Generates a timestamped log file path within a specified folder.
   - Ensures the log directory exists before returning the path.

2. **create_logger_in_process**:
   - Creates and configures a logger for use in multiprocessing environments.
   - Supports logging to both the console and a specified log file.
   - Uses a consistent format for log messages, including timestamps, process 
     names, and log levels.

Features:
- **Multiprocessing Compatibility**:
  - Leverages Python's `multiprocessing` module to ensure that loggers are 
    properly configured for parallel processes.

- **Timestamped Log Files**:
  - Log files are named with the current timestamp for easier organization and 
    debugging.

- **Stream and File Logging**:
  - Logs are output both to the console and a designated log file.

Usage:
    from logging import create_logger_in_process, generate_log_file_path

    # Generate a log file path
    log_file_path = generate_log_file_path(__file__)

    # Create a logger
    logger = create_logger_in_process(log_file_path)

    # Use the logger
    logger.info("Logging setup complete.")

Dependencies:
- **logging**:
  - Standard Python module for logging.
  
- **multiprocessing**:
  - Used to handle logging across multiple processes.

- **pathlib**:
  - Used to create directories for log files if they don't already exist.

"""
import logging
import multiprocessing


def generate_log_file_path(log_folder="logs"):
  import time  # pylint: disable=import-outside-toplevel
  from pathlib import Path  # pylint: disable=import-outside-toplevel

  Path(f"./{log_folder}").mkdir(parents=True, exist_ok=True)
  path_run_name = time.strftime("%Y%m%d-%H%M%S")
  return f"{log_folder}/{path_run_name}_log.txt"


def create_logger_in_process(log_file_path) -> logging.Logger:
  logger = multiprocessing.get_logger()
  if not logger.hasHandlers():
    formatter = logging.Formatter(
        "%(processName)s| %(asctime)s,%(msecs)d %(name)s %(levelname)s "
        "%(message)s"
    )
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(log_file_path)
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
  return logger
