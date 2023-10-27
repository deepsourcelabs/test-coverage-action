#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess  # skipcq: BAN-B404
import sys

# input for the actions are converted to names of a specific format by GitHub
INPUT_KEYS_MAP = {
    "key": "INPUT_KEY",
    "coverage_file": "INPUT_COVERAGE-FILE",
    "dsn": "INPUT_DSN",
    "fail_ci_on_error": "INPUT_FAIL-CI-ON-ERROR",
    "commit_sha": "INPUT_COMMIT-SHA",
}

DEEPSOURCE_CLI_PATH = "/app/bin/deepsource"

DEEPSOURCE_TEST_COVERAGE_ANALYZER_SHORTCODE = "test-coverage"

GITHUB_WORKSPACE_PATH = os.environ.get("GITHUB_WORKSPACE")


def main() -> None:
    """
    Get the metadata required for invoking DeepSource CLI from the environment
    and invoke the CLI to report the test coverage.
    Optionally, fail with a non-zero exit code if the user has configured so.
    """

    input_data = {key: os.getenv(value) for key, value in INPUT_KEYS_MAP.items()}
    commit_sha = input_data["commit_sha"]

    # Case: When user hasn't set the commit sha
    # or, when this action is run on a non-pull request event, the default value is going to
    # be an empty string.
    # in such case, fetch commit sha from the `GITHUB_SHA` environment variable.
    # Doing this is the best way to go because of the following reasons:
    # 1. we don't have to run any git commands to fetch the commit sha,
    # making the action work all the time
    # 2. the default being set to PR's head sha will take care of merge commit.
    # In all other cases, GITHUB_SHA would be accurate.
    # 3. GITHUB_SHA is always set, so we don't have to worry about it being empty.
    if not commit_sha:
        commit_sha = os.getenv("GITHUB_SHA")

    command = [
        DEEPSOURCE_CLI_PATH,
        "report",
        "--analyzer",
        DEEPSOURCE_TEST_COVERAGE_ANALYZER_SHORTCODE,
        "--key",
        input_data["key"],
        "--value-file",
        input_data["coverage_file"],
    ]

    # change the current working directory to the GitHub repository's context
    os.chdir(GITHUB_WORKSPACE_PATH)

    # skipcq: BAN-B603, PYL-W1510
    process = subprocess.run(
        command,
        env=dict(
            os.environ,
            DEEPSOURCE_DSN=input_data["dsn"],
            GHA_HEAD_COMMIT_SHA=commit_sha,
        ),
        capture_output=True,
    )

    if process.returncode != 0:
        if input_data["fail_ci_on_error"] == "true":
            print(f"::error file:main.py::{process.stdout.decode('utf-8')}")
            sys.exit(1)

    print(process.stdout.decode("utf-8"))
    print(process.stderr.decode("utf-8"), file=sys.stderr)


if __name__ == "__main__":
    main()
