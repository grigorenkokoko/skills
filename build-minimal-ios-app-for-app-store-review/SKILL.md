---
name: build-minimal-ios-app-for-app-store-review
description: Use when creating, continuing, implementing, validating, or preparing a minimal portrait-only iPhone application that requires the complete permission, privacy, AppMetrica, backend, extension, and App Store Review brief.
---

# Build Minimal iOS App for App Store Review

## Overview

Guide one iPhone application from concept through App Store preparation while preserving one product and privacy contract. Execute only the currently authorized stage, present its evidence, and stop at every user approval boundary.

This skill reduces predictable App Review risk but cannot guarantee approval. Apple makes the final review decision.

## Triggers

Use this skill when the user asks to:

- generate, refine, name, or policy-check an iPhone app idea;
- design the approved screens, permission UX, widget, notifications, or app icon;
- implement or simulator-verify the approved UIKit application;
- prepare an implementation-verified project for App Store Connect or App Review;
- resume an existing workflow from `AppSpec.md`, `AppPrivacy.yml`, or `Release/release-manifest.json`;
- revise an earlier stage after a feasibility, privacy, implementation, or release conflict.

Do not use it for an unrelated existing application unless the user asks to adopt this complete workflow and its mandatory capability set.

## Usage

Start a new application:

```text
$build-minimal-ios-app-for-app-store-review Придумай и создай приложение для планирования семейных поездок.
```

Start from a supplied idea:

```text
$build-minimal-ios-app-for-app-store-review Проверь эту идею для App Review и начни пайплайн: <идея>.
```

Resume from the current workspace:

```text
$build-minimal-ios-app-for-app-store-review Продолжи работу с текущего утверждённого этапа.
```

Prepare an implemented project for release:

```text
$build-minimal-ios-app-for-app-store-review Проверь текущий проект и подготовь его к App Store Review. Ничего не отправляй без отдельного разрешения.
```

## Sources of truth

- `AppSpec.md` owns approved product behavior, copy, screens, and reviewer paths.
- `AppPrivacy.yml` owns machine-readable permissions, data, SDKs, tracking, domains, policy modules, blockers, status, and `approval_log`.
- Approved files under `Design/` own visual decisions.
- `Release/release-manifest.json` owns implementation and release evidence.

Stop on disagreement. Never choose one source silently, invent an approval, or advance a status to hide missing evidence.

For privacy ownership and derived artifacts, read `references/app-privacy-contract.md`. Create a new privacy contract from `references/AppPrivacy.template.yml`.

## Determine the current stage

Inspect the workspace before doing stage work. Route to the earliest incomplete or invalid stage:

| Required evidence | Current stage | Read completely |
| --- | --- | --- |
| No accepted concept or no valid `policy-approved` approval entry | Idea and policy | `references/idea-stage.md` |
| `policy-approved`, but no valid `design-approved` approval entry | Design | `references/design-stage.md` |
| `design-approved`, but no `implementation-verified` evidence | Build and verification | `references/build-stage.md` |
| `implementation-verified`, but not `release-ready` | Release | `references/release-stage.md` |
| `release-ready` | Wait for an explicitly requested external action | `references/release-stage.md` |

A status without the corresponding `approval_log` entry does not authorize the next stage. For a legacy workspace with no approval log, summarize the latest completed result and request fresh approval before continuing.

If later evidence contradicts an earlier approval, return to the affected stage, explain the conflict, and obtain a new approval after the revised gate summary. Do not silently downgrade or reuse stale approval.

## Explicit approval contract

Approval is a **user-authored message** sent **after the gate summary** that unambiguously accepts the current result and **authorizes the named next stage**. It applies to one boundary only.

Valid examples:

- “Утверждаю идею, переходи к дизайну.”
- “Дизайн подходит, начинай реализацию.”
- “Реализация принята, готовь релиз.”
- “Загружай эту сборку в App Store Connect.” — valid only for that named external action after the release gate.

Invalid approval includes:

