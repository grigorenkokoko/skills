#!/usr/bin/env python3
"""Validate the single-skill iOS App Store workflow contract."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKILL_ROOT = ROOT / "build-ios-app"
ERRORS: list[str] = []


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        ERRORS.append(f"missing file: {relative}")
        return ""
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, context: str) -> None:
    if needle not in text:
        ERRORS.append(f"{context}: missing {needle!r}")


def reject(text: str, needle: str, context: str) -> None:
    if needle in text:
        ERRORS.append(f"{context}: forbidden {needle!r}")


required_files = (
    "build-ios-app/SKILL.md",
    "build-ios-app/scripts/validate_skill.py",
    "build-ios-app/references/idea-stage.md",
    "build-ios-app/references/design-stage.md",
    "build-ios-app/references/build-stage.md",
    "build-ios-app/references/release-stage.md",
    "build-ios-app/references/app-privacy-contract.md",
    "build-ios-app/references/AppPrivacy.template.yml",
    "build-ios-app/version.json",
    "README.md",
)
for required_file in required_files:
    if not (ROOT / required_file).is_file():
        ERRORS.append(f"missing file: {required_file}")

legacy_paths = (
    "generate-ios-app-ideas",
    "design-ios-app-concept",
    "build-ios-app-concept",
    "prepare-ios-app-store-release",
    "evals",
)
for legacy_path in legacy_paths:
    if (ROOT / legacy_path).exists():
        ERRORS.append(f"legacy path still exists: {legacy_path}")

skill_files = sorted(
    path.relative_to(ROOT).as_posix() for path in ROOT.glob("*/SKILL.md")
)
if skill_files != ["build-ios-app/SKILL.md"]:
    ERRORS.append(f"expected one installable skill, found: {skill_files}")

skill = read("build-ios-app/SKILL.md")
idea = read("build-ios-app/references/idea-stage.md")
design = read("build-ios-app/references/design-stage.md")
build = read("build-ios-app/references/build-stage.md")
release = read("build-ios-app/references/release-stage.md")
privacy_reference = read("build-ios-app/references/app-privacy-contract.md")
privacy_template = read("build-ios-app/references/AppPrivacy.template.yml")
readme = read("README.md")

require(skill, "name: build-ios-app", "SKILL.md")
frontmatter_match = re.match(r"^---\n(.*?)\n---", skill, flags=re.DOTALL)
if not frontmatter_match:
    ERRORS.append("SKILL.md: invalid YAML frontmatter boundaries")
else:
    frontmatter: dict[str, str] = {}
    for line in frontmatter_match.group(1).splitlines():
        if ":" not in line:
            ERRORS.append(f"SKILL.md: invalid frontmatter line {line!r}")
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()
    if set(frontmatter) != {"name", "description"}:
        ERRORS.append("SKILL.md: frontmatter must contain only name and description")
    name = frontmatter.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        ERRORS.append("SKILL.md: name must be hyphen-case and at most 64 characters")
    description = frontmatter.get("description", "")
    if not description.startswith("Use when "):
        ERRORS.append("SKILL.md: description must start with 'Use when '")
    if len(description) > 1024 or "<" in description or ">" in description:
        ERRORS.append("SKILL.md: description is invalid or longer than 1024 characters")

for needle in (
    "## Triggers",
    "## Usage",
    "## Explicit approval contract",
    "user-authored message",
    "after the gate summary",
    "authorizes the named next stage",
    "blanket approval",
    "idea-stage.md",
    "design-stage.md",
    "build-stage.md",
    "release-stage.md",
    "policy-approved",
    "design-approved",
    "implementation-verified",
    "archive-validated",
    "release-ready",
    "submitted",
):
    require(skill, needle, "SKILL.md")

for needle in (
    "App Review feasibility gate",
    "AppPrivacy.yml",
    "references/AppPrivacy.template.yml",
    "AppMetrica",
    "Lock Screen widget",
    "Notification Service Extension",
    "Notification Content Extension",
):
    require(idea, needle, "idea-stage.md")
reject(idea, "assets/AppPrivacy.template.yml", "idea-stage.md")

for needle in (
    "policy-approved",
    "AppPrivacy.yml",
    "privacy-policy",
    "design-approved",
    "explicit approval",
):
    require(design, needle, "design-stage.md")

capabilities = (
    "NSBluetoothAlwaysUsageDescription",
    "NSCameraUsageDescription",
    "NSContactsUsageDescription",
    "NSFaceIDUsageDescription",
    "NSLocationWhenInUseUsageDescription",
    "NSMicrophoneUsageDescription",
    "NSPhotoLibraryUsageDescription",
    "NSPhotoLibraryAddUsageDescription",
    "NSUserTrackingUsageDescription",
    "Push notifications",
)
for capability in capabilities:
    require(idea, capability, "idea-stage.md")
    require(build, capability, "build-stage.md")

for needle in (
    "design-approved",
    "AppMetrica",
    "Do not create unit-test or UI-test targets",
    "implementation-verified",
    "manual device",
):
    require(build, needle, "build-stage.md")

for needle in (
    "implementation-verified",
    "archive-validated",
    "release-ready",
    "current primary Apple",
    "Xcode Privacy Report",
    "explicit user approval",
    "manual device",
):
    require(release, needle, "release-stage.md")

for needle in (
    "permissions",
    "data_inventory",
    "third_party_sdks",
    "tracking",
    "domains",
    "privacy_policy",
    "app_store_privacy",
    "policy_modules",
    "approval_log",
    "release_blockers",
):
    require(privacy_template, needle, "AppPrivacy.template.yml")

for needle in (
    "source of truth",
    "AppSpec.md",
    "AppPrivacy.yml",
    "approval_log",
    "AppMetrica",
    "fails closed",
):
    require(privacy_reference, needle, "app-privacy-contract.md")

for needle in (
    "build-ios-app",
    ".agents/skills",
    "/skills",
    "$build-ios-app",
    "## Пошаговый сценарий",
    "### Шаг 0. Открыть рабочую папку приложения",
    "### Шаг 1. Утвердить идею",
    "### Шаг 2. Утвердить дизайн",
    "### Шаг 3. Проверить реализацию",
    "### Шаг 4. Подготовить релиз",
    "### Шаг 5. Разрешить внешнее действие",
    "## Полный пример диалога",
    "## Если нужна доработка",
    "## Как продолжить после паузы",
    "## Когда понадобятся внешние данные",
    "Что создаёт скилл",
    "Что проверить пользователю",
    "Как продолжить",
    "AppSpec.md",
    "AppPrivacy.yml",
    "release-ready",
    "manual-device-checks.md",
    "python3 build-ios-app/scripts/validate_skill.py",
):
    require(readme, needle, "README.md")

for legacy_name in (
    "generate-ios-app-ideas",
    "design-ios-app-concept",
    "build-ios-app-concept",
    "prepare-ios-app-store-release",
    "device-tested",
):
    reject(skill + idea + design + build + release + readme, legacy_name, "public docs")

version_path = SKILL_ROOT / "version.json"
if version_path.is_file():
    try:
        version_data = json.loads(version_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        ERRORS.append(f"version.json: invalid JSON: {error}")
    else:
        if set(version_data) != {"version", "changelog", "category", "author"}:
            ERRORS.append("version.json: expected version, changelog, category, author")
        version = version_data.get("version", "")
        if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
            ERRORS.append("version.json: version must use semantic x.y.z form")
        if not isinstance(version_data.get("category"), str) or not version_data["category"]:
            ERRORS.append("version.json: category must be a non-empty string")
        if not isinstance(version_data.get("author"), str) or not version_data["author"]:
            ERRORS.append("version.json: author must be a non-empty string")
        changelog = version_data.get("changelog")
        if not isinstance(changelog, list) or not changelog:
            ERRORS.append("version.json: changelog must be a non-empty list")
        elif not isinstance(changelog[0], dict) or changelog[0].get("version") != version:
            ERRORS.append("version.json: first changelog version must match version")

if ERRORS:
    print("Skill validation failed:")
    for error in ERRORS:
        print(f"- {error}")
    sys.exit(1)

print("Skill validation passed")
