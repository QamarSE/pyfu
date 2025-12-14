import subprocess
import sys
from pathlib import Path

subprocess.run(["python", "-m", "hatch", "build"], check=True)

wheel = next(Path("dist").glob("*.whl"))

subprocess.run([sys.executable, "-m", "pip", "install", str(wheel)], check=True)

subprocess.run(["pyfu", "--help"], check=False, text=True, stdout=None, stderr=None)

subprocess.run(["pyfu", "tests"], check=False, text=True, stdout=None, stderr=None)
