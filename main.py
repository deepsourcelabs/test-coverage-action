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
}

DEEPSOURCE_CLI_PATH = "/app/bin/deepsource"

DEEPSOURCE_TEST_COVERAGE_ANALYZER_SHORTCODE = "test-coverage"

GITHUB_WORKSPACE_PATH = os.environ.get("GITHUB_WORKSPACE")
print(GITHUB_WORKSPACE_PATH)
print(os.listdir(GITHUB_WORKSPACE_PATH))


def main() -> None:
    """
    Get the metadata required for invoking DeepSource CLI from the environment
    and invoke the CLI to report the test coverage.
    Optionally, fail with a non-zero exit code if the user has configured so.
    """

    input_data = {key: os.getenv(value) for key, value in INPUT_KEYS_MAP.items()}

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

    print("======================")
    print("Changing directory to", GITHUB_WORKSPACE_PATH)
    # change the current working directory to the GitHub repository's context
    os.chdir(GITHUB_WORKSPACE_PATH)

    print("======================")
    print("git log output:")
    p = subprocess.run("git log | head -30", shell=True, capture_output=True)
    print(p.stdout.decode(), "***")

    # skipcq: BAN-B603, PYL-W1510
    process = subprocess.run(
        command,
        env=dict(os.environ, DEEPSOURCE_DSN=input_data["dsn"]),
        capture_output=True,
    )

    if process.returncode != 0:
        if input_data["fail_ci_on_error"] == "true":
            print(f"::error file:main.py::{process.stdout.decode('utf-8')}")
            sys.exit(1)

    print("======================")
    print("DeepSource CLI output:")
    print(process.stdout.decode("utf-8"))
    print(process.stderr.decode("utf-8"), file=sys.stderr)


if __name__ == "__main__":
    main()
