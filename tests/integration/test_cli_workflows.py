from pathlib import Path
import os
import subprocess
import sys


def _run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    repo_root = Path(__file__).resolve().parents[2]
    env = os.environ.copy()
    env["PYTHONPATH"] = str(repo_root / "src")

    return subprocess.run(
        [sys.executable, "-m", "automata_toolkit.cli.main", *args],
        cwd=repo_root,
        capture_output=True,
        text=True,
        env=env,
    )


def test_cli_check_all_runs_successfully() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    sample_file = repo_root / "data" / "raw" / "efrei_test_cases" / "sample_automaton.txt"

    result = _run_cli("--input", str(sample_file), "--check-all")

    assert result.returncode == 0
    assert "Automaton loaded successfully." in result.stdout
    assert "Properties" in result.stdout
    assert "Integrity" in result.stdout
    assert "Deterministic" in result.stdout
    assert "Complete" in result.stdout


def test_cli_word_recognition_reports_acceptance() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    sample_file = repo_root / "data" / "raw" / "efrei_test_cases" / "sample_automaton.txt"

    result = _run_cli("--input", str(sample_file), "--word", "a")

    assert result.returncode == 0
    assert "Word recognition" in result.stdout
    assert "- a -> accepted" in result.stdout


def test_cli_can_export_json_and_dot(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[2]
    sample_file = repo_root / "data" / "raw" / "efrei_test_cases" / "sample_automaton.txt"
    json_path = tmp_path / "automaton.json"
    dot_path = tmp_path / "automaton.dot"

    result = _run_cli(
        "--input",
        str(sample_file),
        "--export-json",
        str(json_path),
        "--export-dot",
        str(dot_path),
    )

    assert result.returncode == 0
    assert json_path.exists()
    assert dot_path.exists()
    assert "JSON exported to" in result.stdout
    assert "DOT exported to" in result.stdout


def test_cli_complete_and_complement_runs_successfully() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    sample_file = repo_root / "data" / "raw" / "efrei_test_cases" / "sample_automaton.txt"

    result = _run_cli(
        "--input",
        str(sample_file),
        "--complete",
        "--complement",
    )

    assert result.returncode == 0
    assert "Transformed automaton" in result.stdout