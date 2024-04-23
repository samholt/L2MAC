# Quickstart

## Installation

```
pip install l2mac
```

Available installation methods can be found in the [Installation](./installation) section

## Configuration

Variations for setting up the LLM API (OpenAI, Azure, etc.) and other components can be found in the [Configuration](./configuration/llm_api_configuration) section.

## Create an entire codebase with a single user prompt

> Note:
>
> Below is a breakdown of the [codebase generator example](https://github.com/samholt/L2MAC/blob/master/examples/generate_codebase_simple_blackjack.py). If you installed L2MAC with the git clone approach, simply run
>
> ```
> l2mac "Create a simple playable blackjack cli game"
> ```
>
> Now, let's get started! We will create a LLM-automatic computer of sequential LLM agents to write all the software based on our initial prompt.

First, import the library

```python
from l2mac import generate
```

Next, run it to generate the codebase

```python
generate("Create a simple playable blackjack cli game")
```

You may expect a similar output to that shown in [CodeBase Generator](../use_cases/codebase_generator)

<!-- ToDo: Add Google Collab here -->
---

## Usage

```                                                                                                                           
 Usage: l2mac [OPTIONS] PROMPT_TASK

 Generate based on the input prompt with LLM-automatic Computer (L2MAC).                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                       
╭─ Arguments ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    prompt_task      TEXT  Your input prompt to generate for such as 'Create a playable snake game in PyGame' [default: None] [required]                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --domain                                    [codebase|book|custom]   Domain to generate, existing options are 'codebase', 'book'. [default: codebase]                                                                                                                               │
│ --run-tests             --no-run-tests                               Whether to run self-generated unit-tests when generating code. [default: no-run-tests]                                                                                                                         │
│ --project-name                              TEXT                     Unique project name, such as 'snakegame'. [default: None]                                                                                                                                                      │
│ --steps                                     INTEGER                  Number of internal steps to use when creating the prompt program internally. [default: 10]                                                                                                                     │
│ --prompt-program                            TEXT                     Path to the prompt program to use, or the prompt program as a string in a list format. [default: None]                                                                                                         │
│ --prompts-file-path                         TEXT                     Overrides the existing prompts to be used. Useful when creating a new prompt set for a new task. [default: None]                                                                                               │
│ --tools-enabled                             TEXT                     List of functions that the agents can use, separated by commas. Defaults to use all tools available. [default: None]                                                                                           │
│ --debugging-level                           [debug|info|warn|error]  Whether to print full context-windows out. [default: info]                                                                                                                                                     │
│ --init-config           --no-init-config                             Initialize the configuration file for L2MAC. [default: no-init-config]                                                                                                                                         │
│ --help                                                               Show this message and exit.                                                                                                                                                                                    │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