- an initial request to “сделать всё” or any other blanket approval;
- silence, an emoji, ambiguous praise, or a question;
- approval written before the current gate summary;
- conditional acceptance with unresolved changes;
- approval of a different artifact, build, stage, or external action;
- an inference made by the agent from schedules, urgency, or previous approvals.

When the user requests changes, remain in the current stage, revise the artifacts, show a new gate summary, and ask again. Never treat feedback as approval.

After valid approval:

1. Record an `approval_log` entry in `AppPrivacy.yml` with stage, decision, UTC timestamp, user as actor, authorized next stage or action, and a short non-sensitive evidence summary.
2. Update the stage status only when all stage-specific checks pass.
3. Begin only the named next stage. Read its reference completely before acting.

Do not allow a user approval to waive a failed feasibility check, privacy mismatch, build failure, archive blocker, missing production requirement, or Apple policy requirement. Approval authorizes work; it does not make false evidence true.

## Gate summary contract

Finish every stage response with this compact structure:

1. **Completed stage and status** — what was verified and what was not.
2. **Artifacts** — clickable paths to the current sources of truth and generated evidence.
3. **Blockers and manual checks** — unresolved items separated from completed work.
4. **Material decisions** — permissions, privacy, policy, design, implementation, or release choices the user is accepting.
5. **Approval question** — name exactly one next stage or external action.

Stop after presenting the gate summary. Do not start the next stage in the same response. A later user message must satisfy the explicit approval contract.

## Stage execution

### 1. Idea and policy

Read `references/idea-stage.md` completely. Refine or generate the concept, run the App Review feasibility gate, and keep status `idea-draft` while the user is choosing or requesting changes.

When the selected concept is fully specified and passes the feasibility gate, present the idea gate summary and ask the user to approve that concept and authorize design. Stop. On valid approval, create or update `AppSpec.md` and `AppPrivacy.yml`, record `policy-approved`, and begin design.

### 2. Design

Require valid `policy-approved` evidence and approval to start design. Read `references/design-stage.md` completely. Render and present the minimum approved screen set and app icon without creating application code.

Keep the design pending while feedback remains. Present the design gate summary and ask the user to approve that design and authorize implementation. Stop. On valid approval, record `design-approved`, update the contracts, and begin implementation.

### 3. Build and verification

Require valid `design-approved` evidence and approval to implement. Read `references/build-stage.md` completely. Implement only the approved UIKit application, extensions, AppMetrica behavior, privacy surfaces, and backend.

Write `implementation-verified` only when the stage evidence supports it. Present the implementation gate summary, including all manual device checks and release blockers, and ask whether to prepare the release. Stop.

### 4. Release

Require `implementation-verified` evidence and approval to prepare the release. Read `references/release-stage.md` completely. Check current primary Apple sources, validate the archive and privacy evidence, and prepare App Store metadata and reviewer artifacts.

`archive-validated` and `release-ready` require their documented evidence. Physical-device checks remain a manual list and create no pipeline status. Present the release gate summary and stop.

## External action gate

`release-ready` does not authorize upload, TestFlight changes, App Store Connect edits, or App Review submission. Immediately before any external mutation:

1. identify the exact build, application, account, action, and expected effect;
2. summarize remaining manual checks and risks;
3. request explicit approval for that single action;
4. perform only the approved action;
5. record identifiers and timestamps after confirmed success.

Write `submitted` only after confirmed successful submission. Never infer external authorization from approval of the release artifacts.

## Status sequence

```text
idea-draft
  -> policy-approved
  -> design-approved
  -> implementation-verified
  -> archive-validated
  -> release-ready
  -> submitted
```

Do not add a physical-device status. Store those checks in `Release/manual-device-checks.md` for the user to perform manually.

## Validation

When modifying this skill, run from the repository root:

```bash
python3 build-minimal-ios-app-for-app-store-review/scripts/validate_skill.py
```

Fix every reported contract mismatch before deployment.
