
# L2MAC: Large Langauge Model Automatic Computer

<p align="center">
<a href=""><img src="docs/public/l2mac-icon-white.png" alt="L2MAC logo: The first practical LLM-based general-purpose stored-program automatic computer (von Neumann architecture) framework, an LLMbased multi-agent system, for extensive and consistent output generation." width="150px"></a>
</p>

<p align="center">
<b>Pioneering the first practical LLM-based general-purpose stored-program automatic computer (von Neumann architecture) framework in an LLM-based multi-agent system, for solving complex tasks through generating extensive and consistent outputs, unbounded by the LLMs fixed context window constraint.</b>
</p>

<p align="center">
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
<a href="docs/guide/roadmap.md"><img src="https://img.shields.io/badge/ROADMAP-blue" alt="roadmap"></a>
<a href="https://discord.gg/z27CxnwdhY"><img src="https://dcbadge.vercel.app/api/server/z27CxnwdhY?style=flat" alt="Discord Follow"></a>
</p>

## News
🌟 May. 7 - 11th, 2024: We will present L2MAC at the International Conference on Learning Representations (ICLR) 2024. Come meet us at ICLR in Vienna Austria! Please reach out to me at sih31 (at) cam.ac.uk so we can meet, virtual meetings accepted as well!

🌟 April. 13, 2024: L2MAC is fully open-sourced with the initial version released.

🚀 Jan. 16, 2024: The paper [L2MAC: Large Language Model Automatic Computer for Extensive Code Generation
](https://arxiv.org/abs/2310.02003) is accepted for presentation at ICLR 2024!

## LLM-Automatic Computer (L2MAC) framework excels at solving large complex tasks, such as being state-of-the-art for generating large codebases, or it can even write entire books, all of which bypass the traditional constraints of the LLMs fixed context window constraint.

* LLM-Automatic Computer can take a **one line input prompt** and generate an extensive and large output, for example generating an entire complex codebase.
  * Internally, the LLM-Automatic Computer uses a **prompt-program** which is a series of prompts, each providing a instruction step to execute. Unless explicitly given, the **prompt-program** is self generated (bootstrapped) and executed. Specifically each instruction step of the **prompt-program** is loaded into a new LLM agent to execute, whose context is managed by a control unit and is provided with tools so that it can read and write to a persistent memory, here a file store, which contains the final and intermediate outputs. This enables it to automatically execute general-purpose prompt programs to solve complex tasks, that require extensive cohesive outputs, where the output is unbounded and not constrained by the LLMs underlying context window constraint.
  
![BlockDiagram](docs/public/l2mac-block-diagram.png)
<p align="center">LLM-Automatic Computer (L2MAC) instantiation for coding a large complex codebase for an entire application based on a <b>single user prompt</b>. Here we provide L2MAC with additional tools to check for any syntax errors within the code and run any unit tests if they exist, and call this instantiation Code-L2MAC.</p>

## Get Started

### Installation

> Ensure that Python 3.7+ is installed on your system. You can check this by using: `python --version`.
> You can use conda like this: `conda create -n l2mac python=3.9 && conda activate l2mac`

```bash
pip install --upgrade l2mac
# or `pip install --upgrade git+https://github.com/samholt/l2mac`
# or `git clone https://github.com/samholt/l2mac && cd l2mac && pip install --upgrade -e .`
```

For detailed installation guidance, please refer to [installation](https://samholt.github.io/L2MAC/guide/get_started/installation.html#install-stable-version)

### Configuration

You can init the config of L2MAC by running the following command, or manually create `~/.L2MAC/config.yaml` file:
```bash
# Check https://samholt.github.io/L2MAC/guide/get_started/configuration.html for more details
l2mac --init-config  # it will create ~/.l2mac/config.yaml, just modify it to your needs
```

You can configure `~/.l2mac/config.yaml` according to the [example](https://github.com/samholt/L2MAC/blob/master/config/config.yaml) and [doc](https://samholt.github.io/L2MAC/guide/get_started/configuration.html):

```yaml
llm:
  api_type: "openai"  # or azure etc. Check ApiType for more options
  model: "gpt-4-turbo-preview"  # or "gpt-4-turbo"
  base_url: "https://api.openai.com/v1"  # or forward url / other llm url
  api_key: "YOUR_API_KEY"
```

### Usage

After installation, you can use L2MAC CLI

```bash
l2mac "Create a beautiful, playable and simple snake game with pygame. Make the snake and food be aligned to the same 10-pixel grid."  # this will create a codebase repo in ./workspace
```

or use it as a library

```python
from l2mac import generate_codebase
codebase: dict = generate_codebase("Create a beautiful, playable and simple snake game with pygame. Make the snake and food be aligned to the same 10-pixel grid.")
print(codebase)  # it will print the codebase (repo) complete with all the files as a dictionary, and produce a local codebase folder in ./workspace
```

### [QuickStart](https://github.com/samholt/L2MAC/guide/get_started/quickstart.html)

## Tutorial

- 🗒 [Online Documentation](https://samholt.github.io/l2mac/)
- 💻 [Usage](https://github.com/samholt/L2MAC/guide/get_started/quickstart.html)  
- 🔎 [What can L2MAC do?](https://samholt.github.io/l2mac/guide/get_started/introduction.html)
- 🖼️ [Gallery of Examples Produced](https://samholt.github.io/l2mac/guide/use_cases/gallery.html)
- 🛠 How to run L2MAC? 
  - [L2MAC Usage & Development Guide | L2MAC 101](https://samholt.github.io/l2mac/guide/tutorials/l2mac_101.html)
- 🧑‍💻 Contribution
  - [Development Roadmap](https://samholt.github.io/l2mac/guide/roadmap.html)
- 🔖 Use Cases
  - [Create a state-of-the-art large codebase](https://samholt.github.io/l2mac/guide/use_cases/codebase_generator.html)
  - [Create an entire book](https://samholt.github.io/l2mac/guide/use_cases/book_generator.html)
- ❓ [FAQs](https://samholt.github.io/l2mac/guide/faq.html)

## Support

### Discord Join US

📢 Join Our [Discord Channel](https://discord.gg/z27CxnwdhY)! Looking forward to seeing you there! 🎉


### Contact Information

If you have any questions or feedback about this project, please feel free to contact us. We highly appreciate your suggestions!

- **Email:** sih31 at cam.ac.uk
- **GitHub Issues:** For more technical inquiries, you can also create a new issue in our [GitHub repository](https://github.com/samholt/L2MAC/issues).

We will respond to all questions within 2-3 business days.

## Citation

To stay updated with the latest research and development, follow [@samianholt](https://twitter.com/samianholt) on Twitter. 

To cite [L2MAC](https://openreview.net/forum?id=EhrzQwsV4K) in publications, please use the following BibTeX entry.

```bibtex
@inproceedings{
    holt2024lmac,
    title={L2{MAC}: Large Language Model Automatic Computer for Unbounded Code Generation},
    author={Samuel Holt and Max Ruiz Luyten and Mihaela van der Schaar},
    booktitle={The Twelfth International Conference on Learning Representations},
    year={2024},
    url={https://openreview.net/forum?id=EhrzQwsV4K}
}
```

