# 🛠️ pyfu — Python Fixer Upper

**pyfu** turns messy, inconsistent, and slightly cursed Python projects into clean, production-ready codebases.

If your code *works* but makes you uncomfortable, pyfu is for you.

---

## ✨ What pyfu does

* 🧹 Fixes bad imports, unsafe patterns, and common mistakes using Ruff
* 🎨 Formats code consistently using Black
* 🧠 Catches type and logic bugs early using Mypy
* ⚡ Improves maintainability with minimal setup
* 🧪 Runs a full fix pipeline without quitting early
* 🗂️ Supports safe, suffixed output files by default

Opinionated by design. Fast by default. Zero patience for bad code.

---

## 🤔 Why pyfu exists

Most Python projects are fixer-uppers:

* scripts that became libraries
* libraries that became monsters
* code that survived purely on hope

pyfu cleans, fixes, and upgrades these projects without forcing you to rewrite everything or risk breaking originals.

---

## 🚀 Installation

```bash
pip install pyfu
```

---

## 🧪 Basic usage

Fix a single file

```bash
pyfu path/to/file.py
```

Fix the current directory

```bash
pyfu .
```

Fix a specific project

```bash
pyfu path/to/project
```

---

## 🧰 Output behavior

By default, pyfu **does not modify your original files**.

Instead, it creates sanitized copies with a suffix:

```text
example.py  →  example_sanitized.py
```

This makes pyfu safe to run on any codebase.

---

## ⚙️ CLI arguments

Custom output suffix

```bash
pyfu . --output-suffix fixed_
```

Disable suffixed output and modify files in place

```bash
pyfu . --no-suffix
```

---

## 🚫 Excluding files

You can exclude specific Python files by creating an `exclude.txt` file at the project root.

One file per line, relative paths:

```text
tests/main.py
legacy/old_code.py
```

Excluded files are ignored even if pyfu is run on the entire directory.

---

## 🧩 What pyfu checks and fixes

* Unused and unsafe imports
* Broken or misleading code patterns
* Formatting inconsistencies
* Obvious logic mistakes
* Type safety issues
* General project hygiene problems

More checks will be added aggressively.

---

## 🧠 Tooling pipeline

pyfu always runs all tools in order:

1. Ruff (auto-fix where possible)
2. Black (formatting)
3. Mypy (type checking)

Even if one tool reports issues, the pipeline continues.

---

## ⚙️ Project philosophy

* Fast tools over fancy abstractions
* Automation over documentation walls
* Fix first, debate later
* Safe defaults > endless configuration

If the tool disagrees with you, it’s probably right.

---

## 🧠 Project status

* Early stage
* Actively evolving
* Breaking changes may happen
* Feedback is welcome

---

## 🤝 Contributing

PRs are welcome.
Bug reports are appreciated.
Style debates are ignored.

---

## 📜 License

MIT

---

Clean code. Fewer regrets. 🚀

![GitHub Stats](https://github-readme-stats-fast.vercel.app/api/pin/?username=pro-grammer-SD\&repo=pyfu\&theme=nord)
