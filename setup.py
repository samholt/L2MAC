from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).resolve().parent
long_description = (here / "README.md").read_text(encoding="utf-8")
requirements = (here / "requirements.txt").read_text(encoding="utf-8").splitlines()


extras_require = {}
extras_require = {"dev": ["pylint~=3.0.3", "black~=23.3.0", "isort~=5.12.0", "pre-commit~=3.6.0"]}

setup(
    name="l2mac",
    version="0.0.2",
    description="The LLM Automatic Computer Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samholt/l2mac",
    author="Sam Holt",
    author_email="samuel.holt.direct@gmail.com",
    license="MIT",
    keywords="l2mac multi-agent programming gpt llm metaprogramming automatic computer llm-automatic",
    packages=find_packages(exclude=["contrib", "docs", "examples", "tests*"]),
    include_package_data=True,
    package_data={
        "": ["*.yaml"],
    },
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require=extras_require,
    entry_points={"console_scripts": ["l2mac = l2mac.core:app"]},
)
