---
name: design-ios-app-concept
description: Use when a portrait-only iPhone concept is policy-approved and the user wants screen structure, permission UX, privacy and policy surfaces, visual mockups, accessibility behavior, widget and notification layouts, or an app icon before implementation.
---

# Design iOS App Concept

## Goal

Turn a policy-approved `AppSpec.md` and `AppPrivacy.yml` into the smallest feasible portrait-only iPhone interface that makes every required permission-backed function, privacy-policy entry, consent recovery path, and selected conditional policy module reachable through a clear user action. Render the application screens and app icon, show them to the user, and stop until the user explicitly approves the design.

Do not create an Xcode project, targets, dependencies, application source code, or backend. Keep product scope centered on the accepted permission-backed functions and add only the navigation, states, explanations, and error handling needed to make them understandable.

## Inputs and source of truth

Read both `AppSpec.md` and `AppPrivacy.yml`. Preserve the accepted product, naming, permission, privacy, tracking, AppMetrica, extension, backend, policy-module, platform, orientation, and review-risk decisions. `AppSpec.md` owns behavior and approved copy; `AppPrivacy.yml` owns machine-readable privacy and release facts. Stop on disagreement instead of choosing one silently.

Require `policy-approved` status and a passed App Review feasibility gate. If either source file is unavailable, the idea is still being selected, or a gate conflict remains, stop and propose `generate-ios-app-ideas` instead of reconstructing approval silently.

Do not reopen accepted decisions unless they create a concrete feasibility, privacy, accessibility, or App Store review conflict. Explain the conflict and obtain approval before changing `AppSpec.md`.

## Design rules

- Use the fewest screens that keep all permission-backed flows understandable. Prefer one primary screen with compact sections, sheets, alerts, and Apple-provided controllers.
- Add a screen only when an accepted interaction becomes materially clearer. Do not invent onboarding, profile, feed, history, settings, or other unrelated product features.
- Map every user-facing feature to at least one required authorization. Supporting navigation, state, configuration, analytics, extensions, backend interaction, and error handling are allowed and must stay minimal.
- Request a permission only after the user selects the visible feature that needs it. Never design a batch of prompts at launch.
- Preserve exact approved feature-specific permission copy. For push authorization, design the app-owned explanation while recognizing that iOS owns the system alert text.
- Cover `notDetermined`, authorized or limited, denied, restricted, unavailable, loading, empty, offline, success, and error states where applicable.
- Keep the core application useful when optional access, including ATT, is denied.
- Make microphone recording, saving, saved, playback, replace, and delete states clear through both status and controls.
- Show explicit standard UIKit success and failure feedback after PhotoKit add operations.
- Keep every layout feasible with programmatic UIKit, Auto Layout, iOS 15, iPhone-only deployment, and portrait-only orientation. Use SwiftUI only for the WidgetKit target where appropriate.
- Use native controls and navigation where practical. Support Dynamic Type, a logical VoiceOver order, meaningful labels and values, 44×44 point touch targets, sufficient light/dark contrast, and non-color status cues.
- Keep the Lock Screen widget glanceable and the notification content compact. Do not design them as substitute application screens.
- Include an easily accessible privacy-policy entry and a clear path to withdraw consent or reach system Settings where applicable.
- Implement every selected conditional policy module in the smallest reviewer-reachable surface. Do not add UI for modules marked `not-applicable`.
- Keep reviewer instructions, required sample data, and special-hardware entry paths consistent with the feasibility gate.

## Workflow

### Phase 1: Validate the accepted specification

Summarize without redefining:

- product name and primary scenario;
- permission-centered MVP and all 10 authorization mappings;
- exact permission and pre-permission copy;
- denial behavior and data handling;
- backend, AppMetrica, ATT, widget, and notification-extension roles;
- `AppPrivacy.yml` data inventory, SDK behavior, domains, privacy-policy disclosures, and release blockers;
- selected conditional policy modules and their required user/reviewer paths;
- passed feasibility-gate evidence and special-hardware review assumptions;
- platform, orientation, general-audience, and review-risk constraints.

Resolve contradictions with the user before rendering. Do not continue from an internally inconsistent specification or silently downgrade `policy-approved` decisions.

### Phase 2: Prepare the design

Provide:

1. Navigation map and minimum screen inventory.
2. Mapping from every accepted feature and permission trigger to a screen and control.
3. Low-fidelity wireframes for every distinct screen or important state.
4. Main, empty, loading, error, permission-not-determined, denied, limited, and authorized states where relevant.
5. The exact action that triggers each system permission request and the approved copy reproduced verbatim.
6. The easily accessible privacy-policy entry, consent-withdrawal paths, and exact Settings recovery behavior.
7. Screens, controls, confirmations, and reviewer paths required by each selected conditional policy module.
8. Widget and notification-content layouts plus relevant notification actions.
9. A compact visual system covering colors, typography, spacing, buttons, cards, icons, and approved light/dark behavior.
10. An accessibility specification covering Dynamic Type, VoiceOver names and order, grouping, touch targets, contrast, and non-color cues.
11. One original square app-icon direction consistent with the approved name and visual system. Keep it recognizable without small text or pre-rounded corners. Do not use an SF Symbol, Apple logo, Apple product glyph, or confusingly similar mark as the app icon or logo.

Run a compact HIG, accessibility, permission-flow, and implementation-feasibility preflight before asking for approval. Fix conflicts between the written design and accepted specification first.

### Phase 3: Render and present

Use the available image-generation capability to create a rendered portrait iPhone mockup for every distinct user-facing screen. At minimum, always render the primary screen. A readable portrait-oriented composite artboard is acceptable when several screens are simple. Do not render landscape, iPad, Mac, or Apple Vision variants.

Render one square app-icon master and show it at full size and a small Home Screen-like preview. Treat mockups as review artifacts, not proof of implementation. Keep every rendered element consistent with the written screen inventory and feasible in programmatic UIKit.

Store approved candidates in the application workspace under `Design/` using clear filenames such as `mockup.png` and `app-icon.png`, and display them inline in the conversation. Do not add design assets inside the skill folder.

### Phase 4: Approval gate

Ask the user to approve the screen structure, feature placement, permission triggers and denied states, visual system, widget and notification layouts, and app icon. **Stop and wait. Do not start implementation.**

After explicit approval, update `AppSpec.md` with:

- `design-status: design-approved`;
- approved screen inventory and navigation;
- permission-to-screen and state mapping;
- privacy-policy, consent-withdrawal, Settings recovery, and conditional policy-module surfaces;
- visual system and accessibility behavior;
- widget and notification layouts;
- paths to approved mockups and app-icon source;
- approval-dependent decisions and remaining release blockers.

Update `AppPrivacy.yml` only with approved screen locations, reviewer paths, privacy-policy entry location, and policy-module UI evidence. Do not change collection, tracking, retention, SDK, or transmission meaning during design.

Do not mark the design approved based on silence or partial feedback. After recording approval, propose `build-ios-app-concept`.

## Handoff

Lead with what the user approved. Provide clickable paths to `AppSpec.md`, `AppPrivacy.yml`, rendered mockups, and the app-icon master. List remaining release blockers and state explicitly that no Xcode project or application code was created by this skill. Propose `build-ios-app-concept`; do not skip directly to release preparation.
