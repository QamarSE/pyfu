import subprocess
import sys
from pathlib import Path
import shutil

def run():
    subprocess.run([sys.executable, "-m", "pip", "uninstall", "pyfu", "-y"], check=True)
    subprocess.run([sys.executable, "-m", "hatch", "build"], check=True)

    wheel = next(Path("dist").glob("*.whl"))
    subprocess.run([sys.executable, "-m", "pip", "install", str(wheel)], check=True)

    print("\n📦 Running pyfu --help")
    subprocess.run(["pyfu", "--help"], check=False, text=True)

    print("\n📂 Running pyfu on tests folder")
    subprocess.run(["pyfu", "tests"], check=False, text=True)

    print("\n⚡ Building standalone exe with PyInstaller into bin/")
    bin_path = Path("bin")
    bin_path.mkdir(parents=True, exist_ok=True)

    subprocess.run([
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--console",
        "--distpath", str(bin_path),
        "src/pyfu/cli.py"
    ], check=True)

    # Remove build/ folder after PyInstaller, ignore permission errors
    build_dir = Path("build")
    if build_dir.exists():
        shutil.rmtree(build_dir, ignore_errors=True)
        print("🗑️ build/ folder removed successfully")

    exe_path = bin_path / "cli.exe"
    if exe_path.exists():
        print(f"\n✅ Build complete: {exe_path.resolve()}")
    else:
        print("\n❌ Build failed")

if __name__ == "__main__":
    run()
    