"""
core.py

This module serves as the entry point for the L2MAC (Large Language Model
Automatic Computer) framework. It provides CLI commands and utility functions
to interact with L2MAC, allowing users to generate codebases, books, or other
artifacts based on natural language prompts. The module leverages Typer for CLI 
interactions and integrates deeply with the L2MAC ecosystem.

Key Components:
1. **Command-Line Interface**:
   - Defines CLI commands using Typer to run the L2MAC framework.
   - Allows users to specify tasks, domains, debugging levels, tools, and more.

2. **Functions**:
   - `run_l2mac`: Executes the core L2MAC functionality based on user-provided 
     input parameters.
   - `generate_codebase`: Simplifies the process of generating code projects 
     using L2MAC.
   - `generate_book`: Generates book content based on structured prompts.
   - `generate_custom`: Allows customization for generating outputs beyond 
     predefined domains.

3. **Internal Logic**:
   - `l2mac_internal`: Encapsulates the core execution logic for running L2MAC, 
     including initializing environments, configuring prompts, and executing 
     tasks.

Features:
- **Domain-Specific Generation**:
  - Supports predefined domains such as `codebase` and `book` while enabling 
    custom tasks.

- **Prompt-Driven Execution**:
  - Accepts natural language prompts and translates them into actionable 
    instructions for L2MAC.

- **Debugging and Logging**:
  - Provides options to enable detailed debugging output for transparency 
    during execution.

- **Configuration Management**:
  - Supports initialization and loading of configuration files.

Example Usage:
1. From the Command Line:
    ```bash
    python core.py run-l2mac "Create a snake game" --domain codebase --steps 5
    ```

2. From Python Code:
    ```python
    from core import generate_codebase

    codebase = generate_codebase(
        prompt_task="Create a simple snake game in PyGame.",
        steps=3,
        run_tests=True
    )
    ```

Dependencies:
- **Typer**:
  - Used for building and managing the command-line interface.

- **L2MAC Framework**:
  - Includes components for configuration management, logging, rate limiting, 
    and environment setup.

- **Third-Party Tools**:
  - Optionally integrates with external tools like Weights & Biases (wandb) 
    for tracking and logging runs.

"""
import traceback
from typing import Optional

import typer
from typing_extensions import Annotated

from l2mac.config import L2MACConfig, WandbConfig, copy_config_to_home, load_config
from l2mac.envs.general import get_env
from l2mac.l2mac import L2MAC
from l2mac.llm_providers.general import setup_chat_rate_limiter
from l2mac.llm_providers.rate_limiter import ChatRateLimiter
from l2mac.prompts.load_prompts import L2MACPrompts, get_l2mac_prompts
from l2mac.utils.logging import create_logger_in_process, generate_log_file_path
from l2mac.utils.run import (
    DebuggingLevel,
    Domain,
    load_prompt_program,
    seed_all,
    to_dotdict,
)

app = typer.Typer(
    help="Generate based on the prompt with LLM-automatic Computer")


@app.command()
def run_l2mac(
    prompt_task: Annotated[
        str,
        typer.Argument(
            help=
            "Your input prompt to generate for such as 'Create a playable "
            "snake game in PyGame'"
        ), ],
    domain: Annotated[
        Domain,
        typer.Option(
            help="Domain to generate, existing options are 'codebase', 'book'."
        ), ] = Domain.CODEBASE,
    run_tests: Annotated[
        bool,
        typer.Option(
            help="Whether to run self-generated unit-tests when generating "
            "code."
        ), ] = False,
    project_name: Annotated[
        Optional[str],
        typer.Option(
            help="Unique project name, such as 'snakegame'."), ] = None,
    steps: Annotated[
        int,
        typer.Option(
            help=
            "Number of internal steps to use when creating the prompt program "
            "internally."
        ), ] = 10,
    prompt_program: Annotated[
        Optional[str],
        typer.Option(
            help=
            "Path to the prompt program to use, or the prompt program as a "
            "string in a list format."
        ), ] = None,
    prompts_file_path: Annotated[
        Optional[str],
        typer.Option(
            help=
            "Overrides the existing prompts to be used. Useful when creating a "
            "new prompt set for a new task."
        ), ] = None,
    tools_enabled: Annotated[
        Optional[str],
        typer.Option(
            help=
            "List of functions that the agents can use, separated by commas. "
            "Defaults to use all tools available."
        ), ] = None,
    debugging_level: Annotated[
        DebuggingLevel,
        typer.Option(help="Whether to print full context-windows out."
                     ), ] = DebuggingLevel.INFO,
    init_config: Annotated[
        bool,
        typer.Option(
            help="Initialize the configuration file for L2MAC.")] = False,
):
  """
    Generate based on the input prompt with LLM-automatic Computer (L2MAC).
    """
  if init_config:
    print("Initializing configuration file...")
    copy_config_to_home()
    return None
  # Process inputs
  if prompt_program is not None:
    prompt_program = load_prompt_program(prompt_program)
  l2mac_prompts = get_l2mac_prompts(prompts_file_path, domain)
  config = load_config()
  log_path = generate_log_file_path(log_folder=config.setup.log_dir)
  config.setup.log_path = log_path
  logger = create_logger_in_process(log_path)
  rate_limiter = setup_chat_rate_limiter(config)
  if config.wandb.track:
    import wandb  # pylint: disable=import-outside-toplevel

    wandb.init(
        project=config.wandb.project,
        config=to_dotdict(config),
    )
  else:
    wandb = None
  seed_all(config.setup.seed)
  if debugging_level == DebuggingLevel.DEBUG:
    logger.info("Starting run \t | See log at : %s", log_path)
    logger.info("[Main Config] %s", config)
  if config.setup.debug_mode:
    output_file_store = l2mac_internal(
        prompt_task,
        domain,
        run_tests,
        project_name,
        steps,
        prompt_program,
        prompts_file_path,
        tools_enabled,
        debugging_level,
        config,
        rate_limiter,
        wandb,
        l2mac_prompts,
        logger,
    )
  else:
    try:
      output_file_store = l2mac_internal(
          prompt_task,
          domain,
          run_tests,
          project_name,
          steps,
          prompt_program,
          prompts_file_path,
          tools_enabled,
          debugging_level,
          config,
          rate_limiter,
          wandb,
          l2mac_prompts,
          logger,
      )
    except (ValueError, TypeError, RuntimeError) as e:
      logger.exception("[Error] %s", e)
      logger.info("[Failed running]\t| error=%s", e)
      traceback.print_exc()
      output_file_store = {"errored": True}
  if config.wandb.track and wandb is not None:
    wandb.finish()
  logger.info("Run completed.")
  return output_file_store


