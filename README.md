# DeepSource Test Coverage Action

[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/deepsourcelabs/test-coverage-action/?ref=repository-badge)

GitHub Action that enables you to upload your test coverage data to DeepSource easily. You must have the [Test Coverage](https://deepsource.io/docs/analyzer/test-coverage.html?utm_source=githubmarketplace&utm_medium=organic) analyzer enabled on your repository for reporting to work. Please refer to the [.deepsource.toml configuration reference](https://deepsource.io/docs/config/deepsource-toml.html?utm_source=githubmarketplace&utm_medium=organic#analyzers) for details.

If you're not using DeepSource yet, [get started for free](https://deepsource.io/signup?utm_source=githubmarketplace&utm_medium=organic).

## Notice

If you’re using the Test coverage action, we recommend switching to using the DeepSource CLI directly.
To do this, rather than using the `test-coverage-action` step, you can do the following:

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v2
    with:
      ref: ${{ github.event.pull_request.head.sha }}

  # Run your tests here ...

  - name: Report test-coverage to DeepSource
    run: |
      # Install the CLI
      curl https://deepsource.io/cli | sh

      # Send the report to DeepSource
      ./bin/deepsource report --analyzer test-coverage --key <language> --value-file <path/to/coverage/file>
```

If you want to continue using the Test coverage action, please add a step before the test coverage action, to add a
`safe.directory` parameter to your `.gitconfig`:

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v2
    with:
      fetch-depth: 50
      ref: ${{ github.event.pull_request.head.sha }}

  # ADD THIS STEP
  - name: Add git safe.directory for container
    run: |
      mkdir -p /home/runner/work/_temp/_github_home
      printf "[safe]\ndirectory = /github/workspace" > /home/runner/work/_temp/_github_home/.gitconfig

  - name: Report test-coverage to DeepSource
    uses: deepsourcelabs/test-coverage-action@master
    with:
      ... The rest of your config is explained in Usage section.
```

Read this [Discuss post](https://discuss.deepsource.io/t/breaking-deepsource-test-coverage-github-action/507) for more information.

## Usage

This Action assumes that the coverage file has already been generated after the tests have run. To integrate it in your workflow, define a step which refers to this Action in your `workflow.yml` file. We recommend that you use `@master` as the ref.

Ensure that you have added the `DEEPSOURCE_DSN` secret in your GitHub repository. It is available under **Settings → Reporting tab** of the repository page on DeepSource.

```yaml
steps:
  - name: Report test coverage to DeepSource
    uses: deepsourcelabs/test-coverage-action@master
    with:
      key: python
      coverage-file: coverage.xml
      dsn: ${{ secrets.DEEPSOURCE_DSN }}
```

The possible inputs to this action are:

* `key` (string, **required**): Programming language shortcode for which coverage is reported. e.g. `python`, `go`, `javascript`.
  See [the docs](https://docs.deepsource.com/docs/analyzers-test-coverage#reporting-coverage-artifact-using-the-cli) for the current list of allowed values.
* `coverage-file` (string, **required**): Path to the coverage data file. e. g. `coverage.xml`
* `dsn` (string, **required**): DeepSource DSN of this repository.
* `fail-ci-on-error` (boolean): Should the CI build fail if there is an error while uploading the report to DeepSource? Allowed values are: `true`, `false`. This is set to `false` by default.

## License

This project is released under the [MIT License](LICENSE).
