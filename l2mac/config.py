"""
config.py

This module handles the configuration management for the L2MAC (Large Language 
Model Automatic Computer) framework. It provides classes and utilities to
define, validate, load, and manage configurations for LLM (Large Language
Model) usage, application setup, and external integrations like Weights & 
Biases (wandb).

Key Components:
1. **Configuration Models**:
   - `LLMCoreConfig`: Defines core LLM-related settings like API type, model, 
      and API key.
   - `LLMSettingsConfig`: Specifies advanced LLM settings, including
      temperature, penalties, and rate limits.
   - `SetupConfig`: Configures application-wide settings such as debug mode,
      logging, and seeding.
   - `WandbConfig`: Manages configurations for Weights & Biases (wandb)
      integration.
   - `L2MACConfig`: Combines all configurations into a single structure for the
      framework.

2. **Utility Functions**:
   - `find_config_file`: Searches for the configuration file in the user's home
      directory or the local project directory.
   - `load_config`: Loads and validates the configuration from the YAML file.
   - `copy_config_to_home`: Initializes a default configuration file in the
      user's home directory.

3. **DEFAULT_CONFIG**:
   - A default YAML configuration template to initialize user-specific settings.

Features:
- **Validation**:
  - Uses Pydantic models for strict validation of configurations.
  - Provides meaningful error messages for invalid configurations.
  
- **Dynamic File Management**:
  - Supports dynamic discovery of configuration files in common locations.
  - Automatically creates and backs up configuration files if needed.

- **Modular and Extensible**:
  - Designed to accommodate multiple API providers (e.g., OpenAI, Azure).
  - Configurable settings for retry mechanisms, rate limiting, and streaming.

Example Usage:
1. Loading a Configuration:
    ```python
    from config import load_config

    config = load_config()
    print("Loaded configuration:", config)
    ```

2. Initializing a Default Configuration:
    ```python
    from config import copy_config_to_home

    copy_config_to_home()
    ```

3. Accessing Specific Settings:
    ```python
    config = load_config()
    print(config.llm.api_key)
    ```

Dependencies:
- **Pydantic**:
  - For validation and definition of configuration models.
  
- **PyYAML**:
  - For loading and parsing YAML configuration files.

- **Pathlib**:
  - For platform-independent file and directory management.

"""
from enum import Enum
from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, ValidationError


class OpenAIRateLimitTier(str, Enum):
  FREE = "free"
  TIER1 = "tier1"
  TIER2 = "tier2"
  TIER3 = "tier3"
  TIER4 = "tier4"
  TIER5 = "tier5"


class ApiType(str, Enum):
  OPENAI = "openai"
  AZURE = "azure"


class LLMCoreConfig(BaseModel):
  api_type: ApiType = ApiType.OPENAI
  model: str = "gpt-4-1106-preview"
  base_url: Optional[str] = "https://api.openai.com/v1"
  api_key: str
  api_version: Optional[str] = None


class LLMSettingsConfig(BaseModel): # pylint: disable=missing-class-docstring
  temperature: float = 0.01
  top_p: float = 1
  frequency_penalty: float = 0
  presence_penalty: float = 0
  stop: str = ""
  parallel_tool_calls: bool = False
  rate_limit_tier: OpenAIRateLimitTier = OpenAIRateLimitTier.TIER3
  rate_limit_requests_per_minute: float = 3000
  api_retry_with_exponential_backoff__initial_delay: float = 1
  api_retry_with_exponential_backoff__exponential_base: float = 2
  api_retry_with_exponential_backoff__jitter: bool = True
  api_retry_with_exponential_backoff__max_retries: float = 10
  api_stream: bool = False


class SetupConfig(BaseModel):
  debug_mode: bool = True
  log_dir: str = "logs"
  enable_tests: bool = True
  log_path: str = ""
  seed: int = 0


class WandbConfig(BaseModel):
  project: str = "l2mac"
  track: bool = False


class L2MACConfig(BaseModel):
  llm: LLMCoreConfig
  llm_settings: LLMSettingsConfig = LLMSettingsConfig()
  setup: SetupConfig = SetupConfig()
  wandb: WandbConfig = WandbConfig()


def find_config_file() -> Path:
  home_config = Path.home() / ".l2mac" / "config.yaml"
  local_config = Path.cwd() / "config" / "config.yaml"

  if home_config.exists():
    return home_config
  elif local_config.exists():
    return local_config
  else:
    raise FileNotFoundError(
        "No config file can be loaded. Please create one at "
        "'~/.l2mac/config.yaml' or './config/config.yaml'."
    )


def load_config() -> L2MACConfig:
  config_path = find_config_file()
  with open(config_path, "r", encoding="utf-8") as file:
    config_data = yaml.safe_load(file)
    try:
      return L2MACConfig(**config_data)
    except ValidationError as validation_error:
      print("Invalid configuration:", validation_error)
      raise validation_error

# pylint: disable=line-too-long
DEFAULT_CONFIG = """# Full Example: https://github.com/samholt/L2MAC/blob/master/config/config.yaml
# Reflected Code: https://github.com/samholt/L2MAC/blob/master/l2mac/config.py
llm:
  api_type: "openai"  # or azure etc. Check ApiType for more options
  model: "gpt-4o"
  base_url: "https://api.openai.com/v1"  # or forward url / other llm url
  api_key: "YOUR_API_KEY"
"""
# pylint: enable=line-too-long

def copy_config_to_home(home_config=Path.home() / ".l2mac" / "config.yaml"):
  """Initialize the configuration file for L2MAC."""

  home_config.parent.mkdir(parents=True, exist_ok=True)

  if home_config.exists():
    backup_path = home_config.with_suffix(".bak")
    home_config.rename(backup_path)
    print(f"Existing configuration file backed up at {backup_path}")

  home_config.write_text(DEFAULT_CONFIG, encoding="utf-8")
  print(f"Configuration file initialized at {home_config}")


if __name__ == "__main__":
  try:
    config = load_config()
    print("Configuration loaded successfully:", config)
  except (FileNotFoundError, ValidationError) as error:
    print("Failed to load configuration:", error)
