"""Tests for the hello_world application."""

import sys

from hello_world import main


def test_main_prints_expected_output(capsys):
    main()

    output = capsys.readouterr().out.splitlines()
    assert output == [
        "a first github trial",
        sys.platform,
        "Testing github...seems to be a very powerful environment",
    ]