def l2mac_internal(
    prompt_task: str,
    domain: Domain,
    run_tests: bool,
    project_name: Optional[str],
    steps: int,
    prompt_program: Optional[str],
    prompts_file_path: Optional[str],
    tools_enabled: Optional[str],
    debugging_level: DebuggingLevel,
    config: L2MACConfig,
    rate_limiter: ChatRateLimiter,
    wandb: Optional[WandbConfig],
    l2mac_prompts: L2MACPrompts,
    logger=None,
):
  env = get_env(domain=domain,
                config=config,
                logger=logger,
                seed=config.setup.seed)
  env.set_seed(seed=config.setup.seed)
  env.reset()
  l2mac = L2MAC(
      prompt_task=prompt_task,
      env=env,
      config=config,
      logger=logger,
      rate_limiter=rate_limiter,
      l2mac_prompts=l2mac_prompts,
      run_tests=run_tests,
      project_name=project_name,
      prompt_program=prompt_program,
      prompts_file_path=prompts_file_path,
      tools_enabled=tools_enabled,
      debugging_level=debugging_level,
      wandb=wandb,
  )
  output_file_store = l2mac.run(steps=steps)
  return output_file_store


def generate_codebase(
    prompt_task: str,
    run_tests: bool = False,
    project_name: Optional[str] = None,
    steps: int = 10,
    prompt_program: Optional[str] = None,
    prompts_file_path: Optional[str] = None,
    tools_enabled: Optional[str] = None,
    debugging_level: DebuggingLevel = DebuggingLevel.INFO,
    init_config: bool = False,
):
  return run_l2mac(
      prompt_task=prompt_task,
      domain=Domain.CODEBASE,
      run_tests=run_tests,
      project_name=project_name,
      steps=steps,
      prompt_program=prompt_program,
      prompts_file_path=prompts_file_path,
      tools_enabled=tools_enabled,
      debugging_level=debugging_level,
      init_config=init_config,
  )


def generate_book(
    prompt_task: str,
    run_tests: bool = False,
    project_name: Optional[str] = None,
    steps: int = 10,
    prompt_program: Optional[str] = None,
    prompts_file_path: Optional[str] = None,
    tools_enabled: Optional[str] = None,
    debugging_level: DebuggingLevel = DebuggingLevel.INFO,
    init_config: bool = False,
):
  return run_l2mac(
      prompt_task=prompt_task,
      domain=Domain.BOOK,
      run_tests=run_tests,
      project_name=project_name,
      steps=steps,
      prompt_program=prompt_program,
      prompts_file_path=prompts_file_path,
      tools_enabled=tools_enabled,
      debugging_level=debugging_level,
      init_config=init_config,
  )


def generate_custom(
    prompt_task: str,
    run_tests: bool = False,
    project_name: Optional[str] = None,
    steps: int = 10,
    prompt_program: Optional[str] = None,
    prompts_file_path: Optional[str] = None,
    tools_enabled: Optional[str] = None,
    debugging_level: DebuggingLevel = DebuggingLevel.INFO,
    init_config: bool = False,
):
  return run_l2mac(
      prompt_task=prompt_task,
      domain=Domain.CUSTOM,
      run_tests=run_tests,
      project_name=project_name,
      steps=steps,
      prompt_program=prompt_program,
      prompts_file_path=prompts_file_path,
      tools_enabled=tools_enabled,
      debugging_level=debugging_level,
      init_config=init_config,
  )


if __name__ == "__main__":
  app()
