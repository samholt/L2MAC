# Installation

We provide several ways to install L2MAC; please select the most appropriate way for your use case.

## Support system and version

| System Version | Python Version | Supported |
| -------------- | -------------- | --------- |
| macOS 13.x     | python 3.9     | Yes       |
| Windows 11     | python 3.9     | Yes       |
| Ubuntu 22.04   | python 3.9     | Yes       |

Ensure that Python 3.9+ is installed on your system. You can check this by using:

```
python3 --version
```

## Install stable version

This is recommended for most users. You can import L2MAC like any Python package, create complete code applications, generate extensive text-based output for tasks, and fully customize the generation and which tools are available or the generation settings for your application.

```
pip install l2mac
```

### Install submodules

- Code Testing, `pip install l2mac[all]`. On macOS/zsh: `pip install 'l2mac[all]'`



## Install the latest development version

Best for experiencing the newest features.

```
pip install git+https://github.com/samholt/l2mac
```

## Install in development mode

This is recommended for developers and researchers looking to customize the framework for their unique requirements, contribute new tools, or extend the framework through core contributions.

```
git clone https://github.com/samholt/L2MAC.git
cd ./L2MAC
pip install -e .
```

### Install submodules

- Code Testing, `pip install -e .[all]`