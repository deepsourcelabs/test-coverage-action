<p align="center">
  <img src="https://cms.deepsource.io/logo-wordmark-dark.svg" />
</p>

<p align="center">
  <a href="https://docs.deepsource.com">Docs</a> |
  <a href="https://deepsource.com">Get Started</a> |
  <a href="https://discuss.deepsource.com/">Discuss</a>
</p>

<p align="center">
  The Code Health Platform
</p>

</p>

---

GitHub Action that enables you to upload your test coverage data to DeepSource easily. You must have the [Test Coverage](https://docs.deepsource.com/docs/analyzers-test-coverage) analyzer enabled on your repository for reporting to work.

If you're not using DeepSource yet, [get started for free](https://deepsource.com/).

## Usage

This Action assumes that the coverage file has already been generated after the tests have run. To integrate it in your workflow, define a step which refers to this Action in your `workflow.yml` file. We recommend that you use `@master` as the ref.

Ensure that you have added the `DEEPSOURCE_DSN` secret in your GitHub repository. It is available under **Settings → Code Coverage** of the repository page on DeepSource.

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
