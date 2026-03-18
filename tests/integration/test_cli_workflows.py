from pathlib import Path
import os
import subprocess
import sys


def test_cli_check_all_runs_successfully() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    sample_file = repo_root / "data" / "raw" / "efrei_test_cases" / "sample_automaton.txt"
    env = os.environ.copy()
    env["PYTHONPATH"] = str(repo_root / "src")

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "automata_toolkit.cli.main",
            "--input",
            str(sample_file),
            "--check-all",
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
        env=env,
    )

    assert result.returncode == 0
    assert "Automaton loaded successfully." in result.stdout
    assert "Properties" in result.stdout
