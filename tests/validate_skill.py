#!/usr/bin/env python3
"""Basic portable sanity checks for AI-LTS Agent Skill files."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = [
    "SKILL.md", "README.md", "agents/openai.yaml",
    "references/ai-lts-standard.zh-CN.md",
    "references/curriculum-design.md",
    "references/diagnosis-and-assessment.md",
    "references/continuity.md",
    "assets/universal-prompt.zh-CN.txt",
    "assets/project-charter.template.md", "assets/curriculum.template.md",
    "assets/diagnosis.template.md", "assets/lesson.template.md",
    "assets/gate-report.template.md", "assets/status-snapshot.template.md",
    "examples/README.md",
    "examples/software-engineering.md", "examples/mathematics.md",
    "examples/english.md", "examples/chinese-history.md",
    "examples/creative-writing.md", "examples/electronic-keyboard.md",
    "examples/internet-business.md", "examples/trading.md",
    "examples/ai-indie-game-developer.md",
]
errors = []
for relative in EXPECTED:
    p = ROOT / relative
    if not p.is_file() or p.stat().st_size == 0:
        errors.append(f"Missing or empty: {relative}")
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
if not skill.startswith("---\nname: ai-long-term-learning\n"):
    errors.append("Incorrect Agent Skills YAML frontmatter name")
if "description:" not in skill.split("---", 2)[1]:
    errors.append("Missing description")
for target in re.findall(r"\]\(([^)]+)\)", skill):
    if target.startswith(("http:", "https:", "#")):
        continue
    if not (ROOT / target.split("#",1)[0]).exists():
        errors.append(f"Invalid Skill link: {target}")
standard = ROOT / "references/ai-lts-standard.zh-CN.md"
if standard.exists() and standard.stat().st_size < 20000:
    errors.append("Full AI-LTS teaching standard looks truncated")
if errors:
    for e in errors: print("ERROR:", e)
    sys.exit(1)
print("OK: AI-LTS standalone Skill structure, references, and nine examples.")
