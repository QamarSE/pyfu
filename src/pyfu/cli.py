import argparse
import subprocess
import sys
from pathlib import Path
import shutil
from rich.console import Console
from rich.panel import Panel

console = Console()

def run(cmd: list[str], title: str) -> int:
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except Exception as e:
        console.print(Panel(f"[red]{e}[/red]", title=f'Running "{title}"', border_style="yellow"))
        return 1

    output = []
    if result.stdout.strip():
        output.append(result.stdout.rstrip())
    if result.stderr.strip():
        output.append(result.stderr.rstrip())

    body = "\n".join(output) if output else "[green]No output[/green]"
    border_color = "cyan" if result.returncode == 0 else "yellow"
    console.print(Panel(body, title=f'Running "{title}"', border_style=border_color))
    return result.returncode

def read_excludes(root: Path) -> set[Path]:
    exclude_file = root / "exclude.txt"
    if not exclude_file.exists():
        return set()
    return {(root / line.strip()).resolve() for line in exclude_file.read_text().splitlines() if line.strip()}

def collect_python_files(target: Path) -> list[Path]:
    if target.is_file() and target.suffix == ".py":
        return [target]
    return list(target.rglob("*.py"))

def suffixed_path(path: Path, suffix: str) -> Path:
    return path.parent / f"{path.stem}{suffix}{path.suffix}"

def main() -> None:
    parser = argparse.ArgumentParser(prog="pyfu")
    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("--output-suffix", default="_sanitized")
    parser.add_argument("--no-suffix", action="store_true")
    args = parser.parse_args()

    target = Path(args.path).resolve()
    if not target.exists():
        console.print(f"[red]Path not found:[/red] {target}")
        sys.exit(1)

    root = target if target.is_dir() else target.parent
    excludes = read_excludes(root)

    original_files = [f for f in collect_python_files(target) if f.resolve() not in excludes]
    if not original_files:
        console.print("[yellow]No Python files to process[/yellow]")
        return

    # Copy to suffixed files first
    work_files = []
    for f in original_files:
        if args.no_suffix:
            work_files.append(f)
        else:
            out = suffixed_path(f, args.output_suffix)
            shutil.copyfile(f, out)
            work_files.append(out)

    console.print(Panel.fit(f"🛠️ pyfu processing {len(work_files)} file(s)", style="bold cyan"))

    # Run formatters only on the copied/suffixed files
    results = {
        "Ruff": run([sys.executable, "-m", "ruff", "check", *map(str, work_files), "--fix", "--exit-zero", "--quiet"], "Ruff"),
        "Black": run([sys.executable, "-m", "black", *map(str, work_files), "--quiet"], "Black"),
        "Mypy": run([sys.executable, "-m", "mypy", *map(str, work_files), "--hide-error-context", "--no-error-summary"], "Mypy"),
    }

    failed = [name for name, code in results.items() if code != 0]
    if failed:
        console.print(Panel.fit("⚠️ pyfu finished with issues in: " + ", ".join(failed), style="bold yellow"))

    console.print(Panel.fit("✅ pyfu finished successfully", style="bold green"))
    console.print(Panel.fit(f"💾 Sanitized files:\n" + "\n".join(map(str, work_files)), style="bold magenta"))

if __name__ == "__main__":
    main()
    