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

app = typer.Typer(help="Generate based on the prompt with LLM-automatic Computer")


@app.command()
def run_l2mac(
    prompt_task: Annotated[
        str, typer.Argument(help="Your input prompt to generate for such as 'Create a playable snake game in PyGame'")
    ],
    domain: Annotated[
        Domain, typer.Option(help="Domain to generate, existing options are 'codebase', 'book'.")
    ] = Domain.codebase,
    run_tests: Annotated[
        bool, typer.Option(help="Whether to run self-generated unit-tests when generating code.")
    ] = False,
    project_name: Annotated[Optional[str], typer.Option(help="Unique project name, such as 'snakegame'.")] = None,
    steps: Annotated[
        int, typer.Option(help="Number of internal steps to use when creating the prompt program internally.")
    ] = 10,
    prompt_program: Annotated[
        Optional[str],
        typer.Option(help="Path to the prompt program to use, or the prompt program as a string in a list format."),
    ] = None,
    prompts_file_path: Annotated[
        Optional[str],
        typer.Option(
            help="Overrides the existing prompts to be used. Useful when creating a new prompt set for a new task."
        ),
    ] = None,
    tools_enabled: Annotated[
        Optional[str],
        typer.Option(
            help="List of functions that the agents can use, separated by commas. Defaults to use all tools available."
        ),
    ] = None,
    debugging_level: Annotated[
        DebuggingLevel, typer.Option(help="Whether to print full context-windows out.")
    ] = DebuggingLevel.info,
    init_config: Annotated[bool, typer.Option(help="Initialize the configuration file for L2MAC.")] = False,
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
    log_path = generate_log_file_path(__file__, log_folder=config.setup.log_dir, config=config)
    config.setup.log_path = log_path
    logger = create_logger_in_process(log_path)
    rate_limiter = setup_chat_rate_limiter(config)
    if config.wandb.track:
        import wandb

        wandb.init(
            project=config.wandb.project,
            config=to_dotdict(config),
        )
    else:
        wandb = None
    seed_all(config.setup.seed)
    if debugging_level == DebuggingLevel.debug:
        logger.info(f"Starting run \t | See log at : {log_path}")
        logger.info(f"[Main Config] {config}")
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
        except Exception as e:
            logger.exception(f"[Error] {e}")
            logger.info(f"[Failed running]\t| error={e}")
            traceback.print_exc()
            output_file_store = {"errored": True}
    if config.wandb.track:
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
    env = get_env(domain=domain, config=config, logger=logger, seed=config.setup.seed)
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
    debugging_level: DebuggingLevel = DebuggingLevel.info,
    init_config: bool = False,
):
    return run_l2mac(
        prompt_task=prompt_task,
        domain=Domain.codebase,
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
    debugging_level: DebuggingLevel = DebuggingLevel.info,
    init_config: bool = False,
):
    return run_l2mac(
        prompt_task=prompt_task,
        domain=Domain.book,
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
    debugging_level: DebuggingLevel = DebuggingLevel.info,
    init_config: bool = False,
):
    return run_l2mac(
        prompt_task=prompt_task,
        domain=Domain.custom,
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
