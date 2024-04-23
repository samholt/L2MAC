# API

## `run_l2mac`

Generate output based on the input prompt for specified domain and settings.

**Parameters:**

- `prompt_task` (str): The input prompt to generate, such as 'Create a playable snake game in PyGame'.
- `domain` (Domain): Domain to generate. Existing options are 'codebase', 'book'. Default is 'codebase'.
- `run_tests` (bool): Whether to run self-generated unit-tests when generating code. Default is `False`.
- `project_name` (Optional[str]): Unique project name, such as 'snakegame'.
- `steps` (int): Number of internal steps to use when creating the prompt program internally. Default is 10.
- `prompt_program` (Optional[str]): Path to the prompt program to use, or the prompt program as a string in list format.
- `prompts_file_path` (Optional[str]): Overrides the existing prompts to be used. Useful when creating a new prompt set for a new task.
- `tools_enabled` (Optional[str]): List of functions that the agents can use, separated by commas. Defaults to use all tools available.
- `debugging_level` (DebuggingLevel): Whether to print full context-windows out. Default is `info`.
- `init_config` (bool): Initialize the configuration file for L2MAC. Default is `False`.

**Examples:**

```bash
python core.py run_l2mac --prompt_task "Create a simple blog in Django" --domain codebase
```

Equivalent python code.

```python
from l2mac import run_l2mac, Domain

code = run_l2mac("Create a beautiful, playable and simple snake game with pygame. Make the snake and food be aligned to the same 10-pixel grid.", domain=Domain.codebase)
```

### Utility Functions

#### `generate_codebase`

Helper function to generate output specifically for codebase domain.

#### `generate_book`

Helper function to generate output specifically for book domain.

#### `generate_custom`

Helper function to generate output for custom domains as specified.

## Configuration

To manage configurations, modify the configuration files located at `config/config.yaml`. Initial setup can be triggered using the `--init_config` flag when running commands.

## Logging

Logging is handled via the `l2mac.utils.logging` module. Logs are stored in the specified directory `logs` in the local folder as per the configuration file.

## Error Handling

Errors are logged with detailed stack traces to assist in debugging. Errors during the generation process are captured and logged, with partial outputs stored if possible.