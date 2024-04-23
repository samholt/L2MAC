## Roadmap

### Long-term Objectives

Enable LLM-Automatic Computer (L2MAC) to run prompt programs with advanced control flows (for example, `while` or `for` loops and conditional `if` statements, combined with additional checks) and re-program its prompt program at runtime. Working towards making the [vision](./faq) and [mission](./mission) a reality.

### Short-term Objective

1. Solve user tasks with the highest ROI.
2. Fully implement complete high-quality codebases (repositories) for projects.
3. Implement the most crucial [future work](https://openreview.net/pdf?id=EhrzQwsV4K).

### Tasks

* Add support for other programming languages other than Python
* Add support for additional tools, such as searching online
* In Python, when generating a codebase, and specific new package versions are being recommended by the LLM generating, creating an on-the-fly python virtualenv to install these the packages in the requirements file, as the requirements file is updated. We are looking for contributors for this feature, so we warmly welcome any PR's implementing this.

1. Usability
   1. Write documentation describing the current features and usage at all levels (ongoing, continuously adding contents to [documentation site](https://samholt.github.io/L2MAC/)
   2. Support Docker
   3. Support multiple languages
2. Features
   1. Improve test coverage of all code
   2. Implement more LLM api types and local running LLMs and their associated providers to map the tools of reading and writing files to work with them.
   3. Support loading an existing file directory of files.
   4. Implement reflecting on the original proposed prompt program n times to improve it (partially implemented).
   4. Support re-planning the prompt program at runtime
   3. Support ToT planning
4. Tools
   1. Implementation a web search tool
   2. Implement a code debugger tool
   3. Implement local data collection for training your own custom local LLM
7. Use cases
   1. Real-world use-cases (please submit your ideas; just open a GitHub issue)
   2. Web Researcher, creating a survey paper or a document summarizing a particular topic or answering a particular question by searching online and synthesizing content.
   3. Analyzing data
8. Evaluation
   1. Reproduce a complete survey paper, e.g. "multi-agent LLM frameworks and systems".
   2. Implement on the [GAIA benchmark](https://arxiv.org/abs/2311.12983).
9. LLM
   1. Support streaming version of all APIs
   2. Support more APIs