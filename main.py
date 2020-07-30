#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import sys

# input for the actions are converted to names of a specific format by GitHub
INPUT_KEYS_MAP = {
    'key': 'INPUT_KEY',
    'coverage_file': 'INPUT_COVERAGEFILE',
    'dsn': 'INPUT_DSN',
    'fail_ci_on_error': 'INPUT_FAILCIONERROR'
}

DEEPSOURCE_CLI_PATH = './bin/deepsource'

DEEPSOURCE_TEST_COVERAGE_ANALYZER_SHORTCODE = 'test-coverage'

def main() -> None:
    """
    Get the metadata required for invoking DeepSource CLI from the environment
    and invoke the CLI to report the test coverage.
    Optionally, fail with a non-zero exit code if the user has configured so.
    """

    input_data = {
        key: os.getenv(value) for key, value in INPUT_KEYS_MAP.items()
    }

    command = [
        {DEEPSOURCE_CLI_PATH},
        '--analyzer',
        DEEPSOURCE_TEST_COVERAGE_ANALYZER_SHORTCODE,
        '--key',
        input_data['key'],
        '--value-file',
        input_data['coverage_file']
    ]

    process = subprocess.run(
        command,
        env=dict(os.environ, DEEPSOURCE_DSN=input_data['dsn']),
        capture_output=True
    )

    if process.returncode != 0:
        if input_data['fail_ci_on_error'] == 'true':
            print(f'::error file:main.py::{process.stdout}')
            sys.exit(1)


if __name__ == '__main__':
    main()
