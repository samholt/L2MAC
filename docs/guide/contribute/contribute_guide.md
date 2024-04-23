# Contribution Guide

We invite developers to join our effort in enhancing L2MAC by contributing to our open-source community. Below are various ways you can contribute to the project:

## How to Contribute

### Code Contributions
- **Implement Features:** Refer to our [`docs/roadmap.md`](../roadmap) for a list of planned features. Implement these features and submit your pull requests (PRs).
- **Beyond the Roadmap:** Feel free to contribute new features, bug fixes, use cases, and even code annotations not listed on the roadmap.

### Documentation
- **Enhance Documentation:** Help improve our documentation by adding tutorials, new exciting use cases, examples, advanced guides, and more.
- **Contribute to Our Docs Site:** Submit supplementary documentation that supports existing or new features.

### Issues
- **Report Bugs:** If you find any bugs while using L2MAC, please submit an issue.
- **Request Features:** Suggest new features that you would like to see implemented.
- **Community Discussions:** Engage in discussions about implementations and applications of L2MAC, by joining our discord [dev/contributors channel](https://discord.gg/z27CxnwdhY).

## Submitting Pull Requests (PR)

Please use [fork and pull request](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project) to submit updates to the code or documentation.

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Implement your changes.
4. Ensure your code adheres to the established standards and guidelines.
5. Submit a pull request to our main branch.

After a PR with more than 10 lines of code is merged, the submitted can join the `L2MAC-dev` group.
We encourage the submission of small, frequent code contributions. Large pull requests often demand a deeper understanding of context and require more time to review. It would be helpful if you could include additional supporting materials with large submissions.

### Before Submission

Please follow these steps to ensure your code is ready for submission:

- **Unit Tests:** Ensure that all unit tests related to modified code pass successfully. Run the specific command, such as `pytest tests/*`, to execute the tests.
- **New Code Testing:** If you are adding new code files, ensure they have corresponding unit tests that pass.
- **Documentation:** All submitted code should include comprehensive `Google Docstring` descriptions and detailed comments explaining the functionality.

Before committing your code, set up `pre-commit` to check that your code meets our standards:

```bash
pip3 install pre-commit
pre-commit install
pre-commit run --all-files
```

This will automatically modify your local code to meet our coding standards. Remember to `git add` the changes again after running pre-commit.

### During Submission

Our project uses a `PULL_REQUEST_TEMPLATE` by default. When you submit a pull request, include the following necessary information:

- **Features:** Describe the features added or issues fixed by your PR. Required.
- **Documentation:** If applicable, link to the corresponding documentation on our docs site. Optional.
- **Impact:** Discuss any potential impacts this PR may have on the project. Optional.
- **Results:** Include results from tests or logs that demonstrate the functionality of your changes. Required.
- **Additional Materials:** Any other supplementary materials can be included here. Optional.

Providing this information helps our reviewers understand your PR better and speeds up the review process.

### After Submission

Once submitted, our default GitHub CI workflow will automatically check your code's compliance and unit tests. If your submission fails, you'll need to make the necessary modifications until it passes. Thus, running `pre-commit` checks and reviewing test results beforehand can greatly enhance the efficiency of this process.

## Issues

When submitting issues, you can include:

- **Bug Reports:** Use the `show_me_the_bug` template to provide a detailed description of the bug, how you might solve it (if known), environment details (like system version, Python version, dependencies), and any relevant screenshots or logs.
- **Feature Requests:** Describe new features you want supported or propose optimizations for existing features. We'll discuss these in the community and potentially add them to our ROADMAP.

## Documentation Contribution

Documentation site [docs](/).

We currently support documentation in English; however, we welcome contributions to create documentation to other languages. Please ensure your submissions are available in both languages:

- **Adding Content:** Follow the structure of existing documents. Save new content as Markdown files in the appropriate directory, e.g., `docs/get_started/`.
- **Media Files:** Store media files like images or videos in `docs/public`. Ensure they are correctly referenced in your documents.
- **Sidebar Updates:** If you add or change documentation, update the sidebar configuration in `docs/.vitepress/config.mts` accordingly.

To verify the appearance of new documents, you can deploy the documentation site locally by running `cd docs && npm ci && npm run docs:dev`.

For any issues or discussions, please join our [Discord Channel](https://discord.gg/z27CxnwdhY).

We look forward to your contributions, and thank you for helping us improve L2MAC!