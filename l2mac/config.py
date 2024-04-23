from enum import Enum
from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, ValidationError


class OpenAIRateLimitTier(str, Enum):
    free = "free"
    tier1 = "tier1"
    tier2 = "tier2"
    tier3 = "tier3"
    tier4 = "tier4"
    tier5 = "tier5"


class ApiType(str, Enum):
    openai = "openai"
    azure = "azure"


class LLMCoreConfig(BaseModel):
    api_type: ApiType = ApiType.openai
    model: str = "gpt-4-1106-preview"
    base_url: Optional[str] = "https://api.openai.com/v1"
    api_key: str
    api_version: Optional[str] = None


class LLMSettingsConfig(BaseModel):
    temperature: float = 0.01
    top_p: float = 1
    frequency_penalty: float = 0
    presence_penalty: float = 0
    stop: str = ""
    rate_limit_tier: OpenAIRateLimitTier = OpenAIRateLimitTier.tier3
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
            "No config file can be loaded. Please create one at '~/.l2mac/config.yaml' or './config/config.yaml'."
        )


def load_config() -> L2MACConfig:
    config_path = find_config_file()
    with open(config_path, "r") as file:
        config_data = yaml.safe_load(file)
        try:
            return L2MACConfig(**config_data)
        except ValidationError as e:
            print("Invalid configuration:", e)
            raise e


DEFAULT_CONFIG = """# Full Example: https://github.com/samholt/L2MAC/blob/master/config/config.yaml
# Reflected Code: https://github.com/samholt/L2MAC/blob/master/l2mac/config.py
llm:
  api_type: "openai"  # or azure etc. Check ApiType for more options
  model: "gpt-4-turbo-preview"  # or "gpt-4-turbo"
  base_url: "https://api.openai.com/v1"  # or forward url / other llm url
  api_key: "YOUR_API_KEY"
"""


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
    except Exception as e:
        print("Failed to load configuration:", e)
