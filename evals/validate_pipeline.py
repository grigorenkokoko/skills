#!/usr/bin/env python3
"""Deterministic contract checks for the four-stage iOS skill pipeline."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
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


def require_trigger_description(text: str, context: str) -> None:
    match = re.search(r"^description:\s*(.+)$", text, flags=re.MULTILINE)
    if not match or not match.group(1).startswith("Use when "):
        ERRORS.append(f"{context}: description must start with 'Use when '")


idea = read("generate-ios-app-ideas/SKILL.md")
design = read("design-ios-app-concept/SKILL.md")
build = read("build-ios-app-concept/SKILL.md")
release = read("prepare-ios-app-store-release/SKILL.md")
privacy_reference = read("generate-ios-app-ideas/references/app-privacy-contract.md")
privacy_template = read("generate-ios-app-ideas/assets/AppPrivacy.template.yml")

for name, text in (
    ("generate-ios-app-ideas", idea),
    ("design-ios-app-concept", design),
    ("build-ios-app-concept", build),
    ("prepare-ios-app-store-release", release),
):
    require_trigger_description(text, name)
    reject(text, "device-tested", name)

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
    require(idea, capability, "generate-ios-app-ideas")
    require(build, capability, "build-ios-app-concept")

for needle in (
    "App Review feasibility gate",
    "policy-approved",
    "AppPrivacy.yml",
    "AppMetrica",
    "Lock Screen widget",
    "Notification Service Extension",
    "Notification Content Extension",
    "conditional policy",
):
    require(idea, needle, "generate-ios-app-ideas")

for needle in (
    "policy-approved",
    "AppPrivacy.yml",
    "privacy-policy",
    "conditional policy",
    "design-approved",
):
    require(design, needle, "design-ios-app-concept")

for needle in (
    "policy-approved",
    "AppPrivacy.yml",
    "AppMetrica",
    "privacy-policy",
    "conditional policy",
    "implementation-verified",
    "prepare-ios-app-store-release",
    "Do not create unit-test or UI-test targets",
    "manual device",
):
    require(build, needle, "build-ios-app-concept")

for needle in (
    "implementation-verified",
    "archive-validated",
    "release-ready",
    "submitted",
    "current primary Apple",
    "AppPrivacy.yml",
    "Xcode Privacy Report",
    "AppMetrica",
    "privacy-policy",
    "conditional policy",
    "manual device",
    "explicit user approval",
):
    require(release, needle, "prepare-ios-app-store-release")

for needle in (
    "permissions",
    "data_inventory",
    "third_party_sdks",
    "tracking",
    "domains",
    "privacy_policy",
    "app_store_privacy",
    "policy_modules",
    "release_blockers",
):
    require(privacy_template, needle, "AppPrivacy.template.yml")

for needle in (
    "source of truth",
    "AppSpec.md",
    "PrivacyInfo.xcprivacy",
    "App Store",
    "AppMetrica",
    "fails closed",
):
    require(privacy_reference, needle, "app-privacy-contract.md")

if ERRORS:
    print("Pipeline contract validation failed:")
    for error in ERRORS:
        print(f"- {error}")
    sys.exit(1)

print("Pipeline contract validation passed")
