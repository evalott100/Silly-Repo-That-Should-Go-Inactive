import subprocess
import sys

from silly_repo_that_may_go_inactive import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "silly_repo_that_may_go_inactive", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
