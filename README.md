# DeepSource Test Coverage Action

[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/deepsourcelabs/test-coverage-action/?ref=repository-badge)

GitHub Action that enables you to upload your test coverage data to DeepSource easily. You must have the [Test Coverage](https://deepsource.io/docs/analyzer/test-coverage.html?utm_source=githubmarketplace&utm_medium=organic) analyzer enabled on your repository for reporting to work. Please refer to the [.deepsource.toml configuration reference](https://deepsource.io/docs/config/deepsource-toml.html?utm_source=githubmarketplace&utm_medium=organic#analyzers) for details.

If you're not using DeepSource yet, [get started for free](https://deepsource.io/signup?utm_source=githubmarketplace&utm_medium=organic).


## Usage

This Action assumes that the coverage file has already been generated after the tests have run. To integrate it in your workflow, define a step which refers to this Action in your `workflow.yml` file. We recommend that you use `@master`as the ref.

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
* `dsn` (string, **required**): DeepSource DSN of this repository. It is available under **Settings → Reporting tab** of the repository page on DeepSource.
* `fail-ci-on-error` (boolean): Should the CI build fail if there is an error while uploading the report to DeepSource? Allowed values are: `true`, `false`. This is set to `false` by default.

## License

This project is released under the [MIT License](LICENSE).